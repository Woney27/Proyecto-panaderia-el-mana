document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".form-agregar-cliente");
    const razonSocial = document.getElementById("razonSocial");
    const cuit = document.getElementById("cuit");
    const domicilio = document.getElementById("domicilio");
    const telefono = document.getElementById("telefono");
    const correo = document.getElementById("correo");
    const tablaClientes = document.querySelector(".tabla-cliente tbody");
    const buscarInput = document.getElementById("buscar"); // Campo de búsqueda

    form.addEventListener("submit", function(event) {
        event.preventDefault(); // Evita que se recargue la página

        // Validaciones
        if (!validarCUIT(cuit.value)) {
            alert("Por favor, ingrese un CUIT válido (solo números, 11 dígitos).");
            return;
        }

        if (!validarTelefono(telefono.value)) {
            alert("Por favor, ingrese un número de teléfono válido (solo números).");
            return;
        }

        if (cuitDuplicado(cuit.value)) {
            alert("El CUIT ingresado ya existe. Por favor, ingrese un CUIT diferente.");
            return;
        }

        // Agregar los datos a la tabla si las validaciones son correctas
        agregarClienteATabla({
            razonSocial: razonSocial.value,
            cuit: cuit.value,
            domicilio: domicilio.value,
            telefono: telefono.value,
            correo: correo.value
        });

        // Limpiar el formulario después de agregar el cliente
        form.reset();
    });

    // Evento para el botón "Cancelar" para vaciar el formulario
    document.getElementById("cancelar").addEventListener("click", function() {
        form.reset();
    });

    function validarCUIT(cuit) {
        // Validar que el CUIT tenga 11 dígitos y solo números
        const cuitRegex = /^\d{11}$/;
        return cuitRegex.test(cuit);
    }

    function validarTelefono(telefono) {
        // Validar que el teléfono solo contenga números y al menos 8 dígitos
        const telefonoRegex = /^\d{8,}$/;
        return telefonoRegex.test(telefono);
    }

    function cuitDuplicado(cuit) {
        const filas = tablaClientes.querySelectorAll("tr");
        for (let fila of filas) {
            const cuitExistente = fila.querySelector("td:nth-child(2)").innerText;
            if (cuitExistente === cuit) {
                return true;
            }
        }
        return false;
    }

    function agregarClienteATabla(cliente) {
        const fila = document.createElement("tr");

        // Crear celdas y agregarlas a la fila
        for (const key in cliente) {
            const celda = document.createElement("td");
            celda.textContent = cliente[key];
            fila.appendChild(celda);
        }

        // Crear botón para modificar
        const celdaModificar = document.createElement("td");
        const botonModificar = document.createElement("button");
        botonModificar.textContent = "Modificar";
        botonModificar.classList.add("btn-modificar");
        celdaModificar.appendChild(botonModificar);
        fila.appendChild(celdaModificar);

        // Agregar la fila a la tabla
        tablaClientes.appendChild(fila);

        // Evento para el botón de modificar
        botonModificar.addEventListener("click", function() {
            modificarCliente(fila);
        });
    }

    function modificarCliente(fila) {
        // Extraer los datos actuales de la fila
        const razonSocial = fila.children[0].innerText;
        const cuit = fila.children[1].innerText;
        const domicilio = fila.children[2].innerText;
        const telefono = fila.children[3].innerText;
        const correo = fila.children[4].innerText;

        // Llenar el formulario con los datos actuales para que puedan ser editados
        document.getElementById("razonSocial").value = razonSocial;
        document.getElementById("cuit").value = cuit;
        document.getElementById("domicilio").value = domicilio;
        document.getElementById("telefono").value = telefono;
        document.getElementById("correo").value = correo;

        // Eliminar la fila actual (para que pueda ser reemplazada por la fila modificada)
        fila.remove();
    }

    // Filtrar clientes en la tabla por nombre (razón social)
    buscarInput.addEventListener("input", function() {
        const filtro = buscarInput.value.toLowerCase();
        const filas = tablaClientes.querySelectorAll("tr");

        filas.forEach(fila => {
            const nombreCliente = fila.children[0].innerText.toLowerCase();
            fila.style.display = nombreCliente.includes(filtro) ? "" : "none";
        });
    });
});
