from django import forms
from .models import Student
class StudentRegistrationForm(forms.ModelForm):
    class Meta():
        model=Student
        # exclude=(profile_image)
        fields=("__all__")
        widgets={
        'first_name':forms.TextInput(attrs={'class':'form_control','placeholder':'first name'}),
        'last_name':forms.TextInput(attrs={'class':'form_control','placeholder':'last name'}),
        'age':forms.NumberInput(attrs={'class':'form_control','placeholder':'Age'}),
        'date_of_birth':forms.DateTimeInput(attrs={'class':'form_control'}),
        'Roll_number':forms.TextInput(attrs={'class':'form_control','placeholder':'Roll number'}),
        'student_id':forms.TextInput(attrs={'class':'form_control','placeholder':'Student Id'}),
        'National_Id':forms.NumberInput(attrs={'class':'form_control','placeholder':'National ID'}),
        'Gender':forms.Select(attrs={'class':'form_control'}),
        'phone_number':forms.NumberInput(attrs={'class':'form_control','placeholder':'Phone Number'}),
        'Guardian_name':forms.TextInput(attrs={'class':'form_control','placeholder':'Guardian name'}),
        'Email_address':forms.EmailInput(attrs={'class':'form_control','placeholder':'Email address'}),
        'country':forms.Select(attrs={'class':'form_control'}),
        'profile_image':forms.FileInput(attrs={'class':'form_control'}),
        'Grade':forms.TextInput(attrs={'class':'form_control','placeholder':'Grade'}),
        'Medical_report':forms.FileInput(attrs={'class':'form_control'}),
        'date_Of_enrollment':forms.DateInput(attrs={'class':'form_control','placeholder':'date of enrollment'}),
        'course_name':forms.TextInput(attrs={'class':'form_control','placeholder':'course name'}),
        'laptop_number':forms.NumberInput(attrs={'class':'form_control','placeholder':'laptop number'}),
        'languages':forms.Select(attrs={'class':'form_control'}),
        }
        