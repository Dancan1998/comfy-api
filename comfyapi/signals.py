# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import ShippingProfile
# from django.contrib.auth import get_user_model
# User = get_user_model()


# @receiver(post_save, sender=User)
# def post_save_create_shipping_profile(sender, instance, created, **kwargs):
#     print('sender', sender)
#     print('instance', instance)
#     print('created', created)
#     if created:
#         ShippingProfile.objects.create(user=instance)
