from django.shortcuts import render, redirect
import json
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, 'farketapp/index.html')

def search(request):
    # response = request.GET("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/idSearch?id="+ {{res.results[0].id}})
    # json_data = json.loads(response.text)
    # print response
    context = {
        "zip": request.POST['zip']
    }
    return render(request, 'farketapp/search.html', context)

#temp button until we put login/registration into the index.
def searchpage(request):
    return render(request, 'farketapp/search.html')
