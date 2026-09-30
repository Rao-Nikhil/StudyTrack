from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class Student:
    student_id: str
    name: str
    email: str
    course: str
    semester: int

    def to_dict(self):
        return asdict(self)

@dataclass
class StudySession:
    session_id: str
    student_id: str
    subject: str
    date: str
    minutes: int
    topics: str

    def to_dict(self):
        return asdict(self)

@dataclass
class Assessment:
    assessment_id: str
    student_id: str
    subject: str
    title: str
    score: float
    max_score: float

    def percentage(self) -> float:
        return round((self.score / self.max_score) * 100, 2) if self.max_score else 0.0

    def to_dict(self):
        data = asdict(self)
        data["percentage"] = self.percentage()
        return data
