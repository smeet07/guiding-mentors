from django.shortcuts import redirect, render
from apti.services.calc_weights import get_weights, generate_field, normalize_ratings
from student.models import StudentBuffer
from apti.services.get_student_details import getStudentBuffer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def student_dashboard(request,responses):
    student = getStudentBuffer(1)
    # add id
    if student is None:
        return
    student.recommended=generate_field(responses)

@csrf_exempt
def quizPage(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect('login')
    return render(request,'quiz.html')