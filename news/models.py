from django.db import models
from django.db.models import Count

from account.models import Author


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def get_status(self):
        statuses = NewsStatus.objects.filter(news=self) \
            .values('status__name').annotate(count=Count('status'))
        result = {}
        for i in statuses:
            result[i['status__name']] = i['count']

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def get_status(self):
        statuses = CommentStatus.objects.filter(comment=self) \
            .values('status__name').annotate(count=Count('status'))
        result = {}
        for i in statuses:
            result[i['status__name']] = i['count']

        return result

    def __str__(self):
        return self.text


class Status(models.Model):
    slug = models.SlugField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class NewsStatus(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status} - {self.author} - {self.news}'

    class Meta:
        unique_together = ['author', 'news']


class CommentStatus(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.status} - {self.author} - {self.comment}'

    class Meta:
        unique_together = ['author', 'comment']
