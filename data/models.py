from django.db import models
class m(models.Model):
    mid = models.CharField(u'movie_id', max_length=10)
    name = models.CharField(u'movie_name', max_length=255)
    year = models.CharField(u"year", max_length=4)
    def __unicode__(self):
        return self.name
class u(models.Model):
    uid = models.CharField(u'user_id', max_length=20)
    name = models.CharField(u'user_name', max_length=100)
    signi = models.CharField(u'signiture', max_length=255)
    def __unicode__(self):
        return self.name
class re(models.Model):
    uid = models.CharField(u'user_id', max_length=20)
    recommend = models.TextField(u'movie_id')
    arating = models.FloatField()
    def __unicode__(self):
        return self.uid
class nr(models.Model):
    uid = models.CharField(u'user_id', max_length=20)
    recommend = models.TextField(u'movie_id')
    arating = models.FloatField()
    def __unicode__(self):
        return self.uid
