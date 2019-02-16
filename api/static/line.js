var command = '';

jQuery(document).ready(function() {
  connect();
  setInterval(readCommand, 1000);
})

function readCommand () {
  jQuery.get('clova/status',
    function (data) {
      try {
        log.console(data);
      } catch (e) {
      }
       if (data === '') {
         return
      }
      command = data;

      if (data === '離陸') {
        socket.send('takeOff');
      }
      if (data === '着陸') {
        socket.send('land');
      }
      if (data === 'フリップ') {
        socket.send('flip f');
      }
  })
  return;
}

function connect () {
  var socket = new WebSocket('ws://192.168.10.1:8889');
  socket.onopen = function(e){
      alert('open websocket!');
  }
  socket.onmessage = function(e){
      var p = document.getElementById('msg');
      p.innerHTML = '送られたメッセージ：' + e.data;
  }
  socket.onerror = function(e){
      alert('error!!');
  }
  socket.onclose = function(e){
      alert('close websocket.');
  }
}
