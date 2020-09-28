from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# from django.contrib.auth.models import User

# Create your models here.


# class MyUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.username

class Folder (MPTTModel):
    name = models.CharField(max_length=200, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name="children")
    # creator = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name