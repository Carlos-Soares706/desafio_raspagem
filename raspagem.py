import pandas as pd
 
from selenium import webdriver
from selenium.webdriver.common.by import By
 

# Aciona o WebDriver no endereço correspondente
driver = webdriver.Chrome()
driver.get("https://www.rpachallenge.com/")



# Especifique o caminho do arquivo Excel
caminho_arquivo = 'caminho/do/seu/arquivo.xlsx'


dados_excel = pd.read_excel(caminho_arquivo)


# Pega o número máximo de colunas -1 (nesse caso, 8 - 1 = 7)
n_cols = sheet.max_column - 1
 
# Mapeia as colunas da planilha para os campos do formulário
mapping = {0: 'labelFirstName', 1: 'labelLastName', 2: 'labelCompanyName',
        3: 'labelRole', 4: 'labelAddress', 5: 'labelEmail', 6: 'labelPhone'}
 
# Aperta o botão de 'Start'
driver.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()
 
# Percorre as linhas da planilha, começando da linha 2 até a linha 11
for row in sheet.iter_rows(min_row=2, max_row=11, values_only=True):
    # Percorre as colunas da linha (de 0 a 7 - 1)
    for i in range(n_cols):
        # Verifica se a coluna tem valor
        if row[i] is not None:
            # Captura o campo do formulário conforme mapeamento
            input_ = driver.find_element(By.XPATH, '//*[@ng-reflect-name="{}"]'.format(mapping[i]))
            # Envia o valor para o campo
            input_.send_keys(row[i])
    # Click no botão 'submit'
    driver.find_element(By.XPATH, '//*[@type="submit"]').click()
 
# Input para parar o WebDriver
input("Pressione Enter para parar o WebDriver...")
 
# Fecha o WebDriver
driver.quit()
