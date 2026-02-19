# NEAR AI Creative Username Generator + Subaccount Creator 🦀🤖🌐

A fun and powerful CLI tool to generate creative NEAR usernames based on specific themes, check their availability, and create sub-accounts instantly.

## Features
- **Theme-based Generation**: Choose from styles like "AI Agent", "Meme Lord", "Cyberpunk", or "Russian Crypto Degenerate".
- **Real-time Availability Check**: Uses NEAR RPC to verify if the name is free to register.
- **Sub-account Creator**: Create your chosen name as a sub-account directly from the CLI.
- **OpenClaw Ready**: Designed to be easily integrated as a skill.

## Installation
```bash
pip install requests
# For sub-account creation, ensure you have near-cli installed:
npm install -g near-cli
```

## Usage

### 1. Generate and Check Names
Run the generator with a specific theme:
```bash
python generator.py --theme "Meme Lord"
```

### 2. Create a Sub-account
Once you find a name you like (e.g., `super_bot.near`), you can create it if you own the parent account:
```bash
python generator.py --create "sub.your_account.near" --master "your_account.near"
```

### 3. List Themes
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
Managing NEAR accounts involves private keys. This tool uses your local `near-cli` configuration. Never share your private keys or seed phrases with anyone.

## Demo
![Demo](https://via.placeholder.com/800x400.png?text=NEAR+Username+Generator+Demo)
