from django.db import models
from resterApp.couponizer import Couponizer

class ResterModel(models.Model):
    meal = models.CharField(max_length=120)
    description = models.TextField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.meal

class CouponerClientModelManager(models.Manager):
    coupon = 'mock coupon from Model Manager'
    def set_coupon(self, coupon):
        couponerClientModelManager = self.create(coupon=coupon)
        return couponerClientModelManager        

class CouponerClientModel(ResterModel):
    mocky_coupon = Couponizer.coupon
    coupon = models.CharField(max_length=35, default=mocky_coupon)
    object = CouponerClientModelManager()





 