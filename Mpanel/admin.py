from django.contrib import admin

from Mpanel.models import Account,UserSession,PasswordReset

admin.site.register(Account)
admin.site.register(UserSession)
admin.site.register(PasswordReset)
