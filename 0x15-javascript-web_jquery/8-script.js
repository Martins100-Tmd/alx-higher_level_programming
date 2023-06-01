$.get("https://swapi-api.alx-tools.com/api/films/?format=json", function(data){
	for(let e in data.results){
		e = parseInt(e);
		$("UL#list_movies").append(`<li>${data.results[e].title}</li>`);
}})
