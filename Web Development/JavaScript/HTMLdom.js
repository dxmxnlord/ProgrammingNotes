/*
 
 --------------------
 JAVASCRIPT HTML DOM
 --------------------

 >> In the DOM, all HTML elements are defined as objects.

 >> A property is a value that you can get or set (like changing the content of an HTML element).

 >> A method is an action you can do (like add or deleting an HTML element).

 >> The most common way to access an HTML element is to use the id of the element

 >> The easiest way to get the content of an element is by using the innerHTML property

 ex. 
	<html>
	<body>

	<p id="demo"></p>

	<script>
	document.getElementById("demo").innerHTML = "Hello World!";
	</script>

	</body>
	</html>

 HTMLFormElement.elements
 ------------------------

 The HTMLFormElement property elements returns an HTMLFormControlsCollection
 listing all the form controls contained in the <form> element. Independently,
 you can obtain just the number of form controls using the length property.

 You can access a particular form control in the returned collection by using
 either an index or the element's name or id

 ex.
 	<form id="my-form">
  		<input type="text" name="username">
  		<input type="text" name="full-name">
  		<input type="password" name="password">
	</form>

	var inputs = document.getElementById("my-form").elements;
	var inputByIndex = inputs[0];
	var inputByName = inputs["username"];

 Input by Input: 
 	vrb=document.forms["fid'];
 	vrb --> [object HTMLFormElement]
 	vrb.elements --> [object HTMLFormControlsCollection]
 	vrb.elements["prop/index"] --> [object HTMLInputElement]
 	vrb.elements["prop/index"].value --> value

 	vrb["prop/index"] --> [object HTMLInputElement]
 	vrb["prop/index"].value --> value

 Getting value
 -------------

 <object>.value --> returns value

 Finding HTML elements
 ---------------------

 1. document.getElementById("id") --> find element by id
 2. document.getElementsByTagName("tag") --> find element by its html tag

	var x = document.getElementById("main");
	var y = x.getElementsByTagName("p");

	> This example finds the element with id="main", and then finds all <p> elements inside "main"

 3. document.getElementsByClassName("class") --> find element by class
 4. document.querySelectorAll("<css selector") --> find elements that match specific css selector

 ex.
 	var x = document.querySelectorAll("p.intro");
 	>  returns a list of all <p> elements with class="intro"

 5. document.forms["id"] --> find the form element with id="id" (see below)

 Changing HTML elements
 ----------------------

 Property

 1. <element>.innerHTML = <new content> --> change inner HTML

 ex.
 	<body>

	<h1 id="id01">Old Heading</h1>

	<script>
	var element = document.getElementById("id01");
	element.innerHTML = "New Heading";
	</script>

	</body>

 2. <element>.<attribute> = <new value> --> change attribute value

 ex.
 	<body>

	<img id="myImage" src="smiley.gif">

	<script>
	document.getElementById("myImage").src = "landscape.jpg";
	</script>

	</body>

 3. <element>.style.<property> = <new style> --> change style

 ex.
 	<body>

	<p id="p2">Hello World!</p>

	<script>
	document.getElementById("p2").style.color = "blue";
	</script>

	<p>The paragraph above was changed by a script.</p>

	</body>

 Method

 <element>,setAttribute(<attribute>,<value>) --> set attribute value

 Adding/Deleting Elements
 ------------------------

 Method	

 document.createElement(<element>)  -->   Create an HTML element
 document.removeChild(<element>)  -->   Remove an HTML element
 document.appendChild(<element>)  -->   Add an HTML element
 document.replaceChild(new, old)  -->   Replace an HTML element
 document.write(text)  -->   Write into the HTML output stream [OVERWRITES]

 Adding Event Handlers
 ---------------------

 Method

 document.getElementById(id).onclick = function(){code}	--> Adding event handler code to an onclick event

 ex.
 	<body>

	<h1 id="id1">My Heading 1</h1>

	<button type="button" 
	onclick="document.getElementById('id1').style.color = 'red'">
	Click Me!</button>

	</body>

 ex2. [WITH THIS]
 	<body>

	<h1 onclick="this.innerHTML = 'Ooops!'">Click on this text!</h1>

	</body>

 ex3.
 	<body>

	<h1 onclick="changeText(this)">Click on this text!</h1>

	// here this refers to the element tag

	<script>
	function changeText(id) { 
	  id.innerHTML = "Ooops!";
	}
	</script>

	</body>

 Finding HTML elements contd
 ---------------------------

 Property	Description	DOM

	document.anchors  -->  Returns all <a> elements that have a name attribute	1
	document.applets  -->  Returns all <applet> elements (Deprecated in HTML5)	1
	document.baseURI  -->  Returns the absolute base URI of the document	3
	document.body  -->  Returns the <body> element	1
	document.cookie  -->  Returns the document's cookie	1
	document.doctype  -->  Returns the document's doctype	3
	document.documentElement  -->  Returns the <html> element	3
	document.documentMode  -->  Returns the mode used by the browser	3
	document.documentURI  -->  Returns the URI of the document	3
	document.domain  -->  Returns the domain name of the document server	1
	document.domConfig	Obsolete.  -->  Returns the DOM configuration	3
	document.embeds  -->  Returns all <embed> elements	3
	document.forms  -->  Returns all <form> elements	1
	document.head  -->  Returns the <head> element	3
	document.images  -->  Returns all <img> elements	1
	document.implementation  -->  Returns the DOM implementation	3
	document.inputEncoding  -->  Returns the document's encoding (character set)	3
	document.lastModified  -->  Returns the date and time the document was updated	3
	document.links  -->  Returns all <area> and <a> elements that have a href attribute	1
	document.readyState  -->  Returns the (loading) status of the document	3
	document.referrer  -->  Returns the URI of the referrer (the linking document)	1
	document.scripts  -->  Returns all <script> elements	3
	document.strictErrorChecking  -->  Returns if error checking is enforced	3
	document.title  -->  Returns the <title> element	1
	document.URL  -->  Returns the complete URL of the document	1

 Onload/Onunload/Onchange/Onmouseover/Onmouseout/Onclick/Onmousedown/up events
 -----------------------------------------------------------------------------

 The onload and onunload events are triggered when the user enters or leaves the page.

 > The onload event can be used to check the visitor's browser type and browser version, and load the proper version of the web page based on the information.

 > The onload and onunload events can be used to deal with cookies.

 ex. <body onload="checkCookies()">

 > The onchange event is often used in combination with validation of input fields.

 Below is an example of how to use the onchange. The upperCase() function will be called when a user changes the content of an input field.

 <input type="text" id="fname" onchange="upperCase()">

 > The onmouseover and onmouseout events can be used to trigger a function when the user mouses over, or out of, an HTML element:
 
 ex.
 	<body>

	<div onmouseover="mOver(this)" onmouseout="mOut(this)" 
	style="background-color:#D94A38;width:120px;height:20px;padding:40px;">
	Mouse Over Me</div>

	<script>
	function mOver(obj) {
	  obj.innerHTML = "Thank You"
	}

	function mOut(obj) {
	  obj.innerHTML = "Mouse Over Me"
	}
	</script>

 > The onmousedown, onmouseup, and onclick events are all parts of a
 	mouse-click. First when a mouse-button is clicked, the onmousedown event is
 	triggered, then, when the mouse-button is released, the onmouseup event is
 	triggered, finally, when the mouse-click is completed, the onclick event is
 	triggered.

 ex.
 	<body>

	<div onmousedown="mDown(this)" onmouseup="mUp(this)"
	style="background-color:#D94A38;width:90px;height:20px;padding:40px;">
	Click Me</div>
1
	<script>
	function mDown(obj) {
	  obj.style.backgroundColor = "#1ec5e5";
	  obj.innerHTML = "Release Me";
	}

	function mUp(obj) {
	  obj.style.backgroundColor="#D94A38";
	  obj.innerHTML="Thank You";
	}
	</script>

	</body>
 
 
