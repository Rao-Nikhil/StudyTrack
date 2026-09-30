from .models import Student, StudySession, Assessment
from .validators import required, email, positive_int, non_negative_int, score, date_string

class StudentManager:
    def __init__(self, db):
        self.db = db

    def add(self, student_id, name, email_address, course, semester):
        if any(s["student_id"] == student_id for s in self.db["students"]):
            raise ValueError("Student ID already exists.")
        student = Student(required(student_id, "Student ID"), required(name, "Name"),
                          email(email_address), required(course, "Course"),
                          positive_int(semester, "Semester"))
        self.db["students"].append(student.to_dict())

    def update(self, student_id, name=None, email_address=None, course=None, semester=None):
        student = self.find(student_id)
        if not student:
            raise ValueError("Student not found.")
        if name is not None: student["name"] = required(name, "Name")
        if email_address is not None: student["email"] = email(email_address)
        if course is not None: student["course"] = required(course, "Course")
        if semester is not None: student["semester"] = positive_int(semester, "Semester")

    def delete(self, student_id):
        before = len(self.db["students"])
        self.db["students"] = [s for s in self.db["students"] if s["student_id"] != student_id]
        if len(self.db["students"]) == before:
            raise ValueError("Student not found.")
        self.db["sessions"] = [s for s in self.db["sessions"] if s["student_id"] != student_id]
        self.db["assessments"] = [a for a in self.db["assessments"] if a["student_id"] != student_id]

    def find(self, student_id):
        return next((s for s in self.db["students"] if s["student_id"] == student_id), None)

    def search(self, query):
        q = query.lower().strip()
        return [s for s in self.db["students"] if q in s["student_id"].lower() or q in s["name"].lower() or q in s["course"].lower()]

class StudyManager:
    def __init__(self, db): self.db = db

    def add(self, session_id, student_id, subject, date, minutes, topics):
        if any(s["session_id"] == session_id for s in self.db["sessions"]):
            raise ValueError("Session ID already exists.")
        if not any(s["student_id"] == student_id for s in self.db["students"]):
            raise ValueError("Student not found.")
        session = StudySession(required(session_id, "Session ID"), student_id, required(subject, "Subject"),
                               date_string(date), non_negative_int(minutes, "Minutes"), required(topics, "Topics"))
        self.db["sessions"].append(session.to_dict())

class AssessmentManager:
    def __init__(self, db): self.db = db

    def add(self, assessment_id, student_id, subject, title, score_value, max_score):
        if any(a["assessment_id"] == assessment_id for a in self.db["assessments"]):
            raise ValueError("Assessment ID already exists.")
        if not any(s["student_id"] == student_id for s in self.db["students"]):
            raise ValueError("Student not found.")
        maximum = float(max_score)
        if maximum <= 0: raise ValueError("Maximum score must be greater than zero.")
        assessment = Assessment(required(assessment_id, "Assessment ID"), student_id,
                                required(subject, "Subject"), required(title, "Title"),
                                score(score_value, maximum), maximum)
        self.db["assessments"].append(assessment.to_dict())
