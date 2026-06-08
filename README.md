# Generative_AI

A hands-on repository of LangChain-based generative AI examples, demos, and prototypes. This workspace includes chatbot implementations, chain examples, retrieval-augmented generation (RAG) experiments, prompt designs, structured output demos, and model integrations with OpenAI and other providers.

## Repository Structure

- `LangChain/`
  - `chatbot_gpt_langchain.py` - Streamlit chatbot demo using OpenAI's `gpt-3.5-turbo` via LangChain.
  - `ollama_chatbot_langchain.py` - Streamlit chatbot demo with LangChain prompt and output parser.
  - `open_ai_practice.ipynb` - Notebook for experimenting with OpenAI and LangChain.
  - `shashi.py` - Simple ChatOpenAI invocation example.
  - `Agents/` - Notes and examples for LangChain agent workflows.
  - `chains/` - Demonstrations of simple, sequential, and parallel LangChain pipelines.
  - `indexes/` - Introductory files for indexing concepts.
  - `memory/` - Notes on memory usage in LangChain.
  - `models/`
    - `chatModels/` - Chat model wrappers and provider integration examples.
    - `LLMs/` - Base large language model examples.
    - `OpenSource/` - Placeholder for open-source model experiments.
  - `pdfReaaders/` - Document loader notes and examples for PDF processing.
  - `prompts/` - Prompt engineering examples and reusable prompt patterns.
  - `rag/` - Retrieval-augmented generation notes and examples.
  - `structured_output/` - Examples of structured output parsing using Pydantic and other LangChain tools.
  - `website_controlling_model/` - A demo notebook for browser-based model control.

## Key Topics Covered

- Chatbot applications with LangChain and OpenAI.
- Prompt templates and prompt engineering patterns.
- Chain composition: simple, sequential, and parallel workflows.
- Retrieval Augmented Generation (RAG) concepts and document loading.
- Structured output parsing with Pydantic.
- Agent reasoning and tool-based workflows.
- Basic OpenAI and Anthropic model integration examples.

## Getting Started

1. Clone this repository.
2. Create a `.env` file in the project root or `LangChain/` folder with your API credentials, for example:

```env
OPENAI_API_KEY=your_openai_api_key_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

3. Install Python dependencies. Example:

```bash
pip install langchain langchain-openai python-dotenv streamlit pydantic
```

Optionally install other providers or connectors as needed for your environment.

## Usage Examples

- Run the OpenAI Streamlit chatbot demo:

```bash
streamlit run LangChain/chatbot_gpt_langchain.py
```

- Run the Ollama/Streamlit example:

```bash
streamlit run LangChain/ollama_chatbot_langchain.py
```

- Run a simple model invocation:

```bash
python LangChain/models/chatModels/chatOpenAI.py
```

- Explore chain examples:

```bash
python LangChain/chains/simplechain.py
python LangChain/chains/sequential_chain.py
python LangChain/chains/parallel chain.py
```

## Notes

- This repository is primarily an exploratory playground for LangChain workflows and generative AI concepts.
- Some scripts depend on external API keys and may require updating to match your local provider configuration.
- Notebooks are included for experimentation and learning; adapt them to your own datasets and workflows.