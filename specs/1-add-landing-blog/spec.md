# Feature Specification: Create landing, blog, profile, library, about & FAQ pages

**Feature Branch**: `1-add-landing-blog`  
**Created**: 2026-02-27  
**Status**: Draft  
**Input**: User description: "I am building a modern Poultry knowledge website. I want it to look sleek, something that would stand out. Should have a landing page with 5 latest published featured articles and Ai tools for Poultry farm. There should be an blog page, and profile page, and library page, and about page, and a FAQ page. blog page Should have 20 articles, and the data is mocked - you do not need to pull anything from any real feed."

> **Constitution Compliance**: This feature MUST comply with the project constitution: API-first principles, stateless backend, modular apps, SASS-only styling (SCSS), security-first validation server-side, and full test coverage guidance.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Landing page highlights (Priority: P1)

As a visitor, I want a sleek landing page that prominently shows the 5 latest published featured articles and a discoverable section for Poultry AI tools, so I can quickly find high-value content and tools.

Why this priority: The landing page is the primary entry point and drives engagement.  
Independent Test: Load the landing page with mock data and verify 5 featured article cards and an AI tools section render correctly.

Acceptance Scenarios:
1. Given the homepage is requested, When there are >=5 published featured articles, Then the page shows exactly 5 featured article cards ordered newest-first.
2. Given the homepage is requested, When AI tools exist, Then an AI Tools panel lists at least one tool card linking to the tools area.

---

### User Story 2 - Blog listing with mocked content (Priority: P1)

As a visitor, I want a blog page that displays 20 mocked articles so I can browse example content and evaluate the UI/UX.

Why this priority: Demonstrates content layout and pagination/search behaviour for the blog product slice.  
Independent Test: Point the blog page at the provided mock dataset and assert 20 article entries are present on the listing view (or across the first N pages if paginated).

Acceptance Scenarios:
1. Given the blog page is requested, When using the supplied mock dataset, Then 20 article items are visible in the listing (or accessible via pagination) with title, excerpt, author, and publish date.

---

### User Story 3 - Article details (Priority: P2)

As a visitor, I want to open an article to read the full content and see media, so I can consume the article.

Independent Test: Click an article from the blog listing and verify the article detail view shows title, content, media, estimated read time, and metadata.

Acceptance Scenarios:
1. Given an article list item is clicked, When that article exists in the mock data, Then the detail page loads the article content and media.

---

### User Story 4 - Profile page (Priority: P2)

As a visitor, I want to view a user's public profile to see their public articles and basic info.

Independent Test: Load a profile route for a mocked user and assert public fields (username, name, public articles count, total read count) are visible and private fields are not.

Acceptance Scenarios:
1. Given a profile page is requested, Then only public profile fields and public articles are shown.

---

### User Story 5 - Library, About & FAQ (Priority: P3)

As a visitor, I want to browse the library resources and read the About and FAQ pages to learn about the platform.

Independent Test: Navigate to Library, About, and FAQ pages and confirm expected sections render with mock content and links.

Acceptance Scenarios:
1. Given the library page is requested, Then a list of mock resources is shown with titles and download links (mocked).
2. Given the FAQ page is requested, Then FAQ entries display question/answer pairs from the mock dataset.

---

### Edge Cases

- No featured articles available: Landing page shows an editorial fallback area and a clear call-to-action.
- Fewer than 5 featured articles: Display as many as available with consistent layout.
- Very long article media: Images must be responsive and capped by client-side styling rules; large files flagged by UI and prevented by backend if uploaded.
- Mobile constraints: All primary flows must remain usable at small viewport widths.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Landing page MUST display exactly 5 latest published featured articles when available (testable by counting rendered cards).
- **FR-002**: Landing page MUST include an AI Tools panel with at least one discoverable tool card linking to the tools area.
- **FR-003**: Blog listing MUST expose 20 mocked articles for this feature (testable using supplied mock data fixture).
- **FR-004**: Article detail view MUST present title, content, media, estimated reading time, author, and publish date.
- **FR-005**: Profile page MUST surface only public fields (username, first/second name, count of public articles, total reads) and block private fields.
- **FR-006**: Library, About, and FAQ pages MUST render mock resources and entries; downloads and links must be mocked (no external calls).
- **FR-007**: All frontend styling MUST be written in Sass (SCSS syntax); no plain CSS or non-Sass styling engines permitted (enforceable via lint/build checks).
- **FR-008**: Pages MUST be responsive across common breakpoints (mobile/tablet/desktop) and pass basic accessibility checks.
- **FR-009**: All mocked data MUST be provided as local JSON fixtures or in-memory mocks; no external feeds are used for this task.

### Key Entities

- **Article**: title, slug, excerpt, content, author, publish_date, status, cover_image, media[]
- **Tool**: name, slug, description, entry_point (URL), example_input
- **UserProfile**: username, first_name, last_name, public_articles_count, total_read_count
- **LibraryResource**: title, type (PDF/Image/Excel), mock_download_url
- **FAQEntry**: question, answer

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Landing page renders 5 featured article cards and an AI Tools panel on first load with mocked data in under 3 seconds on a developer machine.
- **SC-002**: Blog page shows 20 mocked articles (visible or reachable via pagination) when using the provided mocks.
- **SC-003**: Article detail pages render title, content and media for at least 95% of mock entries without layout breaks.
- **SC-004**: All pages are responsive across common breakpoints (mobile: 375px, tablet: 768px, desktop: 1366px) and pass automated accessibility smoke tests.
- **SC-005**: CSS output contains only compiled Sass sources; build tooling must fail if any plain `.css` files are added to source (enforced by CI/lint rule).

## Testing (examples)

- Unit: snapshot components for landing cards, article list items, and tool cards using mock fixtures.
- Integration: navigate from landing → blog → article detail and assert expected DOM and routing behavior using the mocked dataset.
- E2E (optional): run a headless browser smoke test to ensure navigation, rendering of 5 featured cards, and the blog list with 20 items.

## Assumptions

- Mock data will be stored locally (JSON fixtures) and provided to the frontend via a mock API adapter or static import.
- No backend integration is required for this initial UI feature; API contracts will be mocked to match the production API shapes.
- Sass compilation and linting are part of the frontend build; CI will enforce the no-plain-CSS rule.

-- End of spec --
