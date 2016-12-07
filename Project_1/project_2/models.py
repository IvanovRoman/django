from django.db import models

# Create your models here.
class  Category(models.Model):
	name = models.CharField(max_length = 30, unique = True)
	description = models.TextField()
    
class Good(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    description = models.TextField()
    in_stock = models.BooleanField(default = True, db_index = True)
    category = models.ForeignKey(Category)

    def __str__(self):
        s = self.name
        if not self.in_stock:
            s = s + " (нет в наличии)"
        return s

    def get_is_stock(self):
        if self.in_stock:
                return "+"
        else:
            return ""

class Products(models.Model):
	name = models.CharField(max_length = 50, unique = True)
	description = models.TextField()