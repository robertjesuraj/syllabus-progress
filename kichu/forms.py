from django import forms
from .models import Syllabus
from mysite import settings

# class MyForm(forms.ModelForm):
#     # syllabus_text = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
#     # proposed_date_completeion = forms.DateField(widget=forms.DateTimeField())

#     class Meta:
#         model = Syllabus
#         widgets = {'syllabus_text': forms.TextInput(), 'proposed_date_completeion': forms.DateInput(attrs={'class': 'datepicker'})}
#         exclude = []

class DateInput(forms.DateInput):
    input_type = 'date'

class MyModelForm(forms.ModelForm):
    # proposed_date_completeion = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    proposed_date_completeion = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
        )
    proposed_date_completeion = forms.DateTimeField(input_formats='%Y-%m-%d %I:%M %p')
    
    class Meta:
        model = Syllabus
        # fields = '__all__'
        
        fields = ['syllabus_text', 'proposed_date_completeion', 'completion_status']
        # widgets = {
        #     'proposed_date_completeion': DateInput()
        # }
        # proposed_date_completeion = forms.DateField(input_formats=['%d/%m/%Y'])
        