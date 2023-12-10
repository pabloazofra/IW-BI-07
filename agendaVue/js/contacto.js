// contacto.js

// Datos de ejemplo para los contactos (puedes reemplazarlos con un arreglo vacío para empezar)
const contactos = [
    { nombre: 'John Doe', email: 'john.doe@deusto.es', telefono: '555555555' }
    // Puedes añadir más contactos aquí
  ];

new Vue({
el: '#app', // Elemento HTML donde se montará la aplicación Vue
data: {
    contactos: contactos,
    nuevoContacto: { nombre: '', email: '', telefono: '' }
},
methods: {
    agregarContacto: function () {
    this.contactos.push(this.nuevoContacto);
    this.nuevoContacto = { nombre: '', email: '', telefono: '' };
    },
    borrarContacto: function (index) {
    this.contactos.splice(index, 1);
    }
    // Otros métodos que puedas necesitar
}
});
  