from django.urls import path

from .views import StudentCreateView, StudentDetailView, StudentUpdateView, StudentDeleteView, ClassCreateView, ClassListView, ClassDeleteView, SchoolCreateView, SchoolListView, SchoolDeleteView

urlpatterns = [
    path('students/new/', StudentCreateView.as_view(), name='student-create'),
    path('classes/new/', ClassCreateView.as_view(), name='class-create'),
    path('schools/new/', SchoolCreateView.as_view(), name='school-create'),
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('schools/', SchoolListView.as_view(), name='school-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),
    path('classes/<int:pk>/delete/', ClassDeleteView.as_view(), name='class-delete'),
    path('schools/<int:pk>/delete/', SchoolDeleteView.as_view(), name='school-delete'),
]
