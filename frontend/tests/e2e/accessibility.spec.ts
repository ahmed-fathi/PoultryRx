import { test, expect } from '@playwright/test'
import AxeBuilder from '@axe-core/playwright'

test.describe('Accessibility checks', () => {
  test('landing page has no critical accessibility violations', async ({ page }) => {
    await page.goto('/')
    // Wait for content to render
    await page.waitForLoadState('networkidle')

    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze()

    // Log violations for debugging
    if (results.violations.length > 0) {
      console.log('Accessibility violations on /:', JSON.stringify(results.violations, null, 2))
    }

    // No critical (serious/critical) violations allowed
    const criticalViolations = results.violations.filter(
      v => v.impact === 'critical' || v.impact === 'serious'
    )
    expect(criticalViolations).toHaveLength(0)
  })

  test('blog page has no critical accessibility violations', async ({ page }) => {
    await page.goto('/blog')
    await page.waitForLoadState('networkidle')

    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze()

    const criticalViolations = results.violations.filter(
      v => v.impact === 'critical' || v.impact === 'serious'
    )
    expect(criticalViolations).toHaveLength(0)
  })

  test('article detail page has no critical accessibility violations', async ({ page }) => {
    await page.goto('/articles/optimizing-feed-conversion')
    await page.waitForLoadState('networkidle')

    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa'])
      .analyze()

    const criticalViolations = results.violations.filter(
      v => v.impact === 'critical' || v.impact === 'serious'
    )
    expect(criticalViolations).toHaveLength(0)
  })

  test('landing page has correct heading hierarchy', async ({ page }) => {
    await page.goto('/')
    await page.waitForLoadState('networkidle')

    // There should be an h1 on the page
    const h1 = page.getByRole('heading', { level: 1 })
    await expect(h1).toBeVisible()
  })

  test('all images have alt text on landing page', async ({ page }) => {
    await page.goto('/')
    await page.waitForLoadState('networkidle')

    // All images should have non-empty alt attributes
    const images = await page.locator('img').all()
    for (const img of images) {
      const alt = await img.getAttribute('alt')
      expect(alt).toBeTruthy()
    }
  })
})
