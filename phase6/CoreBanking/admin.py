from django.contrib import admin

# Register your models here.
from CoreBanking.models import Member, Customer, Center, CustomerAccount


class MemberAdmin(admin.ModelAdmin):
    list_display = ["membership_type"]
    class Meta:
        model = Member
class CenterAdmin(admin.ModelAdmin):

    class Meta:
        model = Center
class CustomerAdmin(admin.ModelAdmin):
    class Meta:
        model = Customer
class AccountAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomerAccount

admin.site.register(CustomerAccount, AccountAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Customer, CustomerAdmin)

