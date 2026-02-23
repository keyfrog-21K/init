# git_init.py
# Initialize Git repository for Project and remote repository on git providers.
# Using subprocess module to run git commands.

import subprocess
from pathlib import Path


def run_git(cmd, path):
    result = subprocess.run(
        ["git"] + cmd,
        cwd=path,
        capture_output=True,
        text=True
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip())
    return result.stdout.strip()


def git_init(path: str, remote_url: str | None = None):
    path = str(Path(path).resolve())

    if not Path(path).exists():
        raise FileNotFoundError("Project path does not exist")

    run_git(["init"], path)
    run_git(["add", "."], path)
    run_git(["commit", "-m", "Initial commit"], path)
    run_git(["branch", "-M", "main"], path)

    if remote_url:
        run_git(["remote", "add", "origin", remote_url], path)

    return "Git initialized successfully \n to push to remote repository, run: git push -u origin main"

