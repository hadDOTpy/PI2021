$(document ).ready(function() { // quando o documento estiver pronto/carregado

 
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
                '        <img src="../back-end/img_pet/' + pets[i].foto + ' " class="pet_pic" style= width="200" height="200">' +
                '    </div>' +
                '    <div class="container">' +
                '   <p>' + pets[i].nome + '</p>' +
                '   </div>' +
                '</div>';

            // adiciona a linha no corpo da tabela
            $('#grid_pet').append(lin);
        }
    }
 

    // código para mapear click do botão incluir pet
    $(document).on("click", "#btnSubmit", function () {

        var form_data = new FormData($('#MyForm')[0]);
        $.ajax({
            url: 'http://localhost:5000/uploadajax',
            type: 'POST',
            data: form_data,
            contentType: false,
            cache: false,
            processData: false,
            success: function(data) {
                console.log('Success!');
                alert("enviou a foto direitinho!");
            },
            error: function(data) {
                alert("deu ruim na foto");
            }
        });

        var svalue = $('input[name=sexo]:checked', '#MyForm').val();
        var cvalue = $('input[name=castracao]:checked', '#MyForm').val();
        var vvalue = $('input[name=vacinas]:checked', '#MyForm').val();

        //pegar dados da tela
        foto = $("#arquivo").val().split('\\').pop();
        nome = $("#campoNome").val();
        idade = $("#campoIdade").val();
        sexo = $("#campoSexo").val();
        castracao = $("#campoCast").val();
        vacinas = $("#campoVacinas").val();
        desc = $("#campoDesc").val();

        // preparar dados no formato json
        var dados = JSON.stringify({ foto: foto, nome: nome, idade: idade, sexo: svalue, castracao: cvalue, vacinas: vvalue, desc: desc });
        
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
                $("#arquivo").val("");
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

    // código para mapear click do botão incluir usuário
    $(document).on("click", "#btnSubmit", function () {

        nome = $("#campoNome").val();
        email = $("#campoEmail").val();
        estado = $("#campoUF").val();
        cidade = $("#campoCdd").val();
        fone = $("#campoTel").val();

        var dados = JSON.stringify({ nome: nome, email: email, estado: estado, cidade: cidade, fone: fone });

        // fazer requisição para o back-end
        $.ajax({
            url: 'http://localhost:5000/inserir_user',
            type: 'POST',
            dataType: 'json', // os dados são recebidos no formato json
            contentType: 'application/json', // tipo dos dados enviados
            data: dados, // estes são os dados enviados
            success: userInserido, // chama a função listar para processar o resultado
            error: erroAoInserir
        });

        function userInserido(retorno) {
            if (retorno.resultado == "ok") { // a operação deu certo?
                // informar resultado de sucesso
                alert("Usuário incluído com sucesso!");
                // limpar os campos
                $("#campoNome").val("");
                $("#campoEmail").val("");
                $("#campoUF").val("");
                $("#campoCdd").val("");
                $("#campoTel").val("");
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
