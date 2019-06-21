/*

-->ERROR HANDLING<--

 The try statement lets you test a block of code for errors.

 The catch statement lets you handle the error.

 The throw statement lets you create custom errors.

 The finally statement lets you execute code, after try and catch, regardless of the result.

	 try {
	 	Block of code to try
	 	ex. if(check) {throw "error message";}
	 }
	 catch(err) {  [[err is the different throws]]
	 	Block of code to handle errors
		ex. console.log("recieved an" + err + "type of error")
	 } 
	 finally {
	 	Block of code to be executed regardless of the try / catch result
	 }

 Error Object:

 	properties: 

 		name: [[six values can be returned by the error name property]]

 			EvalError			An error has occurred in the eval() function


			RangeError			A number "out of range" has occurred

				var num = 1;
				try {
				  num.toPrecision(500);   // A number cannot have 500 significant digits
				}
				catch(err) {
				  document.getElementById("demo").innerHTML = err.name;
				}


			ReferenceError		An illegal reference has occurred

				var x;
				try {
				  x = y + 1;   // y cannot be referenced (used)
				}
				catch(err) {
				  document.getElementById("demo").innerHTML = err.name;
				}


			SyntaxError			A syntax error has occurred

				try {
				  eval("alert('Hello)");   // Missing ' will produce an error
				}
				catch(err) {
				  document.getElementById("demo").innerHTML = err.name;
				}


			TypeError			A type error has occurred

				var num = 1;
				try {
				  num.toUpperCase();   // You cannot convert a number to upper case
				}
				catch(err) {
				  document.getElementById("demo").innerHTML = err.name;
				}


			URIError			An error in encodeURI() has occurred

				try {
				  decodeURI("%%%");   // You cannot URI decode percent signs
				}
				catch(err) {
				  document.getElementById("demo").innerHTML = err.name;
				}


 -->SCOPE OF VARIABLES<--

 Hoisting:

 	Variables defined with var (but not let,const) are hoisted to the top but not their initialization. You can use them before they are declared.
 
 Types: 

 	1. Global Scope - let/var same

 		var carName = "Volvo";

		// code here can use carName

		function myFunction() {
		  // code here can also use carName 
		}

	2. Function Scope - let/var same

		// code here can NOT use carName

		function myFunction() {
		  var carName = "Volvo";
		  // code here CAN use carName
		}

		// code here can NOT use carName

	3. Block Scope - with var

		{ 
		  var x = 2; 
		}

		// x CAN be used here

	4. Block Scope - with let

		{ 
		  let x = 2;
		}
		// x can NOT be used here

 Redeclaring/loop problems with var:

 	var x = 10;
	// Here x is 10
	{ 
	  var x = 2; // use let instead
	  // Here x is 2
	}
	// Here x is 2

	var i = 5;
	for (var i = 0; i < 10; i++) { // use let instead
	  // some statements
	}
	// Here i is 10

 Global variables with var belong to the window object but not let

 Redeclaring in the same scope: 

 	var-var --> allowed
 	var-let --> no
 	let-let --> no

 Const: create a constant

 	const vname = value; [[cannot give a value later]]

 	scope is similar to let

 	you can change/add a property of a constant object/array but not reassign an object

	you cant redeclare an existing var/let variable to const in the same scope

 'this' referencer: 

 



 

