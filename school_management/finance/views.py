from django.shortcuts import render, redirect
from .models import FeeStructure, Payment
from .form import FeeStructureForm, PaymentForm

def fee_list(request):
    fees = FeeStructure.objects.all()
    return render(request, 'fee_list.html', {'fees': fees})

def payment_list(request):
    payments = Payment.objects.all()
    return render(request, 'payment_list.html', {'payments': payments})

def payment_create(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_list')
    else:
        form = PaymentForm()
    return render(request, 'payment_form.html', {'form': form})