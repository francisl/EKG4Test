from unittest import TestCase
from EKG4Test.reporter import ReporterManager, Reporter

class ReporterManagerTest(TestCase):
    def tearDown(self):
        ReporterManager.REPORTER_LIST = {}
        
    def test_update_should_register_new_reporter_with_status(self):
        ReporterManager.update("Karma", "Projectx", success=0, failures=0, errors=20)
        self.assertEqual(len(ReporterManager.get_reporter_list()), 1)
        
    def test_update_should_register_new_reporter_with_key(self):
        ReporterManager.update("Karma", "Projectx", success=0, failures=0, errors=20)
        self.assertEqual(ReporterManager.get_reporters().keys()[0], "Karma_Projectx")

    def test_get_reporters_should_return_all_reporter_with_keys(self):
        ReporterManager.update("Karma", "Projectx", success=0, failures=0, errors=20)
        self.assertEqual(ReporterManager.get_reporters().keys()[0], "Karma_Projectx")

    def test_REPORTER_LIST_should_contains_reporter_instance(self):
        ReporterManager.update("Karma", "Projectx", success=0, failures=0, errors=20)
        self.assertEqual(ReporterManager.get_reporters().values()[0].runner, "Karma")
        self.assertTrue(isinstance(ReporterManager.get_reporters().values()[0], Reporter))

    def test_REPORTER_LIST_should_contains_total_of_all_reporter(self):
        ReporterManager.update("Karma", "Projectx", success=3, failures=0, errors=20)
        ReporterManager.update("Karma", "Projectx", success=4, failures=5, errors=1)
        self.assertEqual(ReporterManager.total_success(), 7)
        self.assertEqual(ReporterManager.total_failures(), 5)
        self.assertEqual(ReporterManager.total_errors(), 21)



class ReporterTest(TestCase):
    def test_parser_should_register_key_value_element_from_stream(self):
        rep = Reporter("Karma", "Acme", None, None, 0 )
        self.assertFalse(rep.is_valid())
        del rep
        
        rep = Reporter("Karma", "Acme", 3, None, 0 )
        self.assertFalse(rep.is_valid())
        del rep
                
        rep = Reporter("Karma", "Acme", 0, 4, 0)
        self.assertTrue(rep.is_valid())
        del rep
        