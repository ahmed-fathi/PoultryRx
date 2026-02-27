import articles from './mockData/articles.json'
import tools from './mockData/tools.json'
import library from './mockData/library.json'
import faq from './mockData/faq.json'
import profiles from './mockData/profiles.json'

export async function fetchFeatured() {
  const featured = articles.filter((a: any) => a.is_featured && a.status === 'published').slice(0, 5)
  return { articles: featured }
}

export async function fetchTools() {
  return { results: tools }
}

export async function fetchBlog(page = 1, page_size = 20) {
  const start = (page - 1) * page_size
  const results = articles.slice(start, start + page_size)
  return { results, page, page_size, total: articles.length }
}

export async function fetchArticle(slug: string) {
  return articles.find((a: any) => a.slug === slug)
}

export async function fetchProfile(username: string) {
  return profiles.find((p: any) => p.username === username)
}

export async function fetchLibrary() {
  return { results: library }
}

export async function fetchFAQ() {
  return { results: faq }
}
