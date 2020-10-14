from django.db import models
from django.contrib.auth.backends import get_user_model

User = get_user_model()

class Units(models.Model):
    UnitName = models.CharField(max_length=100)
    Lecturer = models.TextField()
    UnitTopics = models.CharField(max_length=100)

    def __str__(self):
        return self.UnitName


class imge(models.Model):
    img = models.ImageField()

    def __str__(self):
        return self.img


class Lesson(models.Model):
    unit = models.ForeignKey(Units, on_delete=models.CASCADE, related_name='lessons')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

class Class(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    unit_taken = models.ForeignKey(Units, on_delete=models.CASCADE)
    

class Attendee(models.Model):
    student = models.ForeignKey(User, on_delete = models.CASCADE)
    lesson = models.ManyToManyField(Lesson)