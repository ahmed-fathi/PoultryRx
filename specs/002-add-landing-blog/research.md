# Research: 002-add-landing-blog

Decisions and clarifications resolved during Phase 0 research.

1) Mock data strategy
- Decision: Use local JSON fixtures under `frontend/src/services/mockData/` consumed by a simple mock API adapter. This keeps the frontend fully decoupled from any backend while adhering to API contract shapes.

2) API shapes
- Covered endpoints and example payloads are captured in `contracts/rest-endpoints.md`.

3) Styling architecture
- SCSS (Sass) only. Folder layout: `styles/abstracts` (variables, mixins), `styles/base` (reset, typography), `styles/components`, `styles/pages`.
- Enforcement: configure a build-time check that searches for `.css` files in `src/` and fails the build; add lint rule to CI.

4) Accessibility & responsiveness
- Baseline: mobile-first responsive design; common breakpoints (375, 768, 1366). Use semantic HTML, aria attributes on interactive controls, and run automated accessibility checks in CI.

5) Mock fixtures content
- Create 20 article JSON objects with fields matching `data-model.md` (title, slug, excerpt, content, author, publish_date, cover_image, media[]). Stored under `specs/002-add-landing-blog/fixtures/articles.json` for initial reference and copied into frontend fixtures during scaffold.

6) Observability notes
- Plan to include structured logging hooks and Sentry integration points in backend apps; for the frontend demo use console structured logs and a placeholder Sentry init snippet.

-- End research --
