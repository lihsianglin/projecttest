from django.db import models

# Create your models here.

class VideoPage(models.Model):
	page_id = models.AutoField(primary_key=True)
	page_title = models.CharField(max_length=50)
	video_url = models.CharField(max_length=20)


	def __str__(self):
		return self.page_title;


class Lyrics(models.Model):
	page_id = models.ForeignKey(VideoPage)
	start_time = models.IntegerField(max_length=5)
	end_time = models.IntegerField(max_length=5)
	content = models.CharField(max_length=100)
	

	def __str__(self):
		return self.content

