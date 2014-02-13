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
        
        def parseError():
            return mp.parse("last one\n")

        try:
            self.assertRaises(ValueError, parseError)
        except Exception as e:
            raise

        self.assertTrue(mp.is_completed())

    def test_parser_should_register_key_value_element_from_stream(self):
        mp = MessageParser()
        mp.parse('{"name": "Acme"}\n')
        self.assertEqual(mp.name, "Acme")
        del mp

        mp = MessageParser()
        mp.parse('{"name": "Acme", "runner": "Karma"}\n')
        self.assertEqual(mp.name, "Acme")
        self.assertFalse(mp.is_valid())
        del mp

        mp = MessageParser()
        mp.parse('{"name": "Acme", "runner": "Karma", "failed": 3, "succeed": 15}\n')
        self.assertEqual(mp.name, "Acme")
        self.assertTrue(mp.is_valid())
        del mp

