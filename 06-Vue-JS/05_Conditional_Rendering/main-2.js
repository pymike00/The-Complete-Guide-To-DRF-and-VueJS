const app = Vue.createApp({
  data() {
    return {
      product: "sunglasses",
      quantity: 150,
      sale: true,
    };
  },
});

const mountedApp = app.mount("#app");
