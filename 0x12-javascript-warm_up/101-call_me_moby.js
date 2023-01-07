#!/usr/bin/node
//write a script that calls a function x times

exports.callMeMoby = function(x, func){
	while(x !== 0)
	{
		func();
		--x;
	}
}

