import click
import requests
import sqlite3
import os

DB_PATH = os.path.expanduser("~/.minakilabs_cli.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS config (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """)
    conn.commit()
    conn.close()

def get_config(key):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM config WHERE key=?", (key,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

def set_config(key, value):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("REPLACE INTO config (key, value) VALUES (?, ?)", (key, value))
    conn.commit()
    conn.close()

@click.group()
def cli():
    """Minaki Labs CLI"""
    init_db()

@cli.command()
def login():
    """Prompt the user to login and store the API key."""
    api_key = click.prompt("Please enter your API key", hide_input=True)
    set_config('api_key', api_key)
    click.echo("API key stored successfully.")

@cli.command()
@click.argument('client_ip')
def generate_vpn(client_ip):
    """Generate a VPN for the given client IP."""
    api_key = get_config('api_key')
    if not api_key:
        click.echo("API key not found. Please login first.")
        return

    headers = {
        "apikey": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "client_ip": client_ip
    }

    try:
        response = requests.post("https://kong.minakilabs.com/vpn/generate_vpn", headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        click.echo("Server Config:\n" + result["server_config"])
        click.echo("Client Config:\n" + result["client_config"])
    except requests.RequestException as e:
        click.echo(f"Error: {e.response.status_code} - {e.response.text}")

if __name__ == "__main__":
    cli()
