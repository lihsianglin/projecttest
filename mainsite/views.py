from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.http import HttpResponse
from django.template.context_processors import csrf
from .models import *


# Create your views here.

def index(request):
	template = 'index.html'
	args = {}

	if request.POST:
		title = request.POST['title'];
		vid = request.POST['vid'];
		lyricsText = request.POST.getlist('lyricsText')
		sTime = request.POST.getlist('sText')
		eTime = request.POST.getlist('eText')
		count = len(lyricsText)

		vp = VideoPage.objects.create(page_title=title, video_url=vid)
		vp.save()

		for i in range(count):
			l = Lyrics.objects.create(videoPage=vp, start_time=float(sTime[i]), end_time=float(eTime[i]), content=lyricsText[i])
			l.save()

		return HttpResponse("OK")
	else:
		return render(request, template, args)

