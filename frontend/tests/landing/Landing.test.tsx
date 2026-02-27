import React from 'react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { MemoryRouter } from 'react-router-dom'
import Landing from '../../src/pages/Landing/Landing'

vi.mock('../../src/services/api', () => ({
  fetchFeatured: vi.fn(),
  fetchTools: vi.fn(),
}))

import { fetchFeatured, fetchTools } from '../../src/services/api'

const mockFeatured = {
  articles: [
    { id: 'a1', title: 'Optimizing Feed Conversion', slug: 'optimizing-feed-conversion', excerpt: 'Tips to improve FCR.', cover_image: 'img1.jpg', status: 'published', is_featured: true, author: { username: 'dr_smith' }, publish_date: '2026-01-01' },
    { id: 'a2', title: 'Ventilation Strategies', slug: 'ventilation-strategies', excerpt: 'How to keep birds cool.', cover_image: 'img2.jpg', status: 'published', is_featured: true, author: { username: 'farmer_jane' }, publish_date: '2026-01-05' },
    { id: 'a3', title: 'Disease Prevention Basics', slug: 'disease-prevention-basics', excerpt: 'Biosecurity essentials.', cover_image: 'img3.jpg', status: 'published', is_featured: true, author: { username: 'vet_mike' }, publish_date: '2026-01-10' },
    { id: 'a4', title: 'Egg Production Optimization', slug: 'egg-production-optimization', excerpt: 'Maximize laying cycles.', cover_image: 'img4.jpg', status: 'published', is_featured: true, author: { username: 'dr_smith' }, publish_date: '2026-01-12' },
    { id: 'a5', title: 'Water Management', slug: 'water-management', excerpt: 'Ensuring clean water access.', cover_image: 'img5.jpg', status: 'published', is_featured: true, author: { username: 'farmer_jane' }, publish_date: '2026-01-15' },
  ]
}

const mockTools = {
  results: [
    { id: 't1', name: 'FCR Calculator', description: 'Feed conversion ratio tool', url: '/tools/fcr' },
    { id: 't2', name: 'EEPI Calculator', description: 'Economic evaluation', url: '/tools/eepi' },
  ]
}

function renderWithProviders(ui: React.ReactElement) {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } })
  return render(
    <QueryClientProvider client={client}>
      <MemoryRouter>{ui}</MemoryRouter>
    </QueryClientProvider>
  )
}

describe('Landing page', () => {
  beforeEach(() => {
    vi.mocked(fetchFeatured).mockResolvedValue(mockFeatured)
    vi.mocked(fetchTools).mockResolvedValue(mockTools)
  })

  it('renders the Featured Articles heading', () => {
    renderWithProviders(<Landing />)
    expect(screen.getByText('Featured Articles')).toBeInTheDocument()
  })

  it('renders the AI Tools heading', () => {
    renderWithProviders(<Landing />)
    expect(screen.getByText('AI Tools')).toBeInTheDocument()
  })

  it('shows exactly 5 featured articles after data loads', async () => {
    renderWithProviders(<Landing />)
    await waitFor(() => {
      expect(screen.getByText('Optimizing Feed Conversion')).toBeInTheDocument()
    })
    const articleCards = screen.getAllByRole('article')
    expect(articleCards).toHaveLength(5)
  })

  it('shows tool cards after data loads', async () => {
    renderWithProviders(<Landing />)
    await waitFor(() => {
      expect(screen.getByText('FCR Calculator')).toBeInTheDocument()
    })
    expect(screen.getByText('EEPI Calculator')).toBeInTheDocument()
  })

  it('links articles to the correct slug paths', async () => {
    renderWithProviders(<Landing />)
    await waitFor(() => {
      expect(screen.getByText('Optimizing Feed Conversion')).toBeInTheDocument()
    })
    const link = screen.getByText('Optimizing Feed Conversion').closest('a')
    expect(link).toHaveAttribute('href', '/articles/optimizing-feed-conversion')
  })
})
