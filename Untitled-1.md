**Step 1: Setup**
- Import the OpenAI client, dotenv loader, and os module
- Load your environment variables from the .env file
- Create a client object, pointing it to Groq's API endpoint instead of OpenAI's default, using your Groq API key

**Step 2: Set up the starting conversation**
- Create a list called `message` that will hold the whole conversation
- Add one starting entry to it: a system-level instruction telling the assistant what role to play (default: "You are a helpful assistant")

**Step 3: Start an infinite loop**
- This loop keeps the chat running until the user decides to quit

**Step 4: Get user input**
- Ask the user to type something
- Store it in a variable

**Step 5: Handle the "switch role" command**
- Check if the input starts with "/switch"
- If yes, take the text after "/switch" and clean up extra spaces, this becomes the new role
- Replace the first item in your `message` list with a new system instruction using that role
- Print a confirmation message
- Skip the rest of the loop and go back to asking for input again

**Step 6: Handle the exit command**
- Check if the input (lowercase) equals "exit"
- If yes, break out of the loop

**Step 7: Add user message to history**
- Append the user's input to the `message` list as a "user" role entry

**Step 8: Call the API with streaming on**
- Send the full `message` list to the model
- Turn on streaming so you get the reply piece by piece instead of waiting for the whole thing

**Step 9: Print the reply as it streams in**
- Set up an empty string to collect the full reply
- Loop through each event coming from the streamed response
- Check if the event type is a text delta (a small chunk of new text)
- If yes, print that chunk immediately without a newline, and also add it to your full reply string

**Step 10: Save the assistant's reply**
- After the streaming loop ends, print a newline
- Append the full reply to the `message` list as an "assistant" role entry, so the bot remembers what it said

**Step 11: Loop back**
- Go back to Step 4 and wait for the next user input
