Comando para rodar servidor em Flask


python3 -m flask --app {nome do arquivo} run

python3 -m flask --app {nome do arquivo}  run --port 8000.

Abre o um host para toda a rede:
python3 -m flask --app ola-flask run --host 0.0.0.0

Decorador é um padrão de projeto de software que permite adicionar um comportamento a um objeto já existente em tempo de execução, ou seja, agrega dinamicamente responsabilidades adicionais a um objeto. Isso significa que você pode adicionar métodos a um objeto sem ter que modificar sua classe.

Uma API Web, ou API RESTful, é um conjunto de definições e protocolos que permitem a comunicação entre diferentes sistemas através da web. Ela funciona como um intermediário, possibilitando que um sistema (cliente) solicite dados ou execute ações em outro sistema (servidor) de forma padronizada e segura.

Uma aplicação pode possuir rotas de API e rotas de aplicação web. As rotas de API são utilizadas para fornecer dados e funcionalidades para outros sistemas, enquanto as rotas de aplicação web são utilizadas para fornecer uma interface interativa para o usuário.

No flask temos os "templates" que são arquivos HTML que são renderizados pelo servidor e enviados para o cliente. Eles são utilizados para criar a interface do usuário.

O Flask utiliza o Jinja2 como mecanismo de renderização de templates. O Jinja2 é um mecanismo de template que permite gerar HTML dinamicamente, permitindo a inclusão de variáveis, estruturas de controle e macros.

Nos arquivos HTML, o código que está entre {{ e }} é um código Python que é executado pelo Flask. Esse código é utilizado para passar informações da aplicação para a página. O código {{ nome }} é utilizado para exibir o valor da variável nome na página. O Flask substitui o código {{ nome }} pelo valor da variável nome antes de enviar a página para o navegador. Esse tipo de código é chamado de template tag e é utilizado para criar páginas dinâmicas com o Flask. Quem quiser saber mais sobre template tags, acesse aqui. A biblioteca utilizada para isso é a Jinja2, que é uma biblioteca de template para Python. Para conhecer mais sobre a Jinja2, acesse aqui.

À medida que sua aplicação Flask cresce, fica difícil manter todo o código (rotas, templates, funções de visualização, etc.) em um único arquivo. Blueprints permitem dividir a aplicação em seções menores e mais gerenciáveis. Imagine-os como plantas (blueprints) de diferentes cômodos em uma casa. Os blueprints podem ser facilmente reutilizados em outras aplicações. Se você desenvolve um módulo para gerenciar usuários, por exemplo, pode embalá-lo em um Blueprint e reutilizá-lo em diferentes projetos.Eles permitem dividir o código em Blueprints torna a aplicação mais escalável. Equipes diferentes podem trabalhar em diferentes Blueprints de forma mais independente.

### Deploy

´´´
pip install gunicorn

´´´

Lixux:
gunicorn projeto-web.app:app

Windows:
waitress-serve --listen=*:8000 myapp.wsgi:application
