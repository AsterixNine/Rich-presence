
![Static Badge](https://img.shields.io/badge/DISCORD-RICH_PRESENCE-blue)
![Static Badge](https://img.shields.io/badge/By%20Athos%20Dev-ff0000)
![Static Badge](https://img.shields.io/badge/%20Python%20-e2dd2b)

---

# Rich Presence Personalizado para Discord 
# CODIGO MANUAL E LIMITADO

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

- `update_interval`: Intervalo de atualização (padrão: 5 segundos)
- `session_duration`: Duração da sessão (padrão: 300 segundos ou 5 minutos)
- `reconnect_delay`: Tempo de reconexão em caso de falha (padrão: 3 segundos)

## 🌟 Recursos Adicionais
- Rotação Aleatória: Os estados e imagens mudam aleatoriamente para maior dinamicidade.
- Tempo Decorrido: Exibe o tempo de sessão diretamente no status do Discord.
- Logs de Atividade: Todas as ações e erros são registrados no arquivo `discord_presence.log`.

## 🚀 Execução
Após configurar corretamente o arquivo `richs.py`, execute o script principal com:

```bash
python richs.py
```


# 🗂 Estrutura do Projeto

📂 RichPresence
* ├── richs.py            # Código principal e suas configurações
* ├── discord_presence.log # Arquivo de logs
* └── README.md          # Documentação do projeto



---

# Discord Rich Presence GUI
# CODIGO AUTOMATICO E COM GUIA GRAFICA
Uma interface gráfica moderna e amigável para configurar e gerenciar o **Discord Rich Presence**, desenvolvida com **ttkbootstrap** para a interface e **pypresence** para integração com o Discord. Este projeto é ideal para usuários que desejam personalizar sua presença no Discord de forma visual e intuitiva.

---

## Recursos Principais

### Interface Gráfica
- Interface moderna e inspirada no tema escuro do Discord.
- Layout dividido em dois painéis principais:
  - **Painel Esquerdo (Configurações):**
    - Campo para Client ID do Discord.
    - Campos para **Estado** e **Detalhes** da presença.
    - Configuração de imagens (chave e texto).
    - Configuração de até dois botões personalizados (nome e URL).
    - Botões de controle: **Iniciar** e **Parar Presence**.
  - **Painel Direito (Preview):**
    - Visualização em tempo real das configurações.
    - Simula exatamente como aparecerá no Discord.
    - Preview de perfil, status e botões.
    - Contador de tempo decorrido.

---

### Funcionalidades Técnicas
- **Atualização em tempo real:** As mudanças feitas nas configurações aparecem instantaneamente na visualização.
- **Conexão com Discord:** Integração via API do Discord usando a biblioteca `pypresence`.
- **Threads:** Sistema de threads para evitar travamentos na interface ao iniciar/parar a conexão.
- **Tratamento de erros:** Logging de erros para garantir a estabilidade da aplicação.
- **Temas visuais:** Possibilidade de alterar o tema visual da interface.

---

### Recursos Adicionais
- **Botão para abrir Discord:** Link direto para o aplicativo Discord.
- **Sistema de créditos:** Exibe informações sobre o criador do software.
- **Interface responsiva e scrollável:** Adapta-se a diferentes resoluções de tela.
- **Tooltips explicativos:** Informações detalhadas sobre cada campo de configuração.

---

## Aspectos Técnicos
- **Programação orientada a objetos:** Estrutura modular para fácil manutenção e extensibilidade.
- **Gerenciamento automático de recursos:** Desconexão segura e eficiente ao encerrar a aplicação.
- **Eventos e callbacks:** Sistema reativo para mudanças no estado e ações do usuário.
- **Integração com API do Discord:** Uso da biblioteca `pypresence` para comunicação com o cliente Discord.

---

## Requisitos do Sistema
- Python 3.9 ou superior.
- Dependências:
  - `ttkbootstrap`
  - `pypresence`

Instale as dependências com o comando:
```bash
pip install ttkbootstrap pypresence
```

# Como Usar
## baixe o programa:
```
https://www.mediafire.com/file/574uccygoxlnxht/rich.exe/file
cd rich
```
# Executando o programa:

double click em `rich.exe`

# Configure sua presença no painel esquerdo:

* Insira o Client ID.
* Preencha o Estado, Detalhes e configurações de imagem.
* Adicione botões personalizados, se desejar.
* Clique em Iniciar Presence para aplicar as mudanças.
* Veja o preview no painel direito e ajuste conforme necessário.

# Créditos
* Desenvolvido por Athos Dev
* Inspirado no design do Discord.
* Biblioteca usada: ttkbootstrap.


# 📄 Licença
**Este projeto é distribuído sob a licença MIT.**
## Aproveite seu Rich Presence personalizado no Discord! 🎉

