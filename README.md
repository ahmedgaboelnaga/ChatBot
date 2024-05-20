# ChatBot Project

This ChatBot application is a simple interactive bot that uses a JSON-based knowledge base to answer user questions. If the bot doesn't know the answer, it can learn from the user's input. The GUI is created using the Tkinter library.

## Features
- Loads and saves a knowledge base in JSON format.
- Uses difflib to find the best match for user questions.
- Allows the bot to learn new answers if it doesn't know the answer to a question.
- Simple Tkinter-based GUI with a chat area, user input field, and send button.

## Requirements
- Python 3.x
- Tkinter (usually included with Python)
- JSON module (included with Python)
- difflib module (included with Python)

## Files
- `chatbot.py`: The main script containing the ChatBot class and functionality.
- `Knowledge_base.json`: The JSON file containing the knowledge base.

## Usage
1. Ensure you have Python installed on your system.
2. Place the `chatbot.py` script and `Knowledge_base.json` file in the same directory.
3. Run the script by executing `python chatbot.py` in your terminal or command prompt.

## Knowledge Base Structure
The knowledge base is stored in a JSON file and structured as follows:
```json
{
    "questions": [
        {
            "question": "What is AI?",
            "answer": "AI stands for Artificial Intelligence."
        },
        {
            "question": "What is Python?",
            "answer": "Python is a programming language."
        }
    ]
}
```

## Script Explanation

### `load_knowledge_base(file_path: str) -> dict`
Loads the knowledge base from the specified JSON file.

### `save_knowledge_base(file_path: str, data: dict) -> None`
Saves the knowledge base to the specified JSON file.

### `find_best_match(user_question: str, questions: list[str]) -> str | None`
Finds the best match for a user's question from a list of known questions using difflib.

### `get_answer_to_question(question: str, knowledge_base: dict) -> str | None`
Retrieves the answer to a specific question from the knowledge base.

### `ChatBotApp`
The main class for the ChatBot application, which initializes the Tkinter GUI and handles user interactions.

### `send_message(event=None)`
Handles the logic for sending and receiving messages, including learning new answers.

### `display_message(message)`
Displays a message in the chat area.

## Example
Run the script and interact with the bot in the GUI. If the bot doesn't know the answer to a question, it will prompt you to teach it. Type your answer or write "skip" to skip teaching.

## License
This project is licensed under the MIT License. Feel free to use and modify the code as per the terms of the license.

## Contact
For any questions or suggestions, please contact ahmedgaboelnaga@gmail.com.
