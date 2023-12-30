# KeePassGitSync

A tool that automatically updates your KeePass database file using git.

## Requirements

- A git repo with your database file in it. (Make sure it is private)
- An SSH key must be generated
- A Windows or Linux machine with Python 3.10+ and git installed

## Dev
```bash
pip install --user poetry
poetry update
poetry install
```

To Run (help menu):
```bash
poetry run kpg-sync -h
```


## Config File Structure

```json
{
    "repoURL": "git@github.com:JudgeGlass/KeePassTest.git",
    "databaseFile": "KeePass_Database.kdbx",
    "location": "/home/judgeglass/Documents/",
    "updateFrequency": 5.0,
    "showMessages": false
}
```

The program also has mirroring command line arguments
