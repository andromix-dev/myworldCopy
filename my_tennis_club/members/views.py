from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
	mymembers = Member.objects.all().values()
	template = loader.get_template('all_members.html')
	context = {
		'mymembers': mymembers,
	}
	return HttpResponse(template.render(context, request))
def details(request, slug):
	mymember = Member.objects.get(slug=slug)
	template = loader.get_template('details.html')
	context = {
		'mymember': mymember,
	}
	return HttpResponse(template.render(context, request))
def main(request):
	template = loader.get_template('main.html')
	return HttpResponse(template.render())
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'], 
	'firstname':'Linus',
  }
  #mydata1 = Member.objects.all().values()
  #mydata2 = Member.objects.values_list('firstname')
  #mydata = Member.objects.filter(firstname='Emil').values()
  #SELECT * FROM members WHERE firstname = 'Emil';
  #AND
  #mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
  #SELECT * FROM members WHERE lastname = 'Refsnes' AND id = 2;
  #OR
  #mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  #mydata = Member.objects.filter(firstname__startswith='L').values()
  #mydata = Member.objects.all().order_by('firstname').values()
  #Descending Order
  #mydata = Member.objects.all().order_by('-firstname').values()
  #To order by more than one field
  #mydata = Member.objects.all().order_by('lastname', '-id').values()

  mydata = Member.objects.filter(firstname='Emil').values()

  context1 = {
	'mymembers': mydata,
  }
  return HttpResponse(template.render(context1, request))