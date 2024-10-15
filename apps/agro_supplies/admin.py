from django.contrib import admin
from  apps.agro_supplies.models import *

# Register your models here.

admin.site.register(Variety)
admin.site.register(Company)
admin.site.register(Supplier)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Warehouse)
admin.site.register(Supply)
admin.site.register(CategoryEquipment)
admin.site.register(SubcategoryEquipment)
admin.site.register(ToolAndEquipment)
admin.site.register(ToolAssignment)
