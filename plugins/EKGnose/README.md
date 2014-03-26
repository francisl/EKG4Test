## Electro Kardio Gram nose plugin

! Proof of concept

### Idea

Display live status of all your test running in the background

It's too easy to forget that there's many test runner running in the background. They are giving you information about the status of your code.

EKG is a Mac OS X statusbar listener that take information from the test runner plugins. It display live if something is broken and need your attention in one simple look.

This is the python nose plugin for [EKG4Test](https://github.com/francisl/EKG4Test)

### Requirements

- python
- nose


### Usage

	python setup.py install

#### to disable

    nosetests --disable-ekgnose


#### set specific host and port

    nosetests --ekgnose-ip 192.168.2.2
    nosetests --ekgnose-ip 192.168.2.2 --ekgnose-port 5000

### Todo For first release


* ~~Record test status~~
* ~~Send report to EKG4Test~~
* Configure de default server address
* Travis integration
* reports connection error
* pypi


### Future

* Replace Socket with libzmq? (require new lib for reporter and widget)
* other client? or EKG4Test will manager other client?
 

