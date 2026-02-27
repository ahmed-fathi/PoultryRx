# Quickstart — 002-add-landing-blog (frontend mock)

This quickstart shows how to run the frontend demo using local mocks.

Prerequisites
- Node.js 18+ and npm or pnpm

Steps

1. From the repository root, scaffold the frontend (if not already present):

```bash
cd frontend
pnpm install
pnpm dev
```

2. Mock data location
- Mock fixtures are stored under `specs/002-add-landing-blog/fixtures/` and the frontend mock adapter will load them at runtime.

3. Enforcing SCSS-only
- The project build includes a check (script `check-no-css`) that fails if any `.css` files are present in `src/`. Run it with:

```bash
pnpm run check-no-css
```

4. Where to find contracts
- See `specs/002-add-landing-blog/contracts/rest-endpoints.md` for API shapes.

Notes
- This quickstart assumes a local frontend-only development loop. When backend APIs are available, swap the mock adapter in `frontend/src/services` with a real API client.

-- End quickstart --
