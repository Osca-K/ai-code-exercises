# Task Manager FAQ

## General

**Q: What is Task Manager?**  
A: Task Manager is a cross-language system for creating, organizing, and prioritizing tasks, with CLI and programmatic interfaces in Python, JavaScript, and Java.

**Q: Who is this tool for?**  
A: Developers, students, and anyone who wants to manage tasks from the command line or integrate task management into their own code.

## Getting Started

**Q: How do I install Task Manager?**  
A: See the README for installation instructions for Python, JavaScript, and Java versions.

**Q: What are the prerequisites?**  
A: Python 3.8+, Node.js 14+, or Java 11+, depending on your chosen implementation.

## Features & Usage

**Q: How do I add a new task?**  
A: Use the CLI:  
- Python: `python cli.py add "Task name" --priority high --due 2026-02-20`  
- JavaScript: `node cli.js add "Task name" --priority high --due 2026-02-20`

**Q: How do I list all tasks?**  
A:  
- Python: `python cli.py list`  
- JavaScript: `node cli.js list`

**Q: Can I set tags and priorities?**  
A: Yes, use `--tag` and `--priority` options when adding or updating tasks.

**Q: How do I mark a task as done?**  
A:  
- Python: `python cli.py done <task_id>`  
- JavaScript: `node cli.js done <task_id>`

## Troubleshooting

**Q: The CLI command is not found. What should I do?**  
A: Make sure you are in the correct directory and have installed all dependencies.

**Q: I get a date format error.**  
A: Use the `YYYY-MM-DD` format for due dates.

**Q: How do I reset or clear all tasks?**  
A: Delete the storage file (e.g., `tasks.json` or `tasks.db`) in the project directory. This will remove all tasks.

## Advanced

**Q: Can I extend Task Manager with new features?**  
A: Yes! The code is modular. See the code structure in the README for where to add new commands or features.

**Q: Is there a way to sync tasks between different language versions?**  
A: Not out of the box, but you can export/import tasks using JSON or CSV and write scripts to sync them.

## Known Issues

- Some features may differ slightly between language implementations.
- Large task lists may slow down the CLI; consider archiving old tasks.

---
Target audience: Developers and CLI users
