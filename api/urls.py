from django.urls import path
from .views import index, home, about, calc, result, studenCreate, studentList, studentDetail, studentUpdatele, studentDelete,teacherDetail,courseDetail
urlpatterns = [
    path("", index, name= "index"),
    path( "home/",home,  name="home"),
    path( "about/",about,  name="about"),
    path( "calc/",calc,  name="calc"),
    path( "calc/result/",result,  name="result"),
    

    path( "students", studentList, name="studentList"),
    path( "detail/<int:pk>", studentDetail, name="studentDetail"),
    path( "students/create", studenCreate, name="studenCreate"),
    path( "detail/students/update/<int:pk>", studentUpdatele, name="studentUpdatele"),
    path( "detail/studentDelete/<int:pk>", studentDelete, name="studentDelete"),


    path("teacher/<int:id>", teacherDetail, name="teacherDetail"),
    path("course/<int:id>", courseDetail, name="courseDetail")
] 