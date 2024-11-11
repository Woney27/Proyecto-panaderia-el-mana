let productos = []; // Array para almacenar los productos agregados

window.onload = function() {
    // Cargar los pedidos iniciales en la tabla
    cargarPedidosIniciales();

    // Configurar la fecha mínima para el campo de fecha de solicitud
    const fechaSolicitud = document.querySelector("input[name='fecha_solicitud']");
    const hoy = new Date();
    hoy.setMinutes(hoy.getMinutes() + 1);
    const dia = hoy.getDate().toString().padStart(2, '0');
    const mes = (hoy.getMonth() + 1).toString().padStart(2, '0');
    const anio = hoy.getFullYear();
    const horas = hoy.getHours().toString().padStart(2, '0');
    const minutos = hoy.getMinutes().toString().padStart(2, '0');
    const fechaMin = `${anio}-${mes}-${dia}T${horas}:${minutos}`;
    fechaSolicitud.setAttribute("min", fechaMin);

    // Agregar evento al botón de agregar producto
    document.getElementById("agregarProducto").addEventListener("click", function(event) {
        event.preventDefault(); // Evitar que el formulario se envíe
        agregarProducto();
    });
};

// Función para cargar los pedidos iniciales en la tabla
function cargarPedidosIniciales() {
    const tablaCuerpo = document.getElementById("listaInsumos");

    // Obtener los pedidos existentes de la plantilla de Django
    const pedidosIniciales = JSON.parse('{{ pedidos|safe }}'.replace(/&quot;/g, '"'));

    pedidosIniciales.forEach((pedido) => {
        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${pedido.producto}</td>
            <td>${pedido.cantidad}</td>
            <td>
                <button class="btn" onclick="editarProducto(${productos.length})">Editar</button>
                <button class="btn btn-danger" onclick="eliminarProducto(${productos.length})">Eliminar</button>
            </td>
        `;

        tablaCuerpo.appendChild(fila); // Añadir la fila a la tabla
        productos.push(pedido); // Agregar el pedido al array de productos
    });
}

// Función para agregar un nuevo producto a la lista
function agregarProducto() {
    const producto = document.querySelector("select[name='producto']").selectedOptions[0].text;
    const cantidad = document.querySelector("input[name='cantidad']").value.trim();

    // Validar si los campos obligatorios están llenos
    if (!producto || !cantidad) {
        alert("Por favor, completa los campos de producto y cantidad.");
        return;
    }

    // Crear el objeto producto con los valores ingresados
    const nuevoProducto = { producto, cantidad };
    productos.push(nuevoProducto);

    // Mostrar el producto en la tabla
    mostrarProductos();

    // Limpiar los campos de entrada
    document.querySelector("input[name='cantidad']").value = "";
}

// Función para mostrar los productos en la tabla
function mostrarProductos() {
    const tablaCuerpo = document.getElementById("listaInsumos");
    tablaCuerpo.innerHTML = ""; // Limpiar la tabla antes de agregar nuevos elementos

    productos.forEach((item, index) => {
        const fila = document.createElement("tr");

        fila.innerHTML = `
            <td>${item.producto}</td>
            <td>${item.cantidad}</td>
            <td>
                <button class="btn" onclick="editarProducto(${index})">Editar</button>
                <button class="btn btn-danger" onclick="eliminarProducto(${index})">Eliminar</button>
            </td>
        `;

        tablaCuerpo.appendChild(fila); // Añadir la fila a la tabla
    });
}

// Función para editar un producto
function editarProducto(index) {
    const producto = productos[index];
    
    // Llenar los campos con los valores del producto actual
    document.querySelector("select[name='producto']").value = producto.producto;
    document.querySelector("input[name='cantidad']").value = producto.cantidad;

    // Eliminar el producto de la lista temporalmente
    eliminarProducto(index);
}

// Función para eliminar un producto
function eliminarProducto(index) {
    productos.splice(index, 1); // Eliminar el producto del array
    mostrarProductos(); // Actualizar la tabla
}
