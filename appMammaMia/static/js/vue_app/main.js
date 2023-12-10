import Vue from 'vue';
import App from './components/App.vue';
import VueRouter from 'vue-router';
import AcercaDeNosotros from './components/AcercaDeNosotros.vue';
import Contacto from './components/Contacto.vue';
import PoliticaPrivacidad from './components/PoliticaPrivacidad.vue';
import TerminosCondiciones from './components/TerminosCondiciones.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: App },
  { path: '/acerca-de-nosotros', component: AcercaDeNosotros },
  { path: '/contacto', component: Contacto },
  { path: '/politica-privacidad', component: PoliticaPrivacidad },
  { path: '/terminos-condiciones', component: TerminosCondiciones },
];

const router = new VueRouter({
  routes,
  mode: 'history',
    base: '/app-mamma-mia/',
});

new Vue({
  el: '#app',
  router,
  render: h => h(App),
});