from unittest import TestCase
from EKG4Test.listener import MessageParser

class MessageParserTest(TestCase):
    def test_MessageParser_should_be_ok_when_all_param_are_set(self):
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
