from django.urls import path
import setting.views as views

app_name = 'setting'

urlpatterns = [
    path('composantes/', views.ComposanteTemplateView.as_view(), name='composantes'),
]