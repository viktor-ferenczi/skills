# Design & Architecture

- **SOLID**:
  - **S**ingle Responsibility — A module/class should have exactly one reason to change.
  - **O**pen/Closed — Open for extension, closed for modification.
  - **L**iskov Substitution — Subtypes must be usable anywhere their base type is expected without surprises.
  - **I**nterface Segregation — Many small, client-specific interfaces beat one fat interface.
  - **D**ependency Inversion — Depend on abstractions, not concrete implementations.
- **SoC** (Separation of Concerns) — Split the system so each part addresses one concern (UI, business logic, persistence, ...).
- **LoD** (Law of Demeter) — Talk only to your immediate collaborators; avoid chained reach-through like `a.getB().getC().doX()`.
- **Composition over Inheritance** — Assemble behavior from small components instead of deep class hierarchies.
- **GRASP** (General Responsibility Assignment) — Assign responsibilities to the class that has the information to fulfill them (Information Expert, Creator, Controller, Low Coupling, High Cohesion, ...).
- **Libraries over Frameworks** — You call a library; a framework calls you. Prefer composable libraries that stay behind small interfaces; adopt a framework only when its conventions carry their weight, since it dictates architecture and creates lock-in.
- **Convention over Configuration** — Provide sensible defaults; require configuration only for deviations.
- **Twelve-Factor App** — For services: config in the environment, stateless processes, logs as event streams, dev/prod parity, disposability.
