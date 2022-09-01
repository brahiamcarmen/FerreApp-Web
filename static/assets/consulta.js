function listadoproductos() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre").innerHTML = "";
			document.getElementById("valoruni").innerHTML = "";
			var numero = document.getElementById('codigo').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni" ).append('<input id="numero1" onchange="sumar1();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productodos() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre2").innerHTML = "";
			document.getElementById("valoruni2").innerHTML = "";
			var numero = document.getElementById('codigo2').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre2" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni2" ).append('<input id="numero3" onchange="sumar2();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productotres() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre3").innerHTML = "";
			document.getElementById("valoruni3").innerHTML = "";
			var numero = document.getElementById('codigo3').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre3" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni3" ).append('<input id="numero5" onchange="sumar3();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productocuatro() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre4").innerHTML = "";
			document.getElementById("valoruni4").innerHTML = "";
			var numero = document.getElementById('codigo4').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre4" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni4" ).append('<input id="numero7" onchange="sumar4();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productocinco() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre5").innerHTML = "";
			document.getElementById("valoruni5").innerHTML = "";
			var numero = document.getElementById('codigo5').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre5" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni5" ).append('<input id="numero9" onchange="sumar5();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productoseis() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre6").innerHTML = "";
			document.getElementById("valoruni6").innerHTML = "";
			var numero = document.getElementById('codigo6').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre6" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni6" ).append('<input id="numero11" onchange="sumar6();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productosiete() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre7").innerHTML = "";
			document.getElementById("valoruni7").innerHTML = "";
			var numero = document.getElementById('codigo7').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre7" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni7" ).append('<input id="numero13" onchange="sumar7();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productoocho() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre8").innerHTML = "";
			document.getElementById("valoruni8").innerHTML = "";
			var numero = document.getElementById('codigo8').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre8" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni8" ).append('<input id="numero15" onchange="sumar8();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}

function productonueve() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre9").innerHTML = "";
			document.getElementById("valoruni9").innerHTML = "";
			var numero = document.getElementById('codigo9').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre9" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni9" ).append('<input id="numero17" onchange="sumar9();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}
function productodiez() {
	$.ajax({
		url: "/usuarios/agregarventa/",
		type: "get",
		dataType: "json",
		success: function(response){
			document.getElementById("nombre10").innerHTML = "";
			document.getElementById("valoruni10").innerHTML = "";
			var numero = document.getElementById('codigo10').value;
			let datos = response;
			let greaterTen2 = datos.filter(datos => datos.pk == numero );
			var nombreproducto = greaterTen2[0].fields.NombreProducto;
			var preciouni = greaterTen2[0].fields.PrecioVenta;
			$( "#nombre10" ).append('<div>' + nombreproducto +'</div');
			$( "#valoruni10" ).append('<input id="numero19" onchange="sumar10();" type="text" value="'+ preciouni+'" disabled>')
		},
		error: function (error) {
			console.log(error)
		}
	});	
}