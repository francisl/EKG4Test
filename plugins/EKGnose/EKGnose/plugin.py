__author__ = 'francisl'

import logging
import os
import json
import socket

from nose.plugins import Plugin


log = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
log.addHandler(ch)

class ReporterConnectionError(Exception):
    pass

class ReporterMessenger:
    def __init__(self):
        if not self.__dict__.get('sock'):
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host='127.0.0.1', port=51116):
        try:
            self.sock.connect((host, port))
        except:
            raise ReporterConnectionError("Application EKG4test not running or configure on a different host/port")
        return self

    def send(self, msg):
        self.sock.sendall(msg + "\n")
        self.sock.close()
        del self.sock


class EKGnose(Plugin):
    name = 'EKGnose'
    score = 150
    enabled = True

    def __init__(self):
        super(EKGnose, self).__init__()
        self.tests = 0
        self.success = 0
        self.failures = 0
        self.errors = 0
        self.host_port = None
        self.host_ip = None

    def options(self, parser, env=os.environ):
        super(EKGnose, self).options(parser, env=env)
        parser.add_option("--disable-ekgnose",
                          action="store_false",
                          default=True,
                          dest="disable_ekgnose",
                          help="disable ekg message, it will not report")

        parser.add_option("--ekgnose-ip",
                          action="store",
                          default="127.0.0.1",
                          dest="ekgnose_ip",
                          help="Set ekgnose default ip to send report")

        # parser.add_option("--ekgnose-port",
        #                   action="store",
        #                   default=51116,
        #                   dest="ekgnose_port",
        #                   help="Set ekgnose default ip to send report")

    def configure(self, options, conf):
        super(EKGnose, self).configure(options, conf)
        if not self.enabled:
            self.enabled = True

        self.host_ip = options.ekgnose_ip
        # self.host_port = options.ekgnose_port

        log.info("ekg option : %s" % options.disable_ekgnose)
        log.info("ekg option : %s" % self.host_ip)
        #log.info("ekg option : %s" % self.host_port)

    def begin(self):
        """
        Begin recording coverage information.
        """
        log.debug("Coverage begin")

    def finalize(self, result):
        log.info("ekg option : %s" % self.enabled)
        log.info("ekg option : %s" % self.host_ip)
        log.info("ekg option : %s" % self.host_port)
        log.info('Runner: %s' % __name__.split(".")[0])
        log.info('App: %s' % os.getcwd().split("/")[-1])
        log.info('All tests: %s' % self.tests)
        log.info('Success: %s' % self.success)
        log.info('Failures: %s' % self.failures)
        log.info('Errors: %s' % self.errors)
        msg = {'name': os.getcwd().split("/")[-1].split(".")[0],
               'runner': __name__.split(".")[0],
               'success': self.success,
               'failures': self.failures,
               'errors': self.errors }
        try:
            ReporterMessenger().connect(self.host_ip, self.host_port).send(json.dumps(msg))
        except ReporterConnectionError, e:
            print("Error : %s" % e)

        t = '-title {!r}'.format(msg["runner"])
        s = '-subtitle {!r}'.format(msg["name"])
        m = '-message {!r}'.format("Success: %s | Failures: %s | Errors: %s" % \
                                   (msg["success"], msg["failures"], msg["errors"]))
        os.system('terminal-notifier {}'.format(' '.join([t, s, m])))

    def addSuccess(self, test):
        self.tests += 1
        self.success += 1

    def addFailure(self, test, err):
        log.info("an failures")
        self.tests += 1
        self.failures += 1

    def addError(self, test, err):
        log.info("an error")
        self.tests += 1
        self.errors += 1