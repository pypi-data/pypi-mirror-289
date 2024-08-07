import asyncio
import warnings
import time
from datetime import datetime
import pyperclip
import re

import pyautogui
from rich.console import Console
from pywinauto.application import Application

from worker_automate_hub.api.client import get_config_by_name
from worker_automate_hub.utils.logger import logger
from worker_automate_hub.utils.util import (
    api_simplifica,
    find_element_center,
    find_target_position,
    kill_process,
    login_emsys,
    take_sreenshot,
    take_target_position,
    type_text_into_field,
)

console = Console()

ASSETS_BASE_PATH = 'assets/descartes_transferencias_images/'
ALMOXARIFADO_DEFAULT = "50"

async def transferencias(task):
    try:
        #Inicializa variaveis
        pre_venda_message = None
        nota_fiscal = None
        observacao = None
        valor_nota = None
        #Get config from BOF
        config = await get_config_by_name("Descartes_Emsys")
        console.print(task)
        itens = task['configEntrada']['itens']

        #Abre um novo emsys
        await kill_process("EMSys")
        app = Application(backend='win32').start("C:\\Rezende\\EMSys3\\EMSys3.exe")
        warnings.filterwarnings("ignore", category=UserWarning, message="32-bit application should be automated using 32-bit Python")
        console.print("\nEMSys iniciando...", style="bold green")
        return_login = await login_emsys(config['conConfiguracao'], app, task)
        
        if return_login['sucesso'] == True:
            type_text_into_field('Cadastro Pré Venda', app['TFrmMenuPrincipal']['Edit'], True, '50')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('enter')
            console.print(f"\nPesquisa: 'Cadastro Pre Venda' realizada com sucesso", style="bold green")
        else:
            logger.info(f"\nError Message: {return_login["retorno"]}")
            console.print(f"\nError Message: {return_login["retorno"]}", style="bold red")
            return return_login

        time.sleep(7)

        #Preenche data de validade

        # field_validade = await find_element_center(ASSETS_BASE_PATH + "field_validade.png", (881, 292, 143, 57), 10)
        # if field_validade is not None:
        #     pyautogui.click(field_validade.x, field_validade.y)
        #     pyautogui.write(f'{datetime.now().strftime("%d/%m/%Y")}', interval=0.1)
        #     pyautogui.press('tab')
        #     console.print(f"\nValidade Digitada: '{datetime.now().strftime("%d/%m/%Y")}'", style="bold green")
        #     time.sleep(1)
        # else:
        #     observacao = f"\nCampo 'Validade' não encontrado"
        #     logger.info(f'{observacao}')
        #     console.print(f"{observacao}", style="bold red")
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
        #     return {"sucesso": False, "retorno": observacao}

        
        #Condição da Pré-Venda
        condicao_field = find_target_position(screenshot_path, "Condição", 10, 0, 15) 
        if condicao_field == None:
            return {"sucesso": False, "retorno": f"Não foi possivel encontrar o campo de condição"}
        pyautogui.click(condicao_field)
        time.sleep(1)
        pyautogui.write("T")
        time.sleep(1)
        screenshot_path = take_sreenshot()
        a_vista_option_position = find_target_position(screenshot_path, "Vista", attempts=15)
        if a_vista_option_position == None:
            return {"sucesso": False, "retorno": f"Não foi possivel encontrar a opção A Vista"}
        
        pyautogui.click(a_vista_option_position)


        #Preenche o campo do cliente com o número da filial

        # cliente_field = await find_element_center(ASSETS_BASE_PATH + "field_cliente.png", (795, 354, 128, 50), 10)
        # if cliente_field is not None:
        #     pyautogui.click(cliente_field.x, cliente_field.y)
        #     pyautogui.hotkey("ctrl", "a")
        #     pyautogui.hotkey("del")
        #     pyautogui.write(task['configEntrada']['filialEmpresaOrigem'])
        #     pyautogui.hotkey("tab")
        #     console.print(f"\nCliente preenchido: '{task['configEntrada']['filialEmpresaOrigem']}'", style="bold green")
        #     time.sleep(6)
        # else:
        #     logger.info(f"\nError Message: Campo 'Cliente' não encontrado")
        #     console.print(f"\nError Message: Campo 'Cliente' não encontrado", style="bold red")

        screenshot_path = take_sreenshot()
        cliente_field_position = find_target_position(screenshot_path, "Cliente", 0, 160, 15)
        if cliente_field_position == None:
            return {"sucesso": False, "retorno": f"Não foi possivel encontrar a o campo cliente"}
        pyautogui.click(cliente_field_position)
        pyautogui.hotkey("ctrl", "a")
        pyautogui.hotkey("del")
        pyautogui.write(task['configEntrada']['filialEmpresaOrigem'])
        pyautogui.hotkey("tab")
        time.sleep(6)


        # Clica em cancelar na Janela "Busca Representante"
        
        # window_busca_representante = await find_element_center(ASSETS_BASE_PATH + "window_busca_representante.png", (695, 342, 537, 106), 20)
        
        # if window_busca_representante is not None:
        #     button_cancelar = await find_element_center(ASSETS_BASE_PATH + "button_cancelar.png", (691, 342, 534, 343), 10)
        #     pyautogui.click(button_cancelar.x, button_cancelar.y)
        
        # time.sleep(2)

        screenshot_path = take_sreenshot()
        window_busca_representante_position = take_target_position(screenshot_path, "Busca Representante")
        if window_busca_representante_position is not None:
            button_cancelar_position = find_target_position(screenshot_path, "Cancelar", attempts=15)            
            pyautogui.click(button_cancelar_position)
        
        time.sleep(2)

        # window_busca_representante_position = take_target_position(screenshot_path, "Busca Representante")
        

        # window_busca_representante = await find_element_center(ASSETS_BASE_PATH + "window_busca_representante.png", (695, 342, 537, 106), 20)
        # if window_busca_representante is not None:
        #     button_cancelar = await find_element_center(ASSETS_BASE_PATH + "button_cancelar.png", (691, 342, 534, 343), 15)
        #     pyautogui.click(button_cancelar.x, button_cancelar.y)
        
        # time.sleep(2)

        # Aviso "Deseja alterar a condição de pagamento informada no cadastro do cliente?"
        # payment_condition_warning = await find_element_center(ASSETS_BASE_PATH + "warning_change_payment_condition.png", (627, 420, 674, 192), 10)

        # if payment_condition_warning is not None:
        #     button_no = await find_element_center(ASSETS_BASE_PATH + "warning_button_no.png", (627, 420, 674, 192), 10)
        #     pyautogui.click(button_no.x, button_no.y)
        #     console.print(f"\nClicou 'No' Mensagem 'Deseja alterar a condição de pagamento informada no cadastro do cliente?'", style="bold green")
        #     time.sleep(6)
        # else:
        #     logger.info(f"\nError Message: Aviso de condição de pagamento não encontrado")
        #     console.print(f"\nError Message: Aviso de condição de pagamento não encontrado", style="bold red")

        # time.sleep(3)

        screenshot_path = take_sreenshot()
        payment_condition_warning_position = take_target_position(screenshot_path, "Deseja alterar a condição de pagamento")
        if payment_condition_warning_position is not None:
            button_no_position = find_target_position(screenshot_path, "No", attempts=15)            
            pyautogui.click(button_no_position)
            console.print(f"\nClicou 'No' Mensagem 'Deseja alterar a condição de pagamento informada no cadastro do cliente?'", style="bold green")
            time.sleep(6)
        else:
            log_msg = f"\nError Message: Aviso de condição de pagamento não encontrado"
            logger.info(log_msg)
            console.print(log_msg, style="bold red")

        #Seleciona 'Custo Médio' (Seleção do tipo de preço)

        # custo_medio_select = await find_element_center(ASSETS_BASE_PATH + "select_custo_medio.png", (826, 430, 276, 179), 10)

        # if custo_medio_select is not None:
        #     pyautogui.click(custo_medio_select.x, custo_medio_select.y)
        #     button_ok = await find_element_center(ASSETS_BASE_PATH + "select_ok_custo_medio.png", (826, 430, 276, 179), 10)
        #     pyautogui.click(button_ok.x, button_ok.y)
        #     time.sleep(5)
        #     console.print(f"\nClicou OK 'Custo médio'", style="bold green")
        # else:
        #     logger.info(f"\nError Message: Campo 'Custo Médio' não encontrado")
        #     console.print(f"\nError Message: Campo 'Custo Médio' não encontrado", style="bold yellow")

        # time.sleep(10)

        screenshot_path = take_sreenshot()
        custo_medio_select_position = find_target_position(screenshot_path, "Custo Médio", attempts=15)
        if custo_medio_select_position is not None:
            pyautogui.click(custo_medio_select_position)
            button_ok_position = find_target_position(screenshot_path, "OK", attempts=15)            
            pyautogui.click(button_ok_position)
            time.sleep(5)
            console.print(f"\nClicou OK 'Custo médio'", style="bold green")
        else:
            log_msg = f"\nError Message: Campo 'Custo Médio' não encontrado"
            logger.info(log_msg)
            console.print(log_msg, style="bold yellow")

        time.sleep(10)

        #Clica em ok na mensagem "Existem Pré-Vendas em aberto para este cliente."
        
        # existing_pre_venda = await find_element_center(ASSETS_BASE_PATH + "existing_pre_venda.png", (831, 437, 247, 156), 10)
        
        # if existing_pre_venda is not None:
        #     button_ok = await find_element_center(ASSETS_BASE_PATH + "button_ok.png", (831, 437, 247, 156), 10)
        #     pyautogui.click(button_ok.x, button_ok.y)
        #     console.print(f"\nClicou OK 'Pre Venda Existente'", style="bold green")
        #     time.sleep(5)
        # else:
        #     logger.info(f"\nError Message: Menssagem de prevenda existente não encontrada")
        #     console.print(f"\nError Message: Menssagem de prevenda existente não encontrada", style="bold yellow")

        screenshot_path = take_sreenshot()
        existing_pre_venda_position = find_target_position(screenshot_path, "Existem Pré-Vendas", attempts=15)
        if existing_pre_venda_position is not None:
            button_ok_position = find_target_position(screenshot_path, "OK", attempts=15)            
            pyautogui.click(button_ok_position)
            console.print(f"\nClicou OK 'Pre Venda Existente'", style="bold green")
            time.sleep(5)
        else:
            log_msg = f"\nError Message: Menssagem de prevenda existente não encontrada"
            logger.info(log_msg)
            console.print(log_msg, style="bold yellow")

        #Define representante para "1"
        
        # field_representante = await find_element_center(ASSETS_BASE_PATH + "field_representante.png", (679, 416, 214, 72), 10)

        # if field_representante is not None:
        #     pyautogui.doubleClick(field_representante.x + 50, field_representante.y + 1)
        #     pyautogui.hotkey("ctrl", "a")
        #     pyautogui.hotkey("del")
        #     pyautogui.write('1')
        #     pyautogui.hotkey("tab")
        
        # time.sleep(3)

        screenshot_path = take_sreenshot()
        field_representante_position = find_target_position(screenshot_path, "Representante", 0, -160, attempts=15)
        if field_representante_position is not None:
            pyautogui.doubleClick(field_representante_position)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("del")
            pyautogui.write('1')
            pyautogui.hotkey("tab")
        
        time.sleep(3)

        #Abre Menu itens
        
        # menu_itens = await find_element_center(ASSETS_BASE_PATH + "menu_itens.png", (526, 286, 152, 45), 10)
        # if menu_itens is not None:
        #     pyautogui.click(menu_itens.x, menu_itens.y)
        
        # time.sleep(2)

        menu_itens = find_target_position(screenshot_path, "Itens", attempts=15)
        if menu_itens is not None:
            pyautogui.click(menu_itens)
        else:
            log_msg = f'Campo "Itens" no menu da pré-venda não encontrado'
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
            return {"sucesso": False, "retorno": log_msg}

        time.sleep(2)

        #Loop de itens
        
        # for item in itens:
        #     #Clica no botão inclui para abrir a tela de item
        #     button_incluir = await find_element_center(ASSETS_BASE_PATH + "button_incluir.png", (840, 549, 116, 45), 10)
        #     pyautogui.click(button_incluir.x, button_incluir.y)
        #     time.sleep(5)
        #     console.print("\nClicou em 'Incluir'", style='bold green')            

        #     # Digita Almoxarifado
        #     button_almoxarifado = await find_element_center(ASSETS_BASE_PATH + "field_almoxarifado.png", (670, 280, 210, 87), 10)
        #     if button_almoxarifado is not None:
        #         pyautogui.doubleClick(button_almoxarifado.x + 129, button_almoxarifado.y)
        #         pyautogui.hotkey('del')
        #         pyautogui.write(task['configEntrada']['filialEmpresaOrigem']+"50")
        #         pyautogui.hotkey('tab')
        #         time.sleep(3)
        #         console.print(f"\nDigitou almoxarifado {task['configEntrada']['filialEmpresaOrigem']+"50"}", style='bold green')            
        #     else:
        #         observacao = f'Botão Almoxarifado não encontrado'
        #         await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
        #         return {"sucesso": False, "retorno": observacao}

        for item in itens:
            screenshot_path = take_sreenshot()
            #Clica no botão inclui para abrir a tela de item
            button_incluir = find_target_position(screenshot_path, "Incluir", attempts=15)
            if button_incluir is not None:
                pyautogui.click(button_incluir)
                console.print("\nClicou em 'Incluir'", style='bold green')            
            else:
                log_msg = f'Botão "Incluir" não encontrado'
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                return {"sucesso": False, "retorno": log_msg}
            time.sleep(3)
            
            screenshot_path = take_sreenshot()
            # Digita Almoxarifado
            field_almoxarifado = find_target_position(screenshot_path, "Almoxarifado",0, 129, 15)
            if field_almoxarifado is not None:
                pyautogui.doubleClick(field_almoxarifado)
                pyautogui.hotkey('del')
                pyautogui.write(task['configEntrada']['filialEmpresaOrigem'] + ALMOXARIFADO_DEFAULT)
                pyautogui.hotkey('tab')
                time.sleep(2)
                console.print(f"\nDigitou almoxarifado {task['configEntrada']['filialEmpresaOrigem'] + ALMOXARIFADO_DEFAULT}", style='bold green')            
            else:
                log_msg = f'Campo Almoxarifado não encontrado'
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                return {"sucesso": False, "retorno": log_msg}


            #Segue para o campo do item
            
            # pyautogui.hotkey('tab')
            # pyautogui.hotkey('tab')
            # pyautogui.write(item['codigoProduto'])
            # pyautogui.hotkey('tab')
            # time.sleep(5)
            # console.print(f"\nDigitou codigo do produto {item['codigoProduto']}", style='bold green')

            field_item = find_target_position(screenshot_path, "Item", 0, 130, 15)
            if field_item is not None:
                pyautogui.click(field_item)
                pyautogui.write(item['codigoProduto'])
                console.print(f"\nDigitou almoxarifado {item['codigoProduto']}", style='bold green')
            else:
                console.print(f"\n Não conseguiu digitar almoxarifado {item['codigoProduto']}", style='bold green')



            #Checa tela de pesquisa de item
            # window_pesquisa_item = await find_element_center(ASSETS_BASE_PATH + "window_pesquisa_item.png", (488, 226, 352, 175), 10)
            # console.log(f"Produto {item['codigoProduto']} encontrado", style="bold green")
            # logger.info(f"Produto {item['codigoProduto']} encontrado")

            # if window_pesquisa_item is not None:
            #     observacao = f"Item {item['codigoProduto']} não encontrado, verificar cadastro"
            #     console.log(f"{observacao}", style="bold green")
            #     logger.info(f"{observacao}")
            #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            #     return {"sucesso": False, "retorno": observacao}

            window_pesquisa_item = take_target_position(screenshot_path, "Pesquisa Item")
            if window_pesquisa_item is not None:
                log_msg = f'Item não encontrado.'
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                return {"sucesso": False, "retorno": log_msg}
            else:
                console.print(f"Item encontrado!", style='bold green')

            screenshot_path = take_sreenshot()

            #Checa se existe alerta de item sem preço, se existir retorna erro(simplifica e bof)
            
            # warning_price = await find_element_center(ASSETS_BASE_PATH + "warning_item_price.png",  (824, 426, 255, 191), 10)
            # if warning_price is not None:
            #     observacao = f"Item {item['codigoProduto']} não possui preço, verificar erro de estoque ou de bloqueio."
            #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            #     return {"sucesso": False, "retorno": observacao}
            
            # time.sleep(3)

            window_preco = take_target_position(screenshot_path, "Pesquisa Item")
            if window_preco is not None:
                log_msg = f'Item {item['codigoProduto']} não possui preço, verificar erro de estoque ou de bloqueio.'
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                return {"sucesso": False, "retorno": log_msg}
            else:
                console.print(f"Item encontrado!", style='bold green')
            
            time.sleep(2)

            #Seleciona o Saldo Disponivel e verifica se ah possibilidade do descarte
            field_saldo_disponivel = find_target_position(screenshot_path + "Saldo", 20 ,0 , 10)
            if field_saldo_disponivel is not None:
                pyautogui.doubleClick(field_saldo_disponivel)
                time.sleep(1)
                pyautogui.doubleClick(field_saldo_disponivel)
                time.sleep(1)
                pyautogui.hotkey('ctrl', 'c')
                amount_avaliable= ''
                amount_avaliable = pyperclip.paste()
                console.print(f"Saldo Disponivel: '{amount_avaliable}'", style="bold green")

                #Verifica se o saldo disponivel é valido para descartar
                if int(amount_avaliable) > 0 and int(amount_avaliable) >= int(item['qtd']): 
                    field_quantidade = find_target_position(screenshot_path, "Quantidade", 20 ,0 , 15)
                    pyautogui.doubleClick(field_quantidade.x, field_quantidade.y)
                    pyautogui.hotkey('del')
                    pyautogui.write(str(item['qtd']))
                    pyautogui.hotkey('tab')
                    time.sleep(2)
                else:
                    log_msg = f"Saldo disponivel: '{amount_avaliable}' é menor que '{item['qtd']}' o valor que deveria ser descartado. Item: '{item['codigoProduto']}'"
                    await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                    console.print(log_msg, style="bold red")
                    return {"sucesso": False, "retorno": log_msg}

            #Clica em incluir para adicionar o item na nota
            
            # button_incluir_item = await find_element_center(ASSETS_BASE_PATH + "button_incluir_item.png", (914, 706, 335, 57), 10)
            # if button_incluir_item is not None:
            #     pyautogui.click(button_incluir_item.x, button_incluir_item.y)
            #     time.sleep(2)
            # else:
            #     observacao = f"Botao incluir item não encontrado"
            #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            #     console.print(observacao, style="bold red")
            #     return {"sucesso": False, "retorno": observacao}

            button_incluir_item = find_target_position(screenshot_path, "Inlcuir",0, 0, 15)
            if button_incluir_item is not None:
                pyautogui.click(button_incluir_item.x, button_incluir_item.y)
                time.sleep(2)
            else:
                log_msg = f"Botao 'Incluir' item não encontrado"
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                console.print(log_msg, style="bold red")
                return {"sucesso": False, "retorno": log_msg}
            
            #Clica em cancelar para fechar a tela e abrir novamente caso houver mais itens
            
            # button_cancela_item = await find_element_center(ASSETS_BASE_PATH + "button_cancela_item.png", (914, 706, 335, 57), 10)
            # if button_cancela_item is not None:
            #     pyautogui.click(button_cancela_item.x, button_cancela_item.y)
            #     time.sleep(2)
            # else:
            #     observacao = f"Botao cancelar para fechar a tela do item nao encontrado"
            #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            #     console.print(observacao, style="bold red")
            #     return {"sucesso": False, "retorno": observacao}
            
        # time.sleep(2)

            button_cancela_item = find_target_position(screenshot_path, "Cancela",0, 0, 15)
            if button_cancela_item is not None:
                pyautogui.click(button_cancela_item)
                time.sleep(2)
            else:
                log_msg = f"Botao cancelar para fechar a tela do item nao encontrado"
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", log_msg, task['configEntrada']['uuidSimplifica'], nota_fiscal, valor_nota)
                console.print(log_msg, style="bold red")
                return {"sucesso": False, "retorno": log_msg}
            
        time.sleep(2)

        #Clica no botão "+" no canto superior esquerdo para lançar a pre-venda
        
        # button_lanca_pre_venda = await find_element_center(ASSETS_BASE_PATH + "button_lanca_prevenda.png", (490, 204, 192, 207), 10)
        # if button_lanca_pre_venda is not None:
        #     pyautogui.click(button_lanca_pre_venda.x, button_lanca_pre_venda.y)
        #     console.print("\nLançou Pré-Venda", style="bold green")
        # else:
        #     observacao = f"Botao lança pre-venda nao encontrado"
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
        #     console.print(observacao, style="bold red")
        #     return {"sucesso": False, "retorno": observacao}
        
        # time.sleep(5)

        screenshot_path = take_sreenshot()
        button_lanca_pre_venda = find_target_position(screenshot_path, attempts=15)

        if button_lanca_pre_venda is not None:
            pyautogui.click(button_lanca_pre_venda)
            console.print("\nLançou Pré-Venda", style="bold green")
        else:
            observacao = f"Botao lança pre-venda nao encontrado"
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            console.print(observacao, style="bold red")
            return {"sucesso": False, "retorno": observacao}
        
        time.sleep(5)

        #Verifica mensagem de "Pré-Venda incluida com número: xxxxx"
        
        # included_pre_venda = await find_element_center(ASSETS_BASE_PATH + "included_pre_venda.png", (752, 436, 393, 199), 10)
        # if included_pre_venda is not None:
        #     #Clica no centro da mensagem e copia o texto para pegar o numero da pre-venda
        #     pyautogui.click(included_pre_venda.x, included_pre_venda.y)
        #     pyautogui.hotkey("ctrl", "c")
        #     pre_venda_message = ""
        #     pre_venda_message = pyperclip.paste()
        #     pre_venda_message = re.findall(r'\d+-\d+', pre_venda_message)
        #     console.print(f"Numero pré-venda: '{pre_venda_message[0]}'",style='bold green')
        #     #Clica no ok da mensagem
        #     button_ok = await find_element_center(ASSETS_BASE_PATH + "button_ok2.png", (752, 436, 393, 199), 10)
        #     pyautogui.click(button_ok.x, button_ok.y)
        # else:
        #     observacao = f"Não achou mensagem Pré-Venda incluida."
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
        #     console.print(observacao, style="bold red")
        #     return {"sucesso": False, "retorno": observacao}
        

        screenshot_path = take_sreenshot()
        included_pre_venda = find_target_position(screenshot_path, attempts=15)
        if included_pre_venda is not None:
            #Clica no centro da mensagem e copia o texto para pegar o numero da pre-venda
            pyautogui.click(included_pre_venda)
            pyautogui.hotkey("ctrl", "c")
            pre_venda_message = ""
            pre_venda_message = pyperclip.paste()
            pre_venda_message = re.findall(r'\d+-\d+', pre_venda_message)
            console.print(f"Numero pré-venda: '{pre_venda_message[0]}'",style='bold green')

            # Clica no ok da mensagem
            # button_ok = await find_element_center(ASSETS_BASE_PATH + "button_ok2.png", (752, 436, 393, 199), 10)
            # pyautogui.click(button_ok.x, button_ok.y)
            
            screenshot_path = take_sreenshot()
            button_ok = find_target_position(screenshot_path, attempts=10)
            pyautogui.click(button_ok)

        else:
            observacao = f"Não achou mensagem Pré-Venda incluida."
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            console.print(observacao, style="bold red")
            return {"sucesso": False, "retorno": observacao}


        # message_prevenda = await find_element_center(ASSETS_BASE_PATH + "message_deseja_pesquisar_pre_venda.png", (752, 436, 393, 199), 10)
        # if message_prevenda is not None:
        #     button_yes= await find_element_center(ASSETS_BASE_PATH + "warning_button_yes.png", (752, 436, 393, 199), 10)
        #     pyautogui.click(button_yes.x, button_yes.y)
        # else:
        #     observacao = f"Mensagem 'Deseja pesquisar pré-venda?' não encontrada."
        #     console.print(observacao, style="bold yellow")

        screenshot_path = take_sreenshot()
        message_prevenda = find_target_position(screenshot_path, attempts=15)
        if message_prevenda is not None:
            screenshot_path = take_sreenshot()
            button_yes= find_target_position(screenshot_path, attempts=15)
            pyautogui.click(button_yes)
        else:
            observacao = f"Mensagem 'Deseja pesquisar pré-venda?' não encontrada."
            console.print(observacao, style="bold yellow")

        #Confirma pré-venda
        screenshot_path = take_sreenshot()
        button_confirma_transferencia = find_target_position(screenshot_path, attempts=15)
        if button_confirma_transferencia is not None:
            pyautogui.click(button_confirma_transferencia)
            console.log("Confirmou transferencia", style="bold green")
        else:
            observacao = f"Botao 'Confirma' não encontrado"
            console.print(observacao, style="bold yellow")
        
        pyautogui.moveTo(1200, 300)

        # message_confirma_transferencia = await find_element_center(ASSETS_BASE_PATH + "message_confirma_pre_venda.png", (755, 408, 376, 205), 10)
        # if message_confirma_transferencia is not None:
        #     #clica em sim na mensagem
        #     button_yes= await find_element_center(ASSETS_BASE_PATH + "warning_button_yes.png", (752, 436, 393, 199), 10)
        #     pyautogui.click(button_yes.x, button_yes.y)
        #     console.log("Cliclou em 'Sim' para cofirmar a pré-venda", style='bold green')
        #     pyautogui.moveTo(1200, 300)
        #     #Clica no OK 'Pre-Venda incluida com sucesso'
        #     button_ok= await find_element_center(ASSETS_BASE_PATH + "button_ok.png", (803, 440, 309, 154), 15)
        #     pyautogui.click(button_ok.x, button_ok.y)
        #     console.log("Cliclou em 'OK' para pré-venda confirmada com sucesso", style='bold green')
        # else:
        #     observacao = f"Mensagem 'Deseja realmente confirmar esta pré-venda?' não encontrada."
        #     console.print(observacao, style="bold yellow")
        
        # pyautogui.moveTo(1000, 500)

        

        #Clica em Faturar
        # button_faturar = await find_element_center(ASSETS_BASE_PATH + "button_faturar.png", (1222, 278, 168, 131), 10)
        # if button_faturar is not None:
        #     pyautogui.click(button_faturar.x, button_faturar.y)
        #     console.print(f"Clicou em: 'Faturar'",style='bold green')
        # else:
        #     observacao = f"Não encontrou botão faturar"
        #     console.print(observacao, style="bold yellow")
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
        #     return {"sucesso": False, "retorno": f'{observacao}'}
         
        # time.sleep(10)

        screenshot_path = take_sreenshot()
        button_faturar = find_target_position(screenshot_path, "Faturar", attempts=15)
        if button_faturar is not None:
            pyautogui.click(button_faturar)
            console.print(f"Clicou em: 'Faturar'", style='bold green')
        else:
            observacao = f"Não encontrou botão faturar"
            console.print(observacao, style="bold yellow")
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
            return {"sucesso": False, "retorno": f'{observacao}'}
         
        time.sleep(10)

        #Verifica se existe a mensagem de recalcular parcelas
        # message_recalcular = await find_element_center(ASSETS_BASE_PATH + "message_recalcular_parcelas.png", (803, 440, 309, 154), 10)
        # #Se existir clica em nao
        # if message_recalcular is not None:
        #     button_no = await find_element_center(ASSETS_BASE_PATH + "warning_button_no.png", (803, 440, 309, 154), 10)
        #     pyautogui.click(button_no.x, button_no.y)
        #     console.log("Cliclou em 'No' na mensagem de recalcular parcelas") 
        # else:
        #     logger.info(f"Mensagem de para recalcular parcelas da pre-venda nao existe")
        #     console.print(f"Mensagem de para recalcular parcelas da pre-venda nao existe", style="bold yellow")
        
        # time.sleep(8)

        screenshot_path = take_sreenshot()
        message_recalcular = find_target_position(screenshot_path, "Recalcular Parcelas", attempts=15)
        #Se existir clica em não
        if message_recalcular is not None:
            screenshot_path = take_sreenshot()
            button_no = find_target_position(screenshot_path, "Não", attempts=15)
            pyautogui.click(button_no)
            console.log("Clicou em 'Não' na mensagem de recalcular parcelas")
        else:
            logger.info(f"Mensagem de para recalcular parcelas da pre-venda não existe")
            console.print(f"Mensagem de para recalcular parcelas da pre-venda não existe", style="bold yellow")
        
        time.sleep(8)

        # #Seleciona o modelo da nota (em teoria em prod nao precisa mas esta aqui por precaução) -- depreciado
        # # pyautogui.hotkey("tab")
        # # pyautogui.write("077")
        # # time.sleep(5) 

        # model_selected = await find_element_center(ASSETS_BASE_PATH + "field_model_select_model_077.png", (556, 186, 611, 117), 10)
        
        # if model_selected is None:
        #     console.print("Selecionando Modelo", style="bold green")
        #     field_modelo_faturamento = await find_element_center(ASSETS_BASE_PATH + "field_modelo_faturamento2.png", (946, 200, 228, 106), 10)
        
        #     if field_modelo_faturamento is not None:
        #         pyautogui.click(field_modelo_faturamento.x, field_modelo_faturamento.y + 10)
        #         time.sleep(1)
        #         for _ in range(15):
        #             pyautogui.keyDown('up')
        #         pyautogui.keyUp('up')
                               
        #         model_to_select = await find_element_center(ASSETS_BASE_PATH + "field_model_select_model_077.png", (636, 249, 506, 140), 10)
        #         pyautogui.click(model_to_select.x, model_to_select.y)

        #     else:
        #         observacao = {
        #         "Numero Pre Venda": pre_venda_message[0],
        #         "Numero da nota": None
        #         }
        #         await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
        #         return {"sucesso": False, "retorno": "Falha ao selecionar modelo: Na tela de Faturamento Pré-Venda"}

        # time.sleep(5)

        screenshot_path = take_sreenshot()
        model_selected = find_target_position(screenshot_path, attempts=15)
        
        if model_selected is None:
            console.print("Selecionando Modelo", style="bold green")
            screenshot_path = take_sreenshot()
            field_modelo_faturamento = find_target_position(screenshot_path, attempts=15)
        
            if field_modelo_faturamento is not None:
                pyautogui.click(field_modelo_faturamento + 10)
                time.sleep(1)
                for _ in range(15):
                    pyautogui.keyDown('up')
                pyautogui.keyUp('up')
                
                screenshot_path = take_sreenshot()
                model_to_select = await find_target_position(screenshot_path, attempts=15)
                pyautogui.click(model_to_select)

            else:
                observacao = {
                "Numero Pre Venda": pre_venda_message[0],
                "Numero da nota": None
                }
                await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, None)
                return {"sucesso": False, "retorno": "Falha ao selecionar modelo: Na tela de Faturamento Pré-Venda"}

        time.sleep(5)
        
        #Pega total da Nota
        
        # field_total_nota = await find_element_center(ASSETS_BASE_PATH + "field_total_nota.png", (1067, 767, 306, 98), 10)
        
        # if field_total_nota is not None:
        #     pyautogui.click(field_total_nota.x, field_total_nota.y)
        #     pyautogui.doubleClick(field_total_nota.x + 35, field_total_nota.y)
        #     pyautogui.hotkey("ctrl", "c")
        #     valor_nota = pyperclip.paste()
        #     valor_nota = re.findall(r'\b\d{1,3}(?:\.\d{3})*,\d{2}\b', valor_nota)
        #     console.print(f"\nValor NF: '{valor_nota[0]}'",style='bold green')
        # else:
        #     console.print(f"\nNão conseguiu extrair o valor da nota",style='bold red')
        #     logger.info("\nNão conseguiu extrair o valor da nota")

        # #Clicar no botao "OK" com um certo verde
        # button_verde = await find_element_center(ASSETS_BASE_PATH + "button_ok_verde.png", (1070, 792, 292, 54), 10)
        # if button_verde is not None:
        #     pyautogui.click(button_verde.x, button_verde.y)

        # time.sleep(5)

        screenshot_path = take_sreenshot()
        field_total_nota = find_target_position(screenshot_path, attempts=15)
        
        if field_total_nota is not None:
            pyautogui.click(field_total_nota)
            pyautogui.doubleClick(field_total_nota + 35, field_total_nota)
            pyautogui.hotkey("ctrl", "c")
            valor_nota = pyperclip.paste()
            valor_nota = re.findall(r'\b\d{1,3}(?:\.\d{3})*,\d{2}\b', valor_nota)
            console.print(f"\nValor NF: '{valor_nota[0]}'",style='bold green')
        else:
            console.print(f"\nNão conseguiu extrair o valor da nota",style='bold red')
            logger.info("\nNão conseguiu extrair o valor da nota")

        #Clicar no botao "OK" com um certo verde
        screenshot_path = take_sreenshot()
        button_verde = await find_target_position(screenshot_path, attempts=15)
        if button_verde is not None:
            pyautogui.click(button_verde)

        time.sleep(5)

        #Aviso "Deseja faturar pré-venda?"
        # faturar_pre_venda = await find_element_center(ASSETS_BASE_PATH + "faturar_pre_venda.png", (803, 440, 309, 154), 10)

        # if faturar_pre_venda is not None:
        #     button_yes = await find_element_center(ASSETS_BASE_PATH + "warning_button_yes.png", (803, 440, 309, 154), 10)
        #     pyautogui.click(button_yes.x , button_yes.y)
        # else:
        #     observacao = {
        #     "numero_pre_venda": pre_venda_message[0],
        #     "numero_nota": ''
        #     }
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, valor_nota[0])
        #     return {"sucesso": False, "retorno": "Falha ao cliclar em: 'SIM' no aviso: 'Deseja realmente faturar esta Pré-Venda ?'"}

        # time.sleep(7)

        # #Mensagem de nota fiscal gerada com número
        # nota_fiscal_gerada = await find_element_center(ASSETS_BASE_PATH + "message_nota_fiscal_gerada.png", (803, 440, 309, 154), 10)
        # pyautogui.click(nota_fiscal_gerada.x, nota_fiscal_gerada.y)
        # pyautogui.hotkey("ctrl", "c")
        # nota_fiscal = pyperclip.paste()
        # nota_fiscal = re.findall(r'\d+-?\d*', nota_fiscal)
        # console.print(f"\nNumero NF: '{nota_fiscal[0]}'",style='bold green')

        # time.sleep(7)

        screenshot_path = take_sreenshot()
        faturar_pre_venda = find_target_position(screenshot_path, attempts=15)

        if faturar_pre_venda is not None:
            screenshot_path = take_sreenshot()
            button_yes = await find_target_position(screenshot_path, attempts=15)
            pyautogui.click(button_yes)
        else:
            observacao = {
            "numero_pre_venda": pre_venda_message[0],
            "numero_nota": ''
            }
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], None, valor_nota[0])
            return {"sucesso": False, "retorno": "Falha ao cliclar em: 'SIM' no aviso: 'Deseja realmente faturar esta Pré-Venda ?'"}

        time.sleep(7)

        #Mensagem de nota fiscal gerada com número
        # nota_fiscal_gerada = await find_element_center(ASSETS_BASE_PATH + "message_nota_fiscal_gerada.png", (803, 440, 309, 154), 10)
        # pyautogui.click(nota_fiscal_gerada.x, nota_fiscal_gerada.y)
        # pyautogui.hotkey("ctrl", "c")
        # nota_fiscal = pyperclip.paste()
        # nota_fiscal = re.findall(r'\d+-?\d*', nota_fiscal)
        # console.print(f"\nNumero NF: '{nota_fiscal[0]}'",style='bold green')

        # time.sleep(7)

        screenshot_path = take_sreenshot()
        nota_fiscal_gerada = find_target_position(screenshot_path, attempts=15)
        pyautogui.click(nota_fiscal_gerada)
        pyautogui.hotkey("ctrl", "c")
        nota_fiscal = pyperclip.paste()
        nota_fiscal = re.findall(r'\d+-?\d*', nota_fiscal)
        console.print(f"\nNumero NF: '{nota_fiscal[0]}'",style='bold green')

        time.sleep(7)

        #Transmitir a nota
        # transmitir = await find_element_center(ASSETS_BASE_PATH + "button_transmitir.png", (807, 436, 374, 204), 10)
        # if transmitir is not None:
        #     pyautogui.click(transmitir.x, transmitir.y)
        #     logger.info("\nNota Transmitida")
        #     console.print("\nNota Transmitida", style="bold green")
        # else:
        #     observacao = f'\nNota não Transmitida'
        #     logger.info(observacao)
        #     console.print(observacao ,style="bold red")
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota)
        #     return {"sucesso": False, "retorno": observacao}

        # time.sleep(7)

        screenshot_path = take_sreenshot()
        transmitir = find_target_position(screenshot_path, attempts=15)
        if transmitir is not None:
            pyautogui.click(transmitir)
            logger.info("\nNota Transmitida")
            console.print("\nNota Transmitida", style="bold green")
        else:
            observacao = f'\nNota não Transmitida'
            logger.info(observacao)
            console.print(observacao ,style="bold red")
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota)
            return {"sucesso": False, "retorno": observacao}

        time.sleep(7)

        #Fechar transmitir nota
        # transmitir_fechar = await find_element_center(ASSETS_BASE_PATH + "button_fechar_transmitir_nota.png", (647, 340, 618, 353), 10)
        # if transmitir_fechar is not None:
        #     pyautogui.click(transmitir_fechar.x, transmitir_fechar.y)
        #     observacao = f'Nota Transmitida com sucesso'
        #     logger.info(observacao)
        #     console.print(observacao)
        # else:
        #     observacao = f'Nota não transmitida'
        #     logger.info(observacao)
        #     console.print(observacao, style='bold red')
        #     await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota[0])
        #     return {"sucesso": False, "retorno": observacao}

        # observacao = {
        #     "numero_pre_venda": pre_venda_message[0],
        #     "numero_nota": nota_fiscal[0],
        #     "valor_nota": valor_nota[0]
        # }

        # await api_simplifica(task['configEntrada']['urlRetorno'], "SUCESSO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota[0])
        # return {"sucesso": True, "retorno": observacao}

        screenshot_path = take_sreenshot()
        transmitir_fechar = find_target_position(screenshot_path, attempts=15)
        if transmitir_fechar is not None:
            pyautogui.click(transmitir_fechar)
            observacao = f'Nota Transmitida com sucesso'
            logger.info(observacao)
            console.print(observacao)
        else:
            observacao = f'Nota não transmitida'
            logger.info(observacao)
            console.print(observacao, style='bold red')
            await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota[0])
            return {"sucesso": False, "retorno": observacao}

        observacao = {
            "numero_pre_venda": pre_venda_message[0],
            "numero_nota": nota_fiscal[0],
            "valor_nota": valor_nota[0]
        }

        await api_simplifica(task['configEntrada']['urlRetorno'], "SUCESSO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota[0])
        return {"sucesso": True, "retorno": observacao}
    
    except Exception as ex:
        observacao = f"Erro Processo Descartes: {str(ex)}"
        logger.error(observacao)
        console.print(observacao, style="bold red")
        await api_simplifica(task['configEntrada']['urlRetorno'], "ERRO", observacao, task['configEntrada']['uuidSimplifica'], nota_fiscal[0], valor_nota[0])
        return {"sucesso": False, "retorno": observacao}