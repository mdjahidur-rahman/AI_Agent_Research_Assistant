# AI Research Assistant

**AI Research Assistant** is an interactive Python application that leverages large language models (LLMs) to generate structured research summaries. It can perform web searches, query Wikipedia, and optionally save research outputs to text files. This project uses **LangChain** for managing prompts, structured outputs, and tool integration.

---

## Features

- Accepts a **user query** and generates a detailed, multi-sentence research summary.
- Outputs results in **JSON format** with the following fields:
  - `topic` – The main research topic
  - `summary` – An elaborated explanation (3–5 sentences)
  - `sources` – Curated references including names and URLs
  - `tools_used` – List of AI or external tools used
- Optional saving of research results to a **timestamped text file**
- Integrated tools for information retrieval:
  - Wikipedia queries
  - DuckDuckGo web search
- User-controlled saving: The agent saves output **only if requested** in the query.
- Easily extendable to add new research utilities.

---

## Usage

1. Ensure you have installed all dependencies from `requirements.txt`.
2. Create a `.env` file with your API keys:
   OPENAI_API_KEY=your_openai_api_key
3. Run the program:
```bash
python main.py
```

## Tools

The project includes the following tools:

| Tool Name                  | Description                                                                 |
|-----------------------------|-----------------------------------------------------------------------------|
| WikipediaQueryRun           | Fetches summaries from Wikipedia for a given topic.                         |
| DuckDuckGoSearchRun         | Performs web searches to gather additional information.                     |
| save_research_to_file       | Saves research output to a text file **only if requested** by the user.     |

> All tools are modular, so you can easily extend or replace them with other utilities.

---

## Dependencies

The project requires the following Python packages and versions:

| Package                  | Version Requirement  | Purpose                                             |
|---------------------------|-------------------|-----------------------------------------------------|
| Python                    | 3.14+             | Core programming language                           |
| langchain                 | latest            | LLM orchestration, prompts, and agent creation     |
| langchain-community       | latest            | Community tools like Wikipedia and DuckDuckGo      |
| openai                    | latest            | OpenAI API access for LLMs                          |
| pydantic                  | 2.12+             | Data validation and structured outputs             |
| python-dotenv             | latest            | Load environment variables (API keys)             |

Install dependencies using:

```bash
pip install -r requirements.txt
