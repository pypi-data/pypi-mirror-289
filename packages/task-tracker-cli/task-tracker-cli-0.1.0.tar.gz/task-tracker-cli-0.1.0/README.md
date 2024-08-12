
# Task Tracker CLI

Task Tracker CLI is a simple command-line interface (CLI) application for managing tasks. You can add, update, delete, and list tasks with various statuses. This tool is perfect for keeping track of your to-do items right from your terminal.

## Features

- **Add Tasks:** Easily add new tasks to your list.
- **Update Tasks:** Modify the description of existing tasks.
- **Delete Tasks:** Remove tasks that are no longer needed.
- **Change Task Status:** Mark tasks as in-progress or done.
- **List Tasks:** Display tasks filtered by status.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/under-script/task-tracker-cli.git
   ```
2. **Navigate to the Project Directory:**
   ```bash
   cd task-tracker-cli
   ```
3. **Install Dependencies:**
   Ensure you have Python installed. Then, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start using the Task Tracker CLI, simply run the Python script with the desired commands.

### Adding a Task

Add a new task by providing a description:
```bash
python main.py add "Your task description"
```

### Updating a Task

Update the description of an existing task by specifying its ID and the new description:
```bash
python main.py update <task_id> "Updated task description"
```

### Deleting a Task

Delete a task by specifying its ID:
```bash
python main.py delete <task_id>
```

### Marking a Task as In-Progress

Change the status of a task to "in-progress":
```bash
python main.py mark_in_progress <task_id>
```

### Marking a Task as Done

Change the status of a task to "done":
```bash
python main.py mark_done <task_id>
```

### Listing Tasks

List all tasks, optionally filtering by status:
```bash
# List all tasks
python main.py list

# List only tasks with a specific status (e.g., todo, in-progress, done)
python main.py list <status>
```

**Note:** The `status` argument is optional. If not provided, all tasks will be listed.

## Task File

All tasks are stored in a `tasks.json` file in the project directory. The structure of this file is managed automatically by the CLI.

### Task Structure

Each task has the following attributes:
- `id`: Unique identifier for the task.
- `description`: The text description of the task.
- `status`: Current status of the task (`todo`, `in-progress`, or `done`).
- `createdAt`: The timestamp when the task was created.
- `updatedAt`: The timestamp when the task was last updated (optional).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [abdulmajidyunusov18@gmail.com].

---

Happy task tracking!