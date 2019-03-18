var app = new Vue({
    el: "#app",
    data: {
        first_name: "John",
        last_name: "Doe"
    },
    computed: {
        getRandomComputed() {
            return Math.random();
        },
        fullName() {
             return `${ this.first_name } ${ this.last_name }`;
        },
        reversedFullName() {
            first = this.first_name.split("").reverse().join("");
            last = this.last_name.split("").reverse().join("");
            return `${ first } ${ last }`;
       },       
    },
    methods: {
        getRandomNumber() {
            return Math.random();
        }
    }
}) 