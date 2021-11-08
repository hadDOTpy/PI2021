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
                '       <a href="#abrirModal"><img src="http://localhost:5000/get_image/' + pets[i].id + '" class="pet_pic" id="img'+ pets[i].id +'" style= width="200" height="200"></a>' +
                '   </div>' +
                '   <div class="container">' +
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
    $(document).on("click", ".pet_pic", function () {
        var clicado = $(this).attr('id');
        var id_pet = clicado.substring(3); // quantidade de caracteres de "img"


        $.ajax({
            url: 'http://localhost:5000/get_pet/' + id_pet,
            method: 'GET',
            dataType: 'json', // os dados são recebidos no formato json
            success: modal, // chama a função modal para processar o resultado
            error: function () {
                alert("erro ao ler dados, verifique o backend");
            }    
        });
            function modal(pet) {
                // var i = $('img, #img_id').val();
                // alert(i);
                $('#nome_pet').text(pet.nome);
                $('#cast_pet').text(pet.castracao);
                $('#vac_pet').text(pet.vacinas);
                $('#idade_pet').text(pet.idade);
                $('#sexo_pet').text(pet.sexo);
                $('#desc_pet').text(pet.descricao);

                // lin =
                //     '<div id="janela">' +
                //     '   <a href="#fechar" title="Fechar" class="fechar">x</a>' +
                //     '   <div id="esq">' +
                //     '       <img src="imagens/cat.jpg" style= width="200" height="200">' +
                //     '       <div>' +
                //     '           <p style="font-size: 20px; text-align: center; margin-top: 10px;">' + pets[i].nome + '</p>' +
                //     '       </div>' +
                //     '       <div id="infocl">' +
                //     '           <p>Doador: xxxx</p>' +
                //     '           <p>Telefone: xxxxxxxx</p>' +
                //     '           <p>E-mail: xxxxx</p>' +
                //     '           </div>' +
                //     '   </div>' +
                //     '   <div id="dir">' +
                //     '       <p>Sou castrado? ' + pets[i].castracao + '</p>' +
                //     '       <p>Sou vacinado? ' + pets[i].vacinas + '</p>' +
                //     '       <p>Sou do sexo ' + pets[i].sexo + '</p>' +
                //     '       <p>Tenho ' + pets[i].idade + ' aninho(s)</p>' +
                //     '       <p>Sobre mim: ' + pets[i].desc + '</p>' +
                //     '       </div>' +
                //     '</div>' +

                // $('#abrirModal').append(lin);
            }
    });
});
