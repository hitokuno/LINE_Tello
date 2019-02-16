var command = '';

jQuery(document).ready(function() {
  connect();
  setInterval(readCommand, 1000);
})

function readCommand () {
  jQuery.get('../api/clova/status',
    function (data) {
      try {
        console.log(data);
      } catch (e) {
      }
       if (data.status === '') {
         return
      }
      command = data.status;

      if (command === 'TakeOff') {
        socket.send('takeOff');
      }
      if (command === 'Land') {
        socket.send('land');
      }
      if (command === 'Flip') {
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
