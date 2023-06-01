$("DIV#toggle_header").on("click", function(){
	$("header").hasClass("green")
	? $("header").attr("class", "red")
	: $("header").attr("class", "green");
})
