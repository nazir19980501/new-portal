from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .models import Students, Enrollment
from django.core.mail import send_mail
from django.conf import settings
import random








def markColor(mark):
  if mark <= 55:
    return 'bg-pink-600'
  elif mark > 55 and mark <= 65:
    return 'bg-orange-300'
  elif mark > 65 and mark <= 75:
    return 'bg-cyan-600'
  elif mark > 75 and mark <= 85:
    return 'bg-indigo-600'
  else:
    return 'bg-teal-400'


def welcome(request, user):
    del request.session['user']
    user_data = Enrollment.objects.filter(student=user)
    marks = user_data.values_list("mark", flat=True)
    colors = []
    for i in marks:
      colors.append(markColor(i))
  
    
    return render(request, 'welcome.html',{
      'user_data':user_data,
      'colors':colors,
      'user':user
      
      })


class Login(View):

  def post(self,request):
    action = request.POST.get('action')
    
    flag = False
    if action == 'login':
      user_id = request.POST['user-id']
      password = request.POST['password']
      
      
      try:
        key = Students.objects.get(user_id=user_id)
        
      except:
        flag = True
        return render(request, 'starting-page.html',{'flag':flag})
      
      request.session['user'] = key.user_id
      if password == key.password:
        
        return welcome(request,user=key)
      else:
          flag = True
          return render(request, 'starting-page.html',{'flag':flag})
     
    
    else: 
      return HttpResponseRedirect('/reset-password')
      
       

  def get(self,request):
    
    return render(request, 'starting-page.html')
  

  





class Reset(View):
  
  def get(self, request):
    return render(request, 'password-reset.html')
  
  def post(self, request):
     user_id = request.session['user']
     user = Students.objects.get(user_id=user_id)
     email = request.POST['email']
     if email == user.email:
      request.session['code'] = str(self.resetPassword(email))
      return HttpResponseRedirect('/code')
      
     else:
       flag = True
       return render(request, 'password-reset.html',{'flag':flag})
  
       

  def resetPassword(self,email):
    code = random.randint(100000,999999)
    message = f'Your Reset password code is {code} please do not share it with anyone'
    send_mail(
      'GHU portal Reset Password',
      message,
      settings.EMAIL_HOST_USER,
      [f'{email}'],
      fail_silently=False
    )
    return code
  


class Code(View):

  def get(self,request):
    if 'code' not in request.session or 'user' not in request.session:
            return HttpResponseRedirect('/reset-password')
    return render(request, 'code.html')
  
  def post(self, request):
    code = request.session['code']
    entered_code = request.POST['code']
    

    if code == entered_code:
        user_id = request.session['user']
        user = Students.objects.get(user_id=user_id)
        new = request.POST['password']
        retype = request.POST['password-retype']
        if new == retype:
            student = Students.objects.get(user_id=user.user_id)
            student.password = new
            student.save()
            return welcome(request, user)
        else:
          flag = True
          return render(request, 'code.html', {
                'flag':flag
              })
    else:
      flag = True
      return render(request, 'code.html', {
        'flag':flag
      })



