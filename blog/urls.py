from django.urls import path
from blog.views import blog_page, detail_page, add_article, add_person, update_page, delete_page

app_name = 'blog'
urlpatterns = [
    path("main/", blog_page, name="blog_page"),
    path("detail/<int:article_id>/", detail_page, name="detail_page"),
    path("update/<int:article_id>/", update_page, name="update_page"),
    path("delete/<int:article_id>/", delete_page, name="delete_page"),
    path("article/", add_article, name="add_article"),
    path("person/", add_person, name="add_person"),
    # path("update/<int:pk>/", update_page, name="update_page"),
]
