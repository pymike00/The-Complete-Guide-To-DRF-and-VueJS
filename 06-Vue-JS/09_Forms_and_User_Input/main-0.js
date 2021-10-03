const app = Vue.createApp({
  data() {
    return {
      text: "",
      checked: true,
      city: ""
    }
  }
});

const mountedApp = app.mount("#app");
