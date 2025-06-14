# OpenAI Agent Project

A Python project that demonstrates the use of OpenAI Agents SDK with Google Gemini API. This project uses modern Python tooling with `uv` for dependency management and includes a simple agent implementation.

## Prerequisites

- Python 3.8 or higher
- Git
- A Google Gemini API key
- `uv` package manager (recommended)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ShaheerShahzadOfficial/openai-agents-assignment.git
cd openai-agents-assignment/openai-agent
```

2. Create and activate a virtual environment:

For Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

For macOS/Linux:
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies using `uv`:
```bash
uv pip install -r requirements.txt
```

Or using pip:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root:
```bash
# Windows
echo GEMINI_API_KEY=your_gemini_api_key_here > .env
echo GEMINI_API_BASE=https://generativelanguage.googleapis.com/v1beta/openai/ >> .env
echo GEMINI_MODEL=gemini-2.0-flash >> .env

# macOS/Linux
echo "GEMINI_API_KEY=your_gemini_api_key_here" > .env
echo "GEMINI_API_BASE=https://generativelanguage.googleapis.com/v1beta/openai/" >> .env
echo "GEMINI_MODEL=gemini-2.0-flash" >> .env
```

Replace `your_gemini_api_key_here` with your actual Google Gemini API key.

## Project Structure
```
openai-agent/
├── .env                    # Environment variables (create this)
├── .gitignore             # Git ignore file
├── .python-version        # Python version specification
├── README.md              # This file
├── main.py               # Main application file
├── pyproject.toml        # Project configuration
├── uv.lock              # UV dependency lock file
└── .venv/               # Virtual environment directory
```

## Running the Project

Run the main application:
```bash
python main.py
```

## Features

- Uses `uv` for fast dependency management
- Implements OpenAI Agents SDK with Gemini API
- Modern Python project structure with `pyproject.toml`
- Environment-based configuration
- Virtual environment management

## Troubleshooting

1. If you get an error about missing dependencies:
```bash
uv pip install -r requirements.txt
```

2. If you get an error about API keys:
- Make sure your `.env` file exists in the project root
- Verify that your Gemini API key is correct
- Check that the `GEMINI_API_BASE` and `GEMINI_MODEL` are set correctly

3. If you get a virtual environment error:
- Make sure you've activated the virtual environment
- Try recreating the virtual environment:
```bash
deactivate  # if active
rm -rf .venv  # or rmdir /s /q .venv on Windows
python -m venv .venv
# Then activate again using the commands in Installation step 2
```

4. If you have issues with `uv`:
- Make sure `uv` is installed: `pip install uv`
- Try using regular pip instead: `pip install -r requirements.txt`

## Development

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 