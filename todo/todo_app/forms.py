from django import forms
from .models import Task

class TasksForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "creator", "description", "done"]
