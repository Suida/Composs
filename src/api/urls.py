from django.urls import path, include


urlpatterns = [
    path('account/', include('api.account.urls')),
    path('article/', include('api.article.urls')),
]
