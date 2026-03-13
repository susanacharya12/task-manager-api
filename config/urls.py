from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Home route with actual demo credentials
def home(request):
    return JsonResponse({
        "message": "Welcome to Task Manager API",
        "swagger_docs": "https://task-manager-api-x87n.onrender.com/swagger/",
        "demo_credentials": {
            "username": "susanacharya",
            "password": "123"
        }
    })

# Swagger schema setup
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="API documentation for Task Manager project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # API routes
    path('api/', include('task.urls')),

    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),

    # Redoc docs (optional)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    # Raw schema
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    # Root API with welcome message and demo credentials
    path('', home),
]