class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def get_discount_price(self):
        if self.discount:
            return self.price - (self.price * self.discount.percentage / 100)
        return self.price

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'قيد الانتظار'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التسليم')
    ])
    created_at = models.DateTimeField(auto_now_add=True)