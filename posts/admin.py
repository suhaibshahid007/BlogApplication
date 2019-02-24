from django.contrib import admin


# regiter your models of app here ....

from posts.models import Post

class PostAminModel(admin.ModelAdmin):
    list_display = ["title" ,"updated" , "timestamp"]
    list_filter = ["updated","timestamp"]
    search_fields = ["title"]



admin.site.register(Post , PostAminModel)
