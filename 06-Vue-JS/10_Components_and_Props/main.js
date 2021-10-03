const app = Vue.createApp({
    data() {
        return {
            comments: [
                {
                    username: "alice",
                    content: "First Comment!"
                },
                {
                    username: "bob",
                    content: "Hello World!"
                },
                {
                    username: "ironman",
                    content: "New Armor Coming Soon!"
                },
                {
                    username: "superman",
                    content: "Kryptonite is Bad!"
                },
            ]
        }
    }
});


app.component("comment", {
    props: {
        comment: {
            type: Object,
            required: true
        }
    },
    template: `
        <div>
            <div class="card-body">
                <strong><p>{{ comment.username }}</p></strong>
                <p>{{ comment.content }}</p>
            </div>
            <hr>
        </div>
    `
});


const mountedApp = app.mount('#app');