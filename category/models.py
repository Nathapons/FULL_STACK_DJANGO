from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    # แปลงข้อมูล Object ดังกล่าวให้สื่อความหมาย
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'category'