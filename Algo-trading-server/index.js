const express = require('express')
const {spawn} = require('child_process');
const app = express()
const port = 3001
app.get('/', (req, res) => {
var largeDataSet = [];
 const python = spawn('python', ['abc.py',2,3]);
 // collect data from script
 python.stdout.on('data', function (data) {
  console.log('Pipe data from python script ...');
  largeDataSet.push(data);
 });
 // in close event we are sure that stream is from child process is closed
 python.on('close', (code) => {
 console.log(`child process close all stdio with code ${code}`);
 // send data to browser
 console.log(largeDataSet)
 res.send(largeDataSet.join(""))
 });
 
})
app.listen(port, () => console.log(`Example app listening on port 
${port}!`))