# Multi-Turn CLI Chatbot

A simple chatbot made with Python using the OpenAI Python SDK and the Groq API. It remembers the conversation, shows replies as they are generated, and lets you change the chatbot's personality during the chat.

## Features

* **Conversation memory:** Remembers everything you and the chatbot have said.
* **Live streaming:** Shows the reply word by word instead of waiting for the full answer.
* **Change personality:** Use `/switch <persona>` to change the chatbot's behavior without losing the conversation.
* **Command-line app:** Runs completely in the terminal.

## Tech Stack

* Python
* OpenAI Python SDK
* Groq API
* python-dotenv

## Setup

1. Clone this repository.

2. Create and activate a virtual environment.

3. Install the required packages:

   ```
   pip install openai python-dotenv
   ```

4. Create a `.env` file in the project folder:

   ```
   GROQ_API_KEY=your_key_here
   ```

5. Run the chatbot:

   ```
   python chatbot.py
   ```

## Usage

Start typing to chat with the bot. It remembers the whole conversation.

### Change the chatbot's personality

```
/switch strict math teacher
```

This changes the chatbot's personality but keeps the conversation history.

### Exit the chatbot

```
exit
```

## Example

```
You : My name is Manasi

Bot : Nice to meet you, Manasi!

You : /switch strict math teacher

Switched to strict math teacher mode.

You : What is my name?

Bot : Your name is Manasi.

You : What is 3 + 4?

Bot : 7.
```

## How It Works

* All messages are stored in a list called `message`.
* Every time you send a message, the whole list is sent to the AI so it remembers the conversation.
* The reply is streamed, so it appears little by little in the terminal.
* When you use `/switch`, only the first message (the developer prompt) is replaced. The rest of the conversation stays the same.

## Notes and Limitations

* Uses Groq's free API with the `openai/gpt-oss-120b` model.
* Chat history is not saved permanently. It is lost when you close the program.
* Personality switching works well, but the chatbot may still show a little of its default behavior sometimes.
