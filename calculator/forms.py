from django import forms

class SGPAForm(forms.Form):
    GRADE_CHOICES = [
        ('A++', 'A++'),
        ('A+', 'A+'),
        ('A', 'A'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('E+', 'E+'),
        ('E', 'E'),
        ('F', 'F'),
    ]

    CHOICE_SIZE = {'style': 'width: 500px; height: 50px;'}  # You can adjust the width and height as needed

    EM = forms.ChoiceField(choices=GRADE_CHOICES, label="Engineering Mathematics", widget=forms.Select(attrs=CHOICE_SIZE))
    BEE = forms.ChoiceField(choices=GRADE_CHOICES, label="Basic Electrical Engg / Basic Civil Engg", widget=forms.Select(attrs=CHOICE_SIZE))
    EC = forms.ChoiceField(choices=GRADE_CHOICES, label="Engg Chemistry / Engg Physics", widget=forms.Select(attrs=CHOICE_SIZE))
    BME = forms.ChoiceField(choices=GRADE_CHOICES, label="Basic Mechanical Engineering / PPS", widget=forms.Select(attrs=CHOICE_SIZE))
    CS = forms.ChoiceField(choices=GRADE_CHOICES, label="Communication Skills / Human Values", widget=forms.Select(attrs=CHOICE_SIZE))
    LL = forms.ChoiceField(choices=GRADE_CHOICES, label="Language Lab / Human Values Lab", widget=forms.Select(attrs=CHOICE_SIZE))
    MPW = forms.ChoiceField(choices=GRADE_CHOICES, label="Manufacturing Practices Workshop / Computer prog. Lab", widget=forms.Select(attrs=CHOICE_SIZE))
    CL = forms.ChoiceField(choices=GRADE_CHOICES, label="Chemistry Lab / Physics Lab", widget=forms.Select(attrs=CHOICE_SIZE))
    BEEL = forms.ChoiceField(choices=GRADE_CHOICES, label="Basic Electrical Engineering Lab / Civil lab", widget=forms.Select(attrs=CHOICE_SIZE))
    CAED = forms.ChoiceField(choices=GRADE_CHOICES, label="Computer Aided Machine Drawing / Engg graphics", widget=forms.Select(attrs=CHOICE_SIZE))
    DECA = forms.ChoiceField(choices=GRADE_CHOICES, label="DECA", widget=forms.Select(attrs=CHOICE_SIZE))
