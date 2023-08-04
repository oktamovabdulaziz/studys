from .serializer import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, \
     RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class GenderView(ListAPIView):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer


class SubjectView(ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class ActivTeacherView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    def list(self, request):
        teacher = self.queryset.filter(activ=True)
        data = TeacherSerializer(teacher, many=True).data
        return Response(data)


class GenderTeacherView(ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, pk):
        gender = Gender.objects.get(id=pk)
        teacher = Teacher.objects.filter(gender=gender)
        data = TeacherSerializer(teacher, many=True).data
        return Response(data)


class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class ActivStudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request):
        student = self.queryset.filter(activ=True)
        data = StudentSerializer(student, many=True).data
        return Response(data)


class GenderStudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def list(self, request, pk):
        gender = Gender.objects.get(id=pk)
        student = Student.objects.filter(gender=gender)
        students = []
        for i in student:
            if i.gender.id in student:
                students.append(i.gender.id)
            if not i.gender.id in student:
                students.append(i.gender.id)
        return Response({"count": len(students)})


class RegistrationView(CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

    def create(self, request):
        data = RegistrationSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response({"success": True})
        else:
            return Response({"success": False})


class GetRegistrationView(ListAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer


class TeacherMoney(ListAPIView):
    serializer_class = TeacherSerializer

    def get_queryset(self):
        teacher_money = Teacher.objects.order_by('-money')[:1]
        return teacher_money


class StudentsWithTeachersBySubject(ListAPIView):
    serializer_class = RegistrationSerializer

    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        return Registration.objects.filter(subject_id=subject_id).select_related('teacher')

    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    from .models import Registration
    from .serializers import RegistrationSerializer

    class StudentRegistration(APIView):
        def post(self, request):
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                subject = serializer.validated_data['subject']
                teacher = Teacher.objects.filter(subject=subject).order_by('-money').first()

                if teacher:
                    registration = serializer.save(teacher=teacher)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({"message": "No teacher available for the selected subject."},
                                    status=status.HTTP_400_BAD_REQUEST)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
