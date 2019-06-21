/* 
  
 In JavaScript there are 5 different data types that can contain values:

	string
	number
	boolean
	object
	function

 There are 3 types of objects:

	Object
	Date
	Array

 And 2 data types that cannot contain values:

	null
	undefined
 	Infinity/-Infinity,NaN - 

 string operations: 

 	"rishi".length --> 5
 	"rishi"[0] --> r
 	"rishi" +" is /"awesome/"" --> "rishi is "awesome""
 	"5" + 2 +3 --> "523"
 	2 + 3 + "5" --> "55"
 	"5" - 2 --> 3
 	"5" /* 2 --> 2.5 or 10 
 		> rishi
 		< 1
 		> var rishi2
 		< undefined
 		> rishi2
 		< undefined
 		> rishi2=null
 		< undefined
 		> rishi2
 		< null

 Inbulit functions:

 	1. alert() - sends a prompt with a message to the user
 	2. console.log() - sends a message that registers in the console log but the user cant see it unless they go into the log
 	3. prompt() - get an input from the user in the form of a string
 	4. readLine() - get an input 
    5. document.write(<value>||linebreak) - write txt/html code onto the html of a page | break a line [[deletes all existing html]]
		document.write("rishi") --> puts rishi on the page
		document.write("<br>") --> actually puts a new line

 Number Properties: Number.MAX_VALUE/MIN_VALUE/POSITIVE_INFINITY/NEGATIVE_INFINITY/NaN/MAX_SAFE_INTEGER/MIN_SAFE_INTEGER

 Now, if the user's browser does not support JavaScript or JavaScript is not enabled, 
 then the message from </noscript> will be displayed on the screen.

  <noscript>
     JavaScript is needed to go ahead.
  </noscript>


*/

var userName=prompt("What is your name?");
alert("Nice to meet you, " + userName);
console.log("Username entered: " +userName);

console.clear(); //clear log

var firstName=prompt("enter first name");
var lastName=prompt("enter last name");
var age=prompt("enter age");
alert(firstName + " " + lastName);
alert(age);

console.clear();






