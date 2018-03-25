
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".
"""
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from testbase.models import Group, Student
from django.urls import reverse


class AddRemoveObjects(TestCase):

    def setUp(self):
        super(AddRemoveObjects, self).setUp()
        self.client = Client()
        self.urls = {
            'create_group': reverse('group_create'),
            'create_student': reverse('student_create')
        }
        self.group = {
            'name': 'TestGroup',
        }
        self.student = {
                    'first_name': 'TestFirstname',
                    'last_name': 'TestSurname',
                    'date_of_birth': '1987-07-08',
                    'cardnumber': '4567',
        }
        self.data ={
                'username': 'TestUser',
                'email': 'user@example.com',
                'password': 'TestPassword',
                'password2': 'TestPassword',
            }

        self.user = User.objects.create_user(self.data['username'], self.data['email'], self.data['password'])
        self.user.is_staff = True

    def test_user_login(self):

        #login by username
        data = self.data
        status = self.client.login(username=data['username'], password=data['password'])
        self.assertEqual(status, True)

        #login by email
        status = self.client.login(username=data['email'], password=data['password'])
        self.assertEqual(status, True)

    def test_add_student_group(self):

        """Add group in site and add student in that group"""
        self.client.login(username=self.data['username'], password=self.data['password'])

        # add group by POST request
        response = self.client.post(self.urls['create_group'], self.group)
        self.assertEqual(response.status_code, 302)
        group = Group.objects.get(name=self.group)
        print(response)

        #add student in added group
        student=self.student
        student['in_group'] = self.group['name']

        response = self.client.post(self.urls['create_student'], student)
        self.assertEquals(response.status_code, 302)


"""
 #check student's group is our added group
        student = Student.objects.get(in_group=self.student[''])
        self.assertEqual(student.off_group_group, group)


        #get added group from db
        group = Group.objects.get(name=self.group)
        self.student['in_group'] = group.pk
"""
