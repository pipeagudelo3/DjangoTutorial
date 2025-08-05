from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.description[:30]
