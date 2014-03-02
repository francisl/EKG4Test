import objc, re, os
from Foundation import NSRunLoop
from Foundation import NSObject
from Foundation import NSDefaultRunLoopMode
from Foundation import NSDate
from Foundation import NSTimer

from AppKit import NSMenu
from AppKit import NSMenuItem
from AppKit import NSStatusBar
from AppKit import NSImage
from AppKit import NSVariableStatusItemLength
from AppKit import NSApplication

#from PyObjCTools import NibClassBuilder
from PyObjCTools import AppHelper

from reporter import ReporterManager
from listener import connect

STARTTIME = NSDate.date()

class MonitorImages(object):
    """ Helper class to loop a list of images """
    IMAGES_LIST = ['./Resources/png/monitor-1.png',
                   './Resources/png/monitor-2.png',
                   './Resources/png/monitor-3.png',
                   './Resources/png/monitor-4.png',
                   './Resources/png/monitor-6.png',
                   './Resources/png/monitor-7.png',
                   './Resources/png/monitor-8.png',
                   './Resources/png/monitor-9.png',
                   './Resources/png/monitor-10.png',
                   './Resources/png/monitor-11.png',
                   './Resources/png/monitor-12.png',
                   './Resources/png/monitor-13.png',
                   './Resources/png/monitor-14.png',
                   './Resources/png/monitor-15.png',
                   './Resources/png/monitor-16.png',
                   './Resources/png/monitor-17.png',
                   './Resources/png/monitor-18.png',
                   './Resources/png/monitor-19.png',
                   './Resources/png/monitor-20.png',
                   './Resources/png/monitor-21.png',
                   './Resources/png/monitor-22.png',
                   './Resources/png/monitor-23.png',
                   './Resources/png/monitor-24.png',
                   './Resources/png/monitor-25.png',
                   './Resources/png/monitor-26.png',
                   './Resources/png/monitor-27.png']

    def __init__(self):
        self.nsimage_list = []
        self.index = -1
        self.load_nsimage()

    def load_nsimage(self):
        for img in MonitorImages.IMAGES_LIST:
            self.nsimage_list.append(NSImage.alloc().initByReferencingFile_(img))

    def next(self):
        if self.index + 1 == len(self.nsimage_list):
            self.index = 0
        else:
            self.index += 1

        return self.nsimage_list[self.index]


class TestRunner(object):
    def __init__(self, running=True):
        self._running = running
        self._has_stop = False

    def is_running(self):
        return self._running

    def has_stop(self):
        if self._has_stop:
            self._has_stop = False
            return True
        return self._has_stop

    def run(self):
        self._running = True

    def stop(self):
        self._running = False
        self._has_stop = True


class EKG4Test(NSObject):

    def applicationDidFinishLaunching_(self, notification):
        sb = NSStatusBar.systemStatusBar()
        self.test_runner = TestRunner()
        self.monitor_images = MonitorImages()
        self.reporter_items = {}
        self.total_passed = 0
        self.total_failed = 0

        # STATUS ITEM
        self.status_item = sb.statusItemWithLength_(NSVariableStatusItemLength)
        self.status_item.setHighlightMode_(1)
        self.status_item.setToolTip_('Listening for test runner')

        # MENU
        self.menu = NSMenu.alloc().init()

        quit_menuitem = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_('Quit', 'terminate:', '')
        self.menu.addItem_(quit_menuitem)

        self.status_item.setMenu_(self.menu)
        # /MENU

        # LOOP
        self.timer = NSTimer.alloc().initWithFireDate_interval_target_selector_userInfo_repeats_(
            STARTTIME,
            0.4,
            self,
            'tick:',
            None,
            True)
        NSRunLoop.currentRunLoop().addTimer_forMode_(self.timer, NSDefaultRunLoopMode)
        self.timer.fire()

    def runtest_(self, notification):
        self.test_runner.run()

    def stoptest_(self, notification):
        self.test_runner.stop()

    def tick_(self, notification):
        if self.test_runner.is_running():
            rlist = ReporterManager.get_reporters()
            print("rlist : %s" % rlist)
            for name, reporter in rlist.items():
                title = "%s - F:%s P:%s" % (name, rlist[name].failed, rlist[name].passed)
                if name in self.reporter_items.keys():
                    self.reporter_items[name].setTitle_(title)
                else:
                    self.reporter_items[name] = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(title, '', '')
                    self.menu.insertItem_atIndex_(self.reporter_items[name], 0)
            self.status_item.setImage_(self.monitor_images.next())
        elif self.test_runner.has_stop():
            self.status_item.setImage_(self.monitor_images.next())

        self.status_item.setTitle_("P:%s F:%s" %
                                   (ReporterManager.total_passed(), ReporterManager.total_failed()))

if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    delegate =  EKG4Test.alloc().init()
    app.setDelegate_(delegate)
    from threading import Thread
    server = Thread(target=connect)
    server.start()
    AppHelper.runEventLoop()
