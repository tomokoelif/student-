from django import forms

class GoalsForm(forms.Form):
    academicGoal1 = forms.CharField(
        label='Academic Goal 1', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first academic goal'})
    )
    academicGoal2 = forms.CharField(
        label='Academic Goal 2', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your second academic goal'})
    )
    academicGoal3 = forms.CharField(
        label='Academic Goal 3', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your third academic goal'})
    )
    personalGoal1 = forms.CharField(
        label='Personal Goal 1', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first personal goal'})
    )
    personalGoal2 = forms.CharField(
        label='Personal Goal 2', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your second personal goal'})
    )
    personalGoal3 = forms.CharField(
        label='Personal Goal 3', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your third personal goal'})
    )
    employmentGoal1 = forms.CharField(
        label='Employment Goal 1', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first employment goal'})
    )
    employmentGoal2 = forms.CharField(
        label='Employment Goal 2', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your second employment goal'})
    )
    employmentGoal3 = forms.CharField(
        label='Employment Goal 3', 
        max_length=100, 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your third employment goal'})
    )
    