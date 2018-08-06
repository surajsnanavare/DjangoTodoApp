from django.conf.urls import url
from . import views

urlpatterns = [
    #/todo/
    url(r'^$',views.index,name = 'index'),

    url(r'^(?P<todo_id>\d+)$',views.edit, name = 'edit'),

    url(r'^addTodo$',views.addTodo, name = 'addTodo'),

    url(r'^delete/(?P<todo_id>\d+)/$',views.delete, name= 'delete' ),

    url(r'^update$',views.update, name= 'update' ),

    #url(r'^(?P<todo_id>[0-9]+)$',views.edit, name= 'edit' ),
    

]
