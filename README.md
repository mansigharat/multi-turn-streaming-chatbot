# Multi-Turn CLI Chatbot

A simple command-line chatbot built with Python and the OpenAI Responses API (via Groq). Supports full conversation memory, live streamed replies, and mid-conversation system prompt switching.

## Features

- **Multi-turn memory**: the bot remembers everything said earlier in the conversation, not just the last message
- **Streaming output**: replies appear live in the terminal, piece by piece, instead of waiting for the full answer
- **System prompt switching**: change the bot's persona mid-chat using `/switch <persona>`, without losing conversation history
- **Simple CLI interface**: no frontend, just terminal in and out

## Tech Stack

- Python
- OpenAI Python SDK
- Groq API (OpenAI-compatible endpoint, used as a free alternative to OpenAI's paid API)
- python-dotenv for API key management

## Setup

1. Clone this repo
2. Create a virtual environment and activate it
3. Install dependencies:
   ```
   pip install openai python-dotenv
   ```
4. Create a `.env` file in the project root with your Groq API key:
   ```
   GROQ_API_KEY=your_key_here
   ```
5. Run the chatbot:
   ```
   python chatbot.py
   ```

## Usage

Type normally to chat. The bot keeps track of everything said so far.

**Switch the bot's persona:**
```
/switch strict math teacher
```
This replaces the bot's system instructions on the spot. Conversation history is kept, only the persona changes.

**Exit the chat:**
```
exit
```

## Example

```
You : My name is Manasi
Bot: Nice to meet you, Manasi! How can I help you today?

You : /switch strict math teacher
Switched to strict math teacher mode.

You : what is my name
Bot: Your name is Manasi.

You : what is 3 + 4
Bot: 7. Remember, addition combines quantities: 3 + 4 = 7.
```

## How It Works

- All messages (developer, user, and assistant) are stored in a single growing list called `message`
- Every API call sends the entire list, not just the newest message, since the model has no memory of its own between calls
- Streaming is handled by looping over `response.output_text.delta` events and printing each piece as it arrives
- `/switch` works by replacing `message[0]`, the developer instruction, instead of appending a new one, so there is only ever one active persona at a time

## Notes and Limitations

- Uses `openai/gpt-oss-120b` on Groq's free tier, not OpenAI's actual paid models
- No persistent storage: conversation history resets every time the script restarts
- Persona switching changes tone and behavior noticeably, but the model's own default personality can still bleed through a little even under a strict persona

