"""AI_Integrated_Buddy_Bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from simple_chatbot.views import SimpleChatbot

admin.site.site_header = "AI Integrated Buddy Bot"
admin.site.site_title = "Buddy Bot"
admin.site.index_title = "Welcome Admin"

urlpatterns = [
    path('', RedirectView.as_view(url='chatbot/', permanent=True)),
    path("", SimpleChatbot.as_view()),
    path('', include('Buddy_Bot.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
