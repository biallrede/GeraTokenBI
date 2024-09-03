import subprocess
from apscheduler.schedulers.background import BackgroundScheduler
import schedule
import threading
from credentials import credenciais_banco
import time
from functools import partial

# Para rodar no windows 
def get_powerbi_access_token(username, password):
    # Cria o script PowerShell que fará login e pegará o token
    powershell_script = f"""
    $password = ConvertTo-SecureString "{password}" -AsPlainText -Force
    $credential = New-Object System.Management.Automation.PSCredential ("{username}", $password)
    Login-PowerBI -Credential $credential
    $token = Get-PowerBIAccessToken -AsString
    $token
    """

    # Executa o script PowerShell
    result = subprocess.run(["powershell", "-Command", powershell_script], capture_output=True, text=True)

    # Verifica se o comando foi bem-sucedido
    if result.returncode == 0:
        token = result.stdout.strip()
        parts = token.split("Bearer ")
        token = parts[1].strip()
        inserir_chave_banco(token)
        # return result.stdout.strip()
    else:
        print("Erro ao executar o PowerShell script:", result.stderr)
        # return None

# Para rodar no linux 
# def get_powerbi_access_token():
#     # Executa o script PowerShell usando 'pwsh'
#     result = subprocess.run(["pwsh", "-File", "get_token.ps1"], capture_output=True, text=True)

#     # Verifica se o comando foi bem-sucedido
#     if result.returncode == 0:
#         token = result.stdout.strip()
#         if token:
#             print("Token obtido com sucesso:", token)
#             inserir_chave_banco(token)
#         else:
#             print("Nenhum token foi obtido. Saída do PowerShell está vazia.")
#     else:
#         print("Erro ao executar o PowerShell script:", result.stderr)

def inserir_chave_banco(access_token_banco):
    conn = credenciais_banco()
    cursor = conn.cursor()
    for tentativa in range(5):
        try:
            cursor.execute("TRUNCATE TABLE API_TOKEN_POWER_BI")
            # Insere os dados no banco
            cursor.execute(
            "INSERT INTO API_TOKEN_POWER_BI (token) "
            "VALUES (?)",
            (
                access_token_banco
            )
        )
            
            conn.commit()
           
            print("Dados inseridos com sucesso!")
            break # Para sair do loop
            # return mensagem_status

        except Exception as e:
            print(f"Falha na tentativa {tentativa + 1}: {e}".format(tentativa,e))
            time.sleep(30)  # segundos
            # return mensagem_status

username = "databi@allrede.com.br"
password = "ab73rj45#@%"

# for i in range(5, 23):
#     time_str = f"{i:02d}:00"
#     job = partial(get_powerbi_access_token, username, password)
#     schedule.every().day.at(time_str).do(job)

# scheduler = BackgroundScheduler()
# scheduler.start()

# while True:
#     schedule.run_pending()
#     threading.Event().wait(1)

get_powerbi_access_token(username,password)