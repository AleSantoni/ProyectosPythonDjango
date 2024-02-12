from django.test import TestCase
from django.contrib.auth.models import User
from .models import Thread, Message

# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('user1', None, 'test1234')
        self.user2 = User.objects.create_user('user2', None, 'test1234')
        self.user3 = User.objects.create_user('user3', None, 'test1234')

        self.thread = Thread.objects.create()
    
    # test para comprobar si el hilo tiene dos usuarios
    def test_add_user_to_thread(self):
        self.thread.user.add(self.user1, self.user2)
        self.assertEqual(len(self.thread.user.all()), 2)
    
    # test para recuperar un hilo filtrado por usuarios
    def test_filter_thread_by_users(self):
        self.thread.user.add(self.user1, self.user2)
        threads = Thread.objects.filter(user=self.user1).filter(user=self.user2)
        self.assertEqual(self.thread, threads[0])
        
    # Recuperar un hilo que no existe 
    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(user=self.user1).filter(user=self.user2)
        self.assertEqual(len(threads), 0)
        
    # test para recuperar un mensaje
    def test_add_messages_to_thread(self):
        self.thread.user.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Muy buenas")
        message2 = Message.objects.create(user=self.user2, content="Hola")
        self.thread.messages.add(message1, message2)
        self.assertEqual(len(self.thread.messages.all()), 2)

        for message in self.thread.messages.all():
            print("({}): {}".format(message.user, message.content))
            
    #agregamos un tercer usuario pero no lo subimos al hilo 
    def test_add_message_from_user_not_in_thread(self):
        self.thread.user.add(self.user1, self.user2)
        message1 = Message.objects.create(user=self.user1, content="Muy buenas")
        message2 = Message.objects.create(user=self.user2, content="Hola")
        message3 = Message.objects.create(user=self.user3, content="Soy un espía")
        self.thread.messages.add(message1, message2, message3)
        self.assertEqual(len(self.thread.messages.all()), 2)
        
    def test_find_thread_with_custom_manager(self):
        self.thread.user.add(self.user1, self.user2)
        thread = Thread.objects.find(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        
    def test_find_or_create_thread_with_custom_manager(self):
        self.thread.user.add(self.user1, self.user2)
        thread = Thread.objects.find_or_create(self.user1, self.user2)
        self.assertEqual(self.thread, thread)
        thread = Thread.objects.find_or_create(self.user1, self.user3)
        self.assertIsNotNone(thread)