class Producto{
    constructor(descripProducto, precio, cantidadDisp, categoria){
        this.descripProducto = descripProducto;
        this.precio = precio;
        this.cantidadDisp = cantidadDisp;
        this.categoria = cantegoria;
    }

    eliminarProducto(fila) {
        fila.remove();
    }
}

let productos = [];

document.addEventListener('DOMContentLoaded',function(){


    document.getElementById('form-producto').addEventListener('submit', function(event) {
        event.preventDefault(); 

        let descripProducto = document.getElementById('descrip-producto').value;
        let precio = document.getElementById('precio').value;
        let cantidadDisp = document.getElementById('cantidad').value;
        let categoria = document.getElementById('categoriaProduc').value;

        let producto = new Producto(descripProducto, precio, cantidadDisp, categoria);

        productos.push(producto);

        actualizarTabla();
    });


    function actualizarTabla() {
        let tablaProducto = document.getElementById('productos');
        let cuerpoTabla = document.getElementById('tbody');

        productos.forEach(producto => {
            let fila = document.createElement('tr');

            fila.innerHTML =`
            <td>${producto.descripProducto}</td>
            <td>${producto.precio}</td>
            <td>${producto.cantidadDisp}</td>
            <td>${producto.cantegoria}</td>
            `;
            cuerpoTabla.appendChild(document.createElement('fila'))
        });
        tablaProducto.appendChild(cuerpoTabla);
    }

    function eliminarReserva(index, boton) {
            productos.splice(index, 1); // Eliminar reserva del array
            actualizarTabla(); // Actualizar la tabla después de eliminar
    };
});