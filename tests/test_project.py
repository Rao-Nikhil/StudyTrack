import tempfile
import unittest
from pathlib import Path
from studytrack.storage import JSONStorage
from studytrack.managers import StudentManager, StudyManager, AssessmentManager
from studytrack.analytics import Analytics

class StudyTrackTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.db = JSONStorage(str(Path(self.tmp.name) / "data.json")).load()
        self.students = StudentManager(self.db)
        self.study = StudyManager(self.db)
        self.assessments = AssessmentManager(self.db)
        self.analytics = Analytics(self.db)

    def tearDown(self): self.tmp.cleanup()

    def test_add_student(self):
        self.students.add("S01", "Aarav", "aarav@example.com", "Python", "2")
        self.assertEqual(self.students.find("S01")["name"], "Aarav")

    def test_duplicate_student_rejected(self):
        self.students.add("S01", "Aarav", "aarav@example.com", "Python", "2")
        with self.assertRaises(ValueError):
            self.students.add("S01", "Other", "other@example.com", "Python", "2")

    def test_assessment_percentage_and_summary(self):
        self.students.add("S01", "Aarav", "aarav@example.com", "Python", "2")
        self.assessments.add("A01", "S01", "Python", "Quiz 1", "80", "100")
        self.study.add("T01", "S01", "Python", "2026-09-30", "90", "Functions")
        summary = self.analytics.student_summary("S01")
        self.assertEqual(summary["average"], 80.0)
        self.assertEqual(summary["study_minutes"], 90)

    def test_invalid_email_rejected(self):
        with self.assertRaises(ValueError):
            self.students.add("S01", "Aarav", "bad-email", "Python", "2")

if __name__ == "__main__": unittest.main()
