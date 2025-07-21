from django.db import models

class LearningGoal(models.Model):
    name = models.CharField(max_length=100) 
    description = models.TextField()

    def __str__(self):
        return self.name

class Topic(models.Model):
    goal = models.ForeignKey(LearningGoal, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    week = models.PositiveIntegerField()
    resource_link = models.URLField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Week {self.week}: {self.title}"
