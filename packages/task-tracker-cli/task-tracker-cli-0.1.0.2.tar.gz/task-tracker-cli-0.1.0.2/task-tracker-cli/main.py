import os
import json
from datetime import datetime
import click
from prettytable import PrettyTable

table = PrettyTable()

TASK_FILE = 'tasks.json'


def load_tasks():
    """Load tasks from the JSON file."""
    if TASK_FILE in os.listdir():
        with open(TASK_FILE, 'r') as file_handle:
            return json.load(file_handle)
    return {"tasks": []}


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASK_FILE, 'w', encoding='utf8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


@click.group()
@click.pass_context
def cli(ctx):
    ctx.ensure_object(dict)
    ctx.obj['tasks'] = load_tasks()


@cli.command()
@click.argument('description')
@click.pass_context
def add(ctx, description):
    tasks = ctx.obj['tasks']

    if any(task.get("description") == description for task in tasks["tasks"]):
        click.echo('Task already added.')
        return

    task_id = tasks["tasks"][-1]["id"] + 1 if tasks["tasks"] else 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': str(datetime.now())
    }
    tasks["tasks"].append(task)
    save_tasks(tasks)
    click.echo(f'Task added successfully (ID: {task["id"]})')


@cli.command()
@click.argument('task_id', type=int)
@click.argument('description')
@click.pass_context
def update(ctx, task_id, description):
    tasks = ctx.obj['tasks']

    for task in tasks["tasks"]:
        if task.get("id") == task_id:
            if task["description"] == description:
                click.echo('No changes to the task.')
                return
            task["description"] = description
            task["updatedAt"] = str(datetime.now())
            save_tasks(tasks)
            click.echo(f'Task description updated (ID: {task["id"]}).')
            return
    click.echo("Task doesn't exist")


@cli.command()
@click.argument('task_id', type=int)
@click.pass_context
def delete(ctx, task_id):
    tasks = ctx.obj['tasks']

    for task in tasks["tasks"]:
        if task.get("id") == task_id:
            tasks["tasks"].remove(task)
            save_tasks(tasks)
            click.echo('Task deleted.')
            return
    click.echo("Task doesn't exist")


@cli.command()
@click.argument('task_id', type=int)
@click.pass_context
def mark_in_progress(ctx, task_id):
    tasks = ctx.obj['tasks']

    for task in tasks["tasks"]:
        if task.get("id") == task_id:
            if task["status"] == "in-progress":
                click.echo('No changes to the task.')
                return
            task["status"] = "in-progress"
            task["updatedAt"] = str(datetime.now())
            save_tasks(tasks)
            click.echo(f'Task status updated (ID: {task["id"]}).')
            return
    click.echo("Task doesn't exist")


@cli.command()
@click.argument('task_id', type=int)
@click.pass_context
def mark_done(ctx, task_id):
    tasks = ctx.obj['tasks']

    for task in tasks["tasks"]:
        if task.get("id") == task_id:
            if task["status"] == "done":
                click.echo('No changes to the task.')
                return
            task["status"] = "done"
            task["updatedAt"] = str(datetime.now())
            save_tasks(tasks)
            click.echo(f'Task status updated (ID: {task["id"]}).')
            return
    click.echo("Task doesn't exist")


@cli.command()
@click.argument('status', required=False)
@click.pass_context
def list(ctx, status=None):
    tasks = ctx.obj['tasks']

    if tasks.get("tasks"):
        table.field_names = ["id", "description", "status", "createdAt", "updatedAt"]
        for task in tasks["tasks"]:
            if status is None or task["status"] == status:
                table.add_row([
                    task["id"],
                    task["description"],
                    task["status"],
                    task["createdAt"],
                    task.get("updatedAt", "N/A")  # Using get() to avoid KeyError
                ])
        if table.rows:
            click.echo(table)
            return
    click.echo("No tasks found.")


if __name__ == '__main__':
    cli(obj={})
