import articles from './mockData/articles.json'
import tools from './mockData/tools.json'
import library from './mockData/library.json'
import faq from './mockData/faq.json'
import profiles from './mockData/profiles.json'

/**
 * Base URL for the real Django backend.
 * Set VITE_API_BASE_URL in your .env file to override.
 * Falls back to mock data if the backend is unreachable.
 */
const API_BASE_URL = (import.meta as any).env?.VITE_API_BASE_URL ?? 'http://localhost:8000'

/**
 * Attempt a fetch from the real API; on any network/HTTP error fall back to
 * the provided `fallback` function that returns mock data.
 */
async function withFallback<T>(
  endpoint: string,
  fallback: () => T
): Promise<T> {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: { Accept: 'application/json' },
      // Short timeout so dev experience is not degraded when backend is down
      signal: AbortSignal.timeout(2000),
    })
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    return (await response.json()) as T
  } catch {
    // Backend unavailable — silently use mock data
    return fallback() as T
  }
}

export async function fetchFeatured() {
  return withFallback('/api/v1/landing/featured', () => {
    const featured = articles.filter(
      (a: any) => a.is_featured && a.status === 'published'
    ).slice(0, 5)
    return { articles: featured }
  })
}

export async function fetchTools() {
  return withFallback('/api/v1/tools/', () => ({ results: tools }))
}

export async function fetchBlog(page = 1, page_size = 20) {
  return withFallback(`/api/v1/blog/?page=${page}&page_size=${page_size}`, () => {
    const start = (page - 1) * page_size
    const results = articles.slice(start, start + page_size)
    return { results, page, page_size, total: articles.length }
  })
}

export async function fetchArticle(slug: string) {
  return withFallback(`/api/v1/articles/${slug}/`, () =>
    articles.find((a: any) => a.slug === slug)
  )
}

export async function fetchProfile(username: string) {
  return withFallback(`/api/v1/profiles/${username}/public`, () =>
    profiles.find((p: any) => p.username === username)
  )
}

export async function fetchLibrary() {
  return withFallback('/api/v1/library/', () => ({ results: library }))
}

export async function fetchFAQ() {
  return withFallback('/api/v1/faq/', () => ({ results: faq }))
}
