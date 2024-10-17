class Producto {
    constructor(descripcion, unidadMedida, precio, cantDispo, categoria) {
        this.descripcion = descripcion;
        this.unidadMedida = unidadMedida;
        this.precio = parseFloat(precio);
        this.cantDispo = parseInt(cantDispo);
        this.categoria = categoria;
    }

    eliminarReserva(listaProductos) {
        const index = listaProductos.indexOf(this);
        if (index > -1) {
            listaProductos.splice(index, 1);
        }
    }
}

let productos = [];

document.addEventListener('DOMContentLoaded', function() {

    document.getElementById('form-producto').addEventListener('submit', function(event) {
        event.preventDefault();

        let descripcion = document.getElementById("descrip-producto").value;
        let unidadMedida = document.getElementById("unidad-medida").value;
        let precio = document.getElementById("precio").value;
        let cantDispo = document.getElementById("cantidad").value;
        let categoria = document.getElementById("categoriaProduc").value;

        let producto = new Producto(descripcion, unidadMedida, precio, cantDispo, categoria);
        productos.push(producto);

        mostrarProductos();
        this.reset(); // Limpiar el formulario después de guardar
    });

    function mostrarProductos() {
        let tablaProductos = document.getElementById("productos").querySelector('tbody');
        tablaProductos.innerHTML = ""; // Limpiar la tabla antes de actualizarla

        productos.forEach((producto, index) => {
            let fila = tablaProductos.insertRow();
            fila.innerHTML = `
                <td>${producto.descripcion}</td>
                <td>${producto.unidadMedida}</td>
                <td>${producto.precio.toFixed(2)}</td>
                <td>${producto.cantDispo}</td>
                <td>${producto.categoria}</td>
                <td><button class="btn btn-danger" onclick="eliminarReserva(${index})">Eliminar</button></td>
            `;
        });
    }

    window.eliminarReserva = function(index) {
        productos.splice(index, 1);
        mostrarProductos(); // Actualizar la tabla después de eliminar
    };
});
