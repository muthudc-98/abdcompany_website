from django import forms
from companyapp.models import companydata

class companyform(forms.ModelForm):
	class Meta:
		model=companydata
		fields='__all__'