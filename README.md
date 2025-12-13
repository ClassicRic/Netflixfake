---

# 🎬 Netflix Fake

Este projeto é uma **aplicação web inspirada na Netflix**, desenvolvida com **Django**, com o objetivo de praticar conceitos de **desenvolvimento backend, integração com banco de dados, armazenamento externo de mídias e deploy em produção**.

A aplicação simula uma plataforma de streaming, permitindo o gerenciamento de filmes via painel administrativo e a exibição do catálogo para os usuários.

---

## 🧠 Objetivo do Projeto

Criar uma aplicação web completa, do backend ao deploy, simulando uma plataforma de streaming, utilizando tecnologias modernas e boas práticas de desenvolvimento com Python e Django.

---

## ⚙️ Funcionalidades

* Aplicação web desenvolvida com **Django**;
* Cadastro e gerenciamento de filmes via **Django Admin**;
* Armazenamento dos arquivos de mídia (filmes/imagens) no **Supabase**;
* Integração do sistema com links externos de mídia armazenados no Supabase;
* Banco de dados **PostgreSQL** para persistência das informações;
* Deploy da aplicação em ambiente de produção utilizando **Railway**;
* Separação entre ambiente de desenvolvimento e produção.

---

## 🧩 Estrutura do Projeto

```
netflix-fake/
│
├── netflixfake/            # Configurações principais do projeto Django
├── filmes/                 # App responsável pelo catálogo de filmes
├── templates/              # Templates HTML da aplicação
├── static/                 # Arquivos estáticos (CSS, JS, imagens)
├── manage.py               # Arquivo principal de gerenciamento do Django
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação do projeto
```

---

## 🐍 Requisitos

* **Python 3.13.3**
* **Django**
* **PostgreSQL**
* Dependências listadas no arquivo `requirements.txt`

Para instalar as dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório**

```bash
git clone https://github.com/ClassicRic/netflix-fake.git
cd netflix-fake
```

2. **Crie e ative um ambiente virtual**

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. **Instale as dependências**

```bash
pip install -r requirements.txt
```

4. **Configure as variáveis de ambiente**

Configure as credenciais do banco PostgreSQL e demais variáveis sensíveis (`SECRET_KEY`, `DATABASE_URL`, etc.).

5. **Execute as migrações**

```bash
python manage.py migrate
```

6. **Crie um superusuário**

```bash
python manage.py createsuperuser
```

7. **Inicie o servidor**

```bash
python manage.py runserver
```

---

## 🗄️ Banco de Dados

O projeto utiliza **PostgreSQL** como banco de dados principal em produção (Railway).

---

## ☁️ Armazenamento de Mídia (Supabase)

Os filmes e/ou imagens não são armazenados diretamente no servidor da aplicação.
Eles são hospedados no **Supabase**, e o **link público do arquivo** é inserido no painel administrativo do Django (Netflix Fake), permitindo:

* Melhor performance;
* Separação entre aplicação e mídia;
* Facilidade de escalabilidade.

---

## 🌐 Deploy

O deploy da aplicação foi realizado utilizando a plataforma **Railway**, com:

* Backend Django em produção;
* Banco de dados PostgreSQL integrado;
* Variáveis de ambiente configuradas diretamente na plataforma.

---

## 🏁 Resultado Esperado

Ao final da execução e deploy:

* A aplicação funciona como uma plataforma de streaming;
* Os filmes são gerenciados pelo painel administrativo;
* O catálogo é exibido dinamicamente para os usuários;
* A aplicação está acessível publicamente via Railway.



Projeto desenvolvido durante o curso da hashtag programacao e aprimorado por mim.
🔗 https://netflixfake-production.up.railway.app/

---

