from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# para rodar o chrome em 2º plano
# from selenium.webdriver.chrome.options import Options
# chrome_options = Options()
# chrome_options.headless = True # also works
# nav = webdriver.Chrome(options=chrome_options)

nav = webdriver.Chrome()

# Acessar EDI Banrsiul com login e senha;
nav.get("https://edi.banrisul.com.br/home.do#login")
time.sleep(5)
nav.find_element(By.NAME, 'userName').send_keys("PERINI")
time.sleep(5)
nav.find_element(By.NAME,'password').send_keys("Per@142536")
nav.find_element(By.NAME, 'password').send_keys(Keys.ENTER)
time.sleep(5)
nav.find_element(By.XPATH, '//*[@eventproxy="TabDownload"]/table/tbody/tr/td').click()

time.sleep(5)
while True:
    try:
        l = len(nav.find_elements(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div/div[3]/div[3]/div/table/tbody/tr'))
    except:
        l = 0


    if l > 1:
        nav.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[1]/td[4]').click()
        time.sleep(5)
        if nav.find_element(By.XPATH, '//*[@eventproxy="isc_IButton_9"]').text == "OK":
            nav.find_element(By.XPATH, '//*[@eventproxy="isc_IButton_9"]').click()
        else:
            nav.find_element(By.XPATH, '//*[@eventproxy="isc_IButton_10"]').click()

        time.sleep(5)
    else:
        break
time.sleep(60)
#//*[@id="isc_K5table"]/tbody/tr[1]/td[4]
#/html/body/div[2]/div[3]/div/div/div[3]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[1]/td[4]
#/html/body/div[3]/div[3]/div/div/div[3]/div[2]/div/div[3]/div[3]/div/table/tbody/tr[1]/td[2]

#//*[@eventproxy="isc_ListGrid_10_body"]/tbody/tr[1]/td[2]

# #Acessar Base de Dados Excel
# df = pd.read_excel("C:/Consulta_Processos/BaseDados.xlsx",dtype={'CNPJ': str})
# i = 0
# index = df.index
# linhas = len(index)
# while(i!=linhas):
#
#     cnpj = df.at[i,'CNPJ']
#
#
#     # Acessar pagina de consulta
#     nav.find_element_by_xpath('//*[@id="navbar"]/div/div[3]/div[1]/a/i').click()
#     time.sleep(1)
#     nav.find_element_by_xpath('//*[@id="main-menu"]/li[3]/a').send_keys(Keys.ENTER)
#     time.sleep(3)
#     nav.find_element_by_xpath('//*[@id="menu-ul-3"]/li[1]/a').click()
#
#     # Colando o CNPJ e Marcando exibir baixados
#     nav.find_element_by_xpath('//*[@id="divStrDocParte"]/dl/dd/input').send_keys(str(cnpj))
#     nav.find_element_by_xpath('//*[@id="divChkExibirBaixados"]/dl/dd/input').click()
#     nav.find_element_by_xpath('//*[@id="divClasseProcessual"]/dl/dd/div/button').click()
#     time.sleep(3)
#     nav.find_element_by_xpath('//*[@id="divClasseProcessual"]/dl/dd/div/div/ul/li[1]/label/input').click()
#
#     nav.find_element_by_xpath('//*[@id="sbmConsultar"]').click()
#
#     #Retornar dados da consulta para o Excel
#     time.sleep(3)
#     #try if, se caso Retorno der erro usar except:
#     try:
#         Retorno = nav.find_element_by_xpath('//*[@id="divInfraExcecao"]/span').get_attribute('class')
#         if Retorno == 'infraExcecao':
#             df.loc[df['CNPJ'] == cnpj , 'PROCESSOS' ] = str ("Nenhum Resultado Encontrado")
#         else:
#             df.loc[df['CNPJ'] == cnpj , 'PROCESSOS' ] = str ("Processo localizado")
#     except:
#         df.loc[df['CNPJ'] == cnpj , 'PROCESSOS' ] = str ("Processo localizado")
#     #Proximo CNPJ Excel
#
#     i = i+1
#
#
# df.to_excel("C:/Consulta_Processos/BaseDados Atualizada.xlsx", index=False)
nav.quit()
