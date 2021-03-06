from django.db import models

# Create your models here.
class  Category(models.Model):
	name = models.CharField(max_length = 30, unique = True)
	description = models.TextField()

	def __str__(self):
		return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50, unique = True)
    description = models.TextField()
    in_stock = models.BooleanField(default = True, db_index = True)
    category = models.ForeignKey(Category)

    def __str__(self):
    	return self.name