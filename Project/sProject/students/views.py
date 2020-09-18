from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student
def regStudent(request):
    return render(request, 'students/registerStudent.html')



def regConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']

    qs = Student(s_name = name , s_major = major, s_age = age , s_grade = grade , s_gender =gender)
    #등록!
    qs.save()

    #등록이 완료가 되면 다시 페이지를 돌아가주게 한다
    return HttpResponseRedirect(reverse('students:stuAll'))


#학생 목록을 보여주는 메소드
def reaStudentAll(request):
    #학생 데이터 다 가져옴
    qs = Student.objects.all()
    #학생 데이터를 list로 넘겨줌
    context = {'student_list': qs}
    return render(request,'students/readStudents.html',context)


def detStudent(request,name):
    qs = Student.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request,'students/detailStudent.html',context)


def reaStudentOne(request,name):
    qs = Student.objects.get(s_name = name)
    context = {'student_info': qs}
    return render(request,'students/modifyStudent.html',context)


def modConStudent(request):
    name = request.POST['name']
    major = request.POST['major']
    age = request.POST['age']
    grade = request.POST['grade']
    gender = request.POST['gender']


    #이제 기존에 등록되어 있던 사람의 데이터를 가져와서 교체하고 다시 save
    qs = Student.objects.get(s_name = name)
    qs.s_name = name
    qs.s_major = major
    qs.s_age = age
    qs.s_grade = grade
    qs.s_gender = gender

    qs.save()

    return HttpResponseRedirect(reverse('students:stuAll'))

