function listadoproductos() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			var numero = document.getElementById('codigo').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			console.log(greaterTen2)
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function filtro(){
	var numero = document.getElementById('codigo').value;
	console.log(numero)
}

$(document).ready(function(){
	listadoproductos()
});