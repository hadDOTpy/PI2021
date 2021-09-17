$(function() { // quando o documento estiver pronto/carregado
    
    $.ajax({
        url: 'http://localhost:5000/listar_pets',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function() {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar (pets) {
        // percorrer a lista de pessoas retornadas; 
        for (var i in pets) { //i vale a posição no vetor

            lin = 
            '<div class="polaroid">'+
            '   <div class="pic_block">'+
            '        <img src="../imagens/cat.jpg" class="pet_pic" style= width="200" height="200">'+
            '    </div>'+
            '    <div class="container">'+
            '   <p>' + pets[i].nome + '</p>'+
            '   </div>'+
            '</div>';

            // adiciona a linha no corpo da tabela
            $('#grid_pet').append(lin);
        }
    }

});