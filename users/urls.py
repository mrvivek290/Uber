from django.urls import path,include
from .views import *

urlpatterns = []

from users.views import *

urlpatterns += [

    path('get-all-students',GetStudentsView.as_view()),
    path('get-and-save-orders',GetOrdersViews.as_view()),
    path('delete-student/<int:pk>',DeleteStudentsView.as_view()),
    path('Student-detail-address/<int:pk>',StudentsDetailAddressViews.as_view())

]