// START ATTENDANCE
function startAttendance(){
    fetch("/start-attendance")
    .then(res => res.json())
    .then(data => {
        alert(data.message)
    })
}


// REGISTER STUDENT
function registerStudent(){

    let name = document.getElementById("name").value
    let roll = document.getElementById("roll").value

    if(name === "" || roll === ""){
        alert("Enter Name and Roll")
        return
    }

    fetch("/register-student", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: `name=${name}&roll=${roll}`
    })
    .then(res => res.json())
    .then(data => {

        alert(data.message)

        // Clear only if successful
        if(data.message.includes("Successful")){
            document.getElementById("name").value = ""
            document.getElementById("roll").value = ""
        }
    })
}


// CLEAR INPUTS
function clearInputs(){
    document.getElementById("name").value = ""
    document.getElementById("roll").value = ""
}


// LOAD REGISTERED STUDENTS
function loadStudents(){

    fetch("/student-data")
    .then(res => res.json())
    .then(data => {

        let table = document.getElementById("students")
        table.innerHTML = ""

        document.getElementById("total").innerText = data.total

        data.students.forEach(s => {
            table.innerHTML += `
                <tr>
                    <td>${s.Name}</td>
                    <td>${s.Roll}</td>
                </tr>
            `
        })
    })
}


// DOWNLOAD ATTENDANCE
function downloadAttendance(){
    window.open("/attendance-file")
}