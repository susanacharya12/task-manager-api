from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Home route with actual demo credentials
# config/urls.py or tasks/views.py
from django.http import HttpResponse

def home(request):
    html_content = """
    <html>
        <head>
            <title>Task Manager API</title>
            <style>
                body { font-family: Arial, sans-serif; background: #f7f7f7; text-align: center; padding: 50px; }
                h1 { color: #333; }
                .button {
                    display: inline-block;
                    margin: 10px;
                    padding: 12px 25px;
                    background: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 5px;
                    font-size: 16px;
                }
                .button:hover { background: #45a049; }
                .credentials { margin-top: 30px; font-size: 16px; color: #555; }
                .credentials p { margin: 5px; }
            </style>
        </head>
        <body>
            <h1>Welcome to Task Manager API</h1>
            <a class="button" href="https://task-manager-api-x87n.onrender.com/swagger/" target="_blank">Open Swagger Docs</a>
            <a class="button" href="https://task-manager-api-x87n.onrender.com/redoc/" target="_blank">Open ReDoc Docs</a>
            <a class="button" href="https://github.com/yourusername/task-manager-api" target="_blank">View GitHub Repo</a>

            <div class="credentials">
                <p><strong>Demo Credentials:</strong></p>
                <p>Username: susanacharya</p>
                <p>Password: 123</p>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html_content)



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