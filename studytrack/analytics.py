class Analytics:
    def __init__(self, db): self.db = db

    def student_summary(self, student_id):
        assessments = [a for a in self.db["assessments"] if a["student_id"] == student_id]
        sessions = [s for s in self.db["sessions"] if s["student_id"] == student_id]
        avg = round(sum(a["percentage"] for a in assessments) / len(assessments), 2) if assessments else 0.0
        total_minutes = sum(s["minutes"] for s in sessions)
        return {"assessments": len(assessments), "average": avg, "study_minutes": total_minutes}

    def subject_report(self, student_id):
        rows = {}
        for a in self.db["assessments"]:
            if a["student_id"] == student_id:
                rows.setdefault(a["subject"], []).append(a["percentage"])
        return {subject: round(sum(values) / len(values), 2) for subject, values in rows.items()}

    def leaderboard(self):
        results = []
        for student in self.db["students"]:
            summary = self.student_summary(student["student_id"])
            results.append((student["name"], summary["average"], summary["study_minutes"]))
        return sorted(results, key=lambda row: (row[1], row[2]), reverse=True)

    def recommendations(self, student_id):
        report = self.subject_report(student_id)
        if not report:
            return ["Add assessment results to receive study recommendations."]
        weak = [subject for subject, avg in report.items() if avg < 60]
        strong = [subject for subject, avg in report.items() if avg >= 80]
        tips = []
        if weak:
            tips.append("Prioritize revision for: " + ", ".join(sorted(weak)) + ".")
        if strong:
            tips.append("Maintain performance in: " + ", ".join(sorted(strong)) + ".")
        if not tips:
            tips.append("Keep a balanced revision schedule and record more study sessions.")
        return tips
