//Final Javascript
//Renee Balmert

var divReg;
var divMain;
var divGauge
var inputElements;
var spanElements;


document.addEventListener
(									//ok to break this out by lines? yep!
	"DOMContentLoaded", function()
		{
		var divReg = document.getElementById("divRegistered"); 
		var divGauge = document.getElementById("divGauge");


		divGauge.addEventListener("focus", fHandleEnter, true); 
		divGauge.addEventListener("blur", fHandleExit, true);

		fProcessForm(); 
	
		var inputElements = document.querySelectorAll("#frmRegister input[type='text'], input[type='password']");	//from Michael! :D
		var spanElements =  document.querySelectorAll("#frmRegister span");	
		inputElements[2].addEventListener("blur", function() {fCompareInput(inputElements[1].value, inputElements[2].value, spanElements[2]);});//TEST!!? 
		inputElements[4].addEventListener("blur", function() {fCompareInput(inputElements[3].value, inputElements[4].value, spanElements[4]);});



		var divAccHead = document.getElementsByClassName("accHeader");		//trying to figure out accordion. list 
		divAcc[0].addEventListener("onclick", function() {accodordionFunc(argument,,,);}); ///derp derp -- first header
		divAcc[1].addEventListener("onclick", function() {accodordionFunc(argument,,,);}); ///derp derp -- 2nd header


		
		var btnReg = document.getElementById("btnRegister");
		btnReg.addEventListener("click", fRobotLion, true);
		}
); 

// $(".slider").diyslider()  attempting carousel....

// function diyslider():
// 	{
	
// 	}

function accodordionFunc()
	{
	var i;

	for (i = 0; i < divAcc.length; i++) //huh??? I miss python!  D:
		{
	    divAcc[i].onclick = function(){
	        this.classList.toggle("active");
	        this.nextElementSibling.classList.toggle("show");
    	}
    };



function fHandleEnter(fcs)
	{
	fcs.target.style.backgroundColor = "yellow";  
	};

function fHandleExit(blr)
	{
	blr.target.style.backgroundColor = "";	//
	};

function fProcessForm()
	{
	var x = location.search;
	var strQueryString = x.replace(/^.*\=/,"");		//from HW4 :D
	if (strQueryString.length > 0)
		{
		var login = strQueryString;
		var divReg = document.getElementById("divRegistered");	//argh! doesn't work unless I declare divReg again? undefined??!
		divReg.innerHTML = "Thank you, " + login + ", you are now registered with Voltron.";	//booyah - nailed syntax for once!
		$("#divRegistered").fadeIn(700);		//my first jQuery! :D couldn't get #divReg to work..? :(
		$("#divGauge").hide();			//hide form... nailed it! jQuery Goddess :D
		}					//no semi colon!!!!! seriously!!! >:(
/*	else				//don't need an else, right? the page just stays as it was.
		{
			?? status quo A-OK?
		}

*/
	};


function fCompareInput(value1, value2, display)		//arguments OK?
	{
	if (value1.length==0 || value2.length==0)	//if blank
		{
		display.innerHTML = "";
		display.target.style.backgroundColor = ""; //grr!! says target undefined, but above line works!!		
		}	
	else if (value1==value2)			//if equal
		{
		display.innerHTML = "entries match :)";	//working first try!! holy cow! that %^&^*%* array works!!
		display.className = 'good';	//trying a work-around... voila!
		}
	else						//if different
		{
		display.innerHTML = "entries don't match :(";
		display.className = 'badboy';		//grr!!! one stupid bracket cost an eternity of troubleshooting >:(
		}
	
	};



			