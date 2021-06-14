from rest_framework import routers

from api.projects.views import ProjectViewSet

app_name = 'api'
router = routers.DefaultRouter()
router.register('projects', ProjectViewSet, basename='projects')
urlpatterns = router.urls
