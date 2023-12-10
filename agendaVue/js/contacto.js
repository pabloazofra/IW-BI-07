// contacto.js

const contactos = [
    { nombre: 'John Doe', email: 'john.doe@deusto.es', telefono: '555555555' }
  ];

new Vue({
el: '#app',
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
}
});
  

