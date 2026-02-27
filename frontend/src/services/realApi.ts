async function getJson<T>(url: string): Promise<T> {
  const res = await fetch(url, {
    headers: {
      Accept: 'application/json',
    },
  })

  if (!res.ok) {
    throw new Error(`Request failed: ${res.status} ${res.statusText}`)
  }

  return (await res.json()) as T
}

export async function fetchFeatured() {
  return getJson<{ articles: any[] }>('/api/v1/landing/featured')
}

export async function fetchTools() {
  return getJson<{ results: any[] }>('/api/v1/tools/')
}

export async function fetchBlog(page = 1, page_size = 20) {
  return getJson<{ results: any[]; page: number; page_size: number; total: number }>(
    `/api/v1/blog/?page=${page}&page_size=${page_size}`,
  )
}

export async function fetchArticle(slug: string) {
  return getJson<any>(`/api/v1/articles/${encodeURIComponent(slug)}/`)
}

export async function fetchProfile(username: string) {
  return getJson<any>(`/api/v1/profiles/${encodeURIComponent(username)}/public`)
}

export async function fetchLibrary() {
  return getJson<{ results: any[] }>('/api/v1/library/')
}

export async function fetchFAQ() {
  return getJson<{ results: any[] }>('/api/v1/faq/')
}
