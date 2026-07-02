# Learning ChatBot

A simple Python Learning ChatBot with a Tkinter GUI that stores its knowledge in a JSON file and learns new question-and-answer pairs from user interactions.

## Features

- Interactive GUI built with Tkinter
- Knowledge base stored in JSON format
- Fuzzy string matching using Python's `difflib`
- Learns new question-and-answer pairs from users
- Automatically saves learned answers for future use
- Persistent knowledge base between sessions

## Requirements

- Python 3.8 or higher
- Tkinter (included with most Python installations)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/1000red/learning-chatbot-python.git
cd learning-chatbot-python
```

2. Install dependencies (optional):

```bash
pip install -r requirements.txt
```

> **Note:** This project uses only Python's standard library, so no additional packages are required.

## Usage

Run the chatbot:

```bash
python LearningChatBot.py
```

## How to Use

1. Type your question in the input field.
2. Press **Enter** or click **Send**.
3. If the chatbot finds a matching question, it displays the corresponding answer.
4. If it doesn't know the answer, it asks you to teach it.
5. The new question and answer are automatically saved in `knowledge_base.json`.
6. Type **quit** to exit the application.

## Example Interaction

```text
You: What is Python?
Bot: Python is a high-level programming language known for its simplicity and readability.

You: How do I learn programming?
Bot: I don't know the answer. Can you teach me?

User: By practicing regularly and building projects.

Bot: Thank you, I have learned a new answer.
```

## File Structure

```text
learning-chatbot-python/
├── LearningChatBot.py
└── README.md
```

## How It Works

1. Loads all questions and answers from `knowledge_base.json`.
2. Uses `difflib.get_close_matches()` to find the closest matching question.
3. Returns the corresponding answer if a match is found.
4. If no suitable match exists, the chatbot asks the user for the correct answer.
5. The new question and answer are saved to the JSON knowledge base for future conversations.

## Main Functions

- `load_knowledge_base()` – Loads questions and answers from the JSON file.
- `find_best_match()` – Finds the closest matching question.
- `get_answer_for_question()` – Retrieves the corresponding answer.
- `save_knowledge_base()` – Saves newly learned questions and answers.
- `chat_bot()` – Starts the graphical chatbot application.

## Technologies Used

- Python
- Tkinter
- JSON
- difflib (Fuzzy String Matching)

## Future Enhancements

- Improve question matching accuracy
- Add Natural Language Processing (NLP)
- Store data in a database instead of JSON
- Develop a web-based interface
- Support multiple languages
- Improve the graphical user interface

## Contributing

Contributions are welcome. Feel free to fork the repository and submit a pull request.

## License

This project is provided for educational purposes.

## Author

Created as a learning project for Python programming and chatbot development.

## Support

If you find a bug or have a suggestion, please open an issue in this repository.
