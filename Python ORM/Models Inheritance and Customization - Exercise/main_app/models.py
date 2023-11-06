from django.db import models

# Create your models here.
# ModelName (SomeOtherModel):
# no Meta - create 1 to 1 relation between ModelName and SomeOtherModel

# ModelName (models.Model):
# class Meta:
# abstract = True - each model which inherits ModelName will have its fields, but no table ModelName will be created
# proxy = True - table ModelName will be created, models which inherit ModelName cannot add fields, but only methods
