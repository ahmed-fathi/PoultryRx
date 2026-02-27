# Data Model: 002-add-landing-blog

Entities and validation rules for the feature (design-level, not implementation).

Article
- id: UUID
- title: string (required, max 255)
- slug: string (auto-generated, unique, supports Arabic & English)
- excerpt: string
- content: rich-text / sanitized HTML
- author_id: UUID (references UserProfile)
- publish_date: datetime (nullable for drafts)
- status: enum [draft, under_review, published, rejected]
- cover_image: URL
- media: array of { url, mime_type, size_bytes }
- estimated_read_time: integer (minutes, auto-calculated)
- created_at: datetime
- updated_at: datetime

UserProfile (public surface)
- id: UUID
- username: string (unique)
- first_name: string
- last_name: string
- public_articles_count: integer
- total_read_count: integer

Tool
- id: UUID
- name: string
- slug: string
- description: string
- entry_point: URL (frontend route or tool URL)
- example_input: object (tool-specific)

LibraryResource
- id: UUID
- title: string
- type: enum [pdf, image, excel, template]
- mock_download_url: URL
- file_size_bytes: integer

FAQEntry
- id: UUID
- question: string
- answer: string

Validation rules highlights
- Sanitize and validate all rich HTML on backend before save.
- Enforce MIME and size validation for uploaded files.
- Slug generation must handle RTL languages and transliteration.

-- End data model --
