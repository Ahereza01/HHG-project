from django.db import models

# Create your models here.

class Stockx(models.Model):
    item_name = models.CharField(max_length=50, null=True, blank=True)
    dealer_name = models.CharField(max_length=50, null=True, blank=True)
    branch_name = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)
    unit_cost = models.IntegerField(default=0, null=True, blank=True)
    total_quantity = models.IntegerField(default=0, null=True, blank=True)
    issued_quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.item_name
    
   #assoiating property item with a particular stock being kept in the stock table 
class Sale(models.Model):
    item = models.ForeignKey(Stockx, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    amount_received = models.IntegerField(default=0, null=True, blank=True)
    issued_to = models.CharField(max_length=50, null=True, blank=True)
    unit_price = models.IntegerField(default=0, null=True, blank=True)

    def get_total(self):
        total = self.quantity * self.unit_price
        return int(total)
    
    def get_change(self):
        change = self.get_total() - self.amount_received
        return abs(int(change))
    
    def __str__(self):
        return self.item.item_name




