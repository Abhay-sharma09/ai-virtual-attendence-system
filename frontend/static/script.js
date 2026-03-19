function startAttendance(){
    fetch("/start-attendance")
}

function registerStudent(){
    let name=document.getElementById("name").value
    let roll=document.getElementById("roll").value

    fetch("/register-student",{
        method:"POST",
        headers:{"Content-Type":"application/x-www-form-urlencoded"},
        body:`name=${name}&roll=${roll}`
    })

    document.getElementById("name").value=""
    document.getElementById("roll").value=""
}

function clearInputs(){
    document.getElementById("name").value=""
    document.getElementById("roll").value=""
}

function loadStudents(){
    fetch("/student-data")
    .then(res=>res.json())
    .then(data=>{
        let table=document.getElementById("students")
        table.innerHTML=""
        document.getElementById("total").innerText=data.total

        data.students.forEach(s=>{
            table.innerHTML+=`<tr><td>${s.Name}</td><td>${s.Roll}</td></tr>`
        })
    })
}

function downloadAttendance(){
    window.open("/attendance-file")
}