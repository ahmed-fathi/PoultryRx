import React from 'react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { MemoryRouter } from 'react-router-dom'
import Library from '../../src/pages/Library/Library'
import FAQ from '../../src/pages/FAQ/FAQ'

vi.mock('../../src/services/mockApi', () => ({
  fetchLibrary: vi.fn(),
  fetchFAQ: vi.fn(),
}))

import { fetchLibrary, fetchFAQ } from '../../src/services/mockApi'

const mockLibrary = {
  results: [
    { id: 'l1', title: 'Poultry Guide 2024', type: 'pdf', mock_download_url: '/download/l1' },
    { id: 'l2', title: 'Biosecurity Manual', type: 'pdf', mock_download_url: '/download/l2' },
  ]
}

const mockFAQ = {
  results: [
    { id: 'f1', question: 'What is FCR?', answer: 'Feed Conversion Ratio.' },
    { id: 'f2', question: 'How often should I vaccinate?', answer: 'Per the schedule.' },
  ]
}

function wrap(ui: React.ReactElement) {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } })
  return render(
    <QueryClientProvider client={client}>
      <MemoryRouter>{ui}</MemoryRouter>
    </QueryClientProvider>
  )
}

describe('Library page', () => {
  beforeEach(() => {
    vi.mocked(fetchLibrary).mockResolvedValue(mockLibrary)
  })

  it('renders the Library heading', () => {
    wrap(<Library />)
    expect(screen.getByRole('heading', { name: 'Library' })).toBeInTheDocument()
  })

  it('renders library resources as links after data loads', async () => {
    wrap(<Library />)
    await waitFor(() => {
      expect(screen.getByText(/Poultry Guide 2024/)).toBeInTheDocument()
    })
    expect(screen.getByText(/Biosecurity Manual/)).toBeInTheDocument()
  })

  it('links resources to their download URLs', async () => {
    wrap(<Library />)
    await waitFor(() => {
      expect(screen.getByText(/Poultry Guide 2024/)).toBeInTheDocument()
    })
    const link = screen.getByRole('link', { name: /Poultry Guide 2024/ })
    expect(link).toHaveAttribute('href', '/download/l1')
  })
})

describe('FAQ page', () => {
  beforeEach(() => {
    vi.mocked(fetchFAQ).mockResolvedValue(mockFAQ)
  })

  it('renders the FAQ heading', () => {
    wrap(<FAQ />)
    expect(screen.getByRole('heading', { name: 'FAQ' })).toBeInTheDocument()
  })

  it('renders questions and answers after data loads', async () => {
    wrap(<FAQ />)
    await waitFor(() => {
      expect(screen.getByText('What is FCR?')).toBeInTheDocument()
    })
    expect(screen.getByText('Feed Conversion Ratio.')).toBeInTheDocument()
    expect(screen.getByText('How often should I vaccinate?')).toBeInTheDocument()
  })

  it('renders each question in a <strong> tag', async () => {
    wrap(<FAQ />)
    await waitFor(() => {
      const q = screen.getByText('What is FCR?')
      expect(q.tagName.toLowerCase()).toBe('strong')
    })
  })
})
