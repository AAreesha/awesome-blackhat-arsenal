# Contributing to Awesome Black Hat Arsenal

Thanks for your interest in contributing!

### 🔧 How to Add a Tool

1. Fork the repo and create a branch.
2. Add your tool to:
   - `data/arsenal_2025.json` (or corresponding year)
   - `README.md` in the appropriate category

### 🧩 JSON Format

Each tool should follow this schema:

```json
{
  "tool_name": "ToolName",
  "speakers": ["Speaker1", "Speaker2"],
  "tracks": ["Red Team", "OSINT"],
  "location": "Business Hall - Arsenal Station X",
  "skill_level": "All",
  "event": "BH-USA-2016",
  "session_type": "Arsenal",
  "github_url": "https://github.com/your/tool",
  "description": "One-line description of what the tool does."
}
