Análise da API de Amigo Oculto

Orientação a Abstrações:
A orientação a abstrações não foi implementada. O projeto não utiliza classes abstratas ou contratos claros entre camadas. Essa funcionalidade será introduzida no futuro pois (o Thiago) preciso estudar mais sobre isso.

Injeção de Dependência:
A injeção de dependências também não foi implementada. Atualmente, as dependências são instanciadas diretamente dentro dos métodos e controladores. 

Persistência em Banco:
Foi utilizada a biblioteca SQLAlchemy para a persistência dos dados e o Flask-Migrate para o versionamento do banco. 

Separação de Preocupações:
A separação de responsabilidades foi aplicada de forma modular, com a organização do projeto dividida em pastas como controllers, services, repositories, models, schemas e exceptions. Esse padrão ajuda a manter o código organizado e facilita a manutenção. No entanto, as validações foram centralizadas em utils (possui uma validação), o que pode ser ajustado para aproveitar ainda mais as funcionalidades dos schemas do Marshmallow. 

Uso de Framework:
O Flask foi utilizado como framework principal com a linguagem Python.

Hierarquia de Exceptions:
Foi implementada uma hierarquia básica de exceptions, cobrindo casos simples como erros de validação e autorização. Contudo, o tratamento de erros poderia ser expandido com a inclusão de mais cenários e um manipulador global para padronizar as respostas de erro.

Validação de Dados:
A validação de dados é parcialmente implementada. O Marshmallow foi utilizado para validar e serializar os dados das requisições. Apesar disso, faltam validações contextuais mais robustas, como verificar a unicidade (palavra bonita) de campos ou checar relações entre diferentes entidades.

Autenticação:
A autenticação foi implementada usando JWT, com geração de access_token e refresh_token. Contudo, não foi configurado o tempo de expiração dos tokens e não há um mecanismo para revogar tokens, como um logout.

Autorização:
A autorização foi parcialmente implementada. Algumas rotas estão protegidas com @jwt_required, mas não há verificações detalhadas para garantir que os usuários acessem apenas seus próprios dados.

Pontos Fortes:
A estrutura do projeto é modular e bem organizada, seguindo boas práticas como o padrão Service-Repository-Controller.

O uso do SQLAlchemy e Flask-Migrate garante uma boa gestão da persistência de dados e versionamento do banco.

O Marshmallow foi integrado para validações e serialização.

A autenticação com JWT é funcional e cobre a maior parte das necessidades básicas de segurança.

Pontos de Melhoria

1. Expansão da Hierarquia de Exceptions: Adicionar novas exceptions para cobrir mais cenários e padronizar as respostas de erro com um manipulador global.

2. Autorização detalhada: Implementar verificações para garantir que cada usuário acesse apenas os dados que lhes pertencem ou recursos para os quais tenham permissão.

3. Rotação e Expiração de Tokens: Configurar o tempo de expiração de tokens (access_token e refresh_token) e considerar a implementação de uma rotação segura de tokens.

4. Injeção de Dependência: Adicionar injeção explícita de dependências para melhorar a modularidade para facilitar até mesmo os testes unitários.

5. Validação Contextual: Melhorar as validações adicionando regras específicas, como verificar a exclusividade dos campos e consistência dos dados com o estado atual do banco.

6. Automatização de Testes: Implementar testes automatizados para endpoints e lógica de negócio.

