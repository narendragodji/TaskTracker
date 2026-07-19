import datetime as dt
from os import path
import json


class TaskManager:
    VALID_STATUSES = {"todo", "in-progress", "done"}

    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = {}
        self.load_tasks()

    def load_tasks(self):
        if not path.exists(self.filename):
            self.tasks = {}
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(self.tasks, f)
            return

        with open(self.filename, "r", encoding="utf-8") as f:
            try:
                self.tasks = json.load(f)
            except json.JSONDecodeError:
                # If file is corrupted, reset to empty tasks
                self.tasks = {}

    def save_tasks(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)

    def get_next_id(self):
        if not self.tasks:
            return "1"

        numeric_ids = []
        for key in self.tasks.keys():
            try:
                numeric_ids.append(int(key))
            except (ValueError, TypeError):
                continue

        if not numeric_ids:
            return "1"

        return str(max(numeric_ids) + 1)

    # CRUD operations
    def add(self, description):
        next_id = self.get_next_id()
        now = str(dt.datetime.now())
        self.tasks[next_id] = {
            "id": next_id,
            "description": description,
            "status": "todo",
            "createdAt": now,
            "updatedAt": now,
        }
        self.save_tasks()
        print(f"Task added successfully (ID: {next_id})")

    def update(self, task_id, description):
        if task_id not in self.tasks:
            print(f"task with ID {task_id} does not exist")
            return
        self.tasks[task_id]["description"] = description
        self.tasks[task_id]["updatedAt"] = str(dt.datetime.now())
        self.save_tasks()
        print(f"Task {task_id} updated")

    def delete(self, task_id):
        if task_id not in self.tasks:
            print(f"task with ID {task_id} does not exist")
            return
        del self.tasks[task_id]
        self.save_tasks()
        print(f"Task {task_id} deleted")

    def mark_in_progress(self, task_id):
        if task_id not in self.tasks:
            print(f"task with ID {task_id} does not exist")
            return
        self.tasks[task_id]["status"] = "in-progress"
        self.tasks[task_id]["updatedAt"] = str(dt.datetime.now())
        self.save_tasks()
        print(f"Task {task_id} marked in-progress")

    def mark_done(self, task_id):
        if task_id not in self.tasks:
            print(f"task with ID {task_id} does not exist")
            return
        self.tasks[task_id]["status"] = "done"
        self.tasks[task_id]["updatedAt"] = str(dt.datetime.now())
        self.save_tasks()
        print(f"Task {task_id} marked done")

    def list_all(self):
        if not self.tasks:
            print("No tasks found")
            return
        for tid in sorted(self.tasks.keys(), key=lambda x: int(x) if x.isdigit() else x):
            t = self.tasks[tid]
            print(f"{tid}: [{t.get('status')}] {t.get('description')} (created: {t.get('createdAt')}, updated: {t.get('updatedAt')})")

    def list_by_status(self, status):
        if status not in self.VALID_STATUSES:
            print(f"Invalid status '{status}'. Valid: todo, in-progress, done")
            return
        found = False
        for tid, t in self.tasks.items():
            if t.get("status") == status:
                print(f"{tid}: {t.get('description')} (updated: {t.get('updatedAt')})")
                found = True
        if not found:
            print(f"No tasks with status '{status}'")
        
