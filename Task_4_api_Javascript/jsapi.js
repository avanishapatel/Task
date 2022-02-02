"use strict"
var user_url = "https://reqres.in/api/users"
var user_table = document.getElementById("user-table")
var user_delete_button = '<input type="button" value="Delete" onclick="deleteUserRow(this)"/>'

var todo_url = "https://jsonplaceholder.typicode.com/todos"
var todo_table = document.getElementById("todo-table")
var todo_delete_button = '<input type="button" value="Delete" onclick="deleteTodoRow(this)"/>'


/**
 * Function for click event we will get User data from(API).
 * @param {object} event onClick event. 
 */
 function getUserData(event) {
    event.preventDefault();
    todo_table.style.display = "none";
    user_table.style.display = "table";
    var data_array = [];
    fetch(user_url)
      .then((response) => response.json())
      .then((data) => {
        var user_data = data.data;
        user_table.className = "table table-hover user-table success";
        for (var i = 0; i < user_data.length; i++) {
          var row = user_table.insertRow(-1);
          data_array = [user_data[i].id, user_data[i].email, user_data[i].first_name, user_data[i].last_name, user_data[i].avatar, user_delete_button];
          for (var j = 0; j <= data_array.length - 1; j++) {
            row.insertCell(j).innerHTML = data_array[j];
          }
        }
      });
  }


/**
* Function for click event we will get ToDo data from(API).
 * @param {object} event onClick event. 
 */
function getToDoData(event) {
    event.preventDefault();
    user_table.style.display = "none";
    todo_table.style.display = "table";
    console.log("get todo data");
    fetch(todo_url)
      .then((response) => response.json())
      .then((data) => {
        todo_table.className = "table table-hover todo-table success";
        for (var i = 0; i < 10; i++) {
          var row = todo_table.insertRow(-1);
          var data_array = [data[i].userId, data[i].id, data[i].title, data[i].completed, todo_delete_button];
          for (var j = 0; j <= data_array.length - 1; j++) {
            row.insertCell(j).innerHTML = data_array[j];
          }
        }
      });
  }


/**
 * Function for Delete row when click on delete button.
 * @param {Object} element take it as argument (html element) from user table.
 */
 function deleteUserRow(element) {
    var index_number = element.parentNode.parentNode.rowIndex;
    user_table.deleteRow(index_number);
    alert("Are you sure to delete row?");
  }


/**
 * Function for Delete row when click on delete button.
 * @param {Object} element take it as argument (html element) from todo table.
 */
 function deleteTodoRow(element) {
    var index_number = element.parentNode.parentNode.rowIndex;
    todo_table.deleteRow(index_number);
    alert("Are you sure to delete row?");
  }




