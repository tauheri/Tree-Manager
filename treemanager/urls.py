from django.contrib import admin
from django.urls import path
from django.urls import path
from treeapp.views import TreeView, AddNodeView, EditNodeView, DeleteNodeView



urlpatterns = [

    path('admin/', admin.site.urls),
    path('tree/', TreeView.as_view(), name='tree'),
    path('tree/add/', AddNodeView.as_view(), name='add-node'),
    path('tree/edit/<int:node_id>/', EditNodeView.as_view(), name='edit-node'),
    path('tree/delete/<int:node_id>/', DeleteNodeView.as_view(), name='delete-node'),
]