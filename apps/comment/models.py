from django.db import models

from apps.product.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(max_length=700)
    created_t = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Comment by {self.author} on {self.product}"