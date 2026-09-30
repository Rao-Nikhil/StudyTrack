# System Architecture

Mermaid diagram:

    flowchart TD
        U[User] --> C[CLI]
        C --> M[Management Layer]
        M --> S[JSON Storage]
        M --> A[Analytics]
        A --> R[Report Generator]
        S --> D[(studytrack.json)]
        R --> O[Text Report]
