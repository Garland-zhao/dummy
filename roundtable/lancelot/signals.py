"""信号机制"""
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save

from .models import Customer


def account_profile(sender, instance, created, **kwargs):
	if created:
		# admin用户名必须以admin开头，否则作为普通用户（还可扩展其它身份类型）
		group = Group.objects.get(name='admin') \
			if str(instance).startswith('admin') \
			else Group.objects.get(name='customer')
		instance.groups.add(group)
		Customer.objects.create(
			user=instance,
			name=instance.username,
		)


# 添加保存信号：创建用户时为期添加身份
post_save.connect(account_profile, sender=User)
