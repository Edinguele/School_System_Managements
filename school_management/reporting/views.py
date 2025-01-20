from django.shortcuts import render
from matplotlib.pyplot import summer
from students.models import Student, Attendance
from teachers.models import Teacher
from finance.models import Payment

def dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_payments = Payment.objects.aggregate(total=summer('amount_paid'))['total']
    return render(request, 'dashboard.html', {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_payments': total_payments,
    })