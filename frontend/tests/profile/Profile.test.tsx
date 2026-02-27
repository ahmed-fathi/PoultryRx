import React from 'react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { MemoryRouter, Route, Routes } from 'react-router-dom'
import Profile from '../../src/pages/Profile/Profile'

vi.mock('../../src/services/api', () => ({
  fetchProfile: vi.fn(),
}))

import { fetchProfile } from '../../src/services/api'

const mockProfile = {
  id: 'p1',
  username: 'dr_smith',
  first_name: 'John',
  last_name: 'Smith',
  public_articles_count: 5,
  total_read_count: 1234,
  public_articles: [
    { id: 'a1', title: 'Optimizing Feed Conversion', slug: 'optimizing-feed-conversion' },
  ],
}

function renderProfile(username = 'dr_smith') {
  const client = new QueryClient({ defaultOptions: { queries: { retry: false } } })
  return render(
    <QueryClientProvider client={client}>
      <MemoryRouter initialEntries={[`/profiles/${username}`]}>
        <Routes>
          <Route path="/profiles/:username" element={<Profile />} />
        </Routes>
      </MemoryRouter>
    </QueryClientProvider>
  )
}

describe('Profile page', () => {
  beforeEach(() => {
    vi.mocked(fetchProfile).mockResolvedValue(mockProfile)
  })

  it('shows loading state initially', () => {
    renderProfile()
    expect(screen.getByText('Loading...')).toBeInTheDocument()
  })

  it('renders the username after data loads', async () => {
    renderProfile()
    await waitFor(() => {
      expect(screen.getByRole('heading', { name: 'dr_smith' })).toBeInTheDocument()
    })
  })

  it('renders first and last name', async () => {
    renderProfile()
    await waitFor(() => {
      expect(screen.getByText(/John.*Smith/)).toBeInTheDocument()
    })
  })

  it('shows public articles count', async () => {
    renderProfile()
    await waitFor(() => {
      expect(screen.getByText(/Public articles: 5/)).toBeInTheDocument()
    })
  })

  it('shows total read count', async () => {
    renderProfile()
    await waitFor(() => {
      expect(screen.getByText(/Total reads: 1234/)).toBeInTheDocument()
    })
  })

  it('only exposes public fields (no email or private data)', async () => {
    renderProfile()
    await waitFor(() => {
      expect(screen.getByRole('heading', { name: 'dr_smith' })).toBeInTheDocument()
    })
    // Verify no private fields are rendered
    expect(screen.queryByText(/email/i)).not.toBeInTheDocument()
    expect(screen.queryByText(/password/i)).not.toBeInTheDocument()
  })
})
