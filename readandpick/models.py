from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now
from django.template.defaultfilters import default


# Create your models here.
class Book(models.Model):
    title = models.CharField('title', max_length=255)   
    author = models.CharField('author', max_length=255)
    price = models.IntegerField()
    description = models.TextField('description', blank=True) 	
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated', null=True)
    image_name = models.CharField('image_name', max_length=255, default='No Image available')

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
        ordering = ['id']
        db_table = 'book'
    
    objects = models.Manager()
    
    @python_2_unicode_compatible    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Book, self).save(*args, **kwargs)
