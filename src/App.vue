<template>
  <div class="d-flex" :class="visibilidadeSidebar" id="wrapper">
    <!-- Sidebar -->
    <!-- /#sidebar-wrapper -->
    <sidebar/>
    <!-- Page Content -->
    <div id="page-content-wrapper">
      <nav class="navbar navbar-expand-lg navbar-light bg-light border-bottom">
        <button
          class="btn btn-primary"
          id="menu-toggle"
          @click="trocaVisibilidadeSidebar()" >
          Toggle Menu
          </button>

        <button
          class="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
            <li class="nav-item active">
              <a class="nav-link" href="#">
                Home
                <span class="sr-only">(current)</span>
              </a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="#">Link</a>
            </li>
          </ul>
        </div>
      </nav>

      <div class="container-fluid">
        <router-view />
      </div>
    </div>
    <!-- /#page-content-wrapper -->
  </div>
</template>

<script>
import Sidebar from './components/Sidebar.vue';


export default {
  name: 'app',
  components: {
    sidebar: Sidebar,
  },
  data() {
    return {
      visibilidadeSidebar: '',
    };
  },
  methods: {
    trocaVisibilidadeSidebar() {
      if (this.visibilidadeSidebar === '') {
        this.visibilidadeSidebar = 'toggled';
      } else {
        this.visibilidadeSidebar = '';
      }
    },
  },
};
</script>

<style>
</style>
