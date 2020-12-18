# Wishlist APIRest

Nessa API é possível cadastrar, atualizar, visualizar e remover clientes, Produtos e criar uma lista de Produtos favoritos.

## 🚀 Começando

Para rodar essas aplicação é preciso ter o Python 3 e o MySQL instalados 

Consulte **Implantação** para saber como implantar o projeto.

### 📋 Pré-requisitos

Todas as bibliotecas externas do projeto estão no arquivo 
```
requirements.txt.
```

### 🔧 Implantação

1 - Clone o repositorio ou baixe o arquivo .zip.

2 - Crie sua maquina virtual usando o comando: 
```
python3 -m venv venv_project e depois
source venv_project/bin/activate para ativar
```
3 - Para instalar as dependencias usadas rode o comando: 
```
pip install -r requirements.txt
```

4 - É necessario gerar uma *Secret Key* e colar no arquivo *Settings .py* que esta em *Wishlist_api*. Copie a chave gerada e cole em SECRET_KEY na linha 25. Você obterá a secret key rodando o comando:
```
python -c "import secrets; print(secrets.token_urlsafe())"
```
> **Não esqueça que a chave deve estar entre aspas no settings .py.**

5 - No MySQL crie um database e atualize as informações NOME, USER e PASSWORD em DATABASES no settings.py ou se preferir, cole o codigo abaixo em DATABASES e use o *sqlite3* nativo do Django.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

6 - O Comando abaixo irá criar a tabela e as colunas.
```
python manage.py makemigrations && python manage.py migrate
```
7 - Agora crie um *Super User* com o comando:
```
python manage.py createsuperuser OU
python manage.py createsuperuser --email admin@example.com --username admin
 ```
> **Você pode alterar o email e o username se quiser**


8 - Nessa etapa, você pode rodar a aplicação e cadastrar os Clientes e Produtos ou pode usar o *Faker* (pacote que gera dados falsos para você), se optar por ele pode usar esse comando:
```
python populate_script.py
 ```
9 - Por fim, rode a aplicação: 
```
python manage.py runserver
 ```

## 📌 O que você vai encontrar

Uma API criada com o DRF - *Django REST FrameWork*

**HOME**

![image](https://user-images.githubusercontent.com/62224847/102552736-7366e400-40a0-11eb-9982-4aedd243553b.png)


**LOGIN: http://127.0.0.1:8001/api-auth/login/?next=/**


![image](https://user-images.githubusercontent.com/62224847/102552854-a3ae8280-40a0-11eb-9664-0e3456131818.png)


**CLIENTS: http://127.0.0.1:8001/clients/**

![image](https://user-images.githubusercontent.com/62224847/102553017-ebcda500-40a0-11eb-929b-247442e5d62c.png)


**PRODUCTS: http://127.0.0.1:8001/products/**

![image](https://user-images.githubusercontent.com/62224847/102553168-30f1d700-40a1-11eb-99c1-53e47e6adfa0.png)


**FAV_PRODUCTS: http://127.0.0.1:8001/Fav_Products/**

![image](https://user-images.githubusercontent.com/62224847/102553532-c2614900-40a1-11eb-8170-5ab47ffce2dc.png)