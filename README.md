# NEAR AI Creative Username Generator 🦀🤖🌐

A fun and useful CLI tool to generate creative NEAR usernames based on specific themes and check their availability in real-time.

## Features
- **Theme-based Generation**: Choose from styles like "AI Agent", "Meme Lord", "Cyberpunk", or "Russian Crypto Degenerate".
- **Real-time Availability Check**: Uses NEAR RPC to verify if the name is free to register.
- **OpenClaw Ready**: Designed to be easily integrated as a skill.

## Installation
```bash
pip install requests
```

## Usage
Run the generator with a specific theme:
```bash
python generator.py --theme "Meme Lord"
```

List all available themes:
```bash
python generator.py --list-themes
```

## OpenClaw Skill Integration
To add this as a skill to your OpenClaw agent, create a `SKILL.md` in your skills directory:

```markdown
---
name: near-username-gen
description: Generates creative NEAR usernames and checks availability.
---
# NEAR Username Gen
Run the generator:
python path/to/generator.py --theme "{{theme}}"
```

## Security Warning 🛡️
Managing NEAR accounts involves private keys. Never share your private keys or seed phrases. Use this tool responsibly to find your perfect identity in the NEAR ecosystem.

## Demo
![Demo](https://via.placeholder.com/800x400.png?text=NEAR+Username+Generator+Demo)
*(Actual GIF/Screenshot would go here)*
