# Task Tracker CLI

Simple Task Tracker CLI to add, update, delete, and list tasks.

Project URL: (https://roadmap.sh/projects/task-tracker)

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
