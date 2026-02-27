📘 PROJECT SPECIFICATION
Project Name: Poultry Knowledge Platform (API-First Architecture)

1️⃣ SYSTEM ARCHITECTURE PRINCIPLES (MANDATORY)

The platform is governed by the following non-negotiable engineering principles:

- API-first design: All features are exposed through well-versioned HTTP JSON APIs. Absolutely no server-rendered templates (e.g., Django templates) may be used.
- Backend statelessness: The backend must remain fully stateless. Any stateful interactions must use external services (e.g., Redis, databases).
- Security-first: Never trust the frontend. All validation, sanitation, and authorization must occur at the backend.
- Modular, feature-based architecture: Organize code by feature (core, users, profiles, blog, tools, library) to enable independent maintenance and scaling.
- Horizontal scalability: Design for horizontal scaling and future microservices decomposition from day one.
- Data-first performance: Optimize database schema, queries, and indexes before applying frontend optimizations.
- Smart caching: Use Redis (or equivalent) for caching and performance-sensitive counters; follow cache eviction and invalidation best practices.
- Observability: Structured JSON logging, Sentry error monitoring, and performance telemetry are mandatory.
- Database health: Enable slow query logging and monitor database performance continuously.
- Automated testing: Full automated coverage (unit, API, permission, integration, and auth flow tests) is required for all production code.

2️⃣ BACKEND SPECIFICATION

Technology stack (guideline): Python, Django, Django REST Framework, PostgreSQL, Redis, Celery, JWT for access & refresh tokens, Sentry for error monitoring.

General backend rules:

- API versioning required (e.g., /api/v1/).
- JSON-only responses for all public API endpoints.
- All endpoints secured by explicit DRF permissions and strict RBAC.
- Throttling enabled (especially authentication endpoints) with brute-force protection and account lockout policies.
- Strict CORS configuration limited to allowed origins.
- All inputs validated and sanitized server-side; never rely solely on client validation.
- Media uploads validated for MIME type, file size, content scanning where feasible, and safe storage.
- Heavy or long-running operations must run via background workers (Celery or equivalent).

3️⃣ BACKEND APPLICATION STRUCTURE

Follow a feature-based modular app layout:

- core/
- users/
- profiles/
- blog/
- tools/
- library/

4️⃣ USERS APPLICATION

Responsibilities: Authentication, registration, session management, credential handling, and JWT issuance/refresh.

Registration methods:

- LinkedIn OAuth
- Email + password (only Gmail, Outlook, Yahoo allowed; OTP verification required)
- Mobile number + password (SMS OTP; account remains inactive until verified)

Security requirements:

- Strong password policies and validation
- Brute-force protection, login throttling, and account lockouts after repeated failures
- All verification and activation flows must be backend enforced

5️⃣ PROFILE APPLICATION

Responsibilities: Manage personal data, article ownership, saved articles, and user preferences.

Public profile view (minimal public surface):

- Public articles, username, first and second name, total article count, total read count. No private data exposed.

Profile fields (editable only by owner unless explicitly public):

- First name, Second name, Username, Email, Secure password-change link, Mobile number
- Social accounts: Facebook, WhatsApp, LinkedIn, Email
- Profile image, Cover image, Work experience, Interested hashtags
- Created date, Last modified date

All sensitive fields must be protected and only editable by the profile owner.

6️⃣ BLOG APPLICATION

Core models: Article, Comment, Like, View, Share, SaveForLater.

Article model requirements:

- Title, Auto-generated slug (supports Arabic & English), Rich-text content, Cover image, Multiple media attachments
- Resources section (links, PDFs, images), Estimated reading time, Submit/modify/publish dates
- Status lifecycle: Draft, Under review, Published, Rejected

Content security and media rules:

- Backend sanitizes HTML, strips scripts, prevents XSS, validates links and MIME types, and enforces file-size limits before DB insertion.
- All media is validated and scanned where feasible; invalid content must be rejected.

Permissions & user flows:

- Logged-in users: create/edit/delete own articles, reply to comments on their own articles, share, save for later (sends scheduled email reminder), like.
- Guests: view and copy URLs, like (tracked anonymously). Guests cannot comment or author content.

Comment rules:

- An article may have many comments.
- Each comment allows at most one reply by the article author and one reply by the original commenter—no unlimited nesting.

View tracking:

- Track views by IP; limit to one view per IP per article per 24 hours. Use cache to reduce DB load.

Share tracking:

- Store article ID/URL, sharer details (or anonymous flag), timestamp, and sharing method (Email, Social, URL).

7️⃣ TOOLS APPLICATION (FUTURE)

Scalable, modular app for poultry tools (FCR, EEPI, ventilation calculators, etc.). Design for plugin-like extensibility.

8️⃣ LIBRARY APPLICATION (FUTURE)

Secure repository for validated/scanned PDFs, images, farm templates, and spreadsheets. Enforce download tracking and file validation.

9️⃣ FRONTEND SPECIFICATION

Technology stack (guideline): React, TypeScript, Vite, React Query, Zustand or Redux Toolkit, React Router, Jest, React Testing Library.

Frontend rules:

- Fully responsive UI that works across major OS and browsers.
- Communicates exclusively via JSON over HTTPS with the backend APIs.
- Authentication uses access + refresh JWT tokens; tokens must be stored in httpOnly cookies (avoid localStorage for sensitive tokens).
- Server state via React Query; global UI state via Zustand/Redux. Minimize ad-hoc useState proliferation.

Styling constraint (MANDATORY):

- All styles must be authored using Sass (SCSS syntax). Use no plain CSS files or alternative styling engines. The project forbids plain CSS or third-party styling engines that do not compile through the Sass toolchain.

Performance patterns:

- Code-splitting and lazy loading
- Memoization where justified (React.memo, useMemo, useCallback)
- Skeleton loaders, optimistic updates, debounced search, and virtualized lists where needed

🔟 TESTING REQUIREMENTS

Backend: unit tests (models, serializers), API tests, permission tests, and integration tests.
Frontend: component tests, integration tests, and full authentication flow tests. High coverage required across both stacks.

1️⃣1️⃣ NON-FUNCTIONAL REQUIREMENTS

- High performance under scale, horizontal scalability, secure media handling, secure authentication, audit logging, structured JSON logs, monitoring dashboards, rate limiting, Redis-based caching, database indexing and slow-query detection.

1️⃣2️⃣ FUTURE SCALABILITY

Design to allow:

- Microservices split, media offload to S3, CDN use, Docker-based deployments, load-balanced multiple backend instances. Backend must remain stateless to enable these transitions.

FINAL INSTRUCTION (ENGINEERING MANDATE)

Build strictly to the API-first, security-first, feature-modular, and scalability-ready principles outlined above. Maintain production-grade standards, strong input validation, and backend-controlled permissions. Use Sass (SCSS) exclusively for all styling.

-- End of specification --
# [PROJECT_NAME] Constitution
<!-- Example: Spec Constitution, TaskFlow Constitution, etc. -->

## Core Principles

### [PRINCIPLE_1_NAME]
<!-- Example: I. Library-First -->
[PRINCIPLE_1_DESCRIPTION]
<!-- Example: Every feature starts as a standalone library; Libraries must be self-contained, independently testable, documented; Clear purpose required - no organizational-only libraries -->

### [PRINCIPLE_2_NAME]
<!-- Example: II. CLI Interface -->
[PRINCIPLE_2_DESCRIPTION]
<!-- Example: Every library exposes functionality via CLI; Text in/out protocol: stdin/args → stdout, errors → stderr; Support JSON + human-readable formats -->

### [PRINCIPLE_3_NAME]
<!-- Example: III. Test-First (NON-NEGOTIABLE) -->
[PRINCIPLE_3_DESCRIPTION]
<!-- Example: TDD mandatory: Tests written → User approved → Tests fail → Then implement; Red-Green-Refactor cycle strictly enforced -->

### [PRINCIPLE_4_NAME]
<!-- Example: IV. Integration Testing -->
[PRINCIPLE_4_DESCRIPTION]
<!-- Example: Focus areas requiring integration tests: New library contract tests, Contract changes, Inter-service communication, Shared schemas -->

### [PRINCIPLE_5_NAME]
<!-- Example: V. Observability, VI. Versioning & Breaking Changes, VII. Simplicity -->
[PRINCIPLE_5_DESCRIPTION]
<!-- Example: Text I/O ensures debuggability; Structured logging required; Or: MAJOR.MINOR.BUILD format; Or: Start simple, YAGNI principles -->

## [SECTION_2_NAME]
<!-- Example: Additional Constraints, Security Requirements, Performance Standards, etc. -->

[SECTION_2_CONTENT]
<!-- Example: Technology stack requirements, compliance standards, deployment policies, etc. -->

## [SECTION_3_NAME]
<!-- Example: Development Workflow, Review Process, Quality Gates, etc. -->

[SECTION_3_CONTENT]
<!-- Example: Code review requirements, testing gates, deployment approval process, etc. -->

## Governance
<!-- Example: Constitution supersedes all other practices; Amendments require documentation, approval, migration plan -->

[GOVERNANCE_RULES]
<!-- Example: All PRs/reviews must verify compliance; Complexity must be justified; Use [GUIDANCE_FILE] for runtime development guidance -->

**Version**: [CONSTITUTION_VERSION] | **Ratified**: [RATIFICATION_DATE] | **Last Amended**: [LAST_AMENDED_DATE]
<!-- Example: Version: 2.1.1 | Ratified: 2025-06-13 | Last Amended: 2025-07-16 -->
