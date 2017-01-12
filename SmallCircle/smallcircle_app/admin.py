from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from models import Category, Media, UserProfile

#Register your models here.

class MediaAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass
class CategoryAdmin(admin.ModelAdmin):
		prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Media, MediaAdmin)
admin.site.register(UserProfile)
