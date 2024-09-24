from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from students.models import studentName

def students(request):
    return HttpResponse("""
            <html>
                <h1 style="text-align: center;">Hello Students</h1>
            </html>
            """)

def hello(request):
    return HttpResponse("""
                        <html>
                            <h1 style="color: violet; text-align: center">Hello world</h1>
                        </html>
                        """)
    
def svec(request):
    return HttpResponse("""
                    <html>
                        <h1 style="text-align: center;">Hello SVEC</h1>
                    </html>
                        """)
    
    
def courses(request):
    template = loader.get_template('courses.html')
    return HttpResponse(template.render())

def student_details(request):
    template = loader.get_template('student_details.html')
    
    student_list = studentName.objects.all().values()
    context = {
        'student_list' : student_list,
    }
    
    return HttpResponse(template.render(context, request))