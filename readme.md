# Whatsapp Exporter

## Esta aplicação faz raspagem de dados no Web Whatsapp, copiando dados de chats específicos, em datas determinadas.

### Para execução, basta seguir o passo a passo abaixo

Tenha o Google Chrome instalado na sua máquina

Baixe e instale o Python para Windows 

https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe

No PowerShell, execute os seguintes comandos

Instale o pipenv

```bash
pip install pipenv --user
```

Entre no shell do pipenv

```bash
python -m pipenv shell
```

Instale as dependências

```bash
python -m pipenv install
```

Com isto, basta executar aplicação

```bash
python main.py
```

O Google Chrome abrirá na página do Web Whatsapp. 

No Whatsapp do celular, navegue até "Aparelhos conectados"  e clique em "Conectar em aparelho". 

Escaneie o QR Code e aguarde a aplicação realizar a cópia dos dados e exportar para o arquivo output.csv.

Uma vez finalizado, verifique o arquivo output.csv na pasta raiz do projeto.
