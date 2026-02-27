import { test, expect } from '@playwright/test'

test.describe('Smoke: Landing → Blog → Article navigation', () => {
  test('loads the landing page', async ({ page }) => {
    await page.goto('/')
    await expect(page.getByRole('heading', { name: 'Featured Articles' })).toBeVisible()
    await expect(page.getByRole('heading', { name: 'AI Tools' })).toBeVisible()
  })

  test('navigates from landing to blog', async ({ page }) => {
    await page.goto('/')
    // Navigate to blog via the nav link
    await page.getByRole('link', { name: /blog/i }).first().click()
    await expect(page).toHaveURL(/\/blog/)
    await expect(page.getByRole('heading', { name: 'Blog' })).toBeVisible()
  })

  test('navigates from blog to article detail', async ({ page }) => {
    await page.goto('/blog')
    // Click the first article card
    const firstArticleLink = page.getByRole('link').first()
    await firstArticleLink.click()
    await expect(page).toHaveURL(/\/articles\//)
    // The article detail should show a heading
    await expect(page.locator('article.article-detail h1')).toBeVisible()
  })

  test('landing shows featured articles', async ({ page }) => {
    await page.goto('/')
    // Wait for articles to load (they come from mock API)
    await expect(page.getByRole('article').first()).toBeVisible({ timeout: 5000 })
    const articles = page.getByRole('article')
    await expect(articles).toHaveCount(5)
  })

  test('blog shows articles list', async ({ page }) => {
    await page.goto('/blog')
    await expect(page.getByRole('article').first()).toBeVisible({ timeout: 5000 })
    const articles = page.getByRole('article')
    // Blog should have 20 articles (one page of results from mock)
    await expect(articles).toHaveCount(20)
  })
})
