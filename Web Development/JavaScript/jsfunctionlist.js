/* 

 list of encountered functions:

 1.1. setInterval - executes a function at every given interval

 	//setInterval(fname,interval in millisec)

 	returns a value n

 1.2. clearInterval - stops the setInterval

 	//clearInterval(n)

 2. innerHTML - write into an html element

 	  <p id="demo">Hello </p>
 		<script>
 			document.getElementById("demo").innerHTML = "hello rishi!"; [[adds the rishi after hello wherever id="demo" is found but the existing content is erased]]
 		</script>

 3. document.write() - write into the html of a page

 	document.write("<br> <h1>Hello!</h1>"); --> writes a new line and hello in h1

 4. typeof <object> / typeof(<object>) --> returns the type of object
 	<object> instanceof <object type> --> returns true if object is an instane of object type

 5. Math.pow(mantissa,exponent) [[or]] mantissa ** exponent 

 6. String methods: 

 	1. str.length --> returns length
 	2. str.indexOf("value"[,strtpos]) --> returns the first index of first occurence else -1
 	3. str.lastindexOf("value"[,strtpos]) --> returns the first index of last occurence else -1
	4. str.search("value") --> search and return the first index
	5. str.slice(strtpos[,endpos]) --> returns a sliced string from strtpos to endpos-1; if negative, counts from end of string
	6. str.substring(strtpos[,endpos]) --> same as slice but cant take negative values
	7. str.substr(strtpos[,extractlen]) --> slices from strtpos and goes until it gets a length extractlen; negative strtpos counts from the end of the string.
	8. str.replace(findstr,repstr) --> returns new string and only replaces first match. 
		 to make case insensitive use regex ~ "findstr" = /findstr/i  
		 to replace all use regex ~ "findstr" = /findstr/g 
	9. str.toUpperCase() --> returns new string
	10. str.toLowerCase() --> returns new string
	11. str.concat("str1",...) --> returns concatenated string
	12. str.trim() --> returns a string with whitespaces removed on both sides
	13. str.charAt(pos) --> returns character at pos
	14. str.charCodeAt(pos) --> returns Unicode of character at pos
	15. str.split("delimiter") --> returns a split array
	16. str.endswith("value") --> check if ends with "value"
	17. str.repeat(num) --> returns a string with itself repeated n times

 7. is<type> - checks type

 	1.isNaN - checks if not a number

 8. Number methods: 

 	1. num.toString(base) - converts a number variable to a string while converting the base from 2-36
	2. num.toExponential([precision]) - returns string with number rounded to precision and expressed in exponent notation
	3. num.toFixed([precision]) - returns string with specified precision [[rounds normally]]
 	4. num.valueOf() - returns the value of num as a number
 	5. Number.isSafeInteger(number) - checks if number is a safe integer or not
 9. JS Global Methods: 

 	1. Number(<var>) - returns the js variable converted to a number; white spaces before or after the number dont affect; if the var is not an acceptible input it returns NaN.
 		Number(new Date("date")) returns the number of milliseconds since 1/1/1970
 	2. parseInt("string"[,radix]) - parses string and returns number; first number found in a group is returned if theyre separated by spaces; else NaN; convertible;
 	3. parseFloat("string"[,radix]) - same as parseInt but floating pt numbers are supported
 
 10. Boolean(expression) - returns true/false

 11. <dtypevar>.constructor - returns constructor function for that data type

 12. Number() - converts to number
 13. String() - converts to strings

 14. Array Methods: 

  	(sort)

  	array.sort() - sorts array of strings
  		array.sort(function(a, b){return a - b}) - sort numeric array in ascending
  		array.sort(function(a, b){return b - a}) - sort numeric array in descending
  		compare function - .sort(func) - specifies a sorting order
  			it takes 2 values (array elements) and returns +,-,0 value
  				if + --> swaps
  				if - --> doesnt swap
  		array.sort(function(a, b){return 0.5 - Math.random()}) - random sort
  		array.sort(function(a, b){return a.property - b.property}) - sort object arrays with numeric values
  		array.sort(function(a, b){var x = a.property.toLowerCase();var y = b.property.toLowerCase();if (x < y) {return -1;}if (x > y) {return 1;}return 0;}) - sort object arrays with string values
  	array.reverse() - reverses the array

  	(find and change)

  	array.length - length of array
  	array.push(element) - add element and returns the new array length
  	array[array.length] = element - add element
  	array.isArray() - checks if array
  	array instanceof Array - checks if array
  	array.indexOf(value[,startpos]) - returns the first index if found, else -1,if startpos -ve then start from end to begginging
  	array.lastIndexOf(value[,startpos]) - returnd first index from last
  	array.toString() - converts array to string of comma separated array values
  	array.join(delimiter) - converts array to string of delimiter separated array values
	array.pop() - removes and returns the last value
	array.shift() - remove the first element and shifts the other elements to the left and return the value that was removed
	array.unshift(element) - insert at the beginning and shift the other elements to the right and return the length of the array
	delete array[index] - removes an element and leaves it undefined
	array.splice(position where new elements are to obe added,how many elements are to be deleted,elements...) - add elements in the middle returns the removed elements in an array
		you can use splice to add elements in the middle splice(n,0,...)
		you can use splice to remove elements in the middle without creating any holes splice(0,n)
		you can use splice to replace elements in the middle splice(n,m,...)
	array1.concat(array2,... or [...]) - RETURNS a concatenated array

	(iteration and checking)

	array.slice(startingpos[,endingpos]) - returns a sliced array 
	array.every(function(val,ind,arr)) - check if every element satisfies a clause. the function should have the checking clause and return true/false. if every recieves a false it stops checking.
	array.forEach(function(currentValue, index, arr)) - calls func for each value
	array.map(function(value,index,arr)) - returns an array by mapping function on the array
	array.filter(function(val,ind,arr)) - returns an array with passed elements. function should return true/false.
	array.reduce(function(ret,val,ind,arr)) - goes L-R running function on each value. the function returns ret each time. the results in a single value.
	array.reduceRight(function(ret,val,ind,arr)[,initialvalue]) - same but goes R-L
	array.some(function(var,ind,arr)) - returns true if some value pass
	array.find(function(var,ind,arr)) - returns the value of the first element that passes the T/F function

15. Math object methods: 

	Math.round(num) - rounds to integer
	Math.pow(num,exp) - num power exp
	Math.sqrt(num) - square root of num
	Math.abs(num) - absolute value
	Math.floor(num) - floor function
	Math.ceil(num) - ceil function
	Math.sin/cos(radians) - sin/cos function
	Math.min(values...) - returns min
	Math.max(values...) - returns max
	Math.random() - returns a random number 0-1
	(there are more math functions da look em up when you need)

16. Random methods:

	Math.random() - random number between 0-1
	Math.floor(Math.random()*upperlimit) + shift - random from shift - (upperlimit-1+shift)




 