# RPA_Challenge
-----
### Este é um projeto simples que demonstra como automatizar o preenchimento de um formulário da web usando Selenium e Pandas em Python. No exemplo fornecido, usamos um site de desafio de automação RPA (Robotic Process Automation) para simular o preenchimento de um formulário.
-----

## Pré-requisitos
-Python 3.x
-Bibliotecas Python: Pandas, Selenium
-Chrome WebDriver (ou WebDriver para o navegador de sua escolha)
-Conexão à internet

-----
## Utilização
Execute o script automacao_formulario.py.
bash
Copy code
python automacao_formulario.py
O script irá abrir o navegador, acessar o site do desafio de automação RPA e preencher o formulário com os dados fornecidos em um arquivo Excel (challenge.xlsx).

O script então submeterá o formulário e repetirá o processo para todas as linhas do arquivo Excel, de acordo com o número de linhas especificado no script.

Após concluir o preenchimento do formulário, o navegador será fechado.
-----
## Personalização
Você pode personalizar o script para se adequar aos seus próprios requisitos, como alterar os campos do formulário, o número de linhas a serem preenchidas, etc.
Certifique-se de ajustar os seletores XPath para corresponder aos elementos do formulário em seu site.
Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue para reportar bugs ou solicitar novos recursos. Se quiser contribuir com código, por favor, abra um pull request.
-----
## Licença
Este projeto está licenciado sob a licença MIT.
