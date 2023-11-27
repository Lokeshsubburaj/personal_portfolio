from django.db import models

# Create your models here.
from django.contrib import admin

from portfolio.models import Project

admin.site.register(Project)