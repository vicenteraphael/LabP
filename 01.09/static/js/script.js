document.addEventListener('DOMContentLoaded', () => {
    const botoes = document.querySelectorAll('.seletor-personagem')
    const containerBiografia = document.getElementById('container-biografia')

    botoes.forEach(botao => {
        botao.addEventListener('click', () => {
            const personagemID = botao.dataset.id
            containerBiografia.innerHTML = '<h2>Carregando...</h2><p></p>'

            fetch(`/biografia/${personagemID}`)

            .then(response => {
                if (!response.ok) {
                    throw new Error("A resposta da rede foi bem sucedida.")
                }
                return response.json()
            })

            .then(data => {
                containerBiografia.innerHTML = `
                    <h2>${data.nome}</h2>
                    <p>${data.texto}</p>
                `
            })

            .catch(error => {
                console.log("Erro ao buscar a biografia:", error)
                containerBiografia.innerHTML = '<h2>Ocorreu um erro.</h2><p>Não foi possível carregar os dados. Verifique o console para mais detalhes</p>'
            })

        })
    })
})