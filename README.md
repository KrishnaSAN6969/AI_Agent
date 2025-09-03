# 🧠 AI Research Assistant

An intelligent research assistant built with **LangChain**, **Anthropic Claude**, and custom tools for searching, retrieving information, and saving research results.  

This project demonstrates how to build an **agent-based research assistant** that:
- Accepts a natural language research query.
- Uses external tools (`search_tool`, `wiki_tool`, `save_tool`) to gather and process information.
- Returns a **structured response** with topic, summary, sources, and tools used.

---

## 🌍 Concept

The assistant works as a **mini research pipeline**:

1. **User Query** – You type in a research question.  
2. **Agent Planning** – The LLM decides which tools are needed.  
3. **Tool Calls** – The agent calls search, wiki, or save tools.  
4. **Final Answer** – A structured JSON-like response is generated.

---

## 📖 Why Structured Output?

The response is parsed into a **Pydantic model** instead of raw text.  
This ensures:
- Consistency in formatting.  
- Easy integration into other applications.  
- Automatic validation of data.  

---

## 📦 Installation

```bash
git clone https://github.com/your-username/ai-research-assistant.git
cd ai-research-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
