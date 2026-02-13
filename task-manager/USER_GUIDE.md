# Task Manager User Guide

## How to Add a New Task

This guide walks you through adding a new task using the Task Manager CLI.

### Prerequisites
- Task Manager installed (see README for setup)
- Terminal or command prompt access
- Basic familiarity with command-line usage

### Steps

1. **Open your terminal**
2. **Navigate to the Task Manager directory**
   - For Python: `cd task-manager/python`
   - For JavaScript: `cd task-manager/javascript`
3. **Run the add command**
   - **Python:**
     ```bash
     python cli.py add "Write project report" --priority high --due 2026-02-20 --tag work
     ```
   - **JavaScript:**
     ```bash
     node cli.js add "Write project report" --priority high --due 2026-02-20 --tag work
     ```
4. **Verify the task was added**
   - **Python:**
     ```bash
     python cli.py list
     ```
   - **JavaScript:**
     ```bash
     node cli.js list
     ```

### Example Output
```
ID   | Title               | Priority | Due Date   | Status | Tags
-----|---------------------|----------|------------|--------|------
1    | Write project report| HIGH     | 2026-02-20 | TODO   | work
```

### Common Issues & Troubleshooting
- **Command not found:** Ensure you are in the correct directory and have installed dependencies.
- **Date format errors:** Use `YYYY-MM-DD` for due dates.
- **Permission denied:** Try running the command as an administrator or check file permissions.

### Tips
- Use `--help` with any command to see available options:
  - `python cli.py --help`
  - `node cli.js --help`
- You can add multiple tags by repeating the `--tag` option.

---
User experience level: Beginner to Intermediate
