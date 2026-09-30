# StudyTrack — Student Study & Performance Manager

## Overview
StudyTrack is a command-line Python application for managing student records, recording study sessions and assessments, and generating performance analytics and text reports. It demonstrates Python fundamentals, modular programming, object-oriented data models, validation, exception handling, JSON file persistence, testing, and reporting.

## Major Functional Modules
1. **Student Management** — add, list, search, update, and delete student records.
2. **Study Session Management** — record study date, subject, duration, and topics.
3. **Assessment Management** — record assessment scores and automatically calculate percentages.
4. **Analytics** — calculate averages, subject performance, study time, leaderboard, and recommendations.
5. **Reporting** — generate a student performance report as a text file.

## Technologies
- Python 3.10+
- Python standard library
- JSON for persistent storage
- `unittest` for tests
- Git/GitHub for version control

## Project Structure
```text
.
├── main.py
├── studytrack/
│   ├── __init__.py
│   ├── analytics.py
│   ├── cli.py
│   ├── managers.py
│   ├── models.py
│   ├── reports.py
│   ├── storage.py
│   └── validators.py
├── data/
│   └── studytrack.json
├── tests/
│   └── test_project.py
├── diagrams/
├── requirements.txt
├── statement.md
└── README.md
```

## Requirements
- Python 3.10 or newer
- A terminal/command prompt
- No external Python packages are required.

## Installation
Clone the repository and enter the project directory:

```bash
git clone <YOUR_PUBLIC_REPOSITORY_URL>
cd studytrack
```

Create and activate a virtual environment (recommended):

### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows
```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install the declared requirements:

```bash
python -m pip install -r requirements.txt
```

## Run
From the repository root:

```bash
python main.py
```

The application presents a numbered command-line menu.

## Testing
Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

## Data and Configuration
The application stores data in `data/studytrack.json`. The program creates the directory/file if it does not exist. The project uses no API keys or external services.

## Example Workflow
1. Add a student.
2. Record one or more study sessions.
3. Record assessment scores.
4. Open student analytics to see average score and study time.
5. Generate a student report.

## Error Handling
The application validates IDs, emails, dates, numeric values, score ranges, required fields, and duplicate IDs. Invalid operations are reported to the user instead of terminating the application.

## Future Enhancements
- SQLite database support
- CSV/PDF report export
- Interactive charts
- Login and role-based access
- Reminder scheduling

## Academic Scope
The project is designed for the Python Essentials course and focuses on applying core Python concepts in a complete command-line application.
