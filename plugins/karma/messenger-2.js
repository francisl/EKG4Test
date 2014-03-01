// now more a tester than anything

var net = require('net');
var s = new net.Socket();

try {
    s.connect(51116, '127.0.0.1');
} catch(err) {
    console.log('Cannot connect to server');
}


s.write('{"runner":"Karma",');
s.write('"name":"XRepo",');
s.write('"failed":0,');
s.write('"passed":20}');
s.write('\n');
s.end();
delete s;

// add another menu

var s;
try {
    s = new net.Socket();
    s.connect(51116, '127.0.0.1');
} catch(err) {
    console.log('Cannot connect to server');
}

s.write('{"runner":"Karma",');
s.write('"name":"Second Repo",');
s.write('"failed":0,');
s.write('"passed":45}');
s.write('\n');
s.end();
