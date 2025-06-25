const socket = io();
console.log('Realtime script loaded, attempting Socket.IO connection');

socket.on('connect', () => {
  console.log('Connected to server via Socket.IO');
});

socket.on('sensor_update', (data) => {
  console.log('Received sensor_update event:', data);
  const { sensor, value } = data;
  switch (sensor) {
    case 'dht':
      document.getElementById('dht-value').textContent = value;
      break;
    case 'mq2':
      document.getElementById('mq2-value').textContent = value;
      break;
    default:
      console.warn('sensor_update for unknown sensor:', sensor);
  }
});
