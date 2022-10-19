var ind_imagem = 1;

var opacidade = 1;

var reduzir = true;

var intervalo_mover_id;

var intervalo_opacidade_id;

var intervalo_trocar_id;

function trocar_imagem() {
    let imagem = document.getElementById('imagem');
    ind_imagem++;

    if (ind_imagem > 7)
        ind_imagem = 1

    imagem.src = 'https://softgraf.com/img/img' + ind_imagem + '.jpg';
}

function mudar_opacidade() {
    let imagem = document.getElementById('imagem');

    if (opacidade <= 0.1)
        reduzir = false;

    else if (opacidade >= 1)
        reduzir = true;


    if (reduzir)
        opacidade -= 0.1;
    else
        opacidade += 0.1;

    imagem.style.opacity = opacidade;

}

function mover_imagem() {
    let imagem = document.getElementById('imagem');
    let margem_esq = parseInt(imagem.style.marginLeft); /* NaN -> Not a Number // Número em formato String = converte usando ParseInt */
    let largura_tela = window.innerWidth;
    let largura_imagem = imagem.width;

    if (Number.isNaN(margem_esq))
        margem_esq = 5;
    else
        margem_esq += 5;

    if (margem_esq > largura_tela)
        margem_esq = - largura_imagem;

    imagem.style.marginLeft = margem_esq + 'px';
}

function auto_trocar() {
    intervalo_trocar_id = setInterval('trocar_imagem()', 1000); /*a cada milissegundo*/
}

const auto_mudar = () => {
    intervalo_opacidade_id = setInterval('mudar_opacidade()', 100); 
}

const auto_mover = () => {
    intervalo_mover_id = setInterval('mover_imagem()', 20);
}

document.addEventListener('DOMContentLoaded', () => {

    document.getElementById('bt_limpar').onclick = () => {
        clearInterval(intervalo_mover_id);
        clearInterval(intervalo_opacidade_id);
        clearInterval(intervalo_trocar_id);
    }
})


