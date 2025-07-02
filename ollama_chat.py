import requests
import json
import sys

# Configuration for your Ollama instance
# Ollama must be running on localhost
OLLAMA_HOST = "http://127.0.0.1"
OLLAMA_PORT = "11434"
OLLAMA_BASE_URL = f"{OLLAMA_HOST}:{OLLAMA_PORT}/api"
ALLOWED_MODEL = "llama3:8b"

# Conversation history, stored as a list of dictionaries
messages = []

def chat_with_ollama():
    print("-" * 50)
    print(f"Welcome to {ALLOWED_MODEL}!")
    print("Type 'exit' or 'quit' to end the session.")
    print("-" * 50)

    # Optional: Add an initial system message
    messages.append({"role": "system", "content": "You are a helpful AI assistant, running on a debian server for students in the University of Dayton chapter of ACM."})

    while True:
        try:
            user_input = input("You: ").strip()

            if user_input.lower() in ["exit", "quit"]:
                print("-" * 50)
                break

            if not user_input:
                continue

            # Add user message to history
            messages.append({"role": "user", "content": user_input})

            # Prepare the payload for the /api/chat endpoint
            payload = {
                "model": ALLOWED_MODEL,
                "messages": messages,
                "stream": True  # Crucially, set to True for streaming
            }

            print("Ollama: ", end="", flush=True) # Print prompt and flush immediately

            full_assistant_response_content = ""
            try:
                with requests.post(f"{OLLAMA_BASE_URL}/chat", json=payload, stream=True) as response:
                    response.raise_for_status() # Raise an exception for HTTP errors (4xx or 5xx)

                    for chunk in response.iter_content(chunk_size=None):
                        if chunk:
                            try:
                                # Decode and split by lines, as each line is a separate JSON object
                                for line in chunk.decode('utf-8').splitlines():
                                    if line.strip(): # Ensure line is not empty
                                        json_data = json.loads(line)
                                        # Check if it's a message chunk
                                        if "message" in json_data and "content" in json_data["message"]:
                                            content = json_data["message"]["content"]
                                            print(content, end="", flush=True) # Print token immediately
                                            full_assistant_response_content += content
                                        # Check for the 'done' flag
                                        if json_data.get("done"):
                                            break # End of stream
                            except json.JSONDecodeError:
                                # Handle cases where a line might not be a complete JSON object yet
                                # (less common with stream=True but good practice)
                                continue

                print() # Newline after the full streamed response

                # Add assistant's complete response to history if content was received
                if full_assistant_response_content:
                    messages.append({"role": "assistant", "content": full_assistant_response_content})
                else:
                    print("Warning: Received no content from Ollama for this turn.", file=sys.stderr)
                    # Optionally remove the last user message if no valid response came back
                    messages.pop()

            except requests.exceptions.ConnectionError:
                print(f"\nError: Could not connect to Ollama at {OLLAMA_HOST}:{OLLAMA_PORT}.", file=sys.stderr)
                print("Please ensure the Ollama server is running on your system.", file=sys.stderr)
                print(f"Also, make sure you have pulled the '{ALLOWED_MODEL}' model.", file=sys.stderr)
                # Remove the last user message from history if connection failed
                messages.pop()
            except requests.exceptions.RequestException as e:
                print(f"\nAn API error occurred: {e}", file=sys.stderr)
                if response and response.text:
                    print(f"Response details: {response.text}", file=sys.stderr)
                # Remove the last user message from history if API error occurred
                messages.pop()
            except Exception as e:
                print(f"\nAn unexpected error occurred: {e}", file=sys.stderr)
                messages.pop()

        except EOFError: # Handles Ctrl+D
            print("\n" + "-" * 50)
            print("Chat session ended (EOF). Goodbye!")
            break
        except KeyboardInterrupt: # Handles Ctrl+C
            print("\n" + "-" * 50)
            print("Chat session interrupted. Goodbye!")
            break

if __name__ == '__main__':
    chat_with_ollama()
