from django.urls import path
from .views import (home, loginView,signupView, 
        groupView, logoutView, createGroup, 
        posts, createPost,addMembers, 
        detailPostView,deleteMembers)

urlpatterns = [
    path('',home, name='home'),
    path('login/', loginView, name='login'),
    path('signup/', signupView, name='signup'),
    path('groups/', groupView, name='groups'),
    path('logout/', logoutView, name='logout'),
    path('groups/create/', createGroup, name='creategroup'),
    path('groups/<int:group_id>/posts/',posts, name='posts'),
    path('post/create/', createPost, name='createpost'),
    path('groups/<int:group_id>/add_members/',addMembers, name='addmembers'),
    path('post/by/<str:username>/', detailPostView, name='detailpost'),
    path('groups/<int:group_id>/delete_members/',deleteMembers, name='deletemembers'),
]