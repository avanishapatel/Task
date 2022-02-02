var start_date = document.getElementById("start_date");
var end_date = document.getElementById("end_date");
var days = document.getElementById("days");

/**
 * Function call after click on button.
 */
function sumbitDate() {    
    days.className = "diff-days success";
    getDiffDays(start_date, end_date);
}


/**
 * 
 * @param {object} date1  take first date which was seleceted.
 * @param {object} date2  take second date which was seleceted.
 * @returns difference of days between two dates.
 */
function getDiffDays(date1, date2) {
    first_date = new Date(date1.value);
    second_date = new Date(date2.value);
    if (date1.value == "" || date2.value == "") {
        alert("Please select date.");
    } else {
        var Difference_In_Time = second_date.getTime() - first_date.getTime();
        var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);
        days.innerHTML = Difference_In_Days;
        return Difference_In_Days;
    }
}


/**
 * Function for convert first selected date in weekday, month day, year formate when change in date input field.
 */
function getStartDate() {
    var copy_date1 = document.getElementById("convert-start-date");
    copy_date1.className = "input-field success";
    copy_date1.innerText = new Date(start_date.value).toLocaleString(
        "en-US",
        { weekday: "long", month: "long", day: "numeric", year: "numeric" }
    );
}


/**
 * Function for convert second selected date in weekday, month day, year formate when change in date input field.
 */
function getEndDate() {
    var copy_date2 = document.getElementById("convert-end-date");
    copy_date2.className = "input-field success";
    copy_date2.innerText = new Date(end_date.value).toLocaleString(
        "en-US",
        { weekday: "long", month: "long", day: "numeric", year: "numeric" }
    );
}

