# Local LLM Document Summarizer

A Python-based tool for summarizing large text documents using local Large Language Models (LLMs) via Ollama. This project efficiently processes documents of any size by intelligently chunking, summarizing, and iteratively condensing content until it reaches a manageable size.

## Features

- **Large Document Processing**: Handles documents of any size through intelligent chunking
- **Iterative Summarization**: Repeatedly summarizes content until reaching the target length
- **Local LLM Integration**: Uses Ollama for privacy-focused, offline text processing
- **Configurable Parameters**: Customize chunk size, overlap, and output length
- **Progress Tracking**: Monitor the summarization process with detailed iteration logs
- **Automatic Rate Limiting**: Prevents server overload with configurable pause intervals
- **Persistent Results**: Saves intermediate and final summaries for review

## Demo

![Demo](https://github.com/atorov/shrd-local-llm-summarizer-py/blob/master/public/demo.gif)

## 🔧 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.ai/) installed and running locally
- A compatible LLM model (e.g., qwen3, llama2, mistral)

## Installation

1 Clone the repository:

```bash
git clone https://github.com/atorov/shrd-local-llm-summarizer-py.git
cd shrd-local-llm-summarizer-py
```

2 Install dependencies:

```bash
pip install -r requirements.txt
```

3 Install and start Ollama:

```bash
# Follow instructions at https://ollama.ai/
ollama serve
```

4 Pull your preferred model:

```bash
ollama pull qwen3
```

## Usage

1 Place your document in the `documents/` directory

2 Configure the parameters in `main.ipynb`:

```python
CHUNK_LEN = 5000                    # Characters per chunk
CHUNK_OVERLAP_LEN = 1000            # Overlap between chunks
DEFAULT_ASSISTANT_MODEL = "qwen3"   # Your Ollama model
DOCUMENT_FILENAME = "your_file.txt" # Document to summarize
LEN_LIMIT = 5000                    # Target summary length
```

3 Run the notebook:

- Open `main.ipynb` in Jupyter or VS Code
- Execute all cells

4 Find your summary in the `results/` directory

## How It Works

1 **Document Loading**: Reads the entire document into memory
2 **Initial Chunking**: Splits the document into overlapping chunks
3 **Iterative Summarization**:

- Summarizes each chunk using the LLM
- Concatenates summaries
- If still above length limit, re-chunks and repeats

4 **Final Output**: Produces a concise summary within the specified length limit

### Example Output Structure

The final summary is formatted with section separators (`ø`) for readability:

```text
ø Summary of chunk 1

ø Summary of chunk 2

ø Summary of chunk 3
```

## Configuration Options

| Parameter                       | Description                      | Default |
| ------------------------------- | -------------------------------- | ------- |
| `CHUNK_LEN`                     | Size of each text chunk          | 5000    |
| `CHUNK_OVERLAP_LEN`             | Character overlap between chunks | 1000    |
| `DEFAULT_ASSISTANT_MODEL`       | Ollama model to use              | "qwen3" |
| `LEN_LIMIT`                     | Maximum summary length target    | 5000    |
| `PREVENT_OVERLOAD_PAUSE`        | Pause duration (seconds)         | 10      |
| `PREVENT_OVERLOAD_PAUSE_PERIOD` | Chunks before pause              | 25      |

## Technical Details

### Summarization Prompt

The tool uses a carefully crafted prompt that instructs the LLM to:

- Create concise summaries in 3 sentences or fewer
- Capture main ideas, supporting details, and conclusions
- Maintain objectivity and original tone
- Preserve factual accuracy
