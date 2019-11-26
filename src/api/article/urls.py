from rest_framework.routers import DefaultRouter

from api.article.views import ArticleViewSet


router = DefaultRouter()
router.register('', ArticleViewSet)


urlpatterns = router.urls
