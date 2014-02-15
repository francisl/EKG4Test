# -*- coding: utf-8 -*-


class ReporterManager(object):
    """ Each plugins who register event is handle by the reporter manager
        It keep track of report status, update report """
    REPORTER_LIST = []
    
    @staticmethod
    def update(plugin, name, failed, succeed):
        ReporterManager.REPORTER_LIST.append({"plugin": plugin,
                                              "name": name,
                                              "failed": failed,
                                              "succeed": succeed})
        
    @staticmethod
    def get_reporter_list():
        return ReporterManager.REPORTER_LIST
    