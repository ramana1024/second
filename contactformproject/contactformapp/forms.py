from django import forms
class EmpForm(forms.Form):
    ename=forms.CharField(
        label="Enter your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    sal=forms.IntegerField(
        label="Enter your salary",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your salary'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your email'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter Your Contact Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your number'
            }
        )
    )
    location=forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your laction'
            }
        )
    )