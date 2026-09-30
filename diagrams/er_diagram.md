# Storage / ER Diagram

Relationships:

- STUDENT 1 → many STUDY_SESSION records
- STUDENT 1 → many ASSESSMENT records

STUDENT fields: student_id, name, email, course, semester.

STUDY_SESSION fields: session_id, student_id, subject, date, minutes, topics.

ASSESSMENT fields: assessment_id, student_id, subject, title, score, max_score, percentage.
