from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.FloatField(default=0.0)

    def update_rating(self):
        post_rating = sum([post.article_rating for post in self.posts.all()]) * 3
        comment_rating = sum(comment.comment_rating for comment in Comment.objects.filter(post__in=self.posts.all()))
        comment_post_rating = sum(post.article_rating for post in self.posts.all())

        self.user_rating = post_rating + comment_rating + comment_post_rating
        self.save()


class Category(models.Model):
    category_name = models.CharField(unique=True, max_length=255)


article = 'AR'
news = 'NE'

options = [
    (article, 'Статья'),
    (news, 'Новости')
]

class Post(models.Model):
    article = 'AR'
    news = 'NE'
    author = models.ForeignKey(Author, on_delete= models.CASCADE, related_name='posts')
    choicefield = models.CharField(max_length=255, choices=options, default= article)
    time_in = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)
    article_title = models.CharField(max_length=255)
    article_text = models.TextField()
    article_rating = models.FloatField(default=0.0)

    def like(self):
        self.article_rating = self.article_rating + 1
        self.save()

    def dislike(self):
        self.article_rating = self.article_rating - 1
        self.save()

    def preview(self):
        if len(self.article_text) > 124:
            return self.article_text[:124] + "..."
        else:
            return self.article_text




class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    comment_rating = models.FloatField(default=0.0)

    def like(self):
        self.post.comment_rating += 1
        self.post.save()

    def dislike(self):
        self.post.comment_rating -= 1
        self.post.save()