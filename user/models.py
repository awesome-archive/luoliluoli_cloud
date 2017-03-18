from django.db import models


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=30, blank=False)
    user_gender = models.CharField(max_length=5, blank=True)
    user_birthday = models.DateField(blank=True)
    user_home = models.CharField(max_length=10, blank=True)

    user_school = models.CharField(max_length=30, blank=True)
    user_grade = models.CharField(max_length=10, blank=True)
    user_location = models.CharField(max_length=40, blank=True)

    user_wechat = models.CharField(max_length=30, blank=True)
    user_QQ = models.CharField(max_length=30, blank=True)
    user_phone = models.CharField(max_length=15, blank=True)

    user_relation_status = models.CharField(max_length=20, blank=True)

    user_major = models.CharField(max_length=30, blank=True)
    user_sign = models.CharField(max_length=50, blank=True)

    user_register_time = models.DateTimeField(auto_now_add=True)

    user_avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True)
    user_avatar_url = models.URLField(max_length=100, blank=True)

    def __str__(self):
        self.user_name


class UserPhoto(models.Model):
    user = models.ForeignKey(User)
    user_photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    user_photo_url = models.CharField(max_length=500, blank=True)




