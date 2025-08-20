# ⚙️ Automação com Python

Este repositório contém exemplos práticos de automação utilizando **Python**, com foco em tarefas repetitivas do dia a dia como acesso à web, manipulação de arquivos, geração de relatórios e integração com APIs.

O objetivo é servir como uma base para quem deseja criar **scripts automatizados**, melhorar a produtividade e padronizar processos.

---

## 📌 O que está incluído  

| Área de Automação | Ferramentas Utilizadas |
|-------------------|------------------------|
| Navegação web e preenchimento automático | Selenium / Requests |
| Manipulação de planilhas | Pandas / OpenPyXL |
| Geração de relatórios | Pandas / ReportLab |
| Agendamento de tarefas | Cron (Linux) / Agendador do Windows / APScheduler |
| Integração com APIs | Requests / JSON |

---

## 🧰 Pré-requisitos  

- ✅ Python 3.10 ou superior instalado;  
- ✅ Git instalado;    
- ✅ (Opcional, recomendado) Ambiente virtual configurado.

---

##  🔧 Criar Ambiente Virtual:
- python -m venv venv  
### 💻 Ativar Ambiente Virtual:
- No Windows:  
venv\Scripts\activate  
- Linux/Mac  
source venv/bin/activate  

---

## 🚀 Como Executar o Projeto  
### Clonar o repositório  
git clone https://github.com/seu-usuario/seu-repo.git  
cd seu-repo  

### Instalar dependências  
pip install -r requirements.txt  

### Executar um exemplo de automação  
python src/exemplo_automacao.py  

---

## 📂 Estrutura do Projeto  

📦 python-automation  
├── 📁 src/                    # Scripts de automação  
│   ├── selenium_example.py  
│   ├── excel_automation.py  
│   ├── api_automation.py  
│   └── ...  
├── 📁 resources/              # Arquivos utilizados nos exemplos  
├── requirements.txt  
└── README.md  

---

## 🤝 Contribuição

Contribuições são bem-vindas!  
Abra uma Issue ou envie um Pull Request com melhorias, novos cenários ou exemplos de integração.

---

## 💡 Boas Práticas

✅ Separe cada tipo de automação em um script diferente;  
⚠️ NUNCA coloque senhas diretamente no código → use variáveis de ambiente;  
➕ Adicione logs (logging) para facilitar o debug das automações;  
🧪 Crie testes automatizados para validar as rotinas mais críticas;  
🔁 Para tarefas recorrentes, utilize APScheduler ou configure um cron job;  
⛔ Evite usar time.sleep() → prefira waits inteligentes (ex. WebDriverWait). 

---

## 👩‍💻 Contato

- Informações	
- Nome	Leonardo da Motta Teixeira  
- Cargo	QA Engineer / Gestor / Tester-Sênior  
- LinkedIn	www.linkedin.com/in/leonardo-da-motta-teixeira-3584734b  
- E-mail	lteixei@hotmail.com  

---

## 📝 Licença

- Este projeto está licenciado sob a MIT License.
