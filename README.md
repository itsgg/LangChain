# LangChain Playground

Playground for LangChain experiments and examples.

## Examples

1. **Basic Chat** (`01_basic_chat.py`): Simple example of using ChatOpenAI for basic question answering.
2. **Streaming Chat** (`02_streaming_chat.py`): Demonstrates streaming responses from ChatGPT for real-time output.
3. **Batch Processing** (`03_batch_chat.py`): Shows how to process multiple chat requests concurrently.
4. **Translation Prompt** (`04_translation_prompt.py`): Example of using prompt templates for language translation.
5. **Business Name Generator** (`05_business_name_generator.py`): Advanced example of using templates to generate business names with specific criteria.

## Setup

### Prerequisites

- [asdf](https://asdf-vm.com/) - Version manager for Python
- asdf Python plugin (install with `asdf plugin add python`)
- Python 3.11.11 (managed via asdf)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/itsgg/LangChain.git
cd LangChain
```

2. Install Python using asdf:

```bash
asdf install
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### Environment Setup

1. Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

2. Add your OpenAI API key to the `.env` file:

```
OPENAI_API_KEY="your-api-key-here"
```
