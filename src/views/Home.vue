<template>
  <dir>
    <h1> Home </h1>
    <b-button variant="primary" @click="getMsg()">
      Get Message from Python
    </b-button>
    <br/>
    <b-alert show dismissible>
      {{ msg }}
    </b-alert>

  </dir>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      msg: ' ',
    };
  },
  methods: {
    getMsg() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },

};
</script>
