from collections import defaultdict
import os
import json

ROOT_DIR = "output_by_location"
MAIN_README = "README.md"

def badge(text, color):
    return f"![{text}](https://img.shields.io/badge/{text.replace(' ', '%20')}-{color})"

main_readme_parts = [
    "# Awesome Black Hat Arsenal [![Awesome](https://awesome.re/badge.svg)](https://awesome.re) [![Last Update](https://img.shields.io/badge/Updated-June%202025-blue)](https://github.com/yourusername/awesome-blackhat-arsenal)",
    "> 🚀 A curated list of cutting-edge cybersecurity tools showcased at the Black Hat Arsenal events — covering offensive, defensive, and research-focused security utilities.",
    "",
    "Whether you're in red teaming, blue teaming, appsec, or OSINT — this list helps you explore and leverage the best tools demonstrated live by security professionals across the world.",
    "---",
    "## 🌍 Locations\n"
]

# Generate main README content and individual year sub-READMEs
for location in sorted(os.listdir(ROOT_DIR)):
    loc_path = os.path.join(ROOT_DIR, location)
    if not os.path.isdir(loc_path):
        continue

    main_readme_parts.append(f"### {location}")
    for year in sorted(os.listdir(loc_path)):
        year_path = os.path.join(loc_path, year)
        if not os.path.isdir(year_path):
            continue

        rel_link = f"{ROOT_DIR}/{location}/{year}/README.md"
        main_readme_parts.append(f"- [{year}]({rel_link})")

        tools_by_category = defaultdict(list)

        for file in os.listdir(year_path):
            if not file.endswith(".json"):
                continue
            with open(os.path.join(year_path, file), "r", encoding="utf-8") as f:
                tool = json.load(f)

            name = tool.get("Tool Name", "Unnamed Tool")
            url = tool.get("Github URL") or None
            event = tool.get("Event", "Unknown")
            year_val = tool.get("Year", year)
            description = tool.get("Description", "No description provided.")
            tracks = tool.get("Tracks", [])
            speakers = tool.get("Speakers", [])
            speakers = speakers if isinstance(speakers, list) else [str(speakers)]

            event_badge = badge(f"{event}", "black" if "USA" in event else "blue")
            category_badge = badge("Tool", "green")
            speaker_badges = " ".join([badge(s, "informational") for s in speakers])

            block = [
                f"### [{name}]({url})" if url else f"### {name}",
                f"{event_badge} {category_badge} {speaker_badges}",
                f"{description}",
                ""
            ]

            tools_by_category["Tools"].append("\n".join(block))

        # Write sub README
        subreadme = [
            f"# {location} {year}",
            "---",
            f"## 🛠️ Tools from {event}",
            ""
        ]
        for entries in tools_by_category.values():
            subreadme.extend(entries)
        sub_path = os.path.join(year_path, "README.md")
        with open(sub_path, "w", encoding="utf-8") as f:
            f.write("\n".join(subreadme))

# Write main README
main_readme_parts.append("---")
main_readme_parts.extend([
    "## 🧩 Contributing",
    "Contributions are welcome! Please:",
    "- Add tools under the right category",
    "- Use Markdown formatting like shown above",
    "- Include at least: name, description, GitHub/project link, and relevant badges",
    "- Optional: Create a `tools/tool-name.json` file with structured metadata",
    "> See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines",
    "---",
    "## 📄 License",
    "[MIT](LICENSE)",
    "---",
    "> Inspired by [Awesome Lists](https://awesome.re) and powered by the Black Hat Arsenal community."
])

with open(MAIN_README, "w", encoding="utf-8") as f:
    f.write("\n".join(main_readme_parts))
