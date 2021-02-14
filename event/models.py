from django.db import models

class EventDetail(models.Model):
    start_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=400)
    img_url = models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Participant(models.Model):
    name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=12)
    event = models.ForeignKey(EventDetail, on_delete=models.CASCADE)
    def __str__(self):
        return self.name