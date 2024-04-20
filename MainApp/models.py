from django.db import models


class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.TextField(max_length=200, default="Базовое описание товара")

    def __str__(self) -> str:
        return f"Item({self.name})"

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.brand}, {self.count})"