import json
import typer
import random
import string
import requests
from rich import print
from rich.console import Console
from rich.table import Table
from rich.box import HEAVY_EDGE, SIMPLE_HEAD, MINIMAL_DOUBLE_HEAD

from .constants import api_url
from .api import api_request, get_user_info

# =============================================================================

# Create a Typer app
app = typer.Typer()

# =============================================================================


@app.callback()
def callback():
    """
    A CLI tool for interacting with the M2C2Kit data and production server API.
    """


@app.command()
def get_started():
    print(
        """
          🚀 Welcome to the M2C2Kit CLI! 🚀
          -----------------------------------
          
          📚 Check out the docs: 
          [green]https://m2c2-project.github.io/m2c2kit[/green]
          
          🔗 Read our integration guides for Qualtrics, Metricwire, and soon REDCAP:
          https://github.com/m2c2-project/m2c2kit-integration-guides
          
          🌟 Give us a Star on Github: 
          [green]https://github.com/m2c2-project/m2c2kit[/green]
          
          -----------------------------------
          
          If you ever need to access our various docs, feel free to run any of the following commands:
          `m2c2 open_m2c2kit_docs`
            `m2c2 open_m2c2kit_github`
            `m2c2 open_m2c2kit_changelog`
            `m2c2 open_m2c2kit_playground`
            `m2c2 open_m2c2kit_integration_guides`
          
          -----------------------------------
          
          📩 Feel free to reach out for help to: 
          [green]m2c2@psu.edu[/green]
          
          
          
          """
    )


# =============================================================================

# Load docs in the browser


@app.command()
def open_m2c2kit_docs():
    print("Opening M2C2Kit's docs 🚀")
    typer.launch("https://m2c2-project.github.io/m2c2kit/")


@app.command()
def open_m2c2kit_github():
    print("Opening M2C2Kit's Github 🚀")
    typer.launch("https://github.com/m2c2-project/m2c2kit")


@app.command()
def open_m2c2kit_changelog():
    print("Opening M2C2Kit's Changelog 🚀")
    typer.launch("https://github.com/m2c2-project/m2c2kit/blob/main/CHANGELOG.md")


@app.command()
def open_m2c2kit_playground():
    print("Opening M2C2Kit Playground 🚀")
    typer.launch("https://m2c2-project.github.io/m2c2kit/playground")


@app.command()
def open_m2c2kit_integration_guides():
    print("Opening M2C2Kit Integration Guides 🚀")
    typer.launch("https://github.com/m2c2-project/m2c2kit-integration-guides")

@app.command()
def open_pypi():
    print("Opening M2C2Kit PyPI 🚀")
    typer.launch("https://pypi.org/project/m2c2kit-data-cli/")
# =============================================================================


# Define the `verify_study` command
# Determines if a study is valid based on the study ID and API key
@app.command()
def verify_study():
    study_id = typer.prompt("Study ID")
    api_key = typer.prompt("API Key")

    url = f"{api_url}/verify/{study_id}/{api_key}"
    headers = {
        "accept": "application/json",
    }

    # Make a request to the API
    response = requests.get(url, headers=headers)

    # Check if the response is successful
    if response.status_code == 200:
        result = response.json()
        if result is True:
            typer.echo("✅ Verification successful!")
        elif result is False:
            typer.echo("❌ Verification failed.")
        else:
            typer.echo(f"Response: {result}")
    else:
        typer.echo(
            {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text,
            }
        )


# =============================================================================


# Define the `register` command
# Registers a user with the API
@app.command()
def register():
    email = typer.prompt("Email")
    phone_number = typer.prompt("Phone Number")
    first_name = typer.prompt("First Name")
    last_name = typer.prompt("Last Name")
    affiliation = typer.prompt("Affiliation")
    username = typer.prompt("Username")
    password = typer.prompt("Password", hide_input=True)  # Hides the input for security
    client_id = typer.prompt("Client ID", default="string")
    client_secret = typer.prompt("Client Secret", default="string")

    url = f"{api_url}/auth/register"
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    params = {
        "email": email,
        "phone_number": phone_number,
        "first_name": first_name,
        "last_name": last_name,
        "affiliation": affiliation,
    }
    data = {
        "grant_type": "password",
        "username": username,
        "password": password,
        "scope": "",
        "client_id": client_id,
        "client_secret": client_secret,
    }

    response = requests.post(url, headers=headers, params=params, data=data)

    if response.status_code == 201:
        typer.echo("✅ Registration successful!")
        typer.echo(response.json())
    else:
        typer.echo("❌ Registration failed.")
        typer.echo(
            {
                "error": f"Request failed with status code {response.status_code}",
                "details": response.text,
            }
        )


# =============================================================================


@app.command()
def generate_password(
    length: int = typer.Option(24, help="Password Length"),
    include_numbers: bool = typer.Option(True, help="Include Numbers"),
    include_lowercase: bool = typer.Option(True, help="Include Lowercase Characters"),
    include_uppercase: bool = typer.Option(True, help="Include Uppercase Characters"),
    begin_with_letter: bool = typer.Option(True, help="Begin With A Letter"),
    include_symbols: bool = typer.Option(True, help="Include Symbols"),
    no_similar_characters: bool = typer.Option(True, help="No Similar Characters"),
    no_duplicate_characters: bool = typer.Option(True, help="No Duplicate Characters"),
    no_sequential_characters: bool = typer.Option(
        True, help="No Sequential Characters"
    ),
    quantity: int = typer.Option(1, help="Quantity of passwords to generate"),
):
    # Character sets
    numbers = string.digits
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    # Similar characters to avoid
    if no_similar_characters:
        similar_characters = "ilLI1oO0"
        numbers = numbers.translate(str.maketrans("", "", similar_characters))
        lowercase = lowercase.translate(str.maketrans("", "", similar_characters))
        uppercase = uppercase.translate(str.maketrans("", "", similar_characters))

    # Assemble the character set
    characters = ""
    if include_numbers:
        characters += numbers
    if include_lowercase:
        characters += lowercase
    if include_uppercase:
        characters += uppercase
    if include_symbols:
        characters += symbols

    if not characters:
        typer.echo("Error: No characters available to generate password.")
        raise typer.Exit()

    passwords = []
    for _ in range(quantity):
        while True:
            password = "".join(random.sample(characters, length))

            # Ensure it begins with a letter
            if begin_with_letter and not password[0].isalpha():
                continue

            # Check for sequential characters if required
            if no_sequential_characters:
                sequential_found = any(
                    ord(password[i]) == ord(password[i + 1]) - 1
                    for i in range(len(password) - 1)
                )
                if sequential_found:
                    continue

            # Check for duplicate characters if required
            if no_duplicate_characters:
                if len(set(password)) != len(password):
                    continue

            passwords.append(password)
            break

    if len(passwords) == 1:
        typer.echo(f"Password: {passwords[0]}")
    else:
        for i, pw in enumerate(passwords, 1):
            typer.echo(f"Password {i}: {pw}")


# =============================================================================


@app.command()
def check_permissions(
    username: str = typer.Option(None, prompt="Username"),
    password: str = typer.Option(None, prompt="Password", hide_input=True),
):

    # Step 1: Get the access token
    token, user_info = get_user_info(username=username, password=password)

    # TODO: use rich.console table
    if user_info:
        console = Console()

        # Create a table
        table = Table(title="User Information", box=HEAVY_EDGE)
        # Add columns to the table
        table.add_column("Field", style="bold")
        table.add_column("Value", style="green")

        # Add rows with the information
        table.add_row("Username", user_info["sub"])
        table.add_row("-" * 10, "-" * 10)
        
        table.add_row("Password", f"{'*' * len(password)}")
        table.add_row("-" * 10, "-" * 10)

        table.add_row("Email", user_info["email"])
        table.add_row("-" * 10, "-" * 10)

        table.add_row("UID", user_info["uid"])
        table.add_row("-" * 10, "-" * 10)

        table.add_row("Studies", "\n".join(user_info["studies"]))
        table.add_row("-" * 10, "-" * 10)

        table.add_row("Token", token)

        # Print the table
        console.print(table)


# =============================================================================
