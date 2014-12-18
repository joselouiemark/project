from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import Context
from django.views.generic.base import TemplateView
from scheduler.forms import ScheduleForm
from scheduler.models import Schedule
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime
from datetime import date

def schedules(request, stat=0, dfrom='', dto=''):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
	if request.POST:
		sdate = request.POST.get('sdate', '')
		edate = request.POST.get('edate', '')
		type = request.POST.get('type', 0)
		
		return HttpResponseRedirect('/scheduler/all/'+type+'/'+datetime.strptime(sdate, '%Y-%m-%d' ).strftime('%Y%m%d')+'/'+datetime.strptime(edate, '%Y-%m-%d' ).strftime('%Y%m%d')+'/')
		
	
	allObjs = Schedule.objects.filter(owner=request.user.username);
	allObjs.filter(status=1).filter(date__lt=date.today()).update(date=date.today())
	stat = int(stat)
	if stat > 0 and stat < 4:
		allObjs = allObjs.filter(status=stat)
	
	if dfrom not in [None, ''] and dto not in [None, '']:
		allObjs = allObjs.filter(date__range=[ datetime.strptime(dfrom, '%Y%m%d' ),datetime.strptime(dto, '%Y%m%d' )])

	return render_to_response('schedules.html',
							{'schedules':allObjs,'full_name': request.user.first_name +" " +request.user.last_name,
							'today':date.today()})

def create(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if request.POST:
		form = ScheduleForm(request.POST)
		form.owner = request.user.username
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/scheduler/all')
	else:
		form = ScheduleForm()
		form.owner = request.user.username
	
	return render_to_response('create_schedule.html',  {
		'form': form,
		'full_name': request.user.first_name +" " +request.user.last_name,
		}, context_instance=RequestContext(request))

def schedule(request, schedule_id = None):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	schedule = Schedule.objects.get(id=schedule_id)
	if request.POST:
		form = ScheduleForm(request.POST, instance=schedule)
		form.owner = request.user.username
		if form.is_valid():
			form.save()
			
			return HttpResponseRedirect('/scheduler/all')
	else:
		form = ScheduleForm(instance=schedule)
		form.owner = request.user.username
	
	return render_to_response('schedule.html',  {
		'form': form,
		'full_name': request.user.first_name +" " +request.user.last_name
		}, context_instance=RequestContext(request))
	
def cancel_schedule(request, schedule_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if schedule_id:
		a = Schedule.objects.get(id=schedule_id)
		a.status = 3
		a.save()
		
	return HttpResponseRedirect('/scheduler/all')

def finish_schedule(request, schedule_id):
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/login/')
		
	if schedule_id:
		a = Schedule.objects.get(id=schedule_id)
		a.status = 2
		a.save()
		
	return HttpResponseRedirect('/scheduler/all')

