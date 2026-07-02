# Learning ChatBot

A simple, interactive chatbot built with Python that learns from user interactions. The bot answers questions based on a knowledge base and can learn new answers when it encounters unfamiliar questions.

## Features

- 💬 Interactive GUI interface using Tkinter
- 🧠 Knowledge base stored in JSON format
- 🎯 Fuzzy string matching to find the best answer
- 📚 Learning capability - the bot can learn new Q&A pairs from users
- 🔄 Persistent storage of learned answers

## Requirements

- Python 3.8 or higher
- tkinter (usually comes with Python)

### Optional Dependencies

- nltk>=3.8 - For natural language processing
- pandas>=1.3.0 - For data manipulation

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd AI
```

2. Install dependencies (optional):

```bash
pip install -r requirements.txt
```

## Usage

Run the chatbot:

```bash
python LearningChatBot.py
```

### How to Use

1. **Ask a Question**: Type your question in the entry field and press Enter or click "Send"
2. **Get Answers**: The bot will search for a matching answer in its knowledge base
3. **Teach the Bot**: If the bot doesn't know the answer, it will ask you to teach it
4. **Exit**: Type "quit" to close the application

### Example Interaction

```
You: What is Python?
Bot: Python is a high-level programming language known for its simplicity and readability.

You: How do I learn programming?
Bot: I don't know the answer. Can you teach me?
User: By practicing regularly and building projects.
Bot: Thank you, I have learned a new answer.
```

## File Structure

```
├── LearningChatBot.py      # Main chatbot application
├── knowledge_base.json     # Stores Q&A pairs (created automatically)
├── requirements.txt        # Project dependencies
└── README.md              # This file
```

## How It Works

1. **Knowledge Base Loading**: The bot loads questions and answers from `knowledge_base.json`
2. **Question Matching**: Uses fuzzy string matching to find the closest matching question
3. **Answer Retrieval**: Returns the corresponding answer or asks for teaching
4. **Learning**: Stores new Q&A pairs in the JSON file for future use

## Code Structure

### Main Functions

- `load_knowledge_base(file_path)` - Loads Q&A pairs from JSON
- `find_best_match(user_question, questions)` - Finds the closest matching question
- `get_answer_for_question(question, knowledge_base)` - Retrieves answer for a question
- `save_knowledge_base(filename, knowledge_base)` - Saves new Q&A pairs
- `chat_bot()` - Main GUI application

## Technologies Used

- **Python** - Programming language
- **Tkinter** - GUI framework
- **JSON** - Data storage
- **difflib** - Fuzzy string matching

## Future Enhancements

- Add natural language processing (NLP) for better understanding
- Implement sentiment analysis
- Add database support instead of JSON
- Create a web interface
- Add multi-language support
- Implement confidence scoring for answers

## Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the MIT License.

## Author

Created as a learning project for AI and chatbot development.

## Support

For issues or questions, please open an issue in the repository.
