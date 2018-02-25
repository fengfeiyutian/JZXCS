from django.shortcuts import render

from users.models import User
import json

from tool_02.models import Blog
# Create your views here.
def index(request):
	a = Blog.objects.all().order_by('-id')[:5]
	return render(request, 'basemain.html', {'blogs': a})
#	return render(request, 'basemain.html')

def accounts_profile(request):
	if request.method == 'POST':
		a = json.loads(request.body.decode('utf-8'))
		print(a)
		b = User.objects.get(email=request.user.email)
		b.name = a['name']
		b.sex = a['sex']
		b.birthday = a['birthday']
		b.job_time = a['job_time']
		b.save()
	return render(request, 'accounts_profile.html')