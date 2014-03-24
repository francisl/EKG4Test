# -*- coding: utf-8 -*-

class Reporter(object):
    def __init__(self, runner, name, success, failures, errors):
        self.runner = runner
        self.name = name
        self.success = success
        self.failures = failures
        self.errors = errors
        
    def is_valid(self):
        return not (self.name is None or
                    self.runner is None or
                    self.success is None or
                    self.failures is None or
                    self.errors is None)
        
    

class ReporterManager(object):
    """ Each plugins who register event is handle by the reporter manager
        It keep track of report status, update report """
    _REPORTER_LIST = {}
    _TOTAL_SUCCESS = 0
    _TOTAL_FAILURES = 0
    _TOTAL_ERRORS = 0

    @staticmethod
    def update_totals():
        ReporterManager._TOTAL_SUCCESS = 0
        ReporterManager._TOTAL_FAILURES = 0
        ReporterManager._TOTAL_ERRORS = 0
        for rep in ReporterManager._REPORTER_LIST.values():
            ReporterManager._TOTAL_SUCCESS += rep.success
            ReporterManager._TOTAL_FAILURES += rep.failures
            ReporterManager._TOTAL_ERRORS += rep.errors

    @staticmethod
    def update(runner, name, success, failures, errors):
        rep = Reporter(runner, name, success, failures, errors)
        if rep.is_valid():
            ReporterManager._REPORTER_LIST.update({runner+"_"+name: rep})
            ReporterManager.update_totals()
            return True
        return False

    @staticmethod
    def total_success():
        return ReporterManager._TOTAL_SUCCESS

    @staticmethod
    def total_failures():
        return ReporterManager._TOTAL_FAILURES

    @staticmethod
    def total_errors():
        return ReporterManager._TOTAL_ERRORS

    @staticmethod
    def get_reporter_list():
        return ReporterManager._REPORTER_LIST.values()

    @staticmethod
    def get_reporters():
        return ReporterManager._REPORTER_LIST

