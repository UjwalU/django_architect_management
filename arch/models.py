from django.db import models

class Architect(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)


class PortfolioItem(models.Model):
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='portfolio/')
    description = models.TextField()


class Project(models.Model):
    name = models.CharField(max_length=255)
    architect = models.ForeignKey(Architect, on_delete=models.CASCADE)
    description = models.TextField()
    location = models.CharField(max_length=255)
    completion_date = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    images = models.ImageField(upload_to='project_images')
    

class Design(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    design_date = models.DateField()
    design_images = models.ImageField(upload_to='design_images')

class Payment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    payment_date = models.DateField()
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)  
      

    def __str__(self):
        return self().name

    def __str__(self):
        return self().name

    def __str__(self):
        return self().name

    def __str__(self):
        return self.project.__str__()

    def __str__(self):
        return self.project.__str__()
