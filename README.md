# Análise da API de Amigo Oculto

Este documento apresenta uma análise técnica sobre a implementação da API de Amigo Oculto. A seguir, são discutidos os principais pontos fortes e de melhoria, além de aspectos da arquitetura e implementação.

## Orientação a Abstrações

A orientação a abstrações não foi implementada. O projeto não utiliza classes abstratas ou contratos claros entre as camadas. Essa funcionalidade será introduzida no futuro, após um estudo mais aprofundado sobre o conceito. 

## Injeção de Dependência

A injeção de dependências ainda não foi implementada. Atualmente, as dependências são instanciadas diretamente dentro dos métodos e controladores. A implementação dessa prática visa melhorar a modularidade e facilitar o desenvolvimento e a realização de testes unitários.

## Persistência em Banco

A biblioteca **SQLAlchemy** foi utilizada para a persistência dos dados, juntamente com o **Flask-Migrate** para o versionamento do banco de dados. Esses componentes garantem uma boa gestão da persistência e a capacidade de realizar migrações de forma simples e eficiente.

## Separação de Preocupações

A separação de responsabilidades foi aplicada de forma modular, com a organização do projeto dividida em pastas como **controllers**, **services**, **repositories**, **models**, **schemas** e **exceptions**. Esse padrão ajuda a manter o código organizado e facilita a manutenção. No entanto, as validações estão centralizadas em **utils** (possui uma validação), o que pode ser ajustado para aproveitar melhor as funcionalidades dos schemas do Marshmallow.

## Uso de Framework

O projeto foi desenvolvido utilizando o **Flask** como framework principal, com a linguagem **Python**.

## Hierarquia de Exceptions

Foi implementada uma hierarquia básica de exceptions, cobrindo casos simples como erros de validação e autorização. No entanto, o tratamento de erros poderia ser expandido com a inclusão de mais cenários e um manipulador global para padronizar as respostas de erro.

## Validação de Dados

A validação de dados é parcialmente implementada. **Marshmallow** foi utilizado para validar e serializar os dados das requisições. Contudo, faltam validações mais robustas, como verificação de unicidade de campos e validação de relações entre diferentes entidades.

## Autenticação

A autenticação foi implementada utilizando **JWT** (JSON Web Tokens), com geração de **access_token** e **refresh_token**. Porém, não foi configurado o tempo de expiração dos tokens e não há um mecanismo para revogação de tokens, como um processo de logout.

## Autorização

A autorização foi implementada parcialmente. Algumas rotas estão protegidas com o decorador **@jwt_required**, mas ainda faltam verificações detalhadas para garantir que os usuários acessem apenas os dados que lhes pertencem.

---

## Pontos Fortes

- A estrutura do projeto é modular e bem organizada, seguindo boas práticas como o padrão **Service-Repository-Controller**.
- O uso de **SQLAlchemy** e **Flask-Migrate** garante uma boa gestão da persistência de dados e versionamento do banco.
- A integração do **Marshmallow** facilita as validações e a serialização de dados.
- A autenticação com **JWT** é funcional e cobre as necessidades básicas de segurança.

---

## Pontos de Melhoria

1. **Expansão da Hierarquia de Exceptions**: 
   - Adicionar novas exceptions para cobrir mais cenários e padronizar as respostas de erro com um manipulador global.
   
2. **Autorização Detalhada**:
   - Implementar verificações para garantir que cada usuário acesse apenas os dados que lhes pertencem ou recursos para os quais tenham permissão.
   
3. **Rotação e Expiração de Tokens**:
   - Configurar o tempo de expiração dos tokens (**access_token** e **refresh_token**) e considerar a implementação de uma rotação segura de tokens.

4. **Injeção de Dependência**:
   - Implementar a injeção explícita de dependências para melhorar a modularidade, o que facilitará tanto a manutenção quanto os testes unitários.

5. **Validação Contextual**:
   - Melhorar as validações, adicionando regras específicas, como verificar a exclusividade de campos e a consistência dos dados com o estado atual do banco de dados.

6. **Automatização de Testes**:
   - Implementar testes automatizados para os endpoints e a lógica de negócios, garantindo maior cobertura e robustez no código.

---
