const express= require('express')
const {spawn} = require('child_process');
const cors=require('cors')
const app=express() 
app.use(cors())


app.get("/",(req,res)=>{
    const childpython = spawn('python', ['./Switch_strikes_HUF.py']);
    childpython.stdout.on('data',(data)=>{
        console.log('stdout:' + data)
    })
    
    childpython.stderr.on('data',(data)=>{
        console.error('stderr:' + data)
    })
    
    childpython.on('close',(code)=>{
        console.log('child process exited with code ' + code)
    })
    res.send({msg:"executed python file"})
})



app.listen(3001,()=>{
    console.log("server running at port 3001")
})