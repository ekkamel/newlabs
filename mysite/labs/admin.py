from django.contrib import admin
from .models import Lab, Sector, Sub_sector, Lab_type, Scope, Equipment, Accreditation

# Register your models here.
admin.site.register(Sector)
admin.site.register(Sub_sector)


class Lab_typeInline(admin.StackedInline): 
    model = Lab_type
    extra = 1

class Lab_typeAdmin(admin.ModelAdmin): 
    fields = ['lab_type']
    

class ScopeInline(admin.StackedInline): 
    model = Scope
    extra = 1
    
class ScopeAdmin(admin.ModelAdmin): 
    fields = ['lab_scope']
    
class EquipmentInline(admin.StackedInline): 
    model = Equipment
    extra = 4

class EquipmentAdmin(admin.ModelAdmin): 
    fields = ['equipment']
    
class AccreditationInline(admin.StackedInline): 
    model = Accreditation
    extra = 1
    
class AccreditationAdmin(admin.ModelAdmin): 
    fields = ['accreditation']


class LabAdmin(admin.ModelAdmin): 
    inlines = [
        Lab_typeInline, 
        ScopeInline,
        AccreditationInline,                     
        EquipmentInline,
    ] 
    
    list_display = ('lab', 'sector', 'sub_sector')

admin.site.register(Lab, LabAdmin)