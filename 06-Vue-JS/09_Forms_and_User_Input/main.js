const app = Vue.createApp({
  data() {
    return {
      comment: null,
      comments: [],
      error: null,
    };
  },
  methods: {
    onSubmit() {
      if (this.comment) {
        let newComment = this.comment;
        this.comments.push(newComment);
        this.comment = null;

        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "The comment field can't be empty!";
      }
    },
  },
});

const mountedApp = app.mount("#app");
