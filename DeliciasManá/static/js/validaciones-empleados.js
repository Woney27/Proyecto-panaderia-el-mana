// validaciones-empleados.js

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("formulario-empleado").addEventListener("submit", function(event) {
        event.preventDefault(); // Previene el envío del formulario

        // Obtener valores de los campos
        const nombre = document.getElementById("nombre").value.trim();
        const cuit = document.getElementById("cuit").value.trim();
        const domicilio = document.getElementById("domicilio").value.trim();
        const telefono = document.getElementById("telefono").value.trim();
        const fechaNac = document.getElementById("fecha-nac").value;
        const cargo = document.getElementById("cargo").value.trim();
        const fechaIngreso = document.getElementById("fecha-ingreso").value;
        const estado = document.getElementById("estado").value;

        let mensajeError = '';
        const hoy = new Date(); // Definimos 'hoy' aquí

        // Validaciones
        if (nombre === "") {
            mensajeError += "El nombre es requerido. \n";
        }
        if (cuit === "" || !/^\d{11}$/.test(cuit)) {
            mensajeError += "El CUIT debe tener exactamente 11 dígitos. \n";
        }
        if (domicilio === "") {
            mensajeError += "El domicilio es requerido. \n";
        }
        if (telefono === "" || !/^\d{10}$/.test(telefono)) {
            mensajeError += "El teléfono debe ser un número de 10 dígitos. \n";
        }
        if (fechaNac === "") {
            mensajeError += "La fecha de nacimiento es requerida. \n";
        } else {
            const fechaNacDate = new Date(fechaNac);
            // Validar que la fecha de nacimiento no sea futura
            if (fechaNacDate > hoy) {
                mensajeError += "La fecha de nacimiento no puede ser una fecha futura. \n";
            }
        }
        if (cargo === "") {
            mensajeError += "El cargo es requerido. \n";
        }
        if (fechaIngreso === "") {
            mensajeError += "La fecha de ingreso es requerida. \n";
        } else {
            const fechaIngresoDate = new Date(fechaIngreso);
            // Validar que la fecha de ingreso no sea futura
            if (fechaIngresoDate > hoy) {
                mensajeError += "La fecha de ingreso no puede ser una fecha futura. \n";
            }
            // Validar que la fecha de ingreso sea posterior a la fecha de nacimiento
            if (fechaNac !== "") {
                const fechaNacDate = new Date(fechaNac);
                if (fechaIngresoDate <= fechaNacDate) {
                    mensajeError += "La fecha de ingreso debe ser posterior a la fecha de nacimiento. \n";
                }
            }
        }

        // Verificar si ya existe un empleado con el mismo CUIT
        const tablaBody = document.querySelector(".tabla-empleados tbody");
        for (let row of tablaBody.rows) {
            const cuitExistente = row.cells[1].textContent.trim(); // Supone que el CUIT está en la segunda celda
            if (cuitExistente === cuit) {
                mensajeError += "Ya existe un empleado con ese CUIT. \n";
                break; // Salir del bucle si encontramos un CUIT existente
            }
        }

        // Mostrar errores si los hay
        const mensajeDiv = document.getElementById("mensaje");
        if (mensajeError) {
            mensajeDiv.textContent = mensajeError; // Mostrar mensaje de error
        } else {
            // Mostrar mensaje de éxito
            mensajeDiv.textContent = "Empleado registrado con éxito!";

            // Agregar empleado a la tabla
            agregarEmpleadoATabla(nombre, cuit, domicilio, telefono, fechaNac, cargo, fechaIngreso, estado);
            
            // Limpiar el formulario
            document.getElementById("formulario-empleado").reset(); 
        }
    });

    // Función para agregar empleado a la tabla
    function agregarEmpleadoATabla(nombre, cuit, domicilio, telefono, fechaNac, cargo, fechaIngreso, estado) {
        const tablaBody = document.querySelector(".tabla-empleados tbody");
        const nuevaFila = tablaBody.insertRow();
        
        // Agregar atributos data-* para los datos adicionales
        nuevaFila.setAttribute("data-domicilio", domicilio);
        nuevaFila.setAttribute("data-fecha-nac", fechaNac);
        
        nuevaFila.innerHTML = `
            <td>${tablaBody.rows.length}</td>
            <td>${cuit}</td>
            <td>${nombre}</td>
            <td>${cargo}</td>
            <td>${estado}</td>
            <td>${fechaIngreso}</td>
            <td>${telefono}</td>
        `;
    }

    // Buscar empleado por CUIT
    document.getElementById("btn-buscar").addEventListener("click", function(event) {
        const cuitBusqueda = document.getElementById("cuit-busqueda").value.trim();
        const mensajeBusquedaDiv = document.getElementById("mensaje-busqueda");
        mensajeBusquedaDiv.textContent = ""; // Limpiar mensajes anteriores

        const tablaBody = document.querySelector(".tabla-empleados tbody");
        let empleadoEncontrado = false;

        for (let row of tablaBody.rows) {
            const cuitExistente = row.cells[1].textContent.trim(); // Supone que el CUIT está en la segunda celda
            if (cuitExistente === cuitBusqueda) {
                // Si encontramos el CUIT, rellenamos los campos del formulario
                document.getElementById("nombre").value = row.cells[2].textContent; // Nombre
                document.getElementById("cuit").value = cuitExistente; // CUIT
                document.getElementById("domicilio").value = row.dataset.domicilio || ''; // Domicilio desde data-attribute
                document.getElementById("telefono").value = row.cells[6].textContent; // Teléfono
                document.getElementById("fecha-nac").value = row.dataset.fechaNac || ''; // Fecha de nacimiento desde data-attribute
                document.getElementById("cargo").value = row.cells[3].textContent; // Cargo
                document.getElementById("fecha-ingreso").value = row.cells[5].textContent; // Fecha de ingreso
                document.getElementById("estado").value = row.cells[4].textContent; // Estado

                empleadoEncontrado = true;
                mensajeBusquedaDiv.textContent = "Empleado encontrado. Puede modificar los datos.";
                break; // Salir del bucle si encontramos el empleado
            }
        }

        if (!empleadoEncontrado) {
            mensajeBusquedaDiv.textContent = "No se encontró ningún empleado con ese CUIT.";
        }
    });
});
