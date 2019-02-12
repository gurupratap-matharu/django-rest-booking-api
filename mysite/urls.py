from api import views
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register(r'match', views.MatchViewSet)

schema_view = get_schema_view(title='Bookings API',
                description='An API to book matches or update odds.')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('schema/', schema_view),
    path('docs/', include_docs_urls(title='Bookings API'))
]
