from django.db import models

# Create your models here.
class Hobby(models.Model):
    text=models.CharField(max_length=30)
    class Meta():
        verbose_name_plural = 'hobbies'
    def __str__(self):
        return self.text

#-------------------------
class Activity(models.Model):
    activity=models.ForeignKey(Hobby,on_delete=models.CASCADE)
    text=models.CharField(max_length=50)

    class Meta():
        verbose_name_plural = 'activities'

    def __str__(self):
            return self.text

#-----------------------------
class Event(models.Model):
    event=models.ForeignKey(Activity,on_delete=models.CASCADE)
    text=models.TextField()
    date = models.DateField()

    def __str__(self):
            return self.text

    def event_date(self):
        return self.date