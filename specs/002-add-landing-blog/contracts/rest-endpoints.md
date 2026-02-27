# REST Endpoints (summary) — 002-add-landing-blog

Base path: `/api/v1/`

GET /api/v1/landing/featured
- Description: Returns up to 5 featured published articles ordered newest-first.
- Response: { articles: [ { id, title, slug, excerpt, cover_image, publish_date, author: { username, first_name, last_name } } ] }

GET /api/v1/blog/?page=1&page_size=20
- Description: Paginated blog listing. For this feature use page_size=20 and local mock data.
- Response: { results: [ { id, title, slug, excerpt, author, publish_date, cover_image } ], page, page_size, total }

GET /api/v1/articles/{slug}/
- Description: Article detail including sanitized content and media list.
- Response: { id, title, slug, content, media: [ { url, mime_type } ], estimated_read_time, author, publish_date }

GET /api/v1/profiles/{username}/public
- Description: Public profile view.
- Response: { username, first_name, last_name, public_articles_count, total_read_count, public_articles: [ { id, title, slug } ] }

GET /api/v1/library/
- Description: List of mock library resources.
- Response: { results: [ { id, title, type, mock_download_url } ] }

GET /api/v1/faq/
- Description: Returns FAQ entries.
- Response: { results: [ { id, question, answer } ] }

GET /api/v1/tools/
- Description: Returns available AI/tool entries.
- Response: { results: [ { id, name, slug, description, entry_point } ] }

Notes for frontend mocking:
- Frontend mock adapter will implement these endpoints locally and return JSON fixtures matching the shapes above.

-- End of contract summary --
