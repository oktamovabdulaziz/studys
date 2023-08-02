from django.urls import path
from .views import *

urlpatterns = [
    path("gender/", GenderView.as_view()),
    path("subject/", SubjectView.as_view()),
    path("teacher/", TeacherView.as_view()),
    path("activ-teacher/", ActivTeacherView.as_view()),
    path("gender-teacher/<int:pk>/", GenderTeacherView.as_view()),
    path("student/", StudentView.as_view()),
    path("activ-student/", ActivStudentView.as_view()),
    path("gender-student/<int:pk>/", GenderStudentView.as_view()),
    path("get-student/<int:pk>/", GetStudentView.as_view())

]
