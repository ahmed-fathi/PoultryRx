# Poultry Knowledge Platform — Frontend

A React + TypeScript + Vite frontend for the Poultry Knowledge Platform, featuring a landing page, blog listing, article detail, public profiles, library, FAQ, and about pages. All styling is written in **SCSS only** — no plain `.css` files in `src/`.

---

## Prerequisites

- **Node.js** ≥ 18
- **npm** ≥ 9

---

## Quickstart

```bash
# 1. Install dependencies
cd frontend
npm install

# 2. Start the development server (http://localhost:5173)
npm run dev
```

---

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server on port 5173 |
| `npm run build` | Production build to `dist/` |
| `npm run preview` | Preview production build locally |
| `npm test` | Run unit tests with Vitest |
| `npm run test:watch` | Run Vitest in watch mode |
| `npm run test:e2e` | Run Playwright E2E tests |
| `npm run check-no-css` | Enforce SCSS-only rule (fails if any `.css` files found in `src/`) |
| `npm run lint` | Lint TypeScript/TSX with ESLint |

---

## Project Structure

```
frontend/
├── src/
│   ├── components/         # Reusable UI components (ArticleCard, ToolCard)
│   ├── pages/              # Route-level page components
│   │   ├── Landing/
│   │   ├── Blog/
│   │   ├── Article/
│   │   ├── Profile/
│   │   ├── Library/
│   │   ├── About/
│   │   └── FAQ/
│   ├── services/
│   │   ├── mockApi.ts      # Mock API adapter (returns fixture data)
│   │   └── mockData/       # JSON fixtures (articles, tools, library, faq, profiles)
│   ├── styles/
│   │   ├── abstracts/      # SCSS variables and mixins
│   │   ├── base/           # Global reset / base styles
│   │   ├── components/     # Component-level SCSS partials
│   │   ├── pages/          # Page-level SCSS partials
│   │   └── main.scss       # Root SCSS entry (imports all partials)
│   ├── test/
│   │   └── setup.ts        # Vitest/jest-dom setup
│   ├── App.tsx             # App router
│   └── main.tsx            # React entry point
├── tests/
│   ├── landing/            # Unit tests for landing & ToolCard
│   ├── blog/               # Unit tests for blog listing
│   ├── article/            # Unit tests for article detail
│   ├── profile/            # Unit tests for profile page
│   ├── library/            # Unit tests for library & FAQ
│   └── e2e/                # Playwright E2E & accessibility tests
├── scripts/
│   └── check-no-css.js     # CI script: fails if plain CSS found in src/
├── .eslintrc.cjs           # ESLint config
├── playwright.config.ts    # Playwright configuration
├── vite.config.ts          # Vite + Vitest configuration
├── tsconfig.json           # TypeScript config
└── package.json
```

---

## Styling Rules

- **SCSS only** — never add plain `.css` files under `src/`
- All styles live in `src/styles/` as SCSS partials imported from `main.scss`
- Component-specific SCSS files live in `src/styles/components/`
- Page-specific SCSS files live in `src/styles/pages/`
- The `check-no-css` script is run in CI to enforce this constraint

---

## Mock API

All data is served from JSON fixtures in `src/services/mockData/`. The `mockApi.ts` adapter exports async functions:

- `fetchFeatured()` — returns up to 5 published, featured articles
- `fetchTools()` — returns all AI tools
- `fetchBlog(page, page_size)` — returns paginated articles (default page_size=20)
- `fetchArticle(slug)` — returns a single article by slug
- `fetchProfile(username)` — returns a public profile by username
- `fetchLibrary()` — returns library resources
- `fetchFAQ()` — returns FAQ items

---

## Security Note

The `Article` detail page uses `dangerouslySetInnerHTML` to render article content. In production, **all HTML content must be sanitised server-side** (e.g. with DOMPurify or an allow-list sanitiser) before storage and delivery. The mock data contains safe static HTML only.

---

## Running E2E Tests

E2E tests require a running dev server and the Playwright browsers to be installed:

```bash
# Install Playwright browsers (first time only)
npx playwright install chromium

# Run E2E tests (starts dev server automatically)
npm run test:e2e
```

---

## Accessibility

Playwright accessibility tests in `tests/e2e/accessibility.spec.ts` use `@axe-core/playwright` to check for WCAG 2.1 A/AA violations on the landing, blog, and article pages.
