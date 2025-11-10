import json
from datetime import datetime
from pathlib import Path
from typing import Any, Optional
from uuid import uuid4

from nigel.enums import TaskStatus


class TaskServices:
    tasks_file = Path(__file__).parent / "tasks_store.json"

    def __init__(self):
        if not self.tasks_file.exists():
            self.tasks_file.write_text("[]")

    def load_tasks(self):
        with open(self.tasks_file, "r") as f:
            return json.load(f)

    def save_task(self, tasks: list[dict[str, Any]]):
        with open(self.tasks_file, "w") as f:
            json.dump(tasks, f, indent=2)

    def add_task(self, task_name: str):
        new_task = {
            "task_id": str(uuid4()),
            "description": task_name,
            "status": TaskStatus.TODO,
            "createdAt": str(datetime.now()),
            "updatedAt": str(datetime.now()),
        }
        tasks = self.load_tasks()
        tasks.append(new_task)
        self.save_task(tasks)

    def remove_task(self, task_id: str):
        tasks = self.load_tasks()

        if not tasks:
            return

        tasks = [task for task in tasks if task["task_id"] != task_id]
        self.save_task(tasks)

    def update_task(
        self,
        task_id: str,
        description: Optional[str] = None,
        status: Optional[str] = None,
    ):
        tasks = self.load_tasks()

        if not tasks:
            return

        for task in tasks:
            if task["task_id"] == task_id:
                if description is not None:
                    task["description"] = description

                if status is not None:
                    task["status"] = status

                from datetime import datetime

                task["updatedAt"] = str(datetime.now())

        self.save_task(tasks)

    def list_task(self, status: Optional[str] = None):
        tasks = self.load_tasks()

        if not tasks:
            return

        if status:
            tasks = [task for task in tasks if task["status"] == status]

        self.print_tasks(tasks)

    def print_tasks(self, tasks: list[dict[str, Any]]):
        for task in tasks:
            print(f"Task ID:  {task['task_id']}")
            print(f"Task Description:  {task['description']}")
            print(f"Task status:  {task['status']}")
            print(f"Task created at:  {task['createdAt']}")
            print(f"Task updated at:  {task['updatedAt']}")
