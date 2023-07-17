import os
import subprocess
import click


REPOS = [
    "ploomber/dummy",
    "ploomber/jupysql",
    "ploomber/ploomber",
    "ploomber/ploomber-engine",
    "ploomber/soopervisor",
    "ploomber/sklearn-evaluation",
    "ploomber/cloud-backend",
    "ploomber/cloud-frontend",
    "ploomber/pkgmt",
    "ploomber/contributing",
    "ploomber/core",
    "ploomber/jupysql-plugin",
    "ploomber/ploomber.io",
]


def _sync(repo, access_token, dry_run):
    parts = [
        "github-label-sync",
        repo,
        "--access-token",
        access_token,
        "--labels",
        "labels.yaml",
    ]

    if dry_run:
        parts.append("--dry-run")

    subprocess.check_call(parts)


@click.command()
@click.option("--dry-run", is_flag=True, help="Perform a dry run")
@click.option("--all-repos", is_flag=True, help="Apply changes to all repositories")
@click.argument("repo", required=False, default="ploomber/dummy")
def cli(repo, dry_run, all_repos):
    if not dry_run and all_repos:
        input_ = click.prompt(
            "Are you sure you want to apply changes to all repos? "
            "Enter apply to continue",
            type=str,
        )

        if input_ != "apply":
            raise click.ClickException("Aborted")

    if dry_run:
        click.echo("Performing dry run...")
    else:
        click.echo("Applying changes...")

    ACCESS_TOKEN = os.environ.get("GITHUB_TOKEN")

    if not ACCESS_TOKEN:
        raise click.ClickException("GITHUB_TOKEN environment variable not set.")

    if not all_repos:
        _sync(repo, ACCESS_TOKEN, dry_run)
    else:
        for repo in REPOS:
            _sync(repo, ACCESS_TOKEN, dry_run)


if __name__ == "__main__":
    cli()
