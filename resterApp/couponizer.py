import random

class Couponizer:
    def getRandomNumberWithDigitsGiven( n):
        return int(random.random()*(10**n)//n)

    coupon = getRandomNumberWithDigitsGiven( 7)

    def __str__(self):
        return coupon