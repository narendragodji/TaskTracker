# Task Tracker CLI

Simple Task Tracker CLI to add, update, delete, and list tasks.

Project URL: <REPLACE_WITH_YOUR_GITHUB_REPOSITORY_URL>

Usage examples:

```bash
# Add a task
python task-cli.py add "Buy groceries"

# Update a task
python task-cli.py update 1 "Buy groceries and cook dinner"

# Delete a task
python task-cli.py delete 1

# Mark in-progress
python task-cli.py mark-in-progress 1

# Mark done
python task-cli.py mark-done 1

# List all
python task-cli.py list

# List by status
python task-cli.py list done
```

Requirements:
- Python 3
- No external libraries

Instructions to publish to GitHub:

1. Create a public repository on GitHub (do not initialize with a README).
2. Run these commands in this project folder:

```bash
git init
git add .
git commit -m "Initial commit"
# replace URL below with the GitHub repo URL shown on GitHub
git remote add origin https://github.com/<your-username>/<repo-name>.git
git branch -M main
git push -u origin main
```

3. Replace the `Project URL` line at the top of this README with the repository URL.

Once you've pushed, return here with the public repository URL and I'll verify the README contains it and the repo looks correct.