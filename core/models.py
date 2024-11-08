from django.db import models

# from django.db import models




class Case(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cases/images/')
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    raised_amount = models.DecimalField(max_digits=10, decimal_places=2)
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def progress_percentage(self):
        return (self.raised_amount / self.goal_amount) * 100



