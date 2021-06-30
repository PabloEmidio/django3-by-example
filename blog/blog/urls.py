from django.urls import path

from . import views as bviews
from .views import PostListView

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',
        bviews.post_detail,
        name='post_detail'
    ),
]