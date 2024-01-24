from django import forms
from .models import TreeNode

class TreeNodeForm(forms.ModelForm):
    class Meta:
        model = TreeNode
        fields = ['parent', 'label']
