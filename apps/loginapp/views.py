# Inside your app's views.py file
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Comments
from django.core.urlresolvers import reverse

def index(request):
    return render(request, 'loginapp/index.html')

# DO NOT PASS THE WHOLE REQUEST OBJECT TO THE MODEL!!!

def register(request):
    #invoke User.objects.register()
    # request.session['first_name'] = request.POST['first_name']. Need to access somehow: confirmpw = request.POST['confirmpw']
    print request.POST['first_name']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    pw = request.POST['pw']
    confirmpw = request.POST['confirmpw']

    registertuple1, registertuple2 = User.objects.register(request, first_name, last_name, email, pw, confirmpw)
    print registertuple2
    if registertuple1 == True:
        request.session['first_name'] = registertuple2.first_name
        request.session['successMsg'] = "You have successfully registered!"
        return render(request, 'loginapp/search.html')

        # return render(request, '../../farketapp/templates/farketapp/search.html')
    else:
        print "Register Else Error"
        # messages.error(request, 'Incorrect Registration Information')
        return render(request, 'loginapp/index.html')
        # return redirect(reverse('login:index'))

def login(request):
    valid, user = User.objects.login(request, email = request.POST['email'], pw = request.POST['pw'])
    if valid == True:
        request.session['first_name'] = user[0].first_name
        request.session['id'] = user[0].id
        request.session['successMsg'] = "You have successfully logged in!"
#this should probably change to a url like (reverse('logreg_success')) or 'farketapp_success' or 'farketapp_home'
        return render(request, 'loginapp/search.html')
        # return render(request, '../../farketapp/templates/farketapp/search.html')
    else:
        print "Login Else Error"
        # messages.error(request, 'Incorrect Login Information')
        return redirect(reverse('login:index'))

def results(request):
    # response = request.GET("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/idSearch?id="+ {{res.results[0].id}})
    # json_data = json.loads(response.text)
    # print response
    context = {
        "zip": request.GET['zip']
    }
    return render(request, 'loginapp/results.html', context)

def logout(request):
    request.session.clear()
    return redirect(reverse('login:index'))

def reviews(request):
    context = {
    "comments" : Comments.objects.all()
    }
    return render(request, 'loginapp/reviews.html', context)

def comments(request):
    print request.POST['comment']
    print request.session['id']
    newcomment = Comments.objects.create(user_id=request.session['id'],comment=request.POST['comment'],comment_creator=request.session['first_name'],rating=request.POST['rating'])
    newcomment.save()
    return redirect('/reviews')

def delete(request, id):
    Comments.objects.filter(id=id).delete()
    return redirect('/reviews')

def search(request):
    return render(request,'loginapp/search.html')
