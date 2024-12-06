from django.db import models

class GoalResponse(models.Model):
    module_number = models.CharField(max_length=51)
    type_of_goal = models.CharField(max_length=51)
    text = models.TextField()

    def __str__(self):
        return self.text
