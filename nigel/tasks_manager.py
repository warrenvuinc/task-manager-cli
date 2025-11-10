import argparse

from nigel.tasks_services import TaskServices


def main():
    task_services = TaskServices()
    parser = argparse.ArgumentParser(description="My CLI tool example")
    subparsers = parser.add_subparsers(title="commands", dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("name", help="Name of the task to add")

    update_parser = subparsers.add_parser("update", help="Update a task")
    update_parser.add_argument("id", help="ID of task")
    update_parser.add_argument("description", help="Description of task")

    remove_parser = subparsers.add_parser("delete", help="Delete a task")
    remove_parser.add_argument("id", help="ID of task")

    mark_in_progress_parser = subparsers.add_parser(
        "mark-in-progress", help="Marking a task as in progress"
    )
    mark_in_progress_parser.add_argument("id", help="ID of task")
    mark_done_parser = subparsers.add_parser(
        "mark-in-done", help="Marking a task as in progress"
    )
    mark_done_parser.add_argument("id", help="ID of task")

    list_task = subparsers.add_parser("list", help="List all task")
    list_task.add_argument(
        "--status",
        help="List by status",
    )

    args = parser.parse_args()

    if args.command == "add":
        task_services.add_task(args.name)

    if args.command == "update":
        task_services.update_task(args.id, description=args.description)

    if args.command == "delete":
        task_services.remove_task(args.id)

    if args.command == "mark-in-progress":
        task_services.update_task(task_id=args.id, status="in-progress")

    if args.command == "mark-in-done":
        task_services.update_task(task_id=args.id, status="done")

    if args.command == "list":
        if not args.status:
            task_services.list_task()

        if args.status:
            task_services.list_task(status=args.status)


if __name__ == "__main__":
    main()
