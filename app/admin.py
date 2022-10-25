# DJANGO DECLARATIONS
from django.contrib import admin

# APP DECLARATIONS
import app.models as am


# DECLARING CLASSES
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'creation', 'modification')
    list_filter = ('user', 'creation', 'modification')


admin.site.register(am.UserProfile, UserProfileAdmin)
