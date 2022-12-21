from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    """Defines a User model with email login"""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save user with email and password"""

        if not email:
            raise ValueError("the given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password"""

        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a Superuser with the given email and password."""

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):

    GENDER_CHOICES = (("M", "Male"), ("F", "Female"))

    phone = models.CharField(max_length=11, unique=True)
    middle_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1)

    # USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.get_full_name()


class common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Measurement(common):
    """This is the model for each measurement"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bust = models.IntegerField()
    Waist = models.IntegerField()
    hip = models.IntegerField()
    back = models.IntegerField()
    sleeve_length = models.IntegerField()
    round_sleeve = models.IntegerField()
    bicep = models.IntegerField()
    half_length = models.IntegerField()
    breast_point = models.IntegerField()
    full_length = models.IntegerField()

    def __str__(self):
        return f"{self.user} measurement"


class ShippingAddress(common):
    """This model stores the shipping information of the user"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=11)
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=30, default="Nigeria")

    def __str__(self):
        return f"{self.user} shipping to {self.street} in {self.city}"


class Image(common):
    """This model take care of all Image Upload"""

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    path = models.FileField(upload_to="mysite/static/images")

    def __str__(self):
        return f"{self.user} owns this image {self.path}"

class Orders(common):
    """sumary_line"""

    shipping_address = models.ForeignKey(ShippingAddress, on_delete=models.CASCADE)
    measurement = models.ForeignKey(Measurement, on_delete=models.CASCADE)
    images = models.ManyToManyField(Image)
    # additional_info = models.TextField(null=True, blank=True)
    # invoice_link = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.measurement.user} order"