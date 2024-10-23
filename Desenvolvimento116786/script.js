// Crie um projeto com dois arquivos: index.html e script.js. 
// No arquivo 'index' insira a estrutura base HTML e dentro da tag 'body' incluindo quatro tags vazias: h1, ul, a, ol. 
// Adicione o atributo id="titulo" à tag h1, o atributo href="https://prozeducacao.com.br" à tag 'a', e o atributo id="lista-ordenada" à tag 'ol'. 
// Na sequência, realize a conexão entre o arquivo HTML e o arquivo JavaScript.

// Nenhum arquivo script.js captura os quatro elementos criados, e usa a propriedade .innerText para adicionar conteúdo textual aos elementos 'h1' e 'a', e a propriedade .innerHTML para adicionar três itens simples na lista não ordenada, e três itens com links para outros sites na lista ordenada.

let conteudoH1 = document.getElementById("titulo"), conteudoA = document.querySelector("body a");
let conteudoOl = document.getElementById("lista-ordenada"), conteudoUl = document.querySelector("ul");
conteudoH1.innerText = "Desenvolvimento #116786"
console.log(conteudoH1);

let conteudos = [
    {
        item: "conteudo 1",
        link: "www.google.com"
    },
    {
        item: "conteudo 2",
        link: "www.facebook.com"
    },
    {
        item: "conteudo 3",
        link: "www.linkedin.com"
    }

]

conteudoA.innerText = "Clique aqui"
console.log(conteudoA);

conteudoUl.innerHTML = 
`<li>${conteudos[0].item}</li>
<li>${conteudos[1].item}</li>
<li>${conteudos[2].item}</li>`

conteudoOl.innerHTML = `
<a href="https://${conteudos[0].link}">${conteudos[0].link}</a> <br>
<a href="https://${conteudos[1].link}">${conteudos[1].link}</a> <br>
<a href="https://${conteudos[2].link}">${conteudos[2].link}</a>`