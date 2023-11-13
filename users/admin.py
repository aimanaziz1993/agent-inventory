from django.contrib import admin
from users.models import NewUser
from profiles.models import Profile

from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models
from django.urls import reverse
from django.utils.html import format_html
from django.shortcuts import get_list_or_404
from django.db.models import Sum


class UserAdminConfig(UserAdmin):

    model = NewUser
    search_fields = ('email', 'user_name', 'first_name',)
    list_filter = ('email', 'user_name', 'first_name', )
    ordering = ('-user_profile__view_count',)
    list_display = ('user_name_link', 'user_profile_link',
                    'user_view', 'email', 'is_active', 'introducer', 'groupId', 'branchId')
    fieldsets = (
        (None, {'fields': ('email', 'user_name', 'first_name',
         'user_view', 'introducer', 'groupId', 'branchId')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('about',)}),
    )
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 20, 'cols': 60})},
    }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 'is_active', 'is_staff', 'user_view', 'introducer', 'groupId', 'branchId',)}
         ),
    )

    def user_name_link(self, obj):
        url = reverse('admin:{}_{}_change'.format(
            obj._meta.app_label,  obj._meta.model_name),  args=[obj.id])
        return format_html('<a href="{}">{}</a>', url, obj.user_name)

    def user_profile_link(self, obj):
        profile_url = "https://onedreamproperty.com.my/{}".format(
            obj.user_name)
        return format_html('<a href="{}" target="_blank">{}</a>', profile_url, obj.user_name)

    # def user_view(self, obj):

    #     profile = get_list_or_404(Profile, user__user_name=obj.user_name)

    #     for item in profile:
    #         return format_html('{}', item.view_count)

    def user_view(self, obj):
        total_view_count = Profile.objects.filter(
            user__user_name=obj.user_name).aggregate(Sum('view_count'))['view_count__sum']

        if total_view_count is not None:
            return total_view_count
        else:
            return 0

    user_profile_link.short_description = 'User Profile'
    user_name_link.short_description = 'User Name'
    user_view.short_description = 'User view'
    user_view.admin_order_field = 'user_profile__view_count'


admin.site.register(NewUser, UserAdminConfig)
