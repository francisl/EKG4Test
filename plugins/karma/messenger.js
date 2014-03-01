
// now more a tester than anything

var net = require('net');
s = new net.Socket();

try {
    s.connect(51116, '127.0.0.1');
} catch(err) {
    console.log('Cannot connect to server');
}


s.write('{"runner":"Karma",');
s.write('"name":"XRepo",');
s.write('"failed":5,');
s.write('"passed":15}');
s.write('\n');
s.end();
