from django.db import models

# Create your models here.
class Sector(models.Model): 
    sector = models.CharField(null=True, max_length=150)
    
    def __str__(self):
        return self.sector


class Sub_sector(models.Model):
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    sub_sector = models.CharField(null=True, max_length=150)

    def __str__(self):
        return self.sub_sector
    

class Lab(models.Model): 
    lab = models.CharField(max_length=200)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    sub_sector = models.ForeignKey(Sub_sector, on_delete=models.CASCADE)    
    
    
    def __str__(self): 
        return self.lab
    
class Lab_type(models.Model): 
    lab_type = models.CharField(null=True, blank=True, max_length=200)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.lab_type
    
    
class Equipment(models.Model): 
    equipment = models.CharField(null=True, blank=True, max_length=250)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.equipment
    
    
class Scope(models.Model): 
    lab_scope = models.CharField(null=True, blank=True, max_length=250)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.lab_scope
    
class Accreditation(models.Model):
    accreditation = models.CharField(null=True, blank=True, max_length=250)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.accreditation
    