from django.db import models

# Create your models here.
class QuickModel(models.Model):
    sender = models.CharField(max_length = 200)
    recipient = models.CharField(max_length=200)
    value = models.BigIntegerField
    blockNumber = models.IntegerField
    txHash = models.CharField(max_length=200)
    nonce = models.IntegerField 