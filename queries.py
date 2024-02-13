import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()


from newsportal.models import *

authors = Author.objects.all()
author1 = Author.objects.get(id=1)
author2 = Author.objects.get(id=2)
for author in authors:
    print(author)

categories = Category.objects.all()
category1 = Category.objects.get(id = 1)
category3 = Category.objects.get(id = 3)
for category in categories:
    print(category)

posts = Post.objects.all()
post1 = Post.objects.get(id = 1)
post2 = Post.objects.get(id = 2)
post3 = Post.objects.get(id = 3)
post1.categories.add(category1, category3)
for i in range(5):
    post1.like()
post2.like()
post3.like()
post3.dislike()
for post in posts:
    print(post)

comments = Comment.objects.all()
comment1 = Comment.objects.get(id = 1)
comment2 = Comment.objects.get(id = 2)
comment3 = Comment.objects.get(id = 3)
comment4 = Comment.objects.get(id = 4)
for comment in comments:
    print(comment)

author1.update_rating()
author2.update_rating()
best_author = Author.objects.all().order_by('-user_rating').first()
print(f"Username: {best_author.User}")
print(f"Rating: {best_author.user_rating}")

best_post = Post.objects.filter(author = best_author).order_by('-article_rating').first()
print(f"\nДата добавления: {best_post.time_in}")
print(f"Username автора: {best_post.author.User.username}")
print(f"Рейтинг статьи: {best_post.article_rating}")
print(f"Заголовок: {best_post.article_title}")
print(f"Превью: {best_post.preview()}")

comments2 = Comment.objects.filter(post=best_post)
print("\nКомментарии:")
for comment in comments:
    print(f"Дата: {comment.time_in}")
    print(f"Пользователь: {comment.user.username}")
    print(f"Рейтинг комментария: {comment.comment_rating}")
    print(f"Текст: {comment.text}")
    print("-" * 20)