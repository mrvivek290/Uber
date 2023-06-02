from django.urls import path,include
from .views import *
from users.views import *

urlpatterns = [
    path('get-all-students',GetStudentsView.as_view()),
    path('get-and-save-order',GetOrdersView.as_view()),
    path('delete-students/<int:pk>',DeleteStudentViews.as_view()),
    path('Student-detail-address/<int:pk>',StudentsDetailAddressViews.as_view()),
    path('Delete-student-address/<int:pk>',DeleteStudentsAddressViews.as_view())


]
