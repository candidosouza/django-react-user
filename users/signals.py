from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def update_user_profile(sender, instance, **kwargs):
    # Verifica se o email foi alterado
    if instance.id:
        old_user = User.objects.get(id=instance.id)
        if old_user.email != instance.email:
            user_profile.email = instance.email
            
            user_profile.save()