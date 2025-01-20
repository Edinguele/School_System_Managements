from django import forms
from .models import FeeStructure, Payment

class FeeStructureForm(forms.ModelForm):
    class Meta:
        model = FeeStructure
        fields = ['student_class', 'amount', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
        }

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['student', 'fee_structure', 'amount_paid']
        widgets = {
            'amount_paid': forms.NumberInput(attrs={'step': '0.01'}),
        }