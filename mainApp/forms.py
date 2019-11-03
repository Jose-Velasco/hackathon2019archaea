from django import forms

class ResolveForm(forms.Form):
	resolveID = forms.IntegerField(widget=forms.HiddenInput(), initial=0)