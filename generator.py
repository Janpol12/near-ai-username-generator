import sys
import random
import requests
import json
import argparse
import subprocess

NEAR_RPC = "https://rpc.mainnet.near.org"

THEMES = {
    "AI Agent": {
        "prefixes": ["bot_", "ai_", "smart_", "agent_", "neuro_", "cyber_"],
        "suffixes": ["_logic", "_brain", "_mind", "_node", "_core", "_synth"],
        "keywords": ["nexus", "matrix", "vector", "tensor", "prompt", "kernel"]
    },
    "Meme Lord": {
        "prefixes": ["doge_", "pepe_", "moon_", "chad_", "kek_", "wojak_"],
        "suffixes": ["_hodl", "_rekt", "_wagmi", "_to_the_moon", "_pump", "_stonks"],
        "keywords": ["lambo", "fomo", "diamond", "hands", "alpha", "based"]
    },
    "NEAR Builder": {
        "prefixes": ["near_", "wasm_", "shard_", "chain_", "open_", "fast_"],
        "suffixes": ["_dev", "_build", "_arch", "_stack", "_protocol", "_hub"],
        "keywords": ["bos", "horizon", "pagoda", "mint", "contract", "gas"]
    },
    "Russian Crypto Degenerate": {
        "prefixes": ["kripto_", "gaz_", "pamp_", "damp_", "tsar_", "brat_"],
        "suffixes": ["_v_shokolade", "_na_lune", "_millioner", "_v_dele", "_invest", "_top"],
        "keywords": ["zavod", "kotleta", "halving", "perekup", "shilling", "raketa"]
    },
    "Cyberpunk": {
        "prefixes": ["neon_", "glitch_", "data_", "grid_", "volt_", "hacker_"],
        "suffixes": ["_runner", "_ghost", "_shell", "_wire", "_daemon", "_static"],
        "keywords": ["chroma", "cipher", "proxy", "uplink", "byte", "neural"]
    }
}

def generate_names(theme_name, count=15):
    theme = THEMES.get(theme_name, THEMES["AI Agent"])
    names = set()
    while len(names) < count:
        choice = random.randint(0, 2)
        if choice == 0:
            name = random.choice(theme["prefixes"]) + random.choice(theme["keywords"])
        elif choice == 1:
            name = random.choice(theme["keywords"]) + random.choice(theme["suffixes"])
        else:
            name = random.choice(theme["prefixes"]) + random.choice(theme["keywords"]) + random.choice(theme["suffixes"])
        
        name = name.replace("__", "_").lower()[:64]
        if name.endswith("_"): name = name[:-1]
        if name.startswith("_"): name = name[1:]
        
        if len(name) >= 2:
            names.add(name + ".near")
    return list(names)

def check_availability(account_id):
    payload = {
        "jsonrpc": "2.0",
        "id": "dontcare",
        "method": "query",
        "params": {
            "request_type": "view_account",
            "finality": "final",
            "account_id": account_id
        }
    }
    try:
        response = requests.post(NEAR_RPC, json=payload, timeout=5).json()
        if "error" in response and "does not exist" in response["error"]["data"]:
            return True
        return False
    except:
        return False

def create_subaccount(account_id, master_account):
    print(f"\n🚀 ATTEMPTING TO CREATE SUB-ACCOUNT: {account_id}")
    print(f"Master Account: {master_account}")
    print("--------------------------------------------------")
    print("⚠️ SECURITY WARNING: This action will use your master account's balance.")
    print("Ensure you have NEAR CLI installed and authorized for the master account.")
    print("--------------------------------------------------\n")
    
    confirm = input(f"Confirm creation of {account_id}? (y/n): ")
    if confirm.lower() != 'y':
        print("Creation cancelled.")
        return

    # Using npx near-cli for broader compatibility
    cmd = ["npx", "near-cli", "create-account", account_id, "--masterAccount", master_account]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Success! Sub-account {account_id} created.")
            print(result.stdout)
        else:
            print(f"❌ Error creating account: {result.stderr}")
    except Exception as e:
        print(f"❌ System error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="NEAR AI Creative Username Generator & Subaccount Creator")
    parser.add_argument("--theme", type=str, help="Theme/Style (e.g. 'Meme Lord', 'Cyberpunk')")
    parser.add_argument("--list-themes", action="store_true", help="List available themes")
    parser.add_argument("--create", type=str, help="Create a sub-account (requires --master)")
    parser.add_argument("--master", type=str, help="Master account ID for sub-account creation")
    
    args = parser.parse_args()

    if args.list_themes:
        print("Available Themes:")
        for t in THEMES.keys():
            print(f" - {t}")
        return

    if args.create:
        if not args.master:
            print("Error: --master account ID is required when using --create")
            sys.exit(1)
        create_subaccount(args.create, args.master)
        return

    theme = args.theme if args.theme else random.choice(list(THEMES.keys()))
    print(f"--- Generating names for theme: {theme} ---")
    
    potential_names = generate_names(theme)
    available = []
    
    for name in potential_names:
        if check_availability(name):
            available.append(name)
            print(f"✅ {name} is AVAILABLE!")
        else:
            # Silence taken names for cleaner output in some modes
            pass
    
    print("\n--- Summary ---")
    if not available:
        print("No available names found in this batch. Try again!")
    else:
        print(f"Found {len(available)} available names:")
        for i, name in enumerate(available, 1):
            print(f"{i}. {name}")
            
    print("\nTo create one of these as a sub-account, run:")
    print(f"python generator.py --create <name> --master <your_account.near>")

if __name__ == "__main__":
    main()
