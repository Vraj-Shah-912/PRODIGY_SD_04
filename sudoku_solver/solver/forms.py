from django import forms

class SudokuForm(forms.Form):
    grid = forms.CharField(widget=forms.Textarea, label='Sudoku Grid')
