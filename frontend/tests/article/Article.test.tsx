import React from 'react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import Article from '../../src/pages/Article/Article'

vi.mock('../../src/services/mockApi', () => ({
  fetchArticle: vi.fn(),
}))

import { fetchArticle } from '../../src/services/mockApi'

const mockArticle = {
  id: 'a1',
  title: 'Optimizing Feed Conversion',
  slug: 'optimizing-feed-conversion',
  content: '<p>Full article content here</p>',
  author: { username: 'dr_smith' },
  publish_date: '2026-01-01',
  cover_image: 'img1.jpg',
  status: 'published',
}

function renderArticle(slug = 'optimizing-feed-conversion') {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } })
  return render(
    <QueryClientProvider client={client}>
      <MemoryRouter initialEntries={[`/articles/${slug}`]}>
        <Routes>
          <Route path="/articles/:slug" element={<Article />} />
        </Routes>
      </MemoryRouter>
    </QueryClientProvider>
  )
}

describe('Article detail page', () => {
  beforeEach(() => {
    vi.mocked(fetchArticle).mockResolvedValue(mockArticle)
  })

  it('shows loading state initially', () => {
    renderArticle()
    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  it('renders the article title after data loads', async () => {
    renderArticle()
    await waitFor(() => {
      expect(screen.getByRole('heading', { name: 'Optimizing Feed Conversion' })).toBeInTheDocument()
    })
  })

  it('renders author and publish date in meta', async () => {
    renderArticle()
    await waitFor(() => {
      expect(screen.getByText(/dr_smith/)).toBeInTheDocument()
      expect(screen.getByText(/2026-01-01/)).toBeInTheDocument()
    })
  })

  it('renders the article content via dangerouslySetInnerHTML', async () => {
    renderArticle()
    await waitFor(() => {
      expect(screen.getByText('Full article content here')).toBeInTheDocument()
    })
  })

  it('calls fetchArticle with the correct slug', () => {
    renderArticle('optimizing-feed-conversion')
    expect(fetchArticle).toHaveBeenCalledWith('optimizing-feed-conversion')
  })
})
