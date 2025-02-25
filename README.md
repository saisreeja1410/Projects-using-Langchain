# Basic LangChain Projects

This repository contains a collection of basic projects demonstrating the capabilities of **LangChain**, a framework for developing applications powered by **large language models (LLMs)**. These projects cover fundamental concepts such as **text translation, retrieval-augmented generation (RAG), memory, and AI agents**.

## 🚀 Projects Included

Each project is maintained in a separate **Git branch**. Switch to the respective branch to explore the project.

### 1️⃣ **Text Translation using LangChain**
- Implements a simple **language translation model** using **LangChain and Google Gemini AI**.
- Uses **ChatGoogleGenerativeAI** to translate sentences into a specified target language.
- Takes user input for both the sentence and the target language.
- Utilizes **prompt engineering** to dynamically create translation prompts.
- **Branch:** `text-translation`

### 2️⃣ **Retrieval-Augmented Generation (RAG)**
- Implements a **retrieval-based AI system** using LangChain, allowing enhanced responses through external knowledge retrieval.
- The project consists of two main components:
  - **Ingestion Pipeline**: Loads, splits, and embeds text documents using **Hugging Face embeddings** and stores them in a **Pinecone vector database**.
  - **Retrieval System**: Takes user queries, retrieves the most relevant documents using **vector search**, and generates responses using **Google Gemini AI**.
- Uses **LangChain’s prompt engineering** to structure retrieval-augmented responses.
- Enhances LLM performance by **integrating structured document retrieval**.
- **Branch:** `RAG`

### 3️⃣ **Memory-based Chatbots**
- Implements **different types of conversational memory** to maintain context across interactions.
- **Buffer Memory**: Stores the entire conversation history, enabling the AI to remember all prior exchanges.
- **Buffer Window Memory**: Retains only the last few interactions (configurable window size), balancing memory efficiency with contextual awareness.
- **Summary Buffer Memory**: Summarizes previous conversations into a concise format, maintaining essential details while reducing memory footprint.
- **Summary Memory**: Generates structured conversation summaries for long-term retention, ensuring context without requiring full history.
- Uses **LangChain’s memory components** with **Google Gemini AI** to create dynamic and context-aware chatbots.
- **Branch:** `memory-chatbot`

### 4️⃣ **AI Agents using LangChain**
- Develops **autonomous agents** capable of reasoning and decision-making.
- Utilizes **LangChain's Agent framework** for handling dynamic tasks.
- Implements various tools to perform specific operations, such as string manipulation, mathematical calculations, and frequency analysis.
- The system allows **easy integration of additional agents** for expanding capabilities.
- Uses **LangChain’s prompt engineering** to guide decision-making processes and determine the best tool for each query.
- **Branch:** `AI-agents`

## 🛠️ Tech Stack
- **LangChain** – Core framework
- **OpenAI GPT-4** – LLM for text generation
- **Google Gemini AI** – Language model for translation and retrieval
- **Hugging Face** – Embeddings and models
- **Pinecone** – Vector database for retrieval
- **FastAPI/Flask** – Backend server for deployment
- **Streamlit** – Interactive UI for chatbot demos

## 🏗️ Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/langchain-projects.git
   cd langchain-projects
   ```
2. **Checkout the specific project branch**
   ```bash
   git checkout <translation | RAG-project | memory-projects | agent-project>
   ```
3. **Create a virtual environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the project**
   ```bash
   python main.py
   ```

## 🤝 Contributing
Contributions are welcome! Feel free to submit **issues** or **pull requests** to improve this repository.

## 📜 License
This project is licensed under the **MIT License**.

## 📬 Contact
For any questions, feel free to reach out:
- **Email:** saisudagani141004@gmail.com
- **LinkedIn:** [Sudhagani Sai Sreeja](https://linkedin.com/in/sudhagani-sai-sreeja-88139a259)
