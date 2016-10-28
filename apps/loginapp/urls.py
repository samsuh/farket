from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^search$', views.search, name='search'),
    url(r'^results$', views.results, name='results'),
    url(r'^register$', views.register, name = 'register'),
    url(r'^logout$', views.logout, name = 'logout'),
    url(r'^reviews$', views.reviews, name = 'reviews'),
    url(r'^comments$', views.comments, name = 'comments'),
    # url(r'^results/(?P<id>\d+)$'), views.results, name = 'results'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name = 'delete')
]
