function disco()	{
	var x = getRandomInt(0, 255);
	var y = getRandomInt(0, 255);
	var z = getRandomInt(0, 255);
	//$('body').css('background', 'rgb('+x+','+y+','+z+')');
	//$('h1').css('color', 'rgb('+y+','+x+','+z+')');
	document.body.style.backgroundColor = 'rgb('+x+','+y+','+z+')';
	setTimeout('disco()', 50);
}
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function niceDisco(x, y, z, bool)	{
	if(bool)	{
		x++;y;z++;
		if(x==255)	{
			bool=false;
		}
	}
	else	{
		x--;y;z--;
		if(x==0)	{
			bool=true;
		}
	}
	$('body').css('background', 'rgb('+x+','+y+','+z+')');
	setTimeout('niceDisco('+x+','+y+','+z+','+bool+')', 50);
}
function discoImg(id, degrees, bool)	{
	if(bool)	{
		degrees++;
		if(degrees>360)	{
			bool=false;
		}
	}
	else	{
		degrees--;
		if(degrees<=0)	{
			bool=true;
		}
	}
	if(navigator.userAgent.match("Chrome")){
		$('img').css('WebkitTransform',"rotate("+degrees+"deg)");
	} else if(navigator.userAgent.match("Firefox")){
		$('img').css('MozTransform', "rotate("+degrees+"deg)");
	} else if(navigator.userAgent.match("MSIE")){
		$('img').css('msTransform', "rotate("+degrees+"deg)");
	} else if(navigator.userAgent.match("Opera")){
		$('img').css('OTransform', "rotate("+degrees+"deg)");
	} else {
		$('img').css('transform',"rotate("+degrees+"deg)");
	}	
	setTimeout('discoImg('+id+','+degrees+','+bool+')', 25);
}

function fun()  {
    disco()
    for(i=1;i<=6;i++)	{
        var degrees=getRandomInt(0, 360);
	    if(i%2==0)	{
    	//discoImg(i+'',degrees, true);
	    }
	    else	{
		//discoImg(i+'', degrees, false);
	    }
    }	
}

window.onload = fun;

