## Electro Kardio Gram for test runner

! Proof of concept

### Idea

It's too easy to forget that there's many test runner running in the background. They are giving you information about the status of your code.

EKG is a Mac OS X statusbar listener that take information from the test runner plugins. It display live if something is broken and need your attention in one simple look.

### Requirements

Mac OS X

### Usage

Simply run the script

    cd EKG4Test
    python ekg4test.py

### Todo

1. ~~Make a NSStatusBarItem (done)~~
2. ~~Test how easy it is to add a menu (done)~~
3. ~~Display animated graph (done)~~
4. Check if its possible to put a gif
5. Add socket listener
6. Add menuitem for new listener

7. Plugins Karma
8. Install Script
9. Plugin nose
