from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# from .models import User, Work, WorkItem, Facility, ContractorRating
from .models import User, Work, WorkItem, Facility


# @admin.register(User)
# class CustomUserAdmin(UserAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'is_active')
#     list_filter = ('role', 'is_active', 'is_staff')
#     search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
#     ordering = ('username',)
#
#     # Add role field to the user form
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
#         (_('Role and Manager'), {'fields': ('role', 'manager')}),
#         (_('Permissions'), {
#             'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
#         }),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#
#     # Add role field to the add user form
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'role', 'email', 'phone_number'),
#         }),
#     )
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'phone_number','idNum', 'is_active')
    list_filter = ('role', 'is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone_number')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone_number', 'idNum')}), #added idnum
        (_('Role'), {'fields': ('role',)}),  # Removed 'manager'
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password', 'password2', 'role', 'email', 'phone_number','idNum'), # Removed 'manager', added idnum
        }),
    )

@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = (
    'work_number', 'classification', 'status', 'contractor', 'manager', 'facility', 'start_date', 'due_end_date')
    list_filter = ('classification', 'status', 'contractor', 'manager', 'facility')
    search_fields = ('work_number', 'contractor__username', 'manager__username', 'facility__name')
    date_hierarchy = 'start_date'


@admin.register(WorkItem)
class WorkItemAdmin(admin.ModelAdmin):
    list_display = (
    'work', 'section', 'description', 'status', 'contract_amount', 'actual_amount', 'total_section_cost')
    list_filter = ('status', 'work__classification')
    search_fields = ('description', 'work__work_number')


@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_number', 'name', 'description')
    search_fields = ('name', 'facility_number')


# @admin.register(ContractorRating)
# class ContractorRatingAdmin(admin.ModelAdmin):
#     list_display = ('contractor', 'work', 'quality_score', 'time_score', 'cost_score', 'rated_by', 'created_at')
#     list_filter = ('contractor', 'rated_by')
#     search_fields = ('contractor__username', 'work__work_number')
#     date_hierarchy = 'created_at'