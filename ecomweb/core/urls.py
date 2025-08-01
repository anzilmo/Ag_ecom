
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('cart/', views.cart_view, name='cart'),
    path('new-cars/',views.newcars,name='new-cars'),
    path('used-car/',views.usedcar,name='used-car'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)