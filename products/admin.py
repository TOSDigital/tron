from django.contrib import admin
from .models import About, Product, ProductMedia, ProductCategory, Founder, Team


admin.site.register(About),

class ProductSteps(admin.TabularInline):
    model = ProductMedia

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductSteps] 

admin.site.register(Product, ProductAdmin)


admin.site.register(ProductCategory),

admin.site.register(Founder),

admin.site.register(Team),




