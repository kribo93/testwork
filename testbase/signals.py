from testbase.models import Student, Group, Model_Log
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from datetime import datetime


"""
Add/Edit log(Student and Group models)
"""
@receiver(post_save, sender=Student)
@receiver(post_save, sender=Group)
def post_save_model(instance, created=False, **kwargs):
    if created:
        log=Model_Log.objects.create(model_name=instance._meta.model_name,
                                     action='СREATED',
                                     object_name=instance.__str__())
        log.datetime=datetime.now()
        log.save()
    else:
        log=Model_Log.objects.create(model_name=instance._meta.model_name,
                                     action='CHANGED',
                                     object_name=instance.__str__())
        log.datetime=datetime.now()
        log.save()


"""
Delete log(Student and Group models)
"""
@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def post_init_model(instance, **kwargs):
    log=Model_Log.objects.create(model_name=instance._meta.model_name,
                                 action='DELETED',
                                 object_name=instance.__str__())
    log.datetime=datetime.now()
    log.save()
