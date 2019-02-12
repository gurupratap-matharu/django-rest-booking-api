from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Market(models.Model):
    name = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport,related_name='markets', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' | ' + self.sport.name

class Selection(models.Model):
    name = models.CharField(max_length=100)
    odds = models.FloatField()
    market = models.ForeignKey(Market,related_name='selections', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Match(models.Model):
    name = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    sport = models.ForeignKey(Sport, related_name='matches', on_delete=models.CASCADE)
    market = models.ForeignKey(Market, related_name='matches', on_delete=models.CASCADE)

    class Meta:
        ordering = ('startTime',)
        verbose_name_plural = 'Matches'

    def __str__(self):
        return self.name
