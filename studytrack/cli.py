from .storage import JSONStorage
from .managers import StudentManager, StudyManager, AssessmentManager
from .analytics import Analytics
from .reports import ReportGenerator

class StudyTrackApp:
    def __init__(self):
        self.storage = JSONStorage()
        self.db = self.storage.load()
        self.students = StudentManager(self.db)
        self.study = StudyManager(self.db)
        self.assessments = AssessmentManager(self.db)
        self.analytics = Analytics(self.db)
        self.reports = ReportGenerator(self.db, self.analytics)

    def save(self): self.storage.save(self.db)

    @staticmethod
    def ask(prompt): return input(prompt).strip()

    def menu(self):
        print("\n=== STUDYTRACK ===")
        print("1. Add student")
        print("2. List students")
        print("3. Search students")
        print("4. Update student")
        print("5. Delete student")
        print("6. Add study session")
        print("7. Add assessment")
        print("8. Student analytics")
        print("9. Leaderboard")
        print("10. Generate student report")
        print("0. Exit")

    def run(self):
        print("Welcome to StudyTrack — Student Study & Performance Manager")
        while True:
            self.menu()
            choice = self.ask("Choose an option: ")
            try:
                if choice == "1": self.add_student()
                elif choice == "2": self.list_students()
                elif choice == "3": self.search_students()
                elif choice == "4": self.update_student()
                elif choice == "5": self.delete_student()
                elif choice == "6": self.add_session()
                elif choice == "7": self.add_assessment()
                elif choice == "8": self.analytics_view()
                elif choice == "9": self.leaderboard()
                elif choice == "10": print("Report created:", self.reports.student_report(self.ask("Student ID: ")))
                elif choice == "0": self.save(); print("Data saved. Goodbye!"); return
                else: print("Invalid option.")
                self.save()
            except ValueError as exc:
                print("Error:", exc)
            except (EOFError, KeyboardInterrupt):
                self.save(); print("\nData saved. Goodbye!"); return

    def add_student(self):
        self.students.add(self.ask("Student ID: "), self.ask("Name: "), self.ask("Email: "), self.ask("Course: "), self.ask("Semester: "))
        print("Student added successfully.")

    def list_students(self):
        rows = self.db["students"]
        if not rows: print("No students found."); return
        for s in rows: print(f"{s['student_id']} | {s['name']} | {s['course']} | Semester {s['semester']}")

    def search_students(self):
        rows = self.students.search(self.ask("Search name, ID, or course: "))
        for s in rows: print(f"{s['student_id']} | {s['name']} | {s['course']}")
        if not rows: print("No matching students.")

    def update_student(self):
        sid = self.ask("Student ID: ")
        print("Press Enter to keep an existing value.")
        self.students.update(sid, self.ask("New name: ") or None, self.ask("New email: ") or None,
                             self.ask("New course: ") or None, self.ask("New semester: ") or None)
        print("Student updated.")

    def delete_student(self):
        self.students.delete(self.ask("Student ID: "))
        print("Student and related records deleted.")

    def add_session(self):
        self.study.add(self.ask("Session ID: "), self.ask("Student ID: "), self.ask("Subject: "),
                       self.ask("Date (YYYY-MM-DD): "), self.ask("Minutes: "), self.ask("Topics covered: "))
        print("Study session recorded.")

    def add_assessment(self):
        self.assessments.add(self.ask("Assessment ID: "), self.ask("Student ID: "), self.ask("Subject: "),
                             self.ask("Assessment title: "), self.ask("Score: "), self.ask("Maximum score: "))
        print("Assessment recorded.")

    def analytics_view(self):
        sid = self.ask("Student ID: ")
        s = self.students.find(sid)
        if not s: raise ValueError("Student not found.")
        summary = self.analytics.student_summary(sid)
        print(f"Average: {summary['average']}% | Study time: {summary['study_minutes']} min")
        print("Subjects:", self.analytics.subject_report(sid))
        for tip in self.analytics.recommendations(sid): print("-", tip)

    def leaderboard(self):
        for i, row in enumerate(self.analytics.leaderboard(), 1):
            print(f"{i}. {row[0]} | Average: {row[1]}% | Study: {row[2]} min")

def main(): StudyTrackApp().run()
