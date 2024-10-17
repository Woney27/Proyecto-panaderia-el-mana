let insumos = []; // Array para almacenar los insumos agregados

window.onload = function() {
    // Captura el campo de fecha
    const fechaSolicitud = document.getElementById('fecha');

    // Crea una fecha actual en formato adecuado (YYYY-MM-DDTHH:mm)
    const hoy = new Date();
    hoy.setMinutes(hoy.getMinutes() + 1); // Añade un minuto al actual para evitar fecha/hora actual
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0'); // Los meses empiezan desde 0
    const anio = hoy.getFullYear();
    const horas = hoy.getHours().toString().padStart(2, '0');
    const minutos = hoy.getMinutes().toString().padStart(2, '0');
    
    const fechaMin = `${anio}-${mes}-${dia}T${horas}:${minutos}`;
    fechaSolicitud.setAttribute("min", fechaMin);

    // Agregar evento submit al formulario
    document.querySelector("form").addEventListener("submit", function(event) {
        event.preventDefault(); // Evitar que la página se recargue
        agregarInsumo();
    });
};

// Función para agregar un insumo a la lista
function agregarInsumo() {
    // Capturar los valores de los inputs
    const descripcion = document.getElementById("proveedor").value.trim();
    const cantidad = document.getElementById("cantidad").value.trim();
    const observacion = document.getElementById("observacion").value.trim() || "N/A";
    const idProveedor = document.getElementById("idProveedor").value.trim();

    // Validar si los campos obligatorios están llenos
    if (!descripcion || !cantidad || !idProveedor) {
        alert("Por favor, completa todos los campos obligatorios.");
        return;
    }

    // Crear el objeto insumo con los valores ingresados
    const insumo = {
        descripcion,
        cantidad,
        observacion,
        idProveedor
    };

    // Agregar el insumo al array
    insumos.push(insumo);

    // Mostrar el insumo en la tabla
    mostrarInsumos();

    // Resetear el formulario para que quede limpio
    document.querySelector("form").reset();
}

// Función para mostrar los insumos en una tabla
function mostrarInsumos() {
    const tablaCuerpo = document.getElementById("listaInsumos");
    tablaCuerpo.innerHTML = ""; // Limpiar la tabla antes de agregar nuevos elementos

    insumos.forEach((insumo, index) => {
        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${insumo.descripcion}</td>
            <td>${insumo.cantidad}</td>
            <td>${insumo.observacion}</td>
            <td>${insumo.idProveedor}</td>
            <td>
                <button class="btn" onclick="editarInsumo(${index})">Editar</button>
                <button class="btn btn-danger" onclick="eliminarInsumo(${index})">Eliminar</button>
            </td>
        `;

        tablaCuerpo.appendChild(fila); // Añadir la fila a la tabla
    });
}

// Función para editar un insumo
function editarInsumo(index) {
    const insumo = insumos[index];

    // Llenar el formulario con los valores actuales del insumo
    document.getElementById("proveedor").value = insumo.descripcion;
    document.getElementById("cantidad").value = insumo.cantidad;
    document.getElementById("observacion").value = insumo.observacion;
    document.getElementById("idProveedor").value = insumo.idProveedor;

    // Eliminar el insumo de la lista temporalmente
    eliminarInsumo(index);
}

// Función para eliminar un insumo
function eliminarInsumo(index) {
    insumos.splice(index, 1); // Eliminar el insumo del array
    mostrarInsumos(); // Actualizar la tabla
}
