// START ATTENDANCE
function startAttendance(){
    fetch("/start-attendance")
    .then(res => res.json())
    .then(data => alert(data.message))
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

        if(data.message.includes("Successful")){
            clearInputs()
        }
    })
}


// CLEAR INPUTS
function clearInputs(){
    document.getElementById("name").value = ""
    document.getElementById("roll").value = ""
}


// VIEW STUDENTS (SHOW)
function loadStudents(){

    // 🔥 SHOW SECTION
    document.getElementById("studentsSection").style.display = "block";

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
                    <td>
                        <button onclick="deleteStudent('${s.Roll}', '${s.Name}')" class="btn red">
                            Delete
                        </button>
                    </td>
                </tr>
            `
        })
    })
}


// 🔍 SEARCH
function searchStudent(){

    let input = document.getElementById("search").value.toLowerCase()
    let rows = document.querySelectorAll("#students tr")

    rows.forEach(row => {
        let text = row.innerText.toLowerCase()
        row.style.display = text.includes(input) ? "" : "none"
    })
}


// ❌ DELETE
function deleteStudent(roll, name){

    if(!confirm("Delete this student?")) return;

    fetch("/delete-student", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            roll: roll,
            name: name
        })
    })
    .then(res => res.json())
    .then(data => {
        alert(data.message)
        loadStudents()
    })
}


// 🔥 HIDE STUDENTS
function hideStudents(){

    document.getElementById("studentsSection").style.display = "none";
}


// DOWNLOAD
function downloadAttendance(){
    window.open("/attendance-file")
}