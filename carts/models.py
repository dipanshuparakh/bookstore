from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.template.defaultfilters import default
from library.models import Book


# Create your models here.
class Cart(models.Model):
    book = models.ForeignKey(Book)
    quantity = models.PositiveIntegerField(default=1)
    price = models.IntegerField()     
    date_created = models.DateTimeField('date created', auto_now=False)
    date_updated = models.DateTimeField('date updated', auto_now=True)

    class Meta:
        verbose_name = 'cart'
        ordering = ['id']
        db_table = 'cart'
    
    objects = models.Manager()
    
    @python_2_unicode_compatible    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Book, self).save(*args, **kwargs)
