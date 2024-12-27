
![Static Badge](https://img.shields.io/badge/DISCORD-RICH_PRESENCE-blue)
![Static Badge](https://img.shields.io/badge/By%20Athos%20Dev-8A2BE2)

---

# Rich Presence Personalizado para Discord

Este projeto é um **Rich Presence** customizável para Discord que exibe status dinâmico no seu perfil. 

---

## 🎯 Recursos
- Estados aleatórios com emojis
- Imagens personalizadas
- Botões para redes sociais
- Exibição de tempo de sessão
- Sistema de reconexão automática
- Logs em arquivo para monitoramento

---

## ⚙️ Configuração

### Passo 1: Configuração do ID do Bot
No arquivo `config.py`, substitua o valor de `client_id` pelo **ID do seu bot Discord**:
```python
"client_id": "USER ID BOT"  # Coloque seu ID do bot Discord aqui
```
### Passo 2: Estados Personalizados
Defina os estados no dicionário `estados.` Você pode adicionar quantos quiser:
```
estados = {
    "status 1": {
        "state": "SEU ESTADO",
        "details": "SUA DESCRIÇÃO",
        "emoji": "SEU EMOJI"
    },
    "status 2": {
        "state": "OUTRO ESTADO",
        "details": "OUTRA DESCRIÇÃO",
        "emoji": "OUTRO EMOJI"
    }
}
```

### Passo 3: Redes Sociais
Atualize os links das suas redes sociais no dicionário `SOCIAL_LINKS:`

```python
Copiar código
SOCIAL_LINKS = {
    "Instagram": "https://www.instagram.com/SEU_USUARIO/",
    "Twitter": "https://x.com/SEU_USUARIO"
}
```

### Passo 4: Imagens Personalizadas
Adicione os nomes das imagens que você configurou no Developer Portal do Discord no array `images`:
```
images = ["sua_imagem1", "sua_imagem2", "sua_imagem3"]

```

## 🔧 Configurações Adicionais
Você pode ajustar os tempos e comportamentos no arquivo `config.py`:

- update_interval: Intervalo de atualização (padrão: 5 segundos)
- session_duration: Duração da sessão (padrão: 300 segundos ou 5 minutos)
- reconnect_delay: Tempo de reconexão em caso de falha (padrão: 3 segundos)

## 🌟 Recursos Adicionais
- Rotação Aleatória: Os estados e imagens mudam aleatoriamente para maior dinamicidade.
- Tempo Decorrido: Exibe o tempo de sessão diretamente no status do Discord.
- Logs de Atividade: Todas as ações e erros são registrados no arquivo `discord_presence.log`.

## 🚀 Execução
Após configurar corretamente o arquivo `config.py`, execute o script principal com:

```bash
python main.py
```


# 🗂 Estrutura do Projeto

📂 RichPresence
* ├── main.py            # Código principal e suas configurações
* ├── discord_presence.log # Arquivo de logs
* └── README.md          # Documentação do projeto

# 📄 Licença
**Este projeto é distribuído sob a licença MIT.**
## Aproveite seu Rich Presence personalizado no Discord! 🎉
