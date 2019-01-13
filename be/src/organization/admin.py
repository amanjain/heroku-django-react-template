from django.contrib import admin

from org.admin import OrgAdmin

from .models import Org

admin.site.register(Org, OrgAdmin, )
