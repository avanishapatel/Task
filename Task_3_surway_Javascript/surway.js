"use strict";

var form = document.getElementById("form");
var radioButton = document.querySelectorAll('input[type="radio"]');
var dataArray = [];

/**
 * Function for submit event.
 * @param {object} event onSubmit event.
 */
function onSubmit(event) {
  event.preventDefault();
  getSelectedData();
  insertDataInTable();
}

/**
 * Function for find checked radio button to get output.
 * @returns Array of total checked radio button column by column (currentlyUse, haveUsed, planToCheck, dontPlanToUse).
 */
function getSelectedData() {
  var checked1 = document.getElementsByClassName("checked1");
  var checked2 = document.getElementsByClassName("checked2");
  var checked3 = document.getElementsByClassName("checked3");
  var checked4 = document.getElementsByClassName("checked4");
  var currentlyUse = 0;
  var haveUsed = 0;
  var planToCheck = 0;
  var dontPlanToUse = 0;
  for (var button of checked1) {
    if (button.checked) {
      currentlyUse += 1;
    }
  }

  for (var button of checked2) {
    if (button.checked) {
      haveUsed += 1;
    }
  }

  for (var button of checked3) {
    if (button.checked) {
      planToCheck += 1;
    }
  }

  for (var button of checked4) {
    if (button.checked) {
      dontPlanToUse += 1;
    }
  }
  dataArray.push(currentlyUse, haveUsed, planToCheck, dontPlanToUse);
  return dataArray;
}

/**
 * Function for insert sumbited data in table.
 */
function insertDataInTable() {
  var resultTable = document.getElementById("result-table");
  resultTable.className = "table result-table success";
  var row = resultTable.insertRow(-1);
  for (var col = 0; col <= dataArray.length - 1; col++) {
    row.insertCell(col).innerHTML = dataArray[col];
  }
  dataArray = new Array();
  resetFrom();
}

/**
 * Function for reset all the radio button after submit from.
 */
function resetFrom() {
  for (var button of radioButton) {
    if (button.checked) {
      button.checked = false;
    }
  }
}