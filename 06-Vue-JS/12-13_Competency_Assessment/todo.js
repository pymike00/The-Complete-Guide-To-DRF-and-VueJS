const app = Vue.createApp({
  data() {
    return {
      tasks: [],
    };
  },
  computed: {
    taskCount() {
      return this.tasks.length;
    },
  },
  methods: {
    addNewTask(newTask) {
      this.tasks.push(newTask);
    },
    removeTask(task) {
      this.tasks.splice(this.tasks.indexOf(task), 1);
    },
  },
});

app.component("to-do", {
  props: {
    tasks: {
      type: Array,
      required: true,
    },
    remaining: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      error: null,
      newTask: null,
    };
  },
  methods: {
    submitTask() {
      if (this.newTask) {
        this.$emit("add-task", this.newTask);
        this.newTask = null;
        if (this.error) {
          this.error = null;
        }
      } else {
        this.error = "The input field can't be empty!";
      }
    },
    removeTask(task) {
      this.$emit("remove-task", task);
    },
  },
  template: `
        <div class="container my-2">
            <p><strong>Remaining Tasks: {{ remaining }}</strong></p>
            <input type="text"
                   v-model="newTask"
                   class="form-control"
                   placeholder="What do you need to do?"
                   @keyup.enter="submitTask">
            <br>
            <div v-for="task in tasks">
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    {{ task }}
                    <button @click="removeTask(task)" type="button" class="close no-outline" data-dismiss="alert" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
            </div> 
            <p v-if="error">{{ error }}</p>
            <p v-if="remaining === 0">To add a new task, write something and press enter!</p>
        </div>
    `,
});

const mountedApp = app.mount("#app");
