import unittest
from models.base_model import BaseModel, Base
from models.assignment import Assignment
from models.comment import Comment
from models.notification import Notification
from models.task import Task
from models.user import User
from models.engine import DBStorage


class TestDBStorage(unittest.TestCase):

    def setUp(self):
        self.storage = DBStorage()

    def test_all(self):
        """Tests the `all()` method"""
        self.assertEqual(self.storage.all(), {})
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {'User.1': user})

    def test_new(self):
        """Tests the `new()` method"""
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {'User.1': user})

    def test_save(self):
        """Tests the `save()` method"""
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.storage.save()
        self.assertEqual(self.storage.all(), {'User.1': user})

    def test_delete(self):
        """Tests the `delete()` method"""
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.storage.delete(user)
        self.assertEqual(self.storage.all(), {})

    def test_reload(self):
        """Tests the `reload()` method"""
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {'User.1': user})

    def test_get(self):
        """Tests the `get()` method"""
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.assertEqual(self.storage.get(User, 1), user)

    def test_count(self):
        """Tests the `count()` method"""
        user = User(id=1, email='johndoe@example.com', password='secret')
        self.storage.new(user)
        self.assertEqual(self.storage.count(), 1)