from django.urls import path
from .views import *

urlpatterns = [
    path("gender/", GenderView.as_view()),
    path("subject/", SubjectView.as_view()),
    path("teacher/", TeacherView.as_view()),
    path("get-teacher-id/<int:pk>/", GetTeacherId.as_view()),
    path("create-teacher/", CreateTeacher.as_view()),
    path("activ-teacher/", ActivTeacherView.as_view()),
    path("gender-teacher/<int:pk>/", GenderTeacherView.as_view()),
    path("student/", StudentView.as_view()),
    path("get-student-id/<int:pk>/", GetStudentId.as_view()),
    path("activ-student/", ActivStudentView.as_view()),
    path("gender-student/<int:pk>/", GenderStudentView.as_view()),
    path("registration/", RegistrationView.as_view()),
    path("get-registration/", GetRegistrationView.as_view()),
    path('teacher-money/', TeacherMoney.as_view()),
    path("create-student/", CreateStudent.as_view()),
    path('teachers-students/<int:teacher_id>/', StudentsByTeacher.as_view()),
    path('teachers-by-students/', TeacherByStudents.as_view()),
]

