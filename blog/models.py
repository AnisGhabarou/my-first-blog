from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    def publish(self):
        self.published_date = timezone.now()# automatically save and publish the post when created
        self.save()

    def __str__(self):
        return self.title #<QuerySet [<Post: Post object (1)>, <Post: Post object (2)>, <Post: Post object (3)>, <Post: Post object (4)>]> -
                                                                                                                                           #|
                                                                                                                                           #|
                        #<QuerySet [<Post: first blog ever>, <Post: 2nd blog>, <Post: 3rd blog>, <Post: Sample title>]>