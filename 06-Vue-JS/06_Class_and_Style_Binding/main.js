const app = Vue.createApp({
  data() {
    return {
      flag: true,
      styleObject: {
        backgroundColor: "green",
        border: "5px solid orange",
      },
    };
  },
  methods: {
    changeShape() {
      this.flag = !this.flag;
    },
  },
});

const mountedApp = app.mount("#app");
