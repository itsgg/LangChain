# LangChain Playground

Playground for LangChain experiments and examples.

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
