from django.db import models

class payuser(models.Model):
    name=models.CharField(max_length=30,default="",blank=False)
    email=models.EmailField(max_length=30,default="",blank=False)
    def __str__(self):
        return [self.name,self.email]


class User(models.Model):
    username = models.CharField(max_length=100, default="",blank=False)
    email = models.EmailField(max_length=30,default="", blank=False)
    phoneno = models.CharField(max_length=10,default="")
    password = models.CharField(max_length=20,default="", blank=False)
    cpassword = models.CharField(max_length=20, default="", blank=False)
    def __str__(self):
        return [self.username,self.email,self.phoneno]

class add(models.Model):
    appliance_CHOICES = (
        ('AC', 'AC'),
        ('Laptop', 'LAPTOP'),
        ('Washing Machine', 'WASHING MACHINE'),
        ('Computers','COMPUTERS'),
        ('Ipod','IPOD'),
        ('Mobile','MOBILE'),
        ('Fridge','FRIDGE'),
        ('Tabs','TABS'),
        ('Television','TELEVISION'),
        ('Projector','PROJECTOR'),
        ('Web Cameras','WEB CAMERAS'),
        ('Music System','MUSIC SYSTEM'),
        ('Fax Machine','FAX MACHINE'),
        ('Printers','PRINTERS'),
        ('Microwave Oven','MICROWAVE OVEN'),

    )
    fullname = models.CharField(max_length=100, default="",blank=False)
    email = models.CharField(max_length=30, default="", blank=False)
    phoneno = models.CharField(max_length=10, default="")
    appliance = models.CharField(max_length=20,choices=appliance_CHOICES,default="",blank=False)
    address = models.CharField(max_length=100, default="", blank=False)
    pincode = models.CharField(max_length=50, default="", blank=False)


    def __str__(self):
        return [self.fullname,self.email,self.phoneno,self.appliance,self.address,self.pincode]


class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name


class Product(models.Model):
   name = models.CharField(max_length=50)
   price = models.IntegerField(default=0)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
   description = models.CharField(max_length=200, default='', null=True, blank=True)
   image = models.ImageField(upload_to='products/')
   class Meta:
       db_table='product_table'
   def __str__(self):
       return self.name

   @staticmethod
   def get_all_products():
       return Product.objects.all()

   @staticmethod
   def get_all_products_by_categoryid(category_id):
       if category_id:
           return Product.objects.filter(category=category_id)
       else:
           return Product.get_all_products();

class Service(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='services/')

    @staticmethod
    def get_all_services():
        return Service.objects.all()




