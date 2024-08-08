# axe/cli.py
import os
import typer
import inquirer
import axe.gitignore_api as api

app = typer.Typer()


@app.command()
def list():
    """📝 List all available .gitignore templates"""
    template_list = api.get_template_list()
    if template_list:
        typer.echo("\n".join(template_list))
    else:
        typer.echo("No templates found.")


@app.command()
def search(term: str):
    """🔍 Search for term in list of available templates"""
    template_list = api.get_template_list()
    matches = [
        template for template in template_list if
        term.lower() in template.lower()
    ]

    emojis = ["1️⃣", "1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣",
              "9️⃣","*️⃣"]

    if matches:
        for idx, match in enumerate(matches):
            emoji = emojis[idx] if idx < len(emojis) else emojis[-1]
            typer.echo(f"{emoji} {match}")
    else:
        typer.echo(f"No templates found for term: {term}")


@app.command()
def new(stack: str):
    """🆕 Create a new .gitignore for the given technologies"""
    gi_stack = stack.split()
    try:
        axe_file = api.get_gitignore(gi_stack)
    except ValueError as ve:
        typer.echo(
            f"❌ ERROR: {ve.args[0]} is invalid or is not supported on gitignore.io."
        )
        raise typer.Exit(code=1)

    axe_file = f"{axe_file}\n# Generated using axe"

    if os.path.isfile(".gitignore"):
        questions = [
            inquirer.List(
                "action",
                message=".gitignore exists in current directory. Continue?",
                choices=["🔄 Backup (b)", "✏️ Overwrite (o)", "🚫 Cancel (c)"],
                carousel=True,
            )
        ]
        answers = inquirer.prompt(questions)

        choice = answers["action"].split(" ")[-1]  # Extract the last part (b, o, c)

        if choice in ["(b)", "backup"]:
            typer.echo("🔄 Backing up .gitignore as 'OLD_gitignore'...")
            os.rename(".gitignore", "OLD_gitignore")
        elif choice in ["(o)", "overwrite"]:
            pass
        elif choice in ["(c)", "cancel"]:
            typer.echo("🚫 Ok. Exiting...")
            raise typer.Exit()
        else:
            typer.echo("Please respond with 'b', 'o' or 'c'.")
            raise typer.Exit(code=1)

    with open(".gitignore", "w") as f:
        f.write(axe_file)

    typer.echo(f"✅ New .gitignore file generated for {', '.join(gi_stack)}.")


@app.command()
def preview(stack: str):
    """🔍 Preview .gitignore for the given technologies"""
    gi_stack = stack.split()
    try:
        axe_file = api.get_gitignore(gi_stack)
    except ValueError as ve:
        typer.echo(
            f"❌ ERROR: {ve.args[0]} is invalid or is not supported on gitignore.io."
        )
        raise typer.Exit(code=1)

    axe_file = f"{axe_file}\n# Generated using axe"
    typer.echo(axe_file)


if __name__ == "__main__":
    app()
