// Ejecutar cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {
    // Simulando datos del usuario logueado
    const vendedorId = "12345"; // Este valor debe provenir de tu sistema de autenticación
    const fechaActual = new Date();
    const numeroComprobante = Math.floor(Math.random() * 1000000); // Genera un número aleatorio para el comprobante

    // Cargar los datos predeterminados al cargar la página
    document.getElementById("vendedor").value = vendedorId; // Cargar ID del vendedor
    document.getElementById("fecha").value = obtenerFechaFormateada(fechaActual); // Cargar fecha actual formateada
    document.getElementById("comprobante").value = numeroComprobante; // Cargar número de comprobante

    // Si deseas deshabilitar los campos, puedes hacerlo aquí
    document.getElementById("venta-num").value = "Auto-generado"; // Ejemplo de campo deshabilitado

    // Vincular el botón "Agregar" a la validación del formulario
    const agregarBtn = document.getElementById("agregar-btn");
    agregarBtn.addEventListener("click", validarFormulario);
});

// Función para validar el formulario al hacer clic en "Agregar"
function validarFormulario(event) {
    // Prevenir el envío del formulario para realizar validaciones
    event.preventDefault(); 

    // Obtener valores de los campos del formulario
    const fecha = document.getElementById("fecha").value;
    const comprobante = document.getElementById("comprobante").value;
    const cliente = document.getElementById("cliente").value;
    const pago = document.getElementById("pago").value;
    const producto = document.getElementById("producto").value;
    const precio = parseFloat(document.getElementById("precio").value);
    const cantidad = parseInt(document.getElementById("cantidad").value);

    // Array para almacenar errores
    let errores = [];

    // Validar fecha
    if (!validarFecha(fecha)) {
        errores.push("La fecha debe estar en el formato dd/mm/aaaa.");
    }

    // Validar campos obligatorios
    if (!comprobante) {
        errores.push("El N° de comprobante es obligatorio.");
    }
    if (cliente === "Seleccionar") {
        errores.push("Debes seleccionar un tipo de cliente.");
    }
    if (pago === "Seleccionar") {
        errores.push("Debes seleccionar una forma de pago.");
    }
    if (!producto) {
        errores.push("El nombre del producto es obligatorio.");
    }

    // Validar precio (debe ser mayor que 0)
    if (isNaN(precio) || precio <= 0) {
        errores.push("El precio debe ser un número mayor que 0.");
    }

    // Validar cantidad (debe ser mayor que 0)
    if (isNaN(cantidad) || cantidad < 1) {
        errores.push("La cantidad debe ser un número mayor o igual a 1.");
    }

    // Mostrar errores si los hay, de lo contrario proceder
    if (errores.length > 0) {
        alert(errores.join("\n"));
    } else {
        alert("Formulario válido. Procediendo con la adición...");
        // Aquí puedes agregar la lógica para agregar el producto a la tabla o cualquier otra acción necesaria
    }
}

// Función para validar la fecha en formato dd/mm/aaaa
function validarFecha(fecha) {
    const regex = /^\d{2}\/\d{2}\/\d{4}$/; // Formato dd/mm/aaaa
    return regex.test(fecha);
}

// Función para obtener la fecha actual formateada como dd/mm/aaaa
function obtenerFechaFormateada(fecha) {
    const dia = String(fecha.getDate()).padStart(2, '0');
    const mes = String(fecha.getMonth() + 1).padStart(2, '0'); // Los meses van de 0-11
    const anio = fecha.getFullYear();
    return `${dia}/${mes}/${anio}`;
}
// Ejecutar cuando el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", () => {
    // Simulando datos del usuario logueado
    const vendedorId = "12345"; // Este valor debe provenir de tu sistema de autenticación
    const fechaActual = new Date();
    const numeroComprobante = Math.floor(Math.random() * 1000000); // Genera un número aleatorio para el comprobante

    // Cargar los datos predeterminados al cargar la página
    document.getElementById("vendedor").value = vendedorId; // Cargar ID del vendedor
    document.getElementById("fecha").value = obtenerFechaFormateada(fechaActual); // Cargar fecha actual formateada
    document.getElementById("comprobante").value = numeroComprobante; // Cargar número de comprobante

    // Si deseas deshabilitar los campos, puedes hacerlo aquí
    document.getElementById("venta-num").value = "Auto-generado"; // Ejemplo de campo deshabilitado

    // Vincular el botón "Agregar" a la validación del formulario
    const agregarBtn = document.getElementById("agregar-btn");
    agregarBtn.addEventListener("click", validarFormulario);
});

// Función para validar el formulario al hacer clic en "Agregar"
function validarFormulario(event) {
    // Prevenir el envío del formulario para realizar validaciones
    event.preventDefault(); 

    // Obtener valores de los campos del formulario
    const fecha = document.getElementById("fecha").value;
    const comprobante = document.getElementById("comprobante").value;
    const cliente = document.getElementById("cliente").value;
    const pago = document.getElementById("pago").value;
    const producto = document.getElementById("producto").value;
    const precio = parseFloat(document.getElementById("precio").value);
    const cantidad = parseInt(document.getElementById("cantidad").value);

    // Array para almacenar errores
    let errores = [];

    // Validar fecha
    if (!validarFecha(fecha)) {
        errores.push("La fecha debe estar en el formato dd/mm/aaaa.");
    }

    // Validar campos obligatorios
    if (!comprobante) {
        errores.push("El N° de comprobante es obligatorio.");
    }
    if (cliente === "Seleccionar") {
        errores.push("Debes seleccionar un tipo de cliente.");
    }
    if (pago === "Seleccionar") {
        errores.push("Debes seleccionar una forma de pago.");
    }
    if (!producto) {
        errores.push("El nombre del producto es obligatorio.");
    }

    // Validar precio (debe ser mayor que 0)
    if (isNaN(precio) || precio <= 0) {
        errores.push("El precio debe ser un número mayor que 0.");
    }

    // Validar cantidad (debe ser mayor que 0)
    if (isNaN(cantidad) || cantidad < 1) {
        errores.push("La cantidad debe ser un número mayor o igual a 1.");
    }

    // Mostrar errores si los hay, de lo contrario proceder
    if (errores.length > 0) {
        alert(errores.join("\n"));
    } else {
        alert("Formulario válido. Procediendo con la adición...");
        // Aquí puedes agregar la lógica para agregar el producto a la tabla o cualquier otra acción necesaria
    }
}

// Función para validar la fecha en formato dd/mm/aaaa
function validarFecha(fecha) {
    const regex = /^\d{2}\/\d{2}\/\d{4}$/; // Formato dd/mm/aaaa
    return regex.test(fecha);
}

// Función para obtener la fecha actual formateada como dd/mm/aaaa
function obtenerFechaFormateada(fecha) {
    const dia = String(fecha.getDate()).padStart(2, '0');
    const mes = String(fecha.getMonth() + 1).padStart(2, '0'); // Los meses van de 0-11
    const anio = fecha.getFullYear();
    return `${dia}/${mes}/${anio}`;
}
