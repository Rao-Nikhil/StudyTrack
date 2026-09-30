import json
from pathlib import Path

class JSONStorage:
    """Simple JSON persistence layer using only the Python standard library."""
    def __init__(self, path: str = "data/studytrack.json"):
        self.path = Path(path)

    def load(self) -> dict:
        if not self.path.exists():
            return {"students": [], "sessions": [], "assessments": []}
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            return {
                "students": data.get("students", []),
                "sessions": data.get("sessions", []),
                "assessments": data.get("assessments", []),
            }
        except (json.JSONDecodeError, OSError):
            return {"students": [], "sessions": [], "assessments": []}

    def save(self, data: dict) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(".tmp")
        with temp.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        temp.replace(self.path)
