from unittest import TestCase
from EKG4Test.reporter import ReporterManager

class ReporterManagerTest(TestCase):
    def test_update_should_register_new_reporter_with_status(self):
        ReporterManager.update("Karma", "Projectx", failed=0, succeed=20)
        self.assertEqual(len(ReporterManager.get_reporter_list()), 1)
        