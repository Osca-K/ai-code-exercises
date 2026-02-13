# Task Manager

A cross-language task management system for creating, organizing, and prioritizing tasks. Includes CLI and programmatic interfaces in Python, JavaScript, and Java.

## Features
- Add, update, and delete tasks
- Set priorities, due dates, and tags
- Mark tasks as done or in review
- Sort and filter tasks by importance
- Merge and sync task lists
- Command-line interface (CLI)
- Modular code structure for easy extension

## Technologies Used
- Python 3.8+
- JavaScript (Node.js 14+)
- Java 11+

## Installation

### Python
1. Navigate to `task-manager/python`
2. (Optional) Create a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### JavaScript
1. Navigate to `task-manager/javascript`
2. Install dependencies:
   ```bash
   npm install
   ```

### Java
1. Navigate to `task-manager/java`
2. Build the project:
   ```bash
   ./gradlew build
   ```

## Usage Examples

### Python CLI
```bash
python cli.py add "Buy groceries" --priority high --due 2026-02-15
python cli.py list --sort priority
```

### JavaScript CLI
```bash
node cli.js add "Finish report" --priority urgent --tag work
node cli.js list --filter done
```

### Java (Programmatic)
```java
TaskManager manager = new TaskManager();
manager.addTask("Read book", Priority.MEDIUM);
manager.listTasks();
```

## Configuration Options
- Task storage location (file/database)
- Custom priority weights
- Tag and status definitions

## Troubleshooting
- Ensure all dependencies are installed for your language
- For Python, activate your virtual environment if using one
- For Java, ensure Java 11+ and Gradle are installed
- For JavaScript, use Node.js 14+ and npm

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

## License
MIT License

## Code Structure Overview
```
task-manager/
  java/        # Java implementation
    app/
    cli/
    model/
    storage/
  javascript/  # JavaScript implementation
    app.js
    cli.js
    models.js
    storage.js
  python/      # Python implementation
    app.py
    cli.py
    models.py
    storage.py
```
