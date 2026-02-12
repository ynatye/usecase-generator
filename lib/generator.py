"""
Playbook Generator - Core generation logic using Claude API
"""

import os
import json
import anthropic
from pathlib import Path
from datetime import datetime


def load_config() -> dict:
    """Load configuration from config.json"""
    config_path = Path(__file__).parent.parent / "config.json"
    with open(config_path) as f:
        return json.load(f)


def load_prompt_template(version: str = "v2") -> str:
    """Load the prompt template"""
    prompt_path = Path(__file__).parent.parent / "prompts" / f"playbook_{version}.md"
    if not prompt_path.exists():
        prompt_path = Path(__file__).parent.parent / "prompts" / "playbook.md"
    with open(prompt_path) as f:
        return f.read()


def slugify(text: str) -> str:
    """Convert text to a filename-safe slug"""
    return text.lower().replace(" & ", "-").replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")


def generate_playbook(
    industry: str,
    department: str,
    api_key: str = None,
    model: str = None,
    version: str = "v2",
    verbose: bool = False
) -> str:
    """
    Generate a playbook for the given industry and department.
    
    Args:
        industry: The industry name
        department: The department name
        api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
        model: Model to use (defaults to config)
        version: Prompt version (v1 or v2)
        verbose: Print progress information
    
    Returns:
        Generated playbook markdown content
    """
    config = load_config()
    
    # Get API key
    api_key = api_key or os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("No API key provided. Set ANTHROPIC_API_KEY or pass api_key parameter.")
    
    # Get model
    model = model or config["settings"]["model"]
    
    # Load and format prompt
    prompt_template = load_prompt_template(version)
    prompt = prompt_template.replace("{{industry}}", industry).replace("{{department}}", department)
    
    if verbose:
        print(f"Generating playbook for {industry} × {department}...")
        print(f"Using model: {model}")
    
    # Call Claude API
    client = anthropic.Anthropic(api_key=api_key)
    
    message = client.messages.create(
        model=model,
        max_tokens=config["settings"]["max_tokens"],
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    # Extract content
    content = message.content[0].text
    
    # Add generation metadata
    timestamp = datetime.now().strftime("%Y-%m-%d")
    if f"*Generated:" not in content:
        content += f"\n\n---\n\n*Generated: {timestamp} | Version: {version} | Model: {model}*"
    
    return content


def save_playbook(
    content: str,
    industry: str,
    department: str,
    output_dir: str = None
) -> Path:
    """
    Save generated playbook to file.
    
    Args:
        content: Playbook markdown content
        industry: Industry name
        department: Department name
        output_dir: Output directory (defaults to config)
    
    Returns:
        Path to saved file
    """
    config = load_config()
    output_dir = output_dir or config["settings"]["output_dir"]
    
    # Create output directory
    output_path = Path(__file__).parent.parent / output_dir
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = f"{slugify(industry)}_{slugify(department)}.md"
    filepath = output_path / filename
    
    # Save file
    with open(filepath, "w") as f:
        f.write(content)
    
    return filepath


def list_generated(output_dir: str = None) -> list:
    """
    List all generated playbooks.
    
    Returns:
        List of dicts with industry, department, and path
    """
    config = load_config()
    output_dir = output_dir or config["settings"]["output_dir"]
    output_path = Path(__file__).parent.parent / output_dir
    
    if not output_path.exists():
        return []
    
    playbooks = []
    for filepath in output_path.glob("*.md"):
        # Parse filename to get industry and department
        name = filepath.stem
        parts = name.rsplit("_", 1)
        if len(parts) == 2:
            playbooks.append({
                "industry_slug": parts[0],
                "department_slug": parts[1],
                "path": filepath,
                "size": filepath.stat().st_size,
                "modified": datetime.fromtimestamp(filepath.stat().st_mtime)
            })
    
    return sorted(playbooks, key=lambda x: x["path"].name)


def get_all_departments(config: dict = None) -> list:
    """Get all departments from all tiers"""
    config = config or load_config()
    departments = []
    for tier in ["tier1", "tier2", "tier3"]:
        departments.extend(config["departments"].get(tier, []))
    return departments


def get_mvp_combinations(config: dict = None) -> list:
    """Get MVP industry × department combinations"""
    config = config or load_config()
    combinations = []
    for industry in config["mvp"]["industries"]:
        for department in config["mvp"]["departments"]:
            combinations.append((industry, department))
    return combinations


def get_tier1_combinations(config: dict = None) -> list:
    """Get all industries × tier1 departments"""
    config = config or load_config()
    combinations = []
    for industry in config["industries"]:
        for department in config["departments"]["tier1"]:
            combinations.append((industry, department))
    return combinations
