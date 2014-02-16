from unittest import TestCase
from EKG4Test.listener import MessageParser
from EKG4Test.reporter import ReporterManager

class MessageParserTest(TestCase):
    def tearDown(self):
        ReporterManager.REPORTER_LIST = {}
    
    
    def test_completed_should_be_true_on_new_line(self):
        mp = MessageParser()
        
        mp.parse("test")
        self.assertFalse(mp.is_completed())
        
        mp.parse("other")
        self.assertFalse(mp.is_completed())
        
        def parse_error():
            return mp.parse("last one\n")

        try:
            self.assertRaises(ValueError, parse_error)
        except Exception as e:
            raise

        self.assertTrue(mp.is_completed())

    def test_parser_should_register_key_value_element_from_stream(self):
        mp = MessageParser()
        mp.parse('{"name": "Acme"}\n')
        self.assertFalse(mp.is_valid())
        del mp

        mp = MessageParser()
        mp.parse('{"name": "Acme", "runner": "Karma"}\n')
        self.assertFalse(mp.is_valid())
        del mp

        mp = MessageParser()
        mp.parse('{"name": "Acme", "runner": "Karma", "failed": 3, "succeed": 15}\n')
        self.assertTrue(mp.is_valid())
        del mp

    def test_parser_should_refuse_stream_when_to_much_data(self):
        mp = MessageParser()

        def parse_too_much():
            mp.parse('"' + ('t' * 1024) + '"\n')

        try:
            self.assertRaises(ValueError, parse_too_much)
        except Exception as e:
            raise

    def test_parser_should_handle_bad_stream_structure(self):
        mp = MessageParser()

        def parse_bad_input():
            mp.parse('Hello, this a invalid input, chock you parser!\n')

        try:
            self.assertRaises(ValueError, parse_bad_input)
        except Exception as e:
            raise