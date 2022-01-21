from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def quantidade_de_digitos():
    if len(cpf) > 11 or len(cpf) < 11:
        return False
    else:
        return True

def numerar_CPF():
    for a in cpf:
        a = int(a)
        cpf_numerado.append(a)

def validar_1_digito():
    if len(cpf_numerado) > 11 or len(cpf_numerado) < 11:
        return False
    else:
        acumular  = 0
        resultado = 0
        controle = 10
        for numeros in cpf_numerado[0:9]:
            resultado = numeros * controle
            acumular += resultado
            controle -= 1
        acumular = acumular * 10 % 11
        if acumular == 10:
            acumular = 0
        if acumular == cpf_numerado[9]:
            return True
        else:
            return False

def validar_2_digito():
    if len(cpf_numerado) > 11 or len(cpf_numerado) < 11:
        return False
    else:
        acumular2  = 0
        resultado2 = 0
        controle2 = 11
        for numeros2 in cpf_numerado[0:10]:
            resultado2 = numeros2 * controle2
            acumular2 += resultado2
            controle2 -= 1
        acumular2 = acumular2 * 10 % 11
        if acumular2 == 10:
            acumular2 = 0
        if acumular2 == cpf_numerado[10]:
            return True
        else:
            return False

def validar_nome():
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.get('https://www.situacao-cadastral.com/')
    sleep(2)
    pesquisa = driver.find_element(By.XPATH, '//*[@id="doc"]')
    pesquisa.send_keys(cpf)
    pesquisa.send_keys(Keys.ENTER)
    sleep(2)
    portador = driver.find_element(By.XPATH, '//*[@id="resultado"]/span[2]').text
    portador = portador.upper()
    portador = portador.split()
    ultimonome = len(portador)
    ultimonomedigitado = len(nome)
    if nome[0] == portador[0] and nome[ultimonomedigitado - 1] == portador[ultimonome - 1]:
        print('Analise feita com sucesso tanto o cpf quanto o portador estao corretos.')
    else:
        print('Falha portador do cpf nao encontrado. O nome pode esta incorreto ou o cpf pertence a outra pessoa')

cpf_numerado = []
cpf = input('Digite o CPF:').replace('.', '').replace('-', '')
nome = input('Nome completo:')
nome = nome.upper()
nome = nome.split()

quantidade_de_digitos()

numerar_CPF()

validar_1_digito()

validar_2_digito()

if quantidade_de_digitos() == True and validar_1_digito() == True and validar_2_digito() == True:
    print('CPF VALIDO. Iniciando validade de portador')
    validar_nome()

else:
    print('CPF INVALIDO')