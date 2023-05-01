from django.urls import path
#from .views import login
from .views import portfolio
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#urlpatterns = [
#    path('login/', login, name='login'),
#]
urlpatterns = [
    path('portfolio/<int:architect_id>/', portfolio, name='portfolio'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # ...
]
