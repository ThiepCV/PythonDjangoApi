from django.shortcuts import render , get_object_or_404,redirect
from django.http import HttpResponse
from .models import Student, Teacher, Candidate, Course
from .forms import StudentForm
# Create your views here.
def studenCreate(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("studentList")
    else:
        form = StudentForm()
        return render(request, "create.html",{ "form": form })
def studentUpdatele(request, pk):
    student = get_object_or_404(Student, pk = pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
            return redirect("studenDetail", pk = pk)
    else:  
        form = StudentForm()
        context = {
            "form" :form,
            "student": student,

        }  
        return render(request, "update.html", context)

def studentList(request):
    students = Student.objects.all()
    context = {
        "students" : students
    }
    return render(request, "list.html", context)
def studentDetail(request, pk):
    student = get_object_or_404(Student, pk =pk)
    context ={
        "student" : student
    
    }
    return render(request, "detail.html", context)
# def studenCreate(request):
#     if request.method == "POST":
#         firstName = request.POST["firstName"]
#         lastName = request.POST["lastName"]
#         biography = request.POST["biography"]
#         age = request.POST["age"]
#         mothersMaidenName = request.POST["mothersMaidenName"]
#         Student.objects.create(
#             firstName  = firstName,
#             lastName = lastName,
#             biography = biography,
#             age = age,
#             mothersMaidenName = mothersMaidenName
#         )
#         return redirect("studentList")  
#     return render(request,"create.html" )  

# def studentUpdatele(request, pk):
#     student = get_object_or_404(Student, pk = pk)
#     if request.method == "POST":
#         student.firstName = request.POST["firstName"]
#         student.lastName = request.POST["lastName"]
#         student.biography = request.POST["biography"]
#         student.age = request.POST["age"]
#         student.mothersMaidenName = request.POST["mothersMaidenName"]
#         student.save()

#         return redirect("studentDetail", pk = pk)
#     return render(request,"update.html" ,{"student" : student}) 
 
def studentDelete(request, pk):
    student = get_object_or_404(Student, pk = pk)
    if request.method == "POST":
        student.delete()
        return redirect("studentList")
    return render(request,"delete.html" ,{"student" : student})  
def index(request):
    return render(request, "index.html")
def home(request):
    context ={
        "user" : "Alexander"
    }
    return render(request, "home.html", context)
def about(request):
    return render(request, "about.html")
def calc(request):
    return render(request, "calc.html")
def result(request):
    firstNumber = request.GET["num1"]
    secondNumber = request.GET["num2"]
    ope = request.GET["operator"]
    op_math ={
        "plus" :"+",
        "minus":"-",
        "times":"*",
        "divide":"/"
    }
    expression = f"{firstNumber}{op_math[ope]}{secondNumber}"
    result = eval(expression)
    
    context ={
        "result": result
    }
    print(result)
    return render(request, "result.html", context)


def teacherDetail(request, id):
    teacher = Teacher.objects.get(pk = id)
    courses = teacher.course.all()
    
    context ={
        "teacher" : teacher,
        "courses" : courses
    }    
    print(context)
    return render(request, "teacherDetail.html", context)

def courseDetail(request, id):
    course = Course.objects.get(pk = id)
    students = course.students.all()

    context ={
        "students" : students,
        "course" : course
    }  

    return render(request, "courseDetail.html", context)