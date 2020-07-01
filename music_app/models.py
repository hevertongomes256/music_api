from django.db import models

class Music(models.Model):

    title = models.CharField('Título', max_length=200)
    seconds = models.IntegerField('Segundos')
    album = models.ForeignKey('Album', related_name='musics', on_delete=models.CASCADE)

    class Meta:
        db_table = 'music'

    def __str__(self):
        return self.title

class Album(models.Model):

    title = models.CharField(max_length=200)
    band = models.ForeignKey('Band', related_name='albuns', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        db_table = 'album'
    
class Band(models.Model):

    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'band'

class Member(models.Model):

    name = models.CharField(max_length=200)
    age = models.IntegerField()
    band = models.ForeignKey('Band', related_name='members', on_delete=models.CASCADE)

    class Meta:
        db_table = 'member'