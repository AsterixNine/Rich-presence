# Discord Rich Presence GUI

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
## Clone o repositório:
```
git clone https://github.com/seu-usuario/rich_gui.git
cd rich_gui
```
# Executando o programa:

double clicl em `rich_gui.exe`

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


# Licença
Este projeto está licenciado sob a `MIT License`. Veja o arquivo LICENSE para mais informações.
