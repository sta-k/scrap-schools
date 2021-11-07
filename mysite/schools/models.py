from django.db import models


class State(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name = models.CharField(max_length=200)
    state = models.ForeignKey('State',on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name

class SubDistrict(models.Model):
    name = models.CharField(max_length=200)
    no_schools = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    district = models.ForeignKey('District',on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return f'{self.name}({self.no_schools})'

class EduDistrict(models.Model):
    name = models.CharField(max_length=200)
    subdistrict = models.ForeignKey('SubDistrict',on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name

class School(models.Model):
    name = models.CharField(max_length=250)
    udise = models.CharField(max_length=11)
    # sub_district = models.ForeignKey('SubDistrict',on_delete=models.CASCADE,null=True)
    edudistrict = models.ForeignKey('EduDistrict',on_delete=models.CASCADE,null=True)
    
    updated_at = models.DateTimeField(blank=True, null=True)
    def __str__(self) -> str:
        return self.name