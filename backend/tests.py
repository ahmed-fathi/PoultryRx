"""
Basic API endpoint tests for PoultryRx backend.
"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient

from apps.blog.models import Article, ArticleMedia
from apps.profiles.models import UserProfile
from apps.tools.models import Tool
from apps.library.models import LibraryResource
from apps.faq.models import FAQEntry


class FeaturedArticlesViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = User.objects.create_user(username='testauthor', password='pass')
        for i in range(6):
            Article.objects.create(
                title=f'Article {i}',
                slug=f'article-{i}',
                status='published',
                is_featured=True,
                publish_date=timezone.now(),
                author=self.author,
            )

    def test_returns_at_most_5_featured(self):
        response = self.client.get('/api/v1/landing/featured')
        self.assertEqual(response.status_code, 200)
        self.assertLessEqual(len(response.data['articles']), 5)

    def test_response_shape(self):
        response = self.client.get('/api/v1/landing/featured')
        self.assertIn('articles', response.data)


class BlogListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = User.objects.create_user(username='blogger', password='pass')
        for i in range(25):
            Article.objects.create(
                title=f'Blog Post {i}',
                slug=f'blog-post-{i}',
                status='published',
                publish_date=timezone.now(),
                author=self.author,
            )

    def test_default_page_size(self):
        response = self.client.get('/api/v1/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)
        self.assertIn('total', response.data)

    def test_total_count(self):
        response = self.client.get('/api/v1/blog/')
        self.assertEqual(response.data['total'], 25)


class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = User.objects.create_user(username='detailauthor', password='pass')
        self.article = Article.objects.create(
            title='Detail Article',
            slug='detail-article',
            content='Full content here.',
            status='published',
            publish_date=timezone.now(),
            author=self.author,
        )

    def test_get_existing_article(self):
        response = self.client.get('/api/v1/articles/detail-article/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['slug'], 'detail-article')

    def test_get_missing_article_returns_404(self):
        response = self.client.get('/api/v1/articles/does-not-exist/')
        self.assertEqual(response.status_code, 404)

    def test_draft_not_exposed(self):
        self.article.status = 'draft'
        self.article.save()
        response = self.client.get('/api/v1/articles/detail-article/')
        self.assertEqual(response.status_code, 404)


class PublicProfileViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='profileuser', first_name='John', last_name='Doe', password='pass'
        )
        self.profile = UserProfile.objects.create(user=self.user, total_read_count=10)

    def test_get_public_profile(self):
        response = self.client.get('/api/v1/profiles/profileuser/public')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], 'profileuser')
        self.assertNotIn('password', response.data)

    def test_missing_profile_returns_404(self):
        response = self.client.get('/api/v1/profiles/nobody/public')
        self.assertEqual(response.status_code, 404)


class ToolsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Tool.objects.create(name='Feed Calculator', slug='feed-calc', entry_point='http://example.com/feed')

    def test_tools_list(self):
        response = self.client.get('/api/v1/tools/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)


class LibraryViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        LibraryResource.objects.create(
            title='Broiler Guide', type='pdf', mock_download_url='http://example.com/broiler.pdf'
        )

    def test_library_list(self):
        response = self.client.get('/api/v1/library/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)


class FAQViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        FAQEntry.objects.create(question='What is PoultryRx?', answer='A knowledge platform.')

    def test_faq_list(self):
        response = self.client.get('/api/v1/faq/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
