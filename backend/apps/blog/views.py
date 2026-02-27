from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import Article
from .serializers import ArticleSummarySerializer, ArticleDetailSerializer


@api_view(['GET'])
def featured_articles(request):
    qs = Article.objects.filter(
        status='published', is_featured=True
    ).select_related('author').order_by('-publish_date')[:5]
    serializer = ArticleSummarySerializer(qs, many=True)
    return Response({'articles': serializer.data})


@api_view(['GET'])
def blog_list(request):
    qs = Article.objects.filter(
        status='published'
    ).select_related('author').order_by('-publish_date')
    paginator = PageNumberPagination()
    paginator.page_size = int(request.query_params.get('page_size', 20))
    page = paginator.paginate_queryset(qs, request)
    serializer = ArticleSummarySerializer(page, many=True)
    return Response({
        'results': serializer.data,
        'page': paginator.page.number,
        'page_size': paginator.page_size,
        'total': paginator.page.paginator.count,
    })


@api_view(['GET'])
def article_detail(request, slug):
    try:
        article = Article.objects.prefetch_related('media').select_related('author').get(
            slug=slug, status='published'
        )
    except Article.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ArticleDetailSerializer(article)
    return Response(serializer.data)
