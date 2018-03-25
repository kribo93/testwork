from testbase.models import Group, Student
from django.core.management.base import BaseCommand
from django.utils import translation


class Command(BaseCommand):
    help = 'Get a list of all permissions available in the system.'

    def handle(self, *args, **options):
        lists = list('\n''Groups and students in group:')
        groups_list = Group.objects.all()

        for v in groups_list:
            group_name = '\n''%s:'% v.name
            lists.append(group_name + '\n')
            students = v.student_set.all()
            for student in students:
                full_name = '%s %s'% (student.first_name, student.last_name)
                lists.append(full_name + "\n")
        translation.deactivate()
        return "".join(lists)
