from django import forms

class ReportFilterForm(forms.Form):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    report_type = forms.ChoiceField(choices=[
        ('students', 'Élèves'),
        ('teachers', 'Enseignants'),
        ('payments', 'Paiements'),
    ])