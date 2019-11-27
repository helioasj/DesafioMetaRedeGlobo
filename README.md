# DesafioMetaRedeGlobo
Desafio teste para selecao da Consultoria Meta

Este Desafio esta dividido em 3 partes:
  -Desafio Logica de Programacao
  -Desafio Integracao
  -Desafio Web API

1) Desafio Logica de Programacao

Na pasta 'Desafio de Logica', existem os seguintes arquivos para cada questao proposta, sendo:
Questao 01 = Arquivo questao01.py
Questao 02 = Arquivo questao02.py
Questao 03 = Arquivo questao03.py
Questao 04 = Arquivo questao04.py

2) Desafio Integracao

Na pasta 'ACME SOLUCAO', existem os arquivos referente ao teste de Integracao.

Pastas:
  -ACMEPLAY-API
  -CORTE-API
  -Integracao
  
  O core deste desafio encontra-se na pasta 'Integracao', onde encontrar-se-ao os seguintes diretorios/arquivos:
  # Integracao
  
  -app (Preparado para guardar arquivos de configuracao)
  -Arquivos Originais Desafio (Arquivos originais enviados no teste)
  -arquivostxts_monitorada (Pasta que sera monitorada pelo processo descrito no desafio)
  -database (Banco de Dados sqlite3, repositorio usado neste desenvolvimento.
  
  # CORTE-API
  
  -corte_api (Api composta para simular os cortes dos videos)
  -videos (Pasta contendo os arquivos simulados de videos, sendo as pastas(originais e cortados))
  
  # ACMEPLAY-API
  
  -acmeplay_api(Apli composta para simular a API descrita no desafio)
  
  # COMO COLOCAR PRA FUNCIONAR?
  
  1) Primeiramente, devemos subir os servicos das API`s.
  
  1.1) Subindo API de Corte
  Posicionar-se no diretorio ../CORTE-API/corte_api
  Executar o comando: python3 manage.py runserver
  
  1.2) Subindo API ACME-Play
  Posicionar-se no diretorio ../AMCEPLAY-API/acmeplay_api
  Executar o comando: python3 manage.py runserver 127.0.0.1:8001 (IMPORTANTE DEVIDO A PORTA JA UTILIZADA)
  
  2) Iniciar os processos de monitoramento/consulta de Status(GET)/ Copia do Video para outro diretorio
  
  2.1) Iniciando o Monitoramento da Pasta
  Posicionar-se no diretorio ../Integracao/
  Executar o comando: python3 readDirectory3.py arquivostxts_monitorada
  
  2.2) Iniciando o processo de consulta a cada X tempo(1 minuto) do status do Processo de Corte
  Posicionar-se no diretorio ../Integracao/
  Executar o comando: python3 refreshStatus.py 
  
  2.3) Iniciando o processo de ENTREGA DO CONTEUDO, que copia o video(arquivo txt simulando o video) para outro diretorio e faz um POST para a API AMCEPLAY.
  Posicionar-se no diretorio ../Integracao/
  Executar o comando: python3 cortaVideos.py 

  # COMO SERA A EXECUCAO
  1) A pasta 'arquivostxts_monitorada' sera monitorada e cada vez que for depositado um arquivo txt, ele sera lido, respeitando as regras do desafio, onde:
    - A leitura ocorrera sempre a partir da ultima linha lida
    - As informacoes serao gravadas no banco de dados acme.db3(sqlite3), localizado no diretorio 'Integracao/database'.
    - O nome da tabela do banco de dados que guardara essas informacoes chama-se 'leituratxt'.
    - Nesta tabela tambem ja sao gravados os dados do ID do Job de corte, Mensagem de retorno do POST. 
    
  2) No momento da leitura, para todos os videos que tiveram mais de 30 minutos de duracao, sera enviado um POST para a API DE CORTE(CORTE-API). 
    - Os dados desta API sao gravados no banco de dados db.sqlite3(sqlite3), localizado no diretorio '../CORTE-API/corte_api'
    - O nome da tabela do banco de dados que guardara essas informacoes chama-se 'corteapp_videos'
    - Cada POST realizado, o corte do video ja fica com status(em relacao ao processo de corte) 'PENDENTE'.
    
  3) A cada 1 minuto, o processo de GET e realizado, obtendo o status do processo de corte e guardando esta informacao na coluna 'status_corte' da tabela 'leituratxt'.
  
  4) A cada 1 minuto, o processo de corte de videos e 'startado', onde localiza o video atraves do campo RECONCILE_KEY, e o copia para a pasta '../CORTE-API/videos/cortados'
    - Apos a executao deste processo, o status do processo, pendente na tabela corteapp_videos e atualizado.
   

  
