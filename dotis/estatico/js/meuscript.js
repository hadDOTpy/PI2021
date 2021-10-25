$(function () { // quando o documento estiver pronto/carregado

    $.ajax({
        url: 'http://localhost:5000/listar_pets',
        method: 'GET',
        dataType: 'json', // os dados são recebidos no formato json
        success: listar, // chama a função listar para processar o resultado
        error: function () {
            alert("erro ao ler dados, verifique o backend");
        }
    });

    function listar(pets) {
        // percorrer a lista de pessoas retornadas; 
        for (var i in pets) { //i vale a posição no vetor

            lin =
                '<div class="polaroid">' +
                '   <div class="pic_block">' +
                '        <img src="http://localhost:5000/get_image/' + pets[i].id + '" class="pet_pic" style= width="200" height="200">' +
                '    </div>' +
                '    <div class="container">' +
                '   <a href="#abrirModal"><p>' + pets[i].nome + '</p></a>' +
                '   </div>' +
                '</div>';

            // adiciona a linha no corpo da tabela
            $('#grid_pet').append(lin);
        }
    }
    // código para mapear click do botão incluir pessoa
    $(document).on("click", "#btnSubmit", function () {
        var svalue = $('input[name=sexo]:checked', '#MyForm').val();
        alert(svalue);
        //pegar dados da tela
        nome = $("#campoNome").val();
        idade = $("#campoIdade").val();
        sexo = $("#campoSexo").val();
        castracao = $("#campoCast").val();
        vacinas = $("#campoVacinas").val();
        desc = $("#campoDesc").val();
        // preparar dados no formato json
        var dados = JSON.stringify({ nome: nome, idade: idade, sexo: svalue, castracao : castracao, vacinas: vacinas, desc: desc });
        // var dados = JSON.stringify({ nome: nome, idade: idade, desc: desc });
        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/inserir_pets',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: petInserido, // chama a função listar para processar o resultado
            error: erroAoInserir
        });
        function petInserido(retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Pet incluído com sucesso!");
                // limpar os campos
                $("#campoNome").val("");
                $("#campoIdade").val("");
                $("#campoSexo").val("");
                $("#campoCast").val("");
                $("#campoVacinas").val("");
                $("#campoDesc").val("");
            } else {
                // informar mensagem de erro
                alert(retorno.resultado + ":" + retorno.detalhes);
            }
        }
        function erroAoInserir(retorno) {
            // informar mensagem de erro
            alert("ERRO: " + retorno.resultado + ":" + retorno.detalhes);
        }
    });

});
