function startAttendance(){

fetch("/start-attendance")
.then(res => res.json())
.then(data=>{
alert("Attendance started. Camera will open.")
})

}


function registerStudent(){

let nameBox = document.getElementById("name")
let rollBox = document.getElementById("roll")

let name = nameBox.value
let roll = rollBox.value

if(name === "" || roll === ""){
alert("Please enter name and roll number")
return
}

fetch("/register-student",{

method:"POST",

headers:{
"Content-Type":"application/x-www-form-urlencoded"
},

body:"name="+name+"&roll="+roll

})

.then(res=>res.json())
.then(data=>{

alert("Registration started. Look at camera.")

nameBox.value=""
rollBox.value=""

})

}


function clearInputs(){

document.getElementById("name").value=""
document.getElementById("roll").value=""

}


function viewAttendance(){

window.open("/attendance-file")

}