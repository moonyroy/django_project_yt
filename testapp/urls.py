from django.urls import path
from .views import BlogView , BlogDetail , AddPost , PostLike , PostUnlike

urlpatterns = [
    path('', BlogView.as_view() , name = 'home'),
    path('blog/<int:pk>' ,BlogDetail.as_view() , name = 'detail'),
    path('additem' , AddPost , name='additem' ),
    path('like/<postid>' , PostLike , name = 'postlike' ),
    path('unlike/<postid>' , PostUnlike , name = 'postunlike' )
]
