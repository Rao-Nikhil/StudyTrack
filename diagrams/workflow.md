# Process Workflow

Mermaid diagram:

    flowchart TD
        A[Start] --> B[Load JSON]
        B --> C[Display Menu]
        C --> D{Operation}
        D --> E[Student Management]
        D --> F[Study Session]
        D --> G[Assessment]
        D --> H[Analytics]
        D --> I[Report]
        E --> J[Validate]
        F --> J
        G --> J
        J --> K[Save JSON]
        H --> C
        I --> C
        K --> C
        D --> L[Exit]
