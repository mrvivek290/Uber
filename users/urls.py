from django.urls import path,include
from .views import *
urlpatterns = []

from users.views import *

urlpatterns = [
    path('get-all-Students',GetStudentsView.as_view()),
    path('get-and-save-Orders',GetOrdersViews.as_view()),
    path('delete-students/<int:pk>',DeleteStudentsView.as_view()),
    path('Student-Details-Address/<int:pk>',StudentsDetailsAddresssViews.as_view())
]
