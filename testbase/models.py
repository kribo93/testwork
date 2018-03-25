from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Model_Log(models.Model):

    ACTION_CHOICES = (
        ('СREATED', 'Created'),
        ('CHANGED', 'Changed'),
        ('DELETED', 'Deleted'),
    )
    action = models.CharField(max_length=10, choices=ACTION_CHOICES, default='CHANGED')
    model_name = models.CharField(verbose_name='Name of model', max_length=254)
    object_name = models.CharField(verbose_name='Odject', max_length=254, default=None)
    datetime = models.DateTimeField(verbose_name='Datetime', blank=True, null=True)


class Group(models.Model):
    name = models.CharField(verbose_name='name of group', max_length=30, unique=True)
    course_leader = models.ForeignKey('testbase.Student', on_delete=models.SET_NULL, blank=True, null=True, default=0)

    class Meta:
        verbose_name = 'group'
        verbose_name_plural = 'groups'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail', args=[self.pk])

    def get_fullname(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(verbose_name='first name', max_length=50)
    last_name = models.CharField(verbose_name='last name', max_length=50)
    date_of_birth = models.DateField(verbose_name='date of birth', blank=True, null=True)
    card_number = models.PositiveIntegerField(verbose_name='card number', unique=True, blank=False)
    in_group = models.ForeignKey(Group, blank=False, null=True, default=0)

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)



