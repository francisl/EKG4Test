## Electro Kardio Gram for test runner

! Proof of concept

### Idea

Display live status of all your test running in the background

It's too easy to forget that there's many test runner running in the background. They are giving you information about the status of your code.

EKG is a Mac OS X statusbar listener that take information from the test runner plugins. It display live if something is broken and need your attention in one simple look.

### Requirements

Mac OS X
pyObjc
    pip install pyobjc

### Usage

Simply run the script

    cd EKG4Test
    python ekg4test.py

### Todo

* ~~Make a NSStatusBarItem (done)~~
* ~~Test how easy it is to add a menu (done)~~
* ~~Display animated graph (done)~~

0.2

* ~~Add socket listener~~

0.3

* ~~Add Message Management~~

0.4

* ~~Add reporter manager~~
* ~~Add menuitem for each reporter~~

0.5

* ~~Don't update menuitem on each pass - check for change~~
* ~~Test reporter total updates~~

0.5.1

* Travis integration

0.6 

* Plugin Nose
* Install Script Nose
* Install Script Widget

0.7

* Plugins Karma
* Bower install

0.8

* Log Previous Results

0.9

* Ready to add Linux or Windows Widget
* Install Script

1.0

* Nicer looking Graph
* Master for 1.0, tag 1.0 start dev branch


### Future

* Linux Widget
* Webview to display results
* Replace Socket with libzmq? (require new lib for reporter and widget)
* replace listitem with webview?

