<template>
    <div class="contact-container">
      <h2>Información de Contacto</h2>
      <p>Puedes contactarnos a través de:</p>
  
      <ul class="contact-list">
        <li class="contact-item" @click="toggleSubMenu('direccion')">
          Dirección
          <div v-show="showSubMenu === 'direccion'" class="submenu-container">
            <p>Nuestra dirección:</p>
            <ul>
              <li>Calle Roma, Número 33</li>
              <li>Bilbao (48001)</li>
              <li>Vizcaya</li>
            </ul>
          </div>
        </li>
  
        <li class="contact-item" @click="toggleSubMenu('telefono')">
          Teléfono
          <div v-show="showSubMenu === 'telefono'" class="submenu-container">
            <p>Nuestro número de teléfono:</p>
            <ul>
              <li>+34 944 41 00 00</li>
            </ul>
          </div>
        </li>
  
        <li class="contact-item" @click="toggleSubMenu('correo')">
          Correo
          <div v-show="showSubMenu === 'correo'" class="submenu-container">
            <p>Nuestra dirección de correo electrónico:</p>
            <ul>
              <li>mammamiapizzeria@info.com</li>
            </ul>
          </div>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        showSubMenu: null,
      };
    },
    methods: {
      toggleSubMenu(subMenu) {
        this.showSubMenu = this.showSubMenu === subMenu ? null : subMenu;
      },
    },
  };
  </script>
  
  <style scoped>
  /* Puedes colocar tus estilos específicos aquí */
  </style>