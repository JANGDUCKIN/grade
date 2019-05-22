from django.db import models
from django.urls import reverse
# from django.contrib.auth.models import Permission, User


# 유저 한명의 올린 파일
class UploadFile(models.Model):
	# name = models.CharField(max_length=250)
	# title = models.CharField(max_length=250)
	# gender = models.CharField(max_length=20)
	# user = models.ForeignKey(User, default=1)
	file = models.FileField()
	score = models.IntegerField(default=0)
	result = models.CharField(max_length=250, default="실패")

	def get_absolute_url(self):
		return reverse('scoring:detail', kwargs={'pk': self.pk})

	def __str__(self):
		 return self.file.name # + '-' + self.title

# 유저가 올린 파일들 
# class File(models.Model):
# 	ui = models.ForeignKey(UI, on_delete=models.CASCADE)
# 	file_type = models.CharField(max_length=100)
# 	file_title = models.CharField(max_length=250)
# 	is_ok = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.file_title


####파일 추가하는 방법
####python manage.py shell
####from scoring.models import UI, File
####UI.objects.all()
#### a = UI(user = " ", title = " ", gender = " ")
#### a.save()
#### a.user, a.pk, a.id ... and so on
#### UI.objects.filter(id=?)


####관련된 클레스를 추가하는 법
#from scoring.models import UI, File
#ui1 = UI.objects.get(pk=2)
#ui1.user
#file = File()
#file.ui = ui1
#file.file_type = ""
#file.file_title = ""
#file.save()
#ui1.file_set.all()
#ui1.file_set.create(file_title = '', file_type = 'py')
#ui1.file_set.count() <- 수 출력 