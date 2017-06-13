var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('Xctf_10m_passwd')
});

var hasUppCase, hasLowCase, hasDigit, hasNonAlphaNum
var nANum = "~!@#$%^&*_-+=`|\\(){}[]:;\"'<>,.?/"
var x = 1

//(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[~!@#$%^&*_\-+=`|\(){}[\]:;"'<>,\.\?\/])(?=.{25,})

/*
1 27 'Vixens.comreaper999MOR098GO'
2 28 'Tickled.comreaper999MOR098GO'
3 24 'Z3_nz92_koz15EJsos250264'
4 26 'Your_Guardian_Angel_050813'
5 31 'you_have_been_hacked_gWSxH1FZfr'
6 30 'weAaQIno0lhLHWsIfL9TQG30ZrI-~B'
*/

lineReader.on('line', function (line) {
	hasUppCase = false
	hasLowCase = false
	hasDigit = false
	hasNonAlphaNum = false

	for(var i in line){
		var ccode = line[i].charCodeAt(0)
		if(ccode > 64 && ccode < 91){ //UpperCase
			hasUppCase = true
		}
		if(ccode > 96 && ccode < 123){ //LowerCase
			hasLowCase = true
		}
		if(ccode > 47 && ccode < 50){ //Num
			hasDigit = true
		}
		if(nANum.indexOf(line[i]) != -1){ //hasNonAlphaNum
			hasNonAlphaNum = true
		}
	}

	if(line.length > 23 && hasUppCase && hasLowCase && hasDigit && hasNonAlphaNum){
		console.log(x, line.length, line)
		x++;
	}
});