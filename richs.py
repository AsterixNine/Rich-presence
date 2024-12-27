#################################################################
#
#   Discord Presence
#   Autor: @athos.rgx11 
#   discord: blackstardev
#   Data: 26/12/2024
#   Versão: 1.0
#   Descrição: https://github.com/AsterixNine/Rich-presence/blob/main/README.md
#   
#################################################################



from pypresence import Presence 
import time 
import sys 
import os
import random 
import logging 
 
# Configuração do logging
logging.basicConfig(
    filename='discord_presence.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s' 
)

# Estados disponíveis
estados = {
    "status 1": {
        "state": "MENTE",
        "details": "TEXTO 1",
        "emoji": "🔥"
    },
    "statu 2": {
        "state": "VIDA",
        "details": "TEXTO 2",
        "emoji": "💯"
    },
    "status 3": {
        "state": "NA ATIVIDADE",
        "details": "TEXTO 3",
        "emoji": "⚡"
    }
}

# Configurações
DISCORD_CONFIG = {
    "client_id": "USER ID BOT ",
    "update_interval": 5, # tempo de atualização
    "session_duration": 300, # tempo de sessão em segundos 5 minutos
    "reconnect_delay": 3 # tempo de reconexão em segundos 3s
}

# Links sociais
# PODEM SER ALTERADOS PARA AS REDES SOCIAIS DO USUÁRIO, TANTO A REDE QUANTO A PLATAFORMA.
SOCIAL_LINKS = {
    "Instagram": "https://www.instagram.com/SUA REDE/",
    "Twitter": "https://x.com/SUA REDE"
}

# Imagens disponíveis
images = ["athos", "athos2", "athos3"]

def run_presence():
    try:
        RPC = Presence(DISCORD_CONFIG["client_id"], pipe=0)
        RPC.connect()
        logging.info("Conectado ao Discord com sucesso")
        
        start_time = time.time()
        end_time = start_time + DISCORD_CONFIG["session_duration"]

        while time.time() < end_time:
            current_image = random.choice(images)
            estado = random.choice(list(estados.values()))
            
            RPC.update(
                state=f"{estado['emoji']} {estado['state']}",
                details=estado['details'],
                large_image=current_image,
                large_text="texto longo",
                start=start_time,
                instance=True,
                buttons=[
                    {"label": "Instagram", "url": SOCIAL_LINKS["Instagram"]},
                    {"label": "Twitter", "url": SOCIAL_LINKS["Twitter"]}
                ]
            )
            time.sleep(DISCORD_CONFIG["update_interval"])
            
    except ConnectionError:
        logging.error("Erro de conexão com Discord")
    except Exception as e:
        logging.error(f"Erro inesperado: {str(e)}")
    finally:
        RPC.close()
        logging.info("Conexão fechada")

if __name__ == "__main__":
    while True:
        run_presence()
        os.execv(sys.executable, ['python'] + sys.argv)
