from django.db import models
from django.conf import settings
from markdown_deux import markdown
from django.utils.safestring import mark_safe

# Create your models here.

#create your models here
# Model View Controller

def upload_location(instance , filename):
    print("hello!!!")
    return "%s/%s" %(instance.id , filename)

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL  , on_delete=models.CASCADE , default=1);
    title = models.CharField(max_length=120)
    image =models.ImageField( upload_to=upload_location,null=True, blank=True , height_field="height_field" , width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True , auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False , auto_now_add=True)

    def __str__(self):
        return  self.title

    def __unicode__(self):
        return  self.title

    def get_markdown(self):
        content = self.content
        markedContent = markdown(content)
        return mark_safe((markedContent))




