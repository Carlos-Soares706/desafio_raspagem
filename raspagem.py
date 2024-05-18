import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
 
inputs_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'inputs'))
xlsx_path = os.path.join(inputs_path, 'challenge.xlsx')

# Aciona o WebDriver no endereço correspondente
driver = webdriver.Chrome()
driver.get("https://www.rpachallenge.com/")

    def download_arquivo():
 #download do arquivo xlsx

        try:
            url = 'https://rpachallenge.com/assets/downloadFiles/challenge.xlsx'
            arquivo = requests.get(url, allow_redirects=True)
            open('challenge.xlsx', 'wb').write(arquivo.content)
            dados = pd.read_excel('challenge.xlsx')
            return dados
        except Exception as error:
            print(f'Erro ao fazer o download do arquivo: {error}')
            raise Exception('Erro ao fazer o download do arquivo')

# Baixa o arquivo Excel
dados_excel = download_arquivo()


def preencher_formulario(dados):
    # Especifique o caminho do arquivo Excel
    # caminho_arquivo = 'caminho/do/seu/arquivo.xlsx' - Comentado pois já estamos baixando o arquivo na função download_arquivo()

    # Pega o número máximo de colunas -1 (nesse caso, 8 - 1 = 7)
    n_cols = dados.shape[1] - 1

    # Mapeia as colunas da planilha para os campos do formulário
    mapping = {0: 'labelFirstName', 1: 'labelLastName', 2: 'labelCompanyName',
               3: 'labelRole', 4: 'labelAddress', 5: 'labelEmail', 6: 'labelPhone'}

    # Aperta o botão de 'Start'
    driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

    # Percorre as linhas da planilha, começando da linha 2 até a linha 11
    for row in dados.iloc[1:12].itertuples(index=False):
        # Percorre as colunas da linha (de 0 a 7 - 1)
        for i in range(n_cols):
            # Verifica se a coluna tem valor
            if getattr(row, dados.columns[i]) is not None:
                # Captura o campo do formulário conforme mapeamento
                input_ = driver.find_element(By.XPATH, '//*[@ng-reflect-name="{}"]'.format(mapping[i]))
                # Envia o valor para o campo
                input_.send_keys(getattr(row, dados.columns[i]))
        # Click no botão 'submit'
        driver.find_element(By.XPATH, '//*[@type="submit"]').click()

# Chama a função para preencher o formulário
preencher_formulario(dados_excel)

# Input para parar o WebDriver
input("Pressione Enter para parar o WebDriver...")

# Fecha o WebDriver
driver.quit()
