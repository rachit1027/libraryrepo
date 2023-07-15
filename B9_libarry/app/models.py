from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    class Meta:
        abstract = True # isse ye hoga ki is class ka table migrations file kuch nahi banega, isko hide kar ke rakho apan bol rahe hai basically isko consider hi mat karo

class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    qty = models.IntegerField()
    is_published = models.BooleanField(default=True) # book published hai ya nhi. Book crete karnenge to vo by default published rahega isliye TRue diya hai apan ne boolean field ko
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "book" # table ka naam diya hai

    def __str__(self):
        return self.name
    