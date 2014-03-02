# -*- coding: utf-8 -*-

class Reporter(object):
    def __init__(self, runner, name, failed, passed):
        self.runner = runner
        self.name = name
        self.failed = failed
        self.passed = passed
        
    def is_valid(self):
        return not (self.name is None or
                    self.runner is None or
                    self.failed is None or
                    self.passed is None)
        
    

class ReporterManager(object):
    """ Each plugins who register event is handle by the reporter manager
        It keep track of report status, update report """
    _REPORTER_LIST = {}
    _TOTAL_FAILED = 0
    _TOTAL_PASSED = 0

    @staticmethod
    def update_totals():
        ReporterManager._TOTAL_FAILED = 0
        ReporterManager._TOTAL_PASSED = 0
        for rep in ReporterManager._REPORTER_LIST.values():
            ReporterManager._TOTAL_FAILED += rep.failed
            ReporterManager._TOTAL_PASSED += rep.passed

    @staticmethod
    def update(runner, name, failed, passed):
        rep = Reporter(runner, name, failed, passed)
        if rep.is_valid():
            ReporterManager._REPORTER_LIST.update({runner+"_"+name: rep})
            ReporterManager.update_totals()
            return True
        return False

    @staticmethod
    def total_failed():
        return ReporterManager._TOTAL_FAILED

    @staticmethod
    def total_passed():
        return ReporterManager._TOTAL_PASSED

    @staticmethod
    def get_reporter_list():
        return ReporterManager._REPORTER_LIST.values()

    @staticmethod
    def get_reporters():
        return ReporterManager._REPORTER_LIST

