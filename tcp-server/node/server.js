var net = require('net');

var HOST = '127.0.0.1';
var PORT = 9999;

// Callback is called everytime new connection is created
// Socket is unique for each connection
var server = net.createServer(function(socket) {
    
    console.log('CONNECTED');
    console.log('Remote',socket.remoteAddress+':'+socket.remotePort);
    console.log('Local',socket.localAddress+':'+socket.localPort);
    
    socket.on('data', function(data) {
        
        console.log('DATA ' + socket.remoteAddress + ': ' + data);
        socket.write('You said "' + data + '"');
        
    });
    
    socket.on('close', function(data) {
        console.log('CLOSED: ' + socket.remoteAddress +' '+ socket.remotePort);
    });
    
});

server.listen(PORT, HOST, function(){
	console.log('Server opened on',server.address());
});