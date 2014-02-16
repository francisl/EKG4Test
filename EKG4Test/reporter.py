# -*- coding: utf-8 -*-

class Reporter(object):
    def __init__(self, runner, name, failed, succeed):
        self.runner = runner
        self.name = name
        self.failed = failed
        self.succeed = succeed
        
    def is_valid(self):
        return not (self.name is None or
                    self.runner is None or
                    self.failed is None or
                    self.succeed is None)
        
    

class ReporterManager(object):
    """ Each plugins who register event is handle by the reporter manager
        It keep track of report status, update report """
    REPORTER_LIST = {}
    
    @staticmethod
    def update(runner, name, failed, succeed):
        rep = Reporter(runner, name, failed, succeed)
        if rep.is_valid():
            ReporterManager.REPORTER_LIST.update({runner: rep})
            return True
        return False
        
    @staticmethod
    def get_reporter_list():
        return ReporterManager.REPORTER_LIST.values()
    