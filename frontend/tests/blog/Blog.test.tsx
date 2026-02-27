import React from 'react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { MemoryRouter } from 'react-router-dom'
import Blog from '../../src/pages/Blog/Blog'

vi.mock('../../src/services/api', () => ({
  fetchBlog: vi.fn(),
}))

import { fetchBlog } from '../../src/services/api'

const makeArticles = (count: number) =>
  Array.from({ length: count }, (_, i) => ({
    id: `a${i + 1}`,
    title: `Article ${i + 1}`,
    slug: `article-${i + 1}`,
    excerpt: `Excerpt ${i + 1}`,
    cover_image: `img${i + 1}.jpg`,
    status: 'published',
    is_featured: false,
    author: { username: 'user1' },
    publish_date: '2026-01-01',
  }))

function renderWithProviders(ui: React.ReactElement) {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } })
  return render(
    <QueryClientProvider client={client}>
      <MemoryRouter>{ui}</MemoryRouter>
    </QueryClientProvider>
  )
}

describe('Blog page', () => {
  beforeEach(() => {
    vi.mocked(fetchBlog).mockResolvedValue({
      results: makeArticles(20),
      page: 1,
      page_size: 20,
      total: 20,
    })
  })

  it('renders the Blog heading', () => {
    renderWithProviders(<Blog />)
    expect(screen.getByRole('heading', { name: 'Blog' })).toBeInTheDocument()
  })

  it('renders 20 article cards after data loads', async () => {
    renderWithProviders(<Blog />)
    await waitFor(() => {
      expect(screen.getByText('Article 1')).toBeInTheDocument()
    })
    const articles = screen.getAllByRole('article')
    expect(articles).toHaveLength(20)
  })

  it('calls fetchBlog with page 1 and page_size 20', () => {
    renderWithProviders(<Blog />)
    expect(fetchBlog).toHaveBeenCalledWith(1, 20)
  })

  it('shows article titles in the listing', async () => {
    renderWithProviders(<Blog />)
    await waitFor(() => {
      expect(screen.getByText('Article 20')).toBeInTheDocument()
    })
  })
})
