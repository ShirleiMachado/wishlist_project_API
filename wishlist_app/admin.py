  
from django.contrib import admin
from wishlist_app.models import Client, Product, Fav_Product

class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ['name', 'email']
    list_per_page = 10

admin.site.register(Client, Clients)

class Products(admin.ModelAdmin):
    list_display = ('id', 'price', 'brand', 'title', 'reviewScore')
    list_display_links = ('id', 'title', 'brand', 'price')
    search_fields = ['title', 'brand']
    list_per_page = 10

admin.site.register(Product, Products)

class Wishlist_app(admin.ModelAdmin):
    list_display = ('id', 'client')
    list_display_links = ('id', 'client')
    search_fields = ['client__name']
    list_per_page = 10

admin.site.register(Fav_Product)