// code for the front end of the website

// we need several methods here:
// 1 - updating the puzzle based on a new input
// 2 - checking if the user has solved the puzzle correctly or not
// 3 - getting the puzzle from code 
// 4 - drawing the sudoku board in html canvas element

// 1 - for each new input, we need to detect the new entry, and send that to the backend.
function updateInput(){ 
    // read from the html element with id=sudoku_input_element_id which is a table element.

    
    // the element is a <table> so we need to get its children elements and iterate through them.
    var tableElement = document.getElementById("sudoku_input_element_id"); // this will be a <table> element, which has several child elements inside it.
    console.log(tableElement); 	// print out to console the value of the sudoku input html element.
    var tableChildrenElements = tableElement.children; // get all children elements from the <table> element.
    // make an array of ints 81 length
    var puzzle = new Array(81).fill(-1); // create a 81 length array filled with -1 values, which will be used as our sudoku board data structure here:
    
    for (let i = 0; i < tableChildrenElements.length; i++) { // iterate through each child element of the sudoku input html element, which is a <table> element.
        //console.log("child element: " + tableChildrenElements[i].id); 		// print out to console the value of the id attribute for this child element. 			}
        // log the integer value of the text in each cell, which is a <td> element.
        //console.log("text: " + tableChildrenElements[i].children[0].innerText); 		// print out to console the value of the innerText attribute for this child element.
        puzzle[tableChildrenElements[i].id] = parseInt(tableChildrenElements[i].children[0].innerText);
    }
    // convert array of ints to string here:
    console.log("stringified puzzle: " + JSON.stringify(puzzle))
    // send the stringifyed puzzle to backend here:
    var code= document.getElementById('code'); // get html element with id=code which is a <textarea> element.
    // send post request to server for this new entry, and receive response from server here:
    fetch('/api/sudoku', { method:'POST', body:JSON.stringify({ "puzzle":puzzle,"code":code })}).then(function(response){ return response.json();})
    }

function checkPuzzle(){
    var tableElement = document.getElementById("sudoku_input_element_id"); // this will be a <table> element, which has several child elements inside it.
    console.log(tableElement); 	// print out to console the value of the sudoku input html element.
    var tableChildrenElements = tableElement.children; // get all children elements from the <table> element.
    // make an array of ints 81 length
    var puzzle = new Array(81).fill(-1); // create a 81 length array filled with -1 values, which will be used as our sudoku board data structure here:
    
    for (let i = 0; i < tableChildrenElements.length; i++) { // iterate through each child element of the sudoku input html element, which is a <table> element.
        //console.log("child element: " + tableChildrenElements[i].id); 		// print out to console the value of the id attribute for this child element. 			}
        // log the integer value of the text in each cell, which is a <td> element.
        //console.log("text: " + tableChildrenElements[i].children[0].innerText); 		// print out to console the value of the innerText attribute for this child element.
        puzzle[tableChildrenElements[i].id] = parseInt(tableChildrenElements[i].children[0].innerText);
    }
    // convert array of ints to string here:
    console.log("stringified puzzle: " + JSON.stringify(puzzle))
    // send the stringifyed puzzle to backend here:
    var code= document.getElementById('code'); // get html element with id=code which is a <textarea> element.
    // send post request to server for this new entry, and receive response from server here:
    fetch('/api/Checksudoku', { method:'POST', body:JSON.stringify({ "puzzle":puzzle,"code":code })}).then(function(response){ return response.json();})
    }
function retrieve(){ // get data from backend here:
    var code= document.getElementById('code'); // get html element with id=code which is a <textarea> element.
    fetch('/api/sudokuretrieve', { method:'POST', body:JSON.stringify({ "code": code })}).then(function(response){
        // draw the sudoku board in html canvas element here:  
        
        var puzzle = new Array(81).fill(-1); // create a 81 length array filled with -1 values, which will be used as our sudoku board data structure here:
        // convert response from json to array of ints here:
        
        // finally draw  
        draw(puzzle);
       })
    }
function draw(puzzle){ // draw the sudoku board in html canvas element here:
    // take the 81 integers and draw them in a 9x9 grid. 
    var grid=document.getElementById('sudoku_input_element_id'); // get html element with id=code which is a <textarea> element.
    for (let i = 0; i < puzzle.length; i++) { // iterate through each child element of the sudoku input html element, which is a 	table> element. 		if(puzzle[i]!=-1){grid.rows[Math.floor((i)/9)
        // if puzzle[i]!-1 then draw it here:
        grid.children[i].innerText=String(puzzle[i]);
    }
}