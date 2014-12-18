from django import forms
from scheduler.models import Schedule

class ScheduleForm(forms.ModelForm):
	class Meta:
		model = Schedule

	def __init__(self, *args, **kwargs):
		super (ScheduleForm, self).__init__(*args,**kwargs)
		self.fields.pop('owner')
		
	def save(self, commit=True):
		sched = super(ScheduleForm, self).save(commit=False)
		if commit:
			sched.save()
		
		return sched
