from django.contrib import admin
from .models import Post,Item,orders,quantity




admin.site.register(Post)
admin.site.register(Item)
admin.site.register(orders)
admin.site.register(quantity)

