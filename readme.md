# Whatsapp Exporter

## Esta aplicação faz raspagem de dados no Web Whatsapp, copiando dados de chats específicos, em datas determinadas.

### Para execução, basta seguir o passo a passo abaixo

Tenha o Google Chrome instalado na sua máquina

Instale o pipenv

```bash
pip install pipenv --user
```

Entre no shell do pipenv

```bash
pipenv shell
```

Instale as dependências

```bash
pipenv install
```

Com isto, basta executar aplicação

```bash
python main.py
```

O Google Chrome abrirá na página do Web Whatsapp. 

No Whatsapp do celular, navegue até "Aparelhos conectados"  e clique em "Conectar em aparelho". 

Escaneie o QR Code e aguarde a aplicação realizar a cópia dos dados e exportar para o arquivo output.csv.

Uma vez finalizado, verifique o arquivo output.csv na pasta raiz do projeto.
