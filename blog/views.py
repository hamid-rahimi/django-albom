from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from blog.models import Article, Person
from blog.forms import CreateArticle, AddPerson, UpdateArticle
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


article_selected_id = 0

def blog_page(request):
    article = Article.objects.all()
    person = Person.objects.all()
    # print(article)
    # print(search_title)
    search_key = request.GET.get("search_title")
    print(request.GET.get('search_text'), 11)
    if search_key:
        article = article.filter(title__icontains=search_key)
        
    paginator = Paginator(article, 3)
    num_page = request.GET.get('page')
    page_obj = paginator.get_page(num_page)

    context = {
        'articles': page_obj,
        'persons': person,
        's_key': search_key,
    }
    return render(request, "blog/index.html", context)


def detail_page(request, article_id):
    if request.method == 'post':
        article_selected_id = request.POST.id
        
    a = get_object_or_404(Article, id=article_id)
    article_selected_id = article_id
    context = {
        'article': a,
    }
    return render(request, "blog/details.html", context)

@login_required
def add_article(request):
    if request.user.is_authenticated:
        print(request.method)
        if request.method == 'GET':
            form = CreateArticle()
        else:
            form = CreateArticle(data=request.POST, files=request.FILES)
            print(f"is valid: {form.is_valid()}")
            if form.is_valid():
                print(form.cleaned_data)
                article_title = form.cleaned_data.get('title')
                article_text = form.cleaned_data['text']
                article_created_date = form.cleaned_data['created_date']
                article_is_show = form.cleaned_data['is_show']
                article_image = form.cleaned_data['image']
                # article_author = form.cleaned_data['author']
                # item = Person.objects.get(pk=article_author)
                Article.objects.create(title=article_title,
                                       text=article_text, created_date=article_created_date,                                   is_show=article_is_show,
                                       image=article_image,
                                       author=request.user
                                    )
                a = Article.objects.last().pk
                print(f"last item is: {a}")
                return redirect('blog:detail_page', a)

        context = {
            'form': form,
        }
        return render(request, "blog/add_article.html", context)
    else:
        return redirect('accounts:login_page')

@login_required
def add_person(request):
    if request.method == 'GET':
        print(request.method)
        form_add = AddPerson()
    else:
        print(request.method)
        form_add = AddPerson(data=request.POST)
        if form_add.is_valid():
            print(f"is valid: {form_add.is_valid()}")
            print(form_add.cleaned_data)
            person_fname = form_add.cleaned_data.get('first_name')
            person_lname = form_add.cleaned_data.get('last_name')
            person_age = form_add.cleaned_data.get('age')
            person_email = form_add.cleaned_data.get('email')
            P = Person.objects.create(
                first_name=person_fname,
                last_name=person_lname,
                age=person_age,
                email=person_email
            )
            return redirect("blog:blog_page")

    return render(request, "blog/add_person.html", {'form': form_add})

@login_required
def update_page(request, article_id):
    record = get_object_or_404(Article, id=article_id)
    print(request.user.id)
    print(record.author.id)
    if request.user.id != record.author.id:
        return HttpResponse("page error...")
    if request.method == 'GET':
        print(record)
        article_form = UpdateArticle(initial={
            'title' : record.title,
            'text' : record.text,
            'created_date' : record.created_date,
            'is_show' : record.is_show,
            # 'imag' : record.image,
            })
    else:
        article_form = UpdateArticle(data=request.POST, files=request.FILES)
        if article_form.is_valid():
            title = article_form.cleaned_data.get('title')
            text = article_form.cleaned_data.get('text')
            # created_date = article_form.cleaned_data.get('created_date')
            is_show = article_form.cleaned_data.get('is_show')
            image = article_form.cleaned_data.get('image')
            
            record.title = title
            record.text = text
            # record.crated_date = created_date
            record.is_show = is_show
            if image:
                record.image = image
            
            record.save()
            
            return redirect('blog:detail_page', article_id)
    context = {'form' : article_form, 'edit' : record}
            
    return render(request, 'blog/edit_article.html', context)

@login_required
def delete_page(request, article_id):
    record = get_object_or_404(Article, pk=article_id)
    if request.user.id != record.author.id:
        return HttpResponse("page error...")
    record.delete()
    return redirect('blog:blog_page')