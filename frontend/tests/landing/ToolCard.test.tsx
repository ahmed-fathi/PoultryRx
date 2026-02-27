import React from 'react'
import { describe, it, expect, vi, beforeEach } from 'vitest'
import { render, screen, waitFor } from '@testing-library/react'
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { MemoryRouter } from 'react-router-dom'
import ToolCard from '../../src/components/ToolCard'

describe('ToolCard component', () => {
  const tool = {
    id: 't1',
    name: 'FCR Calculator',
    description: 'Feed conversion ratio tool',
    url: '/tools/fcr',
    category: 'Nutrition',
  }

  it('renders the tool name', () => {
    render(
      <MemoryRouter>
        <ToolCard tool={tool} />
      </MemoryRouter>
    )
    expect(screen.getByText('FCR Calculator')).toBeInTheDocument()
  })

  it('renders the description', () => {
    render(
      <MemoryRouter>
        <ToolCard tool={tool} />
      </MemoryRouter>
    )
    expect(screen.getByText('Feed conversion ratio tool')).toBeInTheDocument()
  })

  it('renders the category', () => {
    render(
      <MemoryRouter>
        <ToolCard tool={tool} />
      </MemoryRouter>
    )
    expect(screen.getByText('Nutrition')).toBeInTheDocument()
  })

  it('renders the "Learn more" link', () => {
    render(
      <MemoryRouter>
        <ToolCard tool={tool} />
      </MemoryRouter>
    )
    const link = screen.getByRole('link', { name: 'Learn more' })
    expect(link).toHaveAttribute('href', '/tools/fcr')
  })

  it('does not render a link when url is not provided', () => {
    render(
      <MemoryRouter>
        <ToolCard tool={{ id: 't2', name: 'No URL Tool' }} />
      </MemoryRouter>
    )
    expect(screen.queryByRole('link')).not.toBeInTheDocument()
  })
})
