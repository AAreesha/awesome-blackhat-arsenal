import os
import json
from collections import defaultdict

ROOT_DIR = "tools"
MAIN_README = "README.md"

CATEGORY_MAP = {
    "Exploitation and Ethical Hacking": ("🔴 Red Teaming", "red"),
    "Malware Offense": ("🔴 Red Teaming", "red"),
    "Network Attacks": ("🔴 Red Teaming", "red"),
    "Reverse Engineering": ("🧠 Reverse Engineering", "orange"),
    "OSINT - Open Source Intelligence": ("🔍 OSINT", "lightgrey"),
    "Internet of Things": ("🟣 Red Teaming / Embedded", "purple"),
    "Hardware / Embedded": ("🟣 Red Teaming / Embedded", "purple"),
    "Code Assessment": ("🌐 Web/AppSec or Red Teaming", "blue"),
    "Web AppSec": ("🌐 Web/AppSec", "blue"),
    "Vulnerability Assessment": ("🔴 Red Teaming / AppSec", "red"),
    "Smart Grid/Industrial Security": ("🟣 Red Teaming / Embedded", "purple"),
    "Android, iOS and Mobile Hacking": ("📱 Mobile Security", "yellow"),
    "Cryptography": ("🔵 Blue Team & Detection", "cyan"),
    "Network Defense": ("🔵 Blue Team & Detection", "cyan"),
    "Malware Defense": ("🔵 Blue Team & Detection", "cyan"),
    "Data Forensics/Incident Response": ("🔵 Blue Team & Detection", "cyan"),
    "Arsenal Lab": ("⚙️ Miscellaneous / Lab Tools", "gray"),
    "Human Factors": ("🧠 Social Engineering / General", "pink"),
}

def extract_track_label(track_entry):
    if not isinstance(track_entry, str): return ""
    return track_entry.replace("Track:", "").strip()

def determine_category(track_list):
    if not track_list or not isinstance(track_list, list):
        return ("Others", "lightgrey")
    for track in track_list:
        track_clean = extract_track_label(track)
        if track_clean in CATEGORY_MAP:
            return CATEGORY_MAP[track_clean]
    return ("Others", "lightgrey")

def badge(text, color):
    return f"![{text}](https://img.shields.io/badge/{text.replace(' ', '%20')}-{color})"

def sanitize_anchor(text):
    return text.lower().replace(" ", "-").replace("/", "").replace("&", "").replace("--", "-")

main_readme = [
    "# Awesome Black Hat Arsenal [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Update](https://img.shields.io/badge/Updated-June%202025-blue)](https://github.com/yourusername/awesome-blackhat-arsenal)",
    "> 🚀 A curated list of cutting-edge cybersecurity tools showcased at the Black Hat Arsenal events — covering offensive, defensive, and research-focused security utilities.",
    "",
    "Whether you're in red teaming, blue teaming, appsec, or OSINT — this list helps you explore and leverage the best tools demonstrated live by security professionals across the world.",
    "",
    "📌 **How This List is Organized**",
    "- The tools are grouped by the **location** of the Black Hat event (e.g., USA, Europe, Asia).",
    "- Under each location, tools are further organized by **year**.",
    "- Inside each year’s section, you’ll find the tools organized **by track category**, each with descriptions, authors, and GitHub links (where available).",
    "---",
    "## 🌍 Locations"
]

for location in sorted(os.listdir(ROOT_DIR)):
    loc_path = os.path.join(ROOT_DIR, location)
    if not os.path.isdir(loc_path):
        continue

    main_readme.append(f"### {location}")
    for year in sorted(os.listdir(loc_path)):
        year_path = os.path.join(loc_path, year)
        if not os.path.isdir(year_path):
            continue

        rel_readme = f"{ROOT_DIR}/{location}/{year}/README.md"
        main_readme.append(f"- [{year}]({rel_readme})")

        tools_by_category = defaultdict(list)
        for file in os.listdir(year_path):
            if not file.endswith(".json"): continue
            with open(os.path.join(year_path, file), "r", encoding="utf-8") as f:
                data = json.load(f)
            if not isinstance(data, list): data = [data]

            for tool in data:
                name = tool.get("Tool Name", "Unnamed Tool")
                url = (tool.get("Github URL") or "").strip()
                description = tool.get("Description", "No description provided.")
                event = tool.get("Event", "Unknown")
                tracks = tool.get("Tracks", [])
                speakers_raw = tool.get("Speakers", [])
                speakers = speakers_raw if isinstance(speakers_raw, list) else [str(speakers_raw)]

                result = determine_category(tracks)
                if not result: continue
                category, color = result

                speaker_tags = " ".join([badge(s, "informational") for s in speakers])
                event_tag = badge(event, "black" if "USA" in event else "blue")
                category_tag = badge(f"Category: {category}", color)
                link_line = f"🔗 **Link:** [{name}]({url})" if url else "🔗 **Link:** Not Available"

                entry = f"""<details><summary><strong>{name}</strong></summary>\n\n{event_tag} {category_tag} {speaker_tags}\n\n{link_line}  \n📝 **Description:** {description}\n\n</details>\n"""
                tools_by_category[category].append(entry)

        # Sub README creation
        # Sub README creation
        subreadme = [
            f"# {location} {year}",
            "---",
            f"📍 This document lists cybersecurity tools demonstrated during the **Black Hat Arsenal {year}** event held in **{location}**.",
            "Tools are categorized based on their **track theme**, such as Red Teaming, OSINT, Reverse Engineering, etc.",
            "",
            "## 📚 Table of Contents"
        ]
        for cat in sorted(tools_by_category): subreadme.append(f"- [{cat}](#{sanitize_anchor(cat)})")
        subreadme.append("---")

        for cat, tools in tools_by_category.items():
            subreadme.append(f"## {cat}")
            # updated: exclude event_tag
            for tool_block in tools:
                tool_block = tool_block.replace(f"{event_tag} ", "")
                subreadme.append(tool_block)
            subreadme.append("---")

        with open(os.path.join(year_path, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(subreadme))

# with open(MAIN_README, "w", encoding="utf-8") as f:
#     f.write("\n\n".join(main_readme))
# Write main README
main_readme.append("---")
main_readme.extend([
    "## 🧩 Contributing",
    "We welcome community contributions to make this list better!",
    "",
    "### 🛠 How to Contribute:",
    "- 📁 Tools are grouped by **Black Hat event location** (`USA`, `Europe`, etc.) and **year** inside `output_by_location/`.",
    "- 🧠 Inside each year's folder, tools are organized by **track categories** such as `Red Teaming`, `OSINT`, `Reverse Engineering`, etc.",
    "- 📝 Each tool is defined by a structured `.json` file including:",
    "  - Tool Name",
    "  - Description",
    "  - GitHub URL (if available)",
    "  - Tracks",
    "  - Speaker(s)",
    "",
    "### 📄 To Add a Tool:",
    "1. Create a JSON file inside the appropriate folder:",
    "   ```",
    "   output_by_location/{LOCATION}/{YEAR}/tool-name.json",
    "   ```",
    "2. Follow the [CONTRIBUTING.md](CONTRIBUTING.md) for format guidelines.",
    "3. Submit a pull request.",
    "",
    "> ⚠️ Keep content concise and correctly categorized. Badges and README entries are auto-generated.",
    "---",
    "## 📄 License",
    "[MIT](LICENSE)",
    "---",
    "> Inspired by [Awesome Lists](https://awesome.re) and powered by the Black Hat Arsenal community."
])

with open(MAIN_README, "w", encoding="utf-8") as f:
    f.write("\n".join(main_readme))