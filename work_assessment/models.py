from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save


# Create your models here.
class Moringa(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    

    def __str__(self):
        return self.user.username



    # @property
    # def profile_pic_url(self):
    #     if self.profile_pic and hasattr(self.profile_pic, 'url'):
    #         return self.profile_pic.url
    #     else:
    #         return "/media/default.png"

    def save_moringa(self):
        self.save()

    def update_save_moringa(self, using=None, fields=None, **kwargs):
        if fields is not None:
            fields = set(fields)
            deferred_fields = self.get_deferred_fields()
            if fields.intersection(deferred_fields):
                fields = fields.union(deferred_fields)
        super().refresh_from_db(using, fields, **kwargs)

    def delete_save_moringa(self):
        self.delete()


   

    # def create_moringa_profile(sender, **kwargs):
    #     if kwargs['created']:
    #         moringa_profile = Moringa.objects.create(
    #             user=kwargs['instance'])

    # post_save.connect(create_moringa_profile, sender=User)


