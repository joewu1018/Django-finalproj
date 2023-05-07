from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from blog import models
import math
from datetime import datetime, timedelta
from django.utils import timezone
from accounts.models import UserProfile
# Create your views here.

#blog頁面
# def blog(request):
#     return render(request, 'blog/apple-blog.html')

page1 = 1

def index(request, pageindex=None):  #首頁
	q = request.GET.get('q', None)
	newsall  = ''
	if q == None or q == "":
		newsall = models.BlogPost.objects.all().order_by('-id')
	elif q !=  None:
		newsall = models.BlogPost.objects.filter(title__contains=q)
	global page1
	pagesize = 3
	
	datasize = len(newsall)
	totpage = math.ceil(datasize / pagesize)
	if q == None or q == "":
		if pageindex==None:
			page1 = 1
			newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[:pagesize]
		elif pageindex=='1':
			start = (page1-2)*pagesize
			if start >= 0:
				newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
				page1 -= 1
		elif pageindex=='2':
			start = page1*pagesize
			if start < datasize:
				newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
				page1 += 1
		elif pageindex=='3':
			start = (page1-1)*pagesize
			newsunits = models.BlogPost.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
	elif q !=  None:
		if pageindex==None:
			page1 = 1
			newsunits = models.BlogPost.objects.filter(enabled=True, title__contains=q).order_by('-id')[:pagesize]
		elif pageindex=='1':
			start = (page1-2)*pagesize
			if start >= 0:
				newsunits = models.BlogPost.objects.filter(enabled=True, title__contains=q).order_by('-id')[start:(start+pagesize)]
				page1 -= 1
		elif pageindex=='2':
			start = page1*pagesize
			if start < datasize:
				newsunits = models.BlogPost.objects.filter(enabled=True, title__contains=q).order_by('-id')[start:(start+pagesize)]
				page1 += 1
		elif pageindex=='3':
			start = (page1-1)*pagesize
			newsunits = models.BlogPost.objects.filter(enabled=True, title__contains=q).order_by('-id')[start:(start+pagesize)]
	currentpage = page1

	return render(request, "blog/apple-blog.html", locals())

def detail(request, slug=None):  #詳細頁面
	if request.method == 'POST':
		bcontent = request.POST.get('bcontent')
		bblogpost = models.BlogPost.objects.get(id=request.POST.get('bblogpost'))
		bauthor = UserProfile.objects.get(id=request.POST.get('bauthor'))
		board = models.BoardUnit.objects.create(bblogpost=bblogpost, bcontent=bcontent, bauthor=bauthor)
		board.save()
		return redirect(reverse('blog_detail', args=[slug]))
	else:
		unit = models.BlogPost.objects.get(slug=slug)
		category = unit.category
		title = unit.title
		pubtime = unit.publish_time
		tags = unit.tags
		content = unit.content
		unit.press += 1
		unit.save()
		blog = get_object_or_404(models.BlogPost, slug=slug)
		boards = models.BoardUnit.objects.filter(bblogpost=blog)
		now = timezone.now()
		for board in boards:
			timedelta = now - board.btime
			minutes = int(timedelta.seconds / 60)
			board.btimedelta = minutes
			board.save()
	return render(request, "blog/detail.html", locals())