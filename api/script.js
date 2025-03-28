document.addEventListener("DOMContentLoaded", function() {
    new Vue({
        el: "#app",
        data: {
            query: "",
            results: [],
            loading: false
        },
        methods: {
            fetchResults() {
                if (this.query.length < 3) {
                    this.results = [];
                    return;
                }

                this.loading = true;
                console.log("Consultando por:", this.query);
                axios.get(`http://127.0.0.1:5000/search?q=${this.query}`)
                    .then(response => {
                        console.log(response.data);
                        this.results = response.data;
                    })
                    .catch(error => {
                        console.error("Erro na busca:", error);
                    })
                    .finally(() => {
                        this.loading = false;
                    });
            }
        }
    });
});