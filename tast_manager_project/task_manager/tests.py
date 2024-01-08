from rest_framework.test import APITestCase
from django.test import TestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

from tast_manager_project.config import config

class TaskAPITestCase(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create tasks for the user
        self.task1 = Task.objects.create(title='Task 1', description='Description 1', due_date='2023-12-31', status='Pending', user=self.user)
        self.task2 = Task.objects.create(title='Task 2', description='Description 2', due_date='2023-12-31', status='In Progress', user=self.user)

        # Set up authentication token for the user
        response = self.client.post('/login/', {'username': 'testuser', 'password': 'testpassword'}, format='json')
        self.token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')

    def test_list_tasks(self):
        response = self.client.get('/task_manager/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Check if all tasks are retrieved

    def test_retrieve_task(self):
        response = self.client.get(f'/task_manager/tasks/{self.task1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Task 1')  # Check if the retrieved task matches the expected task

    def test_create_task(self):
        data = {'title': 'New Task', 'description': 'New Description', 'due_date': '2023-12-31', 'status': 'Pending'}
        response = self.client.post('/task_manager/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 3)  # Check if a new task is created

    def test_update_task(self):
        data = {'title': 'Updated Task', 'description': 'Updated Description', 'due_date': '2023-12-31', 'status': 'Completed'}
        response = self.client.put(f'/task_manager/tasks/{self.task1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Updated Task')  # Check if the task was updated successfully

    def test_delete_task(self):
        response = self.client.delete(f'/task_manager/tasks/{self.task2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 1)  # Check if a task is deleted

    def test_invalid_task_id(self):
        response = self.client.get('/task_manager/tasks/999/')  # Non-existent task ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_unauthorized_access(self):
        self.client.credentials()  # Clearing authentication credentials
        response = self.client.get('/task_manager/tasks/')  # Access without authentication
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_invalid_data_create(self):
        data = {'title': 'New Task'}  # Incomplete data for creating a task
        response = self.client.post('/task_manager/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_nonexistent_task(self):
        data = {'title': 'Updated Task'}
        response = self.client.put('/task_manager/tasks/999/', data, format='json')  # Non-existent task ID for update
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

def verify(a):
    return a == 1

class AccessSecretsTests(TestCase):
    def test_secret(self):
        self.assertTrue(verify(config['SECRET_1']))