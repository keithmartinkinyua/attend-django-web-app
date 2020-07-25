from django.db import models

class Units(models.Model):
    UnitName = models.CharField(max_length=100)
    Lecturer = models.TextField()
    UnitTopics = models.CharField(max_length=100)

    def __str__(self):
        return self.UnitName



    
