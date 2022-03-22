Analysis Phase: Gantt Diagram - Template
```mermaid
gantt

    title Example Gantt diagram
    dateFormat  YYYY-MM-DD

    section Team 1
    Research & requirements :done, a1, 2000-01-01, 2000-01-20
    Review & documentation  :after a1, 2000-01-14, 20d

    section Team 2
    Implementation      :crit, active, 2000-02-01, 20d
    Testing             :crit, 20d
```