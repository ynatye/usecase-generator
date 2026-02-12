#!/usr/bin/env python3
"""
Use Case Generator CLI

Generate industry × department playbooks for monday.com Solutions Engineers.
"""

import os
import sys
import time
import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.panel import Panel
from rich.markdown import Markdown
from dotenv import load_dotenv

# Add lib to path
sys.path.insert(0, str(Path(__file__).parent))

from lib.generator import (
    load_config,
    generate_playbook,
    save_playbook,
    list_generated,
    get_all_departments,
    get_mvp_combinations,
    get_tier1_combinations,
    slugify
)

# Load environment variables
load_dotenv()

console = Console()


@click.group()
@click.version_option(version="2.0.0")
def cli():
    """
    🎯 Use Case Generator - AI-powered playbooks for monday.com SEs
    
    Generate industry × department playbooks with Vibe prompts and Agent blueprints.
    """
    pass


@cli.command()
@click.argument("industry", required=False)
@click.argument("department", required=False)
@click.option("--all-mvp", is_flag=True, help="Generate all MVP combinations (4×6=24)")
@click.option("--all-tier1", is_flag=True, help="Generate all industries × tier1 departments")
@click.option("--industry-all", "-i", help="Generate all tier1 departments for one industry")
@click.option("--department-all", "-d", help="Generate all industries for one department")
@click.option("--format", "-f", type=click.Choice(["v1", "v2"]), default="v2", help="Output format version")
@click.option("--force", is_flag=True, help="Overwrite existing playbooks")
@click.option("--model", "-m", help="Override model (default: claude-sonnet-4-20250514)")
@click.option("--dry-run", is_flag=True, help="Show what would be generated without generating")
def generate(industry, department, all_mvp, all_tier1, industry_all, department_all, format, force, model, dry_run):
    """
    Generate playbook(s) for industry × department combinations.
    
    Examples:
    
      usecase generate "Banking" "IT"
      
      usecase generate --all-mvp
      
      usecase generate -i "Pharmaceuticals"
      
      usecase generate -d "Operations"
    """
    config = load_config()
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    
    if not api_key:
        console.print("[red]Error:[/red] ANTHROPIC_API_KEY not set. Export it or add to .env file.")
        sys.exit(1)
    
    # Determine combinations to generate
    combinations = []
    
    if all_mvp:
        combinations = get_mvp_combinations(config)
        console.print(f"[cyan]Generating MVP combinations:[/cyan] {len(combinations)} playbooks")
    
    elif all_tier1:
        combinations = get_tier1_combinations(config)
        console.print(f"[cyan]Generating all tier1 combinations:[/cyan] {len(combinations)} playbooks")
    
    elif industry_all:
        # Find matching industry
        matched = None
        for ind in config["industries"]:
            if industry_all.lower() in ind.lower():
                matched = ind
                break
        if not matched:
            console.print(f"[red]Error:[/red] Industry '{industry_all}' not found")
            sys.exit(1)
        for dept in config["departments"]["tier1"]:
            combinations.append((matched, dept))
        console.print(f"[cyan]Generating all tier1 for {matched}:[/cyan] {len(combinations)} playbooks")
    
    elif department_all:
        # Find matching department
        all_depts = get_all_departments(config)
        matched = None
        for dept in all_depts:
            if department_all.lower() in dept.lower():
                matched = dept
                break
        if not matched:
            console.print(f"[red]Error:[/red] Department '{department_all}' not found")
            sys.exit(1)
        for ind in config["industries"]:
            combinations.append((ind, matched))
        console.print(f"[cyan]Generating all industries for {matched}:[/cyan] {len(combinations)} playbooks")
    
    elif industry and department:
        # Single generation - find matching industry and department
        matched_ind = None
        for ind in config["industries"]:
            if industry.lower() in ind.lower():
                matched_ind = ind
                break
        
        matched_dept = None
        all_depts = get_all_departments(config)
        for dept in all_depts:
            if department.lower() in dept.lower():
                matched_dept = dept
                break
        
        if not matched_ind:
            console.print(f"[red]Error:[/red] Industry '{industry}' not found")
            console.print("Use [cyan]usecase industries[/cyan] to see available options")
            sys.exit(1)
        
        if not matched_dept:
            console.print(f"[red]Error:[/red] Department '{department}' not found")
            console.print("Use [cyan]usecase departments[/cyan] to see available options")
            sys.exit(1)
        
        combinations = [(matched_ind, matched_dept)]
    
    else:
        console.print("[yellow]Usage:[/yellow] usecase generate <industry> <department>")
        console.print("       usecase generate --all-mvp")
        console.print("       usecase generate -i <industry>")
        console.print("       usecase generate -d <department>")
        sys.exit(1)
    
    # Check for existing files if not force
    if not force and not dry_run:
        existing = []
        output_dir = Path(__file__).parent / config["settings"]["output_dir"]
        for ind, dept in combinations:
            filename = f"{slugify(ind)}_{slugify(dept)}.md"
            if (output_dir / filename).exists():
                existing.append(f"{ind} × {dept}")
        
        if existing:
            console.print(f"[yellow]Warning:[/yellow] {len(existing)} playbook(s) already exist. Use --force to overwrite.")
            for e in existing[:5]:
                console.print(f"  - {e}")
            if len(existing) > 5:
                console.print(f"  ... and {len(existing) - 5} more")
            
            # Filter out existing
            combinations = [
                (ind, dept) for ind, dept in combinations
                if not (output_dir / f"{slugify(ind)}_{slugify(dept)}.md").exists()
            ]
            
            if not combinations:
                console.print("[yellow]Nothing to generate.[/yellow]")
                sys.exit(0)
            
            console.print(f"[cyan]Generating {len(combinations)} new playbook(s)[/cyan]")
    
    # Dry run - just show what would be generated
    if dry_run:
        table = Table(title="Playbooks to Generate")
        table.add_column("Industry", style="cyan")
        table.add_column("Department", style="green")
        table.add_column("Filename", style="dim")
        
        for ind, dept in combinations:
            table.add_row(ind, dept, f"{slugify(ind)}_{slugify(dept)}.md")
        
        console.print(table)
        console.print(f"\n[dim]Total: {len(combinations)} playbooks[/dim]")
        return
    
    # Generate playbooks
    success = 0
    failed = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console
    ) as progress:
        task = progress.add_task("Generating...", total=len(combinations))
        
        for ind, dept in combinations:
            progress.update(task, description=f"[cyan]{ind}[/cyan] × [green]{dept}[/green]")
            
            try:
                content = generate_playbook(
                    industry=ind,
                    department=dept,
                    api_key=api_key,
                    model=model,
                    version=format
                )
                
                filepath = save_playbook(content, ind, dept)
                success += 1
                
            except Exception as e:
                failed.append((ind, dept, str(e)))
            
            progress.advance(task)
            
            # Rate limiting - small delay between requests
            if len(combinations) > 1:
                time.sleep(1)
    
    # Summary
    console.print()
    console.print(Panel(
        f"[green]✓ Generated:[/green] {success}\n"
        f"[red]✗ Failed:[/red] {len(failed)}",
        title="Generation Complete"
    ))
    
    if failed:
        console.print("\n[red]Failed generations:[/red]")
        for ind, dept, error in failed:
            console.print(f"  - {ind} × {dept}: {error[:50]}...")


@cli.command()
def list():
    """List all generated playbooks."""
    playbooks = list_generated()
    
    if not playbooks:
        console.print("[yellow]No playbooks generated yet.[/yellow]")
        console.print("Run [cyan]usecase generate --all-mvp[/cyan] to generate MVP playbooks.")
        return
    
    table = Table(title=f"Generated Playbooks ({len(playbooks)})")
    table.add_column("Industry", style="cyan")
    table.add_column("Department", style="green")
    table.add_column("Size", justify="right")
    table.add_column("Modified", style="dim")
    
    for pb in playbooks:
        size_kb = pb["size"] / 1024
        table.add_row(
            pb["industry_slug"],
            pb["department_slug"],
            f"{size_kb:.1f} KB",
            pb["modified"].strftime("%Y-%m-%d %H:%M")
        )
    
    console.print(table)


@cli.command()
def status():
    """Show generation status matrix."""
    config = load_config()
    playbooks = list_generated()
    
    # Build set of generated combinations
    generated = set()
    for pb in playbooks:
        generated.add((pb["industry_slug"], pb["department_slug"]))
    
    # MVP status
    console.print("\n[bold]MVP Status (4 industries × 6 departments)[/bold]\n")
    
    table = Table()
    table.add_column("Industry", style="cyan")
    for dept in config["mvp"]["departments"]:
        table.add_column(dept[:3], justify="center")
    
    mvp_total = 0
    mvp_done = 0
    
    for ind in config["mvp"]["industries"]:
        row = [ind[:25]]
        for dept in config["mvp"]["departments"]:
            mvp_total += 1
            key = (slugify(ind), slugify(dept))
            if key in generated:
                row.append("[green]✓[/green]")
                mvp_done += 1
            else:
                row.append("[red]✗[/red]")
        table.add_row(*row)
    
    console.print(table)
    console.print(f"\n[dim]MVP Progress: {mvp_done}/{mvp_total} ({mvp_done/mvp_total*100:.0f}%)[/dim]")
    
    # Overall status
    total_possible = len(config["industries"]) * len(get_all_departments(config))
    console.print(f"[dim]Total Generated: {len(playbooks)} / {total_possible} possible combinations[/dim]")


@cli.command()
@click.option("--search", "-s", help="Search/filter industries")
def industries(search):
    """List all available industries."""
    config = load_config()
    
    industries = config["industries"]
    if search:
        industries = [i for i in industries if search.lower() in i.lower()]
    
    table = Table(title=f"Industries ({len(industries)})")
    table.add_column("#", style="dim", width=4)
    table.add_column("Industry", style="cyan")
    table.add_column("MVP", justify="center")
    
    for i, ind in enumerate(industries, 1):
        is_mvp = "✓" if ind in config["mvp"]["industries"] else ""
        table.add_row(str(i), ind, f"[green]{is_mvp}[/green]")
    
    console.print(table)


@cli.command()
def departments():
    """List all available departments."""
    config = load_config()
    
    table = Table(title="Departments")
    table.add_column("Tier", style="dim")
    table.add_column("Department", style="green")
    table.add_column("MVP", justify="center")
    
    for tier_name, tier_label in [("tier1", "Tier 1"), ("tier2", "Tier 2"), ("tier3", "Tier 3")]:
        for dept in config["departments"][tier_name]:
            is_mvp = "✓" if dept in config["mvp"]["departments"] else ""
            table.add_row(tier_label, dept, f"[green]{is_mvp}[/green]")
    
    console.print(table)


@cli.command()
@click.argument("industry")
@click.argument("department")
def show(industry, department):
    """Show a generated playbook."""
    config = load_config()
    output_dir = Path(__file__).parent / config["settings"]["output_dir"]
    
    # Find matching file
    filename = f"{slugify(industry)}_{slugify(department)}.md"
    filepath = output_dir / filename
    
    if not filepath.exists():
        # Try fuzzy match
        for f in output_dir.glob("*.md"):
            if industry.lower() in f.stem.lower() and department.lower() in f.stem.lower():
                filepath = f
                break
    
    if not filepath.exists():
        console.print(f"[red]Error:[/red] Playbook not found: {filename}")
        console.print("Run [cyan]usecase list[/cyan] to see available playbooks.")
        sys.exit(1)
    
    with open(filepath) as f:
        content = f.read()
    
    console.print(Markdown(content))


@cli.command()
@click.argument("industry")
@click.argument("department")
def open(industry, department):
    """Open a playbook in the default editor."""
    import subprocess
    
    config = load_config()
    output_dir = Path(__file__).parent / config["settings"]["output_dir"]
    
    filename = f"{slugify(industry)}_{slugify(department)}.md"
    filepath = output_dir / filename
    
    if not filepath.exists():
        console.print(f"[red]Error:[/red] Playbook not found: {filename}")
        sys.exit(1)
    
    editor = os.environ.get("EDITOR", "nano")
    subprocess.run([editor, str(filepath)])


if __name__ == "__main__":
    cli()
