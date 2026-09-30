from datetime import datetime
from pathlib import Path

class ReportGenerator:
    def __init__(self, db, analytics):
        self.db, self.analytics = db, analytics

    def student_report(self, student_id, output_dir="reports"):
        student = next((s for s in self.db["students"] if s["student_id"] == student_id), None)
        if not student: raise ValueError("Student not found.")
        summary = self.analytics.student_summary(student_id)
        subjects = self.analytics.subject_report(student_id)
        tips = self.analytics.recommendations(student_id)
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        path = Path(output_dir) / f"student_{student_id}.txt"
        lines = ["STUDYTRACK STUDENT REPORT", "=" * 28, f"Generated: {datetime.now():%Y-%m-%d %H:%M}", "",
                 f"Student: {student['name']}", f"ID: {student['student_id']}", f"Course: {student['course']}",
                 f"Semester: {student['semester']}", "", "SUMMARY", "-------",
                 f"Assessments: {summary['assessments']}", f"Average score: {summary['average']}%",
                 f"Study time: {summary['study_minutes']} minutes", "", "SUBJECT PERFORMANCE", "-------------------"]
        lines += [f"{subject}: {avg}%" for subject, avg in sorted(subjects.items())]
        lines += ["", "RECOMMENDATIONS", "---------------"] + [f"- {tip}" for tip in tips]
        path.write_text("
".join(lines), encoding="utf-8")
        return str(path)
