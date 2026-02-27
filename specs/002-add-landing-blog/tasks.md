# Tasks: 002-add-landing-blog

Phase 1: Setup

- [x] T001 Create frontend scaffold and config (Vite + React + TypeScript) in frontend/ (frontend/package.json, frontend/vite.config.ts, frontend/tsconfig.json)
- [x] T002 Add app entry and routing (`frontend/src/main.tsx`, `frontend/src/App.tsx`)
- [x] T003 Add SCSS architecture and main entry (`frontend/src/styles/` and `frontend/src/styles/main.scss`)
- [x] T004 Add `check-no-css` enforcement script and npm script (`frontend/scripts/check-no-css.js`, frontend/package.json#scripts)
- [x] T005 Add quickstart docs and developer plan (`specs/002-add-landing-blog/quickstart.md`, specs/002-add-landing-blog/plan.md)

Phase 2: Foundational

- [x] T006 Add mock fixtures for articles, tools, library, faq and profiles (`frontend/src/services/mockData/*.json`, specs/002-add-landing-blog/fixtures/)
- [x] T007 Implement mock API adapter that serves fixtures (frontend/src/services/mockApi.ts)
- [x] T008 Add REST contract summary for frontend to follow (`specs/002-add-landing-blog/contracts/rest-endpoints.md`)
- [x] T009 Add data model and validation guidance (`specs/002-add-landing-blog/data-model.md`)
- [x] T010 Add Phase 0 research and decisions (`specs/002-add-landing-blog/research.md`)

Phase 3: User Story Phases (priority order)

US1 - Landing highlights & Tools (Priority: P1)
- [x] T011 [P] [US1] Implement `ArticleCard` component and its SCSS (`frontend/src/components/ArticleCard.tsx`, frontend/src/styles/components/_article-card.scss)
- [x] T012 [P] [US1] Implement `ToolsList`/`ToolCard` components and SCSS (`frontend/src/components/ToolCard.tsx`, frontend/src/styles/components/_tool-card.scss)
- [x] T013 [US1] Implement `Landing` page UI and wire to mock API (`frontend/src/pages/Landing/Landing.tsx`)
- [x] T014 [US1] Style landing page and ensure responsive grid for featured list (`frontend/src/styles/pages/_landing.scss`, frontend/src/styles/main.scss)
- [x] T015 [US1] Add unit tests for landing components (Jest/React Testing Library) (`frontend/tests/landing/*.test.tsx`)

US2 - Blog listing with 20 mocked articles (Priority: P1)
- [x] T016 [P] [US2] Implement `Blog` page listing and pagination UI (`frontend/src/pages/Blog/Blog.tsx`)
- [x] T017 [P] [US2] Wire `fetchBlog` in mock API and ensure page_size=20 (`frontend/src/services/mockApi.ts`, frontend/src/services/mockData/articles.json)
- [x] T018 [US2] Add responsive styles for article list (`frontend/src/styles/pages/_blog.scss`)
- [x] T019 [US2] Add snapshot and integration tests for blog listing (`frontend/tests/blog/*.test.tsx`)

US3 - Article detail view (Priority: P2)
- [x] T020 [US3] Implement `Article` detail page and route (`frontend/src/pages/Article/Article.tsx`)
- [x] T021 [US3] Ensure sanitized content rendering guidance and placeholder sanitizer in mock adapter (document server-side enforcement) (`frontend/src/services/mockApi.ts`, specs/002-add-landing-blog/data-model.md)
- [x] T022 [US3] Add styles for article detail (`frontend/src/styles/pages/_article.scss`)
- [x] T023 [US3] Add tests for article detail rendering and media presence (`frontend/tests/article/*.test.tsx`)

US4 - Public profile view (Priority: P2)
- [x] T024 [P] [US4] Implement `Profile` public page and connect to mock profile fixtures (`frontend/src/pages/Profile/Profile.tsx`, frontend/src/services/mockData/profiles.json)
- [x] T025 [US4] Add profile styles and test for public-only surface (`frontend/src/styles/pages/_profile.scss`, frontend/tests/profile/*.test.tsx)

US5 - Library, About & FAQ (Priority: P3)
- [x] T026 [P] [US5] Implement `Library`, `About`, and `FAQ` pages using mock fixtures (`frontend/src/pages/Library/Library.tsx`, frontend/src/pages/About/About.tsx`, frontend/src/pages/FAQ/FAQ.tsx`)
- [x] T027 [US5] Add styles and tests for library & FAQ pages (`frontend/src/styles/pages/_library.scss`, frontend/tests/library/*.test.tsx)

Final Phase: Polish & Cross-Cutting Concerns

- [x] T028 Add frontend linting, TypeScript checks, and SCSS linter; add CI check that fails on plain `.css` files (frontend/.eslintrc, frontend/.github/workflows/ci.yml, frontend/scripts/check-no-css.js)
- [x] T029 Add accessibility smoke tests and run in CI (axe or Playwright checks) (`frontend/tests/e2e/accessibility.spec.ts`)
- [x] T030 Prepare README and quickstart steps (`frontend/README.md`, specs/002-add-landing-blog/quickstart.md`)
- [x] T031 [P] Add basic E2E smoke test: landing → blog → article navigation (frontend/tests/e2e/smoke.spec.ts)

Dependencies

- Story completion order (high level): Foundational tasks (T006–T010) → US1 & US2 (T011–T019) → US3 & US4 (T020–T025) → US5 (T026–T027) → Final polish (T028–T031).

Parallel execution examples

- Frontend component implementation (T011, T012, T016) can run in parallel with mock API adapter (T007) and fixture creation (T006).  
- Styling (T014, T018, T022, T025) may run in parallel across pages.  
- Tests (T015, T019, T023, T025) can be written in parallel as components/pages complete.

Independent test criteria (per user story)

- US1: Landing shows exactly 5 featured published articles and at least one tool card when run with provided fixtures (`specs/002-add-landing-blog/contracts/rest-endpoints.md` shapes).  
- US2: Blog listing surfaces 20 mocked articles (visible or via pagination) from fixtures.  
- US3: Article detail loads sanitized content, media list, and metadata for a given slug.  
- US4: Profile page exposes only public fields and lists public articles.  
- US5: Library lists mock resources and FAQ shows Q/A pairs.

Suggested MVP scope

- Minimum viable scope: US1 (Landing highlights + Tools) and US2 (Blog listing with 20 mocked articles) implemented, including fixtures, mock API adapter, and SCSS-only styling enforcement.

Format validation

- All tasks follow the required checklist format: `- [ ] T### [P?] [US?] Description with file path`.

Totals & Summary

- Total tasks: 31
- Tasks per story: US1:5, US2:4, US3:4, US4:2, US5:2, Setup/Foundational/Final:14