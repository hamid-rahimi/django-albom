from django.shortcuts import render
from blog.models import Person, Article
# import jdatetime
# from django.http import HttpResponse

def main_home(request):
    pList = Person.objects.all()
    aList = Article.objects.all()
    
    context = {
        'pList' : pList,
        'aList' : aList
    }
    return render(request, "home\index.html", context)
