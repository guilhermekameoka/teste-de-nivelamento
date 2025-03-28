document.addEventListener("DOMContentLoaded", function() {
    new Vue({
        el: "#app",
        data: {
            query: "",
            results: [],
            loading: false,
            timeout: null, // Para armazenar o setTimeout
        },
        methods: {
            fetchResults() {
                if (this.query.length < 3) {
                    this.results = []; // Clear results if the query is too short
                    return;
                }

                // Limpa o timeout anterior
                clearTimeout(this.timeout);

                this.loading = true;
                console.log("Consultando por:", this.query);

                // Adiciona um atraso de 2000ms antes de fazer a requisição
                this.timeout = setTimeout(() => {
                    axios.get(`http://127.0.0.1:5001/search?q=${this.query}&limit=10`)
                        .then(response => {
                            console.log("Dados recebidos:", response.data);
                            let items = [];
                            
                            try {
                                response.data = response.data.replace(/NaN/g, "null");
                                // Verifica se a resposta é uma string JSON e tenta convertê-la
                                if (typeof response.data === "string") {
                                    items = JSON.parse(response.data);  // Converte a string JSON para um objeto
                                } else {
                                    items = response.data.items || [];  // Caso já seja um objeto
                                }
                            } catch (e) {
                                console.error("Erro ao parsear os dados JSON:", e);
                            }

                            this.results = [];
                            items.forEach(item => {
                                Vue.set(this.results, this.results.length, item); // Força a atualização de cada item
                            });
                        })
                        .catch(error => {
                            console.error("Erro na busca:", error);
                        })
                        .finally(() => {
                            this.loading = false;
                        });
                }, 2000); // Tempo de espera em milissegundos
            }
        }
    });
});