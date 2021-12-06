from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('add',views.add_entry,name='add_entry'),
    path('show',views.show_current,name='show'),
    path('done',views.show_done,name='done'),
    path('markdone/<int:todo_id>', views.mark_done, name='markdone'),
    path('markdelete/<int:todo_id>',views.mark_delete,name='markdelete'),
    path('deleted',views.show_deleted,name='show_deleted'),
    path('all',views.show_all,name='all'),

]