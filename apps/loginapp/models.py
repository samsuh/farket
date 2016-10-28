
import re
from django.db import models
from django.contrib import messages
# import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
name_regex = re.compile(r'^[a-zA-Z]+$')


#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):

    def register(self, request, first_name, last_name, email, pw, confirmpw):
        valid = True
        if len(first_name)<1:
            messages.error(request, 'First Name is empty')
            valid = False
        if not name_regex.match(first_name):
            messages.error(request, 'First Name is invalid')
            valid = False
        if len(last_name)<1:
            messages.error(request, 'Last Name is empty')
            valid = False
        if not name_regex.match(last_name):
            messages.error(request, 'Last Name is invalid')
            valid = False
        if len(email)<1:
            messages.error(request, 'Email is empty')
            valid = False
        elif not email_regex.match(email):
            messages.error(request, 'Email is invalid')
            valid = False
        elif pw != confirmpw:
            messages.error(request, 'Passwords do not match')
            valid = False
        #check that email they enter is already in the database
        #if they dont match, valid = False
        try:
            dbemailcheck = user.objects.get(email = email)
            #if email already exists, throw error
            messages.error(request, 'Email already exists')
            valid = False
        except:
            pass

        if valid == True:
            user = User.objects.create(first_name = first_name,last_name = last_name, email = email, pw = pw)
            user.save()
            return valid, user
        elif valid == False:
            messages.error(request, 'Failed to register new user')
            return valid, None

    def login(self, request, email, pw):
        valid = True
        if len(email)<1:
            messages.error(request, 'Email is empty')
            valid = False
        elif not email_regex.match(email):
            messages.error(request, 'Email is invalid')
            valid = False

        if valid == True:
            user = User.objects.filter(email=email)

            if pw != user[0].pw:
                messages.error(request, 'Invalid password')
                valid = False
            else:
                pass
            return valid, user
        elif valid == False:
            return valid, None

        #get statement to compare emails, if it returns error, user doesnt exist. try/except here.
        #compare hashed pw to hashed request.POST['pw'] which is being passed postData

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    pw = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Comments(models.Model):
    comment = models.TextField(max_length=1000)
    comment_creator = models.CharField(max_length=45)
    rating = models.IntegerField()
    user = models.ForeignKey(User)
    created_at= models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
