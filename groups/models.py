from django.db import models
from django.utils.text import slugify
import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
from django import template
# Create your models here.

User = get_user_model()
registr = template.Library()

class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMembers')

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug':self.slug})
    
    class Meta:
        ordering = ['name']


class GroupMembers(models.Model):
    group = models.ForeignKey(Group, related_name='membership')
    user = models.ForeignKey(User, related_name='user_groups')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')