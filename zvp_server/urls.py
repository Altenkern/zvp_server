"""ZVP_QUIZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
import control_panel,quiz_app
from control_panel import views
from quiz_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', control_panel.views.index_render, name='index'),
    path('quiz_app/questions', quiz_app.views.render_question_list, name='questions'),
    url(r'', include('student_uploader.urls')),
]