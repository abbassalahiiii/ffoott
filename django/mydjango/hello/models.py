from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from extensions.utils import jalali_converter
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment

# my manager


class ArticlManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class NewsManager(models.Manager):
    def published(self):
        return self.filter(status='p')
# Create your models here.


    
class category(models.Model):
    parent=models.ForeignKey('self',default=None,null=True,blank=True,on_delete=models.SET_NULL,related_name="childeren",verbose_name="زیردسته")
    title=models.CharField(max_length=200,verbose_name="عنوان دسته‌بندی")
    slug = models.SlugField(max_length=200,unique=True,verbose_name="آدرس دسته‌بندی")
    status=models.BooleanField(default=True,verbose_name="آیا نشان داده شود؟")
    position=models.IntegerField(verbose_name="پوزیشن")
    class Meta():
        verbose_name="دسته‌بندی"
        verbose_name_plural="دسته‌بندی ها"
        ordering=['parent__id','position']

    def __str__(self):
        return self.title

class News(models.Model):
    STATUS_CHOICES=(
        ('d','پیش‌نویس'),
        ('p','منتشر شده'),
        )
    title=models.CharField(max_length=200,verbose_name="منبع")
    discriptions=models.TextField(verbose_name="متن")
    category=models.ManyToManyField(category,verbose_name="دسته‌بندی",related_name="news")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    slug = models.SlugField(max_length=200,unique=True,verbose_name="آدرس خبر")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")
    class Meta():
        verbose_name="اخبار کوتاه"
        verbose_name_plural="اخبار های کوتاه"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("account:home")
    objects=NewsManager()

class Natayej(models.Model):
    STATUS_CHOICES=(
        ('d','پیش‌نویس'),
        ('p','منتشر شده'),
        )
    logomizban=models.ImageField(upload_to="images",verbose_name="لوگو ی میزبان")
    logomihman=models.ImageField(upload_to="images",verbose_name="لوگو ی میهمان")
    mizban=models.CharField(max_length=200,verbose_name="نام تیم میزبان")
    mihman=models.CharField(max_length=200,verbose_name="نام تیم میهمان")
    goalemizban=models.IntegerField(verbose_name="گل میزبان")
    goalemihman=models.IntegerField(verbose_name="گل میهمان")
    category=models.ManyToManyField(category,verbose_name="لیگ",related_name="natayej")
    slug = models.SlugField(max_length=200,unique=True,verbose_name="آدرس")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")
    class Meta():
        verbose_name="نتیجه بازی"
        verbose_name_plural="نتیجه بازی ها"

class Tables(models.Model):
    STATUS_CHOICES=(
        ('d','پیش‌نویس'),
        ('p','منتشر شده'),
        )
    
    thunbnail=models.ImageField(upload_to="images",verbose_name="لوگو")
    title=models.CharField(max_length=200,verbose_name="نام تیم")
    bazi=models.IntegerField(verbose_name="بازی")
    bord=models.IntegerField(verbose_name="برد")
    tasavi=models.IntegerField(verbose_name="تساوی")
    bakht=models.IntegerField(verbose_name="باخت")
    goalezade=models.IntegerField(verbose_name="گل زده")
    goalekhorde=models.IntegerField(verbose_name="گل خورده")
    tafazolegoal=models.IntegerField(verbose_name="تفاضل گل")
    emtiaz=models.IntegerField(verbose_name="امتیاز")
    rotbeh=models.IntegerField(verbose_name="رتبه در جدول")
    category=models.ManyToManyField(category,verbose_name="لیگ",related_name="tables")
    slug = models.SlugField(max_length=200,unique=True,verbose_name="آدرس")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")
    class Meta():
        verbose_name="جدول بازی"
        verbose_name_plural="جدول‌های بازی"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("account:home")
    objects=NewsManager()

class Rooznameh(models.Model):
    STATUS_CHOICES=(
        ('d','پیش‌نویس'),
        ('p','منتشر شده'),
        )
    title=models.CharField(max_length=200,verbose_name="نام روزنامه")
    thunbnail=models.ImageField(upload_to="images",verbose_name="لوگو")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    slug= models.SlugField(max_length=200,unique=True,verbose_name="آدرس")
    category=models.ManyToManyField(category,verbose_name="لیگ",related_name="rooznam")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")
    class Meta():
        verbose_name="روزنامه"
        verbose_name_plural="روزنامه ها"
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("account:home")
    objects=NewsManager()

class Article(models.Model):
    STATUS_CHOICES=(
        ('d','پیش‌نویس'),
        ('p','منتشر شده'),
        ('i','در حال بررسی'),
        ('b','برگشت داده شده'),
    )
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name="articles",verbose_name="نویسنده")
    title=models.CharField(max_length=200,verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=200,unique=True,verbose_name="آدرس")
    category=models.ManyToManyField(category,verbose_name="دسته‌بندی",related_name="articles")
    discriptions=models.TextField(verbose_name="محتوا")
    thunbnail=models.ImageField(upload_to="images",verbose_name="تصویر")
    alt=models.TextField(verbose_name="alt")
    publish=models.DateTimeField(default=timezone.now,verbose_name="زمان انتشار")
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name="وضعیت")
    comments = GenericRelation(Comment)


    class Meta():
        verbose_name="مقاله"
        verbose_name_plural="مقالات"
        ordering=['-publish']

    def __str__(self):
        return self.title
    def jpublish(self):
        return jalali_converter(self.publish)
    jpublish.short_description="زمان انتشار"

    def category_published(self):
        return self.category.filter(status=True)

    def get_absolute_url(self):
        return reverse("account:home")

    def category_str(self):
        return ", ".join([category.title for category in self.category_published()])
    category_str.short_description="دسته‌بندی"

    objects=ArticlManager()



class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    # the field name should be comments
    comments = GenericRelation(Comment)


    

   


