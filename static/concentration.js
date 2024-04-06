/*
Purpose: Responsible for the main game logic
*/

const qlist = [
`
for (int i=0;i<5;i++) {
    for (int j=0;j<=i;j++) {
        printf("* ");
    }
}
`,
`
for (int i=0;i<5;i++) { 
for (int j=0;j<5-i;j++) { 
printf("j "); 
	} 
} 
`,
`
for (int i=0;i<5;i++) { 
for (int j=0; j<5;j++) { 
if (i>0 && i<4 && j>0 && j<4)  
	printf("  ");  
else  
	printf("* "); 
	}
} 
`,
`
int rows = 4; 
int n = 1; 
for (int i=0;i<rows;i++) { 
for (int j=0;j<=i;j++) { 
printf("%d",n++); 
    } 
} 
`,
`
int x=10, y=2;  
while(x+y-1)  
{  
printf("%d %d",x--,y--);  
}  
`,
`
I run atleast once and need not 
stop unless you give me a good 
reason to! I am a _______ loop!
`,
`
I am an infinity loop!
Put a face to my name!
`,
`
int k = 0;
for (k < 3; k++)
printf("Hello");
What does this result in?
`
]

const alist = [
`
*
* *
* * *
* * * *
* * * * *
`,
`
1 2 3 4 5
1 2 3 4
1 2 3 
1 2
1
`,
`
* * * * *
*       *
*       *
*       *
* * * * *
`,
`
1
2 3
4 5 6
7 8 9 10
`,
`
10 2
9  1
8  0
7  -1
.....
`,
`
do - while loop
`,
`
for(;;)
`,
`
Compile - time error!
`
]

var myClient = prompt("Please enter your name: ", "Anonymous User");
if (myClient.length === 0) {
	myClient = "Anonymous User";
}
var tracker = [];
var idTracker = [];
var bigBoard = 0;
var smallBoard = 0;
var guesses = 0;
var myLevel = 2;
var levelDisplay = 1;

$(document).ready(function() {
	loadMe()
})

/*
	Function: loadMe
	 Purpose: Fires up the game as soon as the homepage loads by sending an AJAX 
			  request, in the success step of ajax request call the function which
			  loads the game. 
*/

function loadMe() {
	myLevel += 2;
	postObj = {
		username: myClient,
		level: myLevel
	}
	$.ajax({
		url: "/intro",
		type: "POST", 
		contentType: "application/json", // type of content being sent
		dataType: "json", // type of content being received
		data: JSON.stringify(postObj),
		success: function(data) {
					guesses = 0;
					bigBoard = data.board.length;
					smallBoard = data.board[0].length;
					$("#title").html("Player Name: " + data.username);
					$("#level").html("Level: " + (data.level - (data.level - 1)));
					$("#tries").html("Guesses: ");

					var name = 0;
					for (var i = 0; i < data.board.length; i++) {
						a = "a".repeat(i + 1);
						$("#board").append("<tr id = " + a + "></tr>");
						for (var j = 0; j < data.board[i].length; j++) {
							$("#" + a).append("<td><div value = " + i + " name =" + j + " id =" + name + " class = 'tile'></div></td>");
							name++;
						}
					}
					click(data);
				}
	});
}
/*
	Function: click
	 Purpose: Event listener function which loops through all the div elements
			  and waits for a click to happen, the reason for the for loop 
			  is to identify the div by its id and call in the chosenBlock
			  function in its call back to send to the server
		  in: data
*/
function click(data) {
	var name = 0;
	for (var i = 0; i < data.board.length; i++) {
		for (var j = 0; j < data.board[i].length; j++) {
			// Selector is the element extracted using the name
			$("#" + name).click(function() {
				chosenBlock($("#" + this.id).attr("value"), $("#" + this.id).attr("name"), this.id);
			})
			name++; // incrementing name selector 
		}
	}
}
/*
	Function: chosenBlock
	Purpose: The click event listener calls this function in its callback,
			  this function is responsible for sending an AJAX request to the
			  server telling it exactly which tile is being clicked
	Input: i, j, id
*/
function chosenBlock(i, j, id) {
	var obj = {};
	obj.bigBox = i;
	obj.smallerBox = j;
	obj.id = id;
	postObj = {
		username: myClient,
		choice: JSON.stringify(obj)
	}
	$.ajax({
		url: "/card",
		type: "POST",
		contentType: "application/json",
		dataType: "json",
		data: JSON.stringify(postObj),
		success: function(data) {
			// Prevents from inputting values inside the tile once it's already flipped
			if (!document.getElementById(data.id).hasChildNodes()) {
				activate(data.id, data.value);
				tracker.push(data.value);
				idTracker.push(data.id);
				guesses++;
				scan(guesses);
				currentGuesses = Math.round(guesses / 2);
				$("#tries").html("Guesses: " + currentGuesses);

				if (tracker.length > 1) {

					setTimeout(function() {
					var firstTileContent = tracker[0];
					var secondTileContent = tracker[1];

					console.log("First Tile Content: ", firstTileContent);
					console.log("Second Tile Content: ", secondTileContent);

					// Search for the content of the flipped tiles in qlist and alist
					var firstTileIndex = qlist.indexOf(firstTileContent);
					if (firstTileIndex === -1) {
						firstTileIndex = alist.indexOf(firstTileContent);
					}
					console.log("First Tile Index: ", firstTileIndex);

					var secondTileIndex = alist.indexOf(secondTileContent);
					if (secondTileIndex === -1) {
						secondTileIndex = qlist.indexOf(secondTileContent);
					}
					console.log("Second Tile Index: ", secondTileIndex);


					if (firstTileIndex !== -1 && secondTileIndex !== -1 && firstTileIndex === secondTileIndex) {
						// If both values are found and their indices are equal, leave the tiles flipped
							tracker.pop();
							tracker.pop();
							idTracker.pop();
							idTracker.pop();
						
					} 
					
					if (firstTileIndex !== secondTileIndex || firstTileIndex == -1 || secondTileIndex == -1) {
						deactivate(data.id); // Deactivate the current selection
						deactivate(idTracker[0]); // Deactivate the one before as well
						tracker.pop(); // Empty out the arrays to be filled with new ones
						idTracker.pop(); // Empty the id tracking array as well
						tracker.pop();
						idTracker.pop();
						scan(guesses); // scan for guesses
					}
					}, 500);
				}
			}
		},
	});
}
/*
	Function: activate
	Purpose: Flips the tile when clicked and adds a value
	Input: id, value
*/
function activate(id, value) {
	$("#" + id).attr("class", "flipped");
	var lines = value.split('\n'); // Split multiline string into separate lines
	for (var i = 0; i < lines.length; i++) {
		$("#" + id).append("<span>" + lines[i] + "</span><br>"); // Append each line with a line break
	}
}
/*
	Function: deactivate
	Purpose: When clicked removes a value by removing the span and changes the physical look of the tile
	Input: id
*/
function deactivate(id) {
	window.setTimeout(function() {
		$("#" + id).attr("class", "tile");
		$("#" + id).children().remove();
	}, 800);
}

/*
	Function: scan
	Purpose: Scans all the blocks to check if all of the blocks have been flipped
	Input: guesses 
*/
function scan(guesses) {
	var number = 0;
	var count = 0;
	// Everytime the for loop starts count gets incremented
	for (var i = 0; i < bigBoard; i++) {
		for (var j = 0; j < smallBoard; j++) {
			if (document.getElementById(number).hasChildNodes()) {
				count++;
			}
			number++;
		}
	}
}