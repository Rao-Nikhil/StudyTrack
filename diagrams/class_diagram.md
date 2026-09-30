# Class / Component Diagram

Core classes/components:

- Student
- StudySession
- Assessment
- StudentManager
- StudyManager
- AssessmentManager
- Analytics
- ReportGenerator
- JSONStorage

Managers create and update their corresponding models. Analytics reads stored data, and ReportGenerator uses Analytics to create reports.
