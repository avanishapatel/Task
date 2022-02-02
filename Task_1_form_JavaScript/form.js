"use strict"


var form = document.getElementById("form");
var student_name = document.getElementById("stu_name");
var email = document.getElementById("stu_email");
var address = document.getElementById("stu_address");
var course =document.getElementById("stu_course");
var stuData = [student_name, email, address, course]
var valid = false;


/**
* Function will be call after click on form's sumbit button.
* first it check validation if there any validation then show message, 
* else will submit form and insert data into the table.
*/
function submitFrom(event){
    event.preventDefault();       
    if (validate()){
        if(valid = true){
            validate();
        }
    }
    else{
        insertDataInTable();
        resetForm();
    }    
}


/**
 * Check validation.
 * @returns {Boolean} True/ False 
 */
function validate(){
    const name = document.getElementById("stu_name").value.trim();
    const email = document.getElementById("stu_email").value.trim();
    const address = document.getElementById("stu_address").value.trim();
    const course =document.getElementById("stu_course").value.trim();
    valid = false;

    // validation for name
    var re_name = /^[A-Za-z\s]{2,25}$/ 
    if (name === "") {
        setErrorMsg(stu_name, "Please enter name");
        valid = true;        
    }
    else if(!(re_name.test(name))){
        setErrorMsg(stu_name, "Please enter valid name");
        valid = true; 
    }    
    else{
        successMsg(stu_name);
    }
        
    // validation for email
    var re_email = /^[\w._+-]+@[\w.-]+\.[a-zA-Z]{2,4}$/;    
    if(email === ""){
        setErrorMsg(stu_email, "Please enter email");
        valid = true;
    }
    else if(!(re_email.test(email))){
        setErrorMsg(stu_email, "Please enter valid email.")
        valid = true;
    }
    else{
        successMsg(stu_email);
    }

    // validation for address 
    if(address === ""){
        setErrorMsg(stu_address, "Please enter address");
        valid = true;
    }
    else{
        successMsg(stu_address);
    }
    
    // validation for course 
    if(course === ""){
        setErrorMsg(stu_course, "Please enter course");
        valid = true;
    }
    else{
        successMsg(stu_course);
    }

  return valid;
}


/**
 * Show validation error message.
 * @param {Object} input    Input Field id.
 * @param {String} errormsg Show error message string.
 */
function setErrorMsg(input, errormsg){
    var formField = input.parentElement;
    var small = formField.querySelector("small");
    formField.className="form-field error"
    small.innerHTML = errormsg;
}


/**
 * Function for success message.
 * @param {String} input    Input Field id. 
 */
function successMsg(input){
    var formField = input.parentElement;
    formField.className="form-field success"
}


/**
 * Function for insert data into the table.
 */
function insertDataInTable(){
    var table = document.getElementById("table"); 
    table.className="table success"
    var row = table.insertRow(-1);
    for (var col = 0; col <= stuData.length-1; col++){
        row.insertCell(col).innerHTML = stuData[col].value;
    }
}


/**
 * Function for reset input field.
 */
function resetForm(){
    student_name.value = '';
    email.value = '';
    address.value = '';
    course.value = '';
}