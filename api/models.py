from django.db import models


class ModelBase(models.Model):
    id = models.BigAutoField(primary_key=True)
    removed = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Twitters(ModelBase):
    tweetdate = models.DateTimeField(auto_now_add=True)
    nick = models.CharField(max_length=15, blank=True, null=True)
    tweet = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.nick, self.tweet)
