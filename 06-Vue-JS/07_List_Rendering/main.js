const app = Vue.createApp({
  data() {
    return {
      users: [
        {
          id: 567,
          name: "alice",
          profession: "developer",
        },
        {
          id: 568,
          name: "bob",
          profession: "developer",
        },
        {
          id: 569,
          name: "batman",
          profession: "manager",
        },
        {
          id: 570,
          name: "jane",
          profession: "designer",
        },
        {
          id: 571,
          name: "superman",
          profession: "developer",
        },
      ],
    };
  },
});

const mountedApp = app.mount("#app");
