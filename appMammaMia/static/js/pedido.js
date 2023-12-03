const btnAbrirVentana = document.getElementById("enviar");
const ventana = document.getElementById("ventana");
const btnGuardarDatos = document.getElementById("guardar");
const checkboxs = document.querySelectorAll("input[type='checkbox']");
btnAbrirVentana.addEventListener("click", ()=> {
    let alMenosUnoSeleccionado = false;
    checkboxs.forEach(checkbox => {
        if (checkbox.checked) {
            alMenosUnoSeleccionado = true;
        }
        });
        if (alMenosUnoSeleccionado) {
            ventana.showModal();
        } else {
            alert("Tienes que seleccionar almenos un producto");
        }
    
})

const nombre = document.getElementById("nombre");
const apellidos = document.getElementById("apellidos");
const direccion = document.getElementById("direccion");
const telefono = document.getElementById("telefono");

const regex = /^\d{9}$/;

btnGuardarDatos.addEventListener("click", () => {
    if (nombre && apellidos && direccion && telefono && regex.test(telefono.value)) {

        var checkboxEntrantes = Array.from(document.querySelectorAll('input[type="checkbox"][id="entrantes_checkbox"]:checked')).map(checkbox => checkbox.value);
        var checkboxPizzas = Array.from(document.querySelectorAll('input[type="checkbox"][id="pizza_checkbox"]:checked')).map(checkbox => checkbox.value);
        var checkboxMasas = Array.from(document.querySelectorAll('input[type="checkbox"][id="masa_checkbox"]:checked')).map(checkbox => checkbox.value);
        var checkboxIngredientes = Array.from(document.querySelectorAll('input[type="checkbox"][id="ingrediente_checkbox"]:checked')).map(checkbox => checkbox.value);
        var checkboxBebidas = Array.from(document.querySelectorAll('input[type="checkbox"][id="bebida_checkbox"]:checked')).map(checkbox => checkbox.value);
        var comentarioValor = $("#comentario").val();

        var nombreValor = nombre.value;
        var apellidosValor = apellidos.value;
        var direccionValor = direccion.value;
        var telefonoValor = telefono.value;

        var csrftoken = $('[name=csrfmiddlewaretoken]').val();
        
        // Envia los datos al servidor
        $.ajax({
            url: "/appMammaMia/pedido/",
            type: "POST",
            headers: {
                'X-CSRFToken': csrftoken
            },
            
            data: {
                nombreCliente: nombreValor,
                apellidos: apellidosValor,
                direccion: direccionValor,
                telefono: telefonoValor,
                pizza: checkboxPizzas,
                masa: checkboxMasas,
                ingrediente: checkboxIngredientes,
                entrantes: checkboxEntrantes,
                bebidas: checkboxBebidas,
                comentario: comentarioValor,
            },
            success: function (response) {
                // Maneja la respuesta del servidor
                console.log(response);
            },
            error: function (error) {
                // Maneja errores
                console.log(error);
            }
        });

        ventana.close();
    } else {
        alert('No has rellenado todos los campos');
    }
});
