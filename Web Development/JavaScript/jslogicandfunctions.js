/* 
 
 Operators:

 	1. stanndard operators

 	1.5. == --> equal value

 		true == "1" --> true
 		0 == false --> true
 		null == undefined --> true
 		NaN == NaN --> false

 	2. === --> equal value and equal type

 		var x = 99;
 		x == "99" --> true (because of type coersion - converts type to check for same value)
 		x === "99" --> false

 		var x = null;
 		x == undefined --> true
 		x === undefined --> false

 	3. !== --> not equal value or equal type

 	4. &&,||,!

 	5. ++,--

 Operator Precedence:

 	20	( )	Expression grouping	(3 + 4)
 	 	 	 
	19	.	Member	person.name
	19	[]	Member	person["name"]
	19	()	Function call	myFunction()
	19	new	Create	new Date()
	 	 	 	 
	17	++	Postfix Increment	i++
	17	--	Postfix Decrement	i--
	 	 	 	 
	16	++	Prefix Increment	++i
	16	--	Prefix Decrement	--i
	16	!	Logical not	!(x==y)
	16	typeof	Type	typeof x
	 	 	 	 
	15	**	Exponentiation (ES7)	10 ** 2
	 	 	 	 
	14	*	Multiplication	10 * 5
	14	/	Division	10 / 5
	14	%	Division Remainder	10 % 5
	 	 	 	 
	13	+	Addition	10 + 5
	13	-	Subtraction	10 - 5
	 	 	 	 
	12	<<	Shift left	x << 2
	12	>>	Shift right	x >> 2
	12	>>>	Shift right (unsigned)	x >>> 2
	 	 	 	 
	11	<	Less than	x < y 
	11	<=	Less than or equal	x <= y
	11	>	Greater than	x > y
	11	>=	Greater than or equal	x >= y
	11	in	Property in Object	"PI" in Math
	11	instanceof	Instance of Object	instanceof Array
	 	 	 	 
	10	==	Equal	x == y
	10	===	Strict equal	x === y
	10	!=	Unequal	x != y
	10	!==	Strict unequal	x !== y
	 	 	 	 
	9	&	Bitwise AND	x & y
	8	^	Bitwise XOR	x ^ y
	7	|	Bitwise OR	x | y
	6	&&	Logical AND	x && y
	5	||	Logical OR	x || y
	4	? :	Condition	? "Yes" : "No"
	 	 	 	 
	3	+=	Assignment	x += y
	3	+=	Assignment	x += y
	3	-=	Assignment	x -= y
	3	*=	Assignment	x *= y
	3	%=	Assignment	x %= y
	3	<<=	Assignment	x <<= y
	3	>>=	Assignment	x >>= y
	3	>>>=	Assignment	x >>>= y
	3	&=	Assignment	x &= y
	3	^=	Assignment	x ^= y
	3	|=	Assignment	x |= y
	 	 	 	 
	2	yield	Pause Function	yield x
	1	,	Comma	5 , 6

 Truthy Falsey: 
 
 	every value in Js is inherently truthy or falsey. To find out which:

 		1. !<value> --> negation of answer is result
 		2. !!<value> --> answer is result

 		> !"hello"
 		< false --> "hello" is truthy
	 
	 falsy values: false,0,"",null,undefined,NaN
	 truthy values: everything else

 Boolean object: var x = new Boolean(false) [[x = false but type is object not boolean]]

 Conditions:

 	1. if --> if(condn)  {}
 	2. elseif --> else if(condn) {}
 	3. else --> else {}
	4. Conditional --> (condition) ? true : false
	5. switch --> switch(expression){ case case'n': statements;break; [default: statements] } [[uses === comparison while matching cases]]

 typeof() --> check datatype
 Number() --> converts to a number
 	ex var v1= Number(prompt("enter a number"));
 string.indexOf("value") --> returns starting position of value else -1

 Loops:

 	1. while - while(condn) {}
 	2. dowhile - do {} while(condn); [[semicolon is necessary]]
 	3. for - for(initialization;check condition; step) {}
 	4. for in - for(var variable in object) {} [[like python]]
 	5. for of - for(let variable of array|string) {}

 Loop Control: 

 	1. break;
 	2. continue;
 	3. labels - <identifier>: 

 	ex label1: {
	 statements1;
	 break label1; [[jumps out and statements2 dont get executed]]
	 statementss2;
 	} 

 	ex	outerloop:
 			loop1{
				innerloop:
					loop2{
						if(){
							break innerloop; --> quits loop2
						}
						else if{
							break outerloop; --> quits loop1
						}
						else{
							continue outerloop; --> skip below go to outerloop instead of next iteration
						}
					}
 			}

 function declaration - function fname (parameters) {[return]}

 	> fname()
 	< [[executed function]]
 	> fname 
 	< [[function code]]

 function expression - var fname = function(parameters) {} [[creates function object]]

 function constructor - var fname = new Function("arg1",...,"argn","function body with statements separated by semicolons") [[dynamically allocate , creates an object of type Function]]
 
 anonymous function - function() {}

 	function with no name that is declared for only one moment or use

 	ex higherorderfunction(arg1,function(){},arg3) {}

