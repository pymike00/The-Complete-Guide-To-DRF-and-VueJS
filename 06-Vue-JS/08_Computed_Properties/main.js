const app = Vue.createApp({
    data() {
        return {
            first_name: "John",
            last_name: "Doe"
        }
    },
    computed: {
        getRandomComputed() {
            return Math.random();
        },
        fullName() {
            return `${this.first_name} ${this.last_name}`;
        },
        reversedFullName() {
            let first = this.first_name.split("").reverse().join("");
            let last = this.last_name.split("").reverse().join("");
            return `${ first } ${ last }`;
        }
    },
    methods: {
        getRandomNumber() {
            return Math.random();
        }
    }
});


const mountedApp = app.mount('#app');