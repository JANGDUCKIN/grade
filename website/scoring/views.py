from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .models import UploadFile
from .forms import UserForm, LoginForm
# , UploadFileForm
# 파일 실행
from subprocess import PIPE, Popen

class IndexView(generic.ListView):
	template_name = 'scoring/index.html'
	context_object_name = 'all_files' # <<<< default 값

	def get_queryset(self):
		return UploadFile.objects.all()


class DetailView(generic.DetailView):
	model = UploadFile
	template_name = 'scoring/detail.html'

	def post(self, request, pk):
		# form = UploadFileForm(request.POST or None, request.FILES or None)
		# if form.is_valid():
		process = Popen(["python", "/Users/jangdeog-in/Desktop/grade/website/media/test.py"], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		# print(process)
		# instance = model.objects.create(file="/Users/jangdeog-in/Desktop/website/media/test2.py", score="asdf")

		sq = UploadFile.objects.get(file ="test.py")
		# print(sq.score)
		if sq :
			sq.score = stdout.decode('utf-8')
			if int(sq.score) >= 70 :
				sq.result = "성공"
			else :
				sq.result = "실패"
			sq.save()
		else:	
			sq.score = stderr.decode('utf-8')
		# print(stdout.decode('utf-8'))
		return redirect('scoring:index')
		# return render(request, self.template_name)
	# def get(self, request, pk):
	# 	form = self.form_class(None)
	# 	return render(request, self.template_name, {'form' : form})

	# def post(self, request):
	# 	form = self.form_class(request.POST)

	# 	if form.is_valid():
	# 		process = Popen(['python', 'media/test.py'], stdout=PIPE, stderr=PIPE)
	# 		stdout, stderr = process.communicate()
	# 		print(stdout)
	# 		return render(request, self.template_name, {'form' : form})

class UploadFileCreate(CreateView):
	model = UploadFile
	fields = ['file']

	# def post(request):
	# 	form = UploadFileForm(request.POST or None, request.FILES or None)
	# 	if form.is_valid():
	# 		sq = form.save(commit=False)
	# 		sq.user = request.user


class UploadFileUpdate(UpdateView):
	model = UploadFile
	fields = ['file']

class UploadFileDelete(DeleteView):
	model = UploadFile
	success_url = reverse_lazy('scoring:index')
	

# 회원가입

class UserFormView(View):
	form_class = UserForm
	template_name = 'scoring/registration_form.html'

	# display blank form 
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form' : form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# clean (nomalized) data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			# user.username = '바꾸기'
			user.set_password(password)
			user.save() 	

			# returns User objects if credentials are coreect
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('scoring:index')

		return render(request, self.template_name, {'form' : form})			

#로그인

def login_user(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username = username, password = password)		

		if user is not None:
			if user.is_active:
				login(request, user)
				files = UploadFile.objects.filter(pk=request.user.pk)
				return render(request, 'scoring/index.html', {'files' : files})
			else:
				return render(request, 'scoring/login.html', {'error_message' : 'Your account has been disabled'})
		else:
			return render(request, 'scoring/login.html', {'error_message' : 'Invalid login'})
	return render(request, 'scoring/login.html')			

#로그아웃
def logout_user(request):
	logout(request)
	form = UserForm(request.POST or None)
	context = {
		"form":form,
	}
	return render(request, 'scoring/login.html', context)

## 파일 업로드 후 실행 도전  
# class Run(CreateView):
# 	model = GREP
# 	fields = ['pf']

# 	def upload_file(self, request):
# 		if request.method == 'POST':
# 			form = GREP(request.POST, request.FILES)
# 			if form.is_valid():
# 				form.save()
# 				# return render(request, 'scoring/index.html', {''})
# 		else:
# 			form = GREP()
# 		return render(request, 'scoring/grep_form.html', {'form': form})			


# 초기 모델

# from django.http import Http404
# # from django.http import HttpResponse
# # from django.template import loader
# from django.shortcuts import render, get_object_or_404
# from .models import UI


# def index(request):
# 	all_ui = UI.objects.all()
# 	# html = ''
# 	# for ui in all_ui:
# 	# 	url = '/scoring/' + str(ui.id) + '/'
# 	# 	html += '<a href="' + url + '">' + ui.title + '</a><br>'
# 	# return HttpResponse("<h1> This is the Scoring homepage</h1>")
# 	# return HttpResponse(html)
# 	# template = loader.get_template('scoring/index.html')
# 	# context = {
# 	# 	'all_ui' : all_ui, 
# 	# }
# 	# return HttpResponse(template.render(context, request))
# 	return render(request, 'scoring/index.html', {'all_ui' : all_ui})

# def detail(request, ui_id):
# 	# return HttpResponse("<h2>Details for UI id : " + str(ui_id) + "</h2>")
# 	# try:
# 	# 	ui = UI.objects.get(pk=ui_id)
# 	# except UI.DoesNotExist:
# 	# 	raise Http404("UI does not exist")	
# 	ui = get_object_or_404(UI, pk = ui_id)
# 	return render(request, 'scoring/detail.html', {'ui' : ui})

# def ok(request, ui_id):
# 	ui = get_object_or_404(UI, pk = ui_id)
# 	try:
# 		selected_file = ui.file_set.get(pk=request.POST['file'])
# 	except (KeyError, File.DoesNotExist):
# 		return render(request, 'scoring/detail.html', {
# 			'ui' : ui,
# 			'error_message' : "You did not select a great file",
# 		})
# 	else:
# 		selected_file.is_ok = True
# 		selected_file.save()
# 		return render(request, 'scoring/detail.html', {'ui' : ui})
# ##의문점 : ui_id 와 ui.id 의 차이점이란 

