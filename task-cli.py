import sys
from taskmanager import TaskManager

USAGE = (
    "Usage:\n"
    "  task-cli add \"<description>\"\n"
    "  task-cli update <id> \"<description>\"\n"
    "  task-cli delete <id>\n"
    "  task-cli mark-in-progress <id>\n"
    "  task-cli mark-done <id>\n"
    "  task-cli list [done|todo|in-progress]"
)

tm = TaskManager()

if len(sys.argv) == 1:
    print(USAGE)
    sys.exit(1)

command = sys.argv[1]

try:
    if command == "add":
        tm.add(sys.argv[2])

    elif command == "update":
        tm.update(sys.argv[2], sys.argv[3])

    elif command == "delete":
        tm.delete(sys.argv[2])

    elif command == "mark-in-progress":
        tm.mark_in_progress(sys.argv[2])

    elif command == "mark-done":
        tm.mark_done(sys.argv[2])

    elif command == "list":
        if len(sys.argv) == 2:
            tm.list_all()
        else:
            tm.list_by_status(sys.argv[2])

    else:
        print(f"Unknown command '{command}'")
        print(USAGE)
        sys.exit(1)

except IndexError:
    print(f"Missing arguments for '{command}'")
    print(USAGE)
    sys.exit(1)