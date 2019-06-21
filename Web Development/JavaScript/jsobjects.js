
 
 javascript is an object-oriented programming language

 Objects:

 objects allow a particular instance to store multiple attributes. They are either properties or methods.

 Declaring: 
	
	 	var <objname> = {
		prop1: value,
		prop2: value,
		method1: function() {}
	 	};
 
 Accessing: 

 	1. objectName.propertyName / objectName.methodName() [[without () returns the fdefinition]]
 	2. objectName["propertyName"]

 new - if a variable is declared with new then it becomes an object

 	avoid: var x = new String() [[string object]] / Number() / Boolean(); [[slower exec speed]]
 	okay: var x = new <existing object>() {}

 check if dtype: 

 	function isArray(mydtype) {
  		return mydtype.constructor.toString().indexOf("dtype") > -1;
	}

 

 Arrays:

  syn: var aname = [item1,item2,...]; / var aname = new Array(item1,item2,..);

  access/reassign: arr[index] = newvalue

  elements can be - strings,numbers,objects,functions,other arrays

  properties / methods: 

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

 looping through an array: 

 	1. for(var;var<array.length-1;var++)
 	2. array.forEach(function) - the function contains the loop code
