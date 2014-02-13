from unittest import TestCase
from EKG4Test.listener import MessageParser

class MessageParserTest(TestCase):
    def test_is_valid_should_be_ok_when_all_param_are_set(self):
        mp = MessageParser()
        self.assertFalse(mp.is_valid())
        
        mp.name = "Acme"
        self.assertFalse(mp.is_valid())
        
        mp.runner = "Karma"
        self.assertFalse(mp.is_valid())
        
        mp.failed = 0
        self.assertFalse(mp.is_valid())

        mp.succeed = 0
        self.assertTrue(mp.is_valid())

    def test_completed_should_be_true_on_new_line(self):
        mp = MessageParser()
        
        mp.parse("test")
        self.assertFalse(mp.is_completed())
        
        mp.parse("other")
        self.assertFalse(mp.is_completed())
        
        mp.parse("last one\n")
        self.assertTrue(mp.is_completed())