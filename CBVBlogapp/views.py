from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from .models import Blogs
from .forms import SignupForm
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

class landingpage(TemplateView):
    template_name = "CBVBlogapp/landingpage.html"


class ViewallBlogs(ListView):
    model=Blogs


def SignupPage(request):
    signupform = SignupForm()
    mydict = {'signupform':signupform}
    if request.method == 'POST':
        signupform = SignupForm(request.POST)
        if signupform.is_valid():
            user=signupform.save()
            user.set_password(user.password)
            user.save()
            subject = "Welcome to Pushpak Blog"
            message = "Hello, "+user.first_name+"! Thank you for registering on Pushpak Blogs. We welcome you and wish you Happy Blogging!"
            recipient_list = [user.email]
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject,message,email_from,recipient_list)
            mydict.update({'msg':'Registered Successfully. Welcome mail sent'})
    return render(request, 'CBVBlogapp/signup.html',context=mydict)





class DetailBlog(DetailView):
    model=Blogs


class CreateNewBlog(CreateView):
    model=Blogs
    fields='__all__'
    def get_success_url(self):
        return reverse('home')


class UpdateBlog(UpdateView):
    model=Blogs
    fields='__all__'
    def get_success_url(self):
        return reverse('home')


class DeleteBlog(DeleteView):
    model=Blogs
    def get_success_url(self):
        return reverse('home')
