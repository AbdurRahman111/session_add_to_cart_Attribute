from django.db import models

# Create your models here.


# product Category table
class Product_Category(models.Model):
    class Meta:
        verbose_name_plural = 'Product Category'
    Category_Name = models.CharField(max_length=255)
    def __str__(self):
        return self.Category_Name


# product table
class Product_Table(models.Model):
    class Meta:
        verbose_name_plural = 'Product Table'

    Product_Name = models.CharField(max_length=256, blank=True, null=True)
    Product_Category = models.ForeignKey(Product_Category, default=None, blank=True, null=True, on_delete=models.CASCADE)
    Product_Picture_upload_1 = models.ImageField(upload_to='img/product/', blank=True, null=True, help_text = "Insert 500X500 pixel image")
    Description = models.TextField(blank=True, null=True)
    status = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )
    availability = models.CharField(max_length=256, choices=status, default='Available', blank=True, null=True)

    def __str__(self):
        return self.Product_Name

    def get_all_colors(self):
        return color.objects.filter(Product=self, availability="Available")

    def get_all_sizes(self):
        return size.objects.filter(Product=self, availability="Available")

    def get_all_Embroidery(self):
        return Embroidery.objects.filter(Product=self, availability="Available")


class color(models.Model):
    class Meta:
        verbose_name_plural = 'Colors'

    Product = models.ForeignKey(Product_Table, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    status = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )
    availability = models.CharField(max_length=256, choices=status, default='Available', blank=True, null=True)
    def __str__(self):
        return self.color


class size(models.Model):
    class Meta:
        verbose_name_plural = 'Sizes'
    Product = models.ForeignKey(Product_Table, on_delete=models.CASCADE)
    size = models.CharField(max_length=255)
    price = models.IntegerField()
    status = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )
    availability = models.CharField(max_length=256, choices=status, default='Available', blank=True, null=True)
    def __str__(self):
        return self.size


class Embroidery(models.Model):
    class Meta:
        verbose_name_plural = 'Embroidery'
    Product = models.ForeignKey(Product_Table, on_delete=models.CASCADE)
    Embroidery = models.CharField(max_length=255)
    Additional_Price = models.IntegerField()
    status = (
        ('Available', 'Available'),
        ('Not Available', 'Not Available'),
    )
    availability = models.CharField(max_length=256, choices=status, default='Available', blank=True, null=True)
    def __str__(self):
        return self.Embroidery


class Cart(models.Model):
    class Meta:
        verbose_name_plural = 'Cart'
    Anonymous_User_session_id = models.CharField(max_length=300, null=True, blank=True)
    Total_Cart_Amount = models.IntegerField(default=0)

    def __str__(self):
        return self.Anonymous_User_session_id


class CartItem(models.Model):
    class Meta:
        verbose_name_plural = 'CartItems'

    Anonymous_User_session_id = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product_Table, on_delete=models.CASCADE)
    Color = models.ForeignKey(color, on_delete=models.CASCADE, blank=True)
    Size = models.ForeignKey(size, on_delete=models.CASCADE, blank=True)
    Embroidery = models.ForeignKey(Embroidery, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    Subtotal_price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def sub_total(self):
        return self.product.price * self.quantity

    def __unicode__(self):
        return self.product
