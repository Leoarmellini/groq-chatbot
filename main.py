import requests

# API Configuration
API_KEY = "your_api_key_here"
API_URL = "https://api.groq.com/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def ask_groq(question):
    """Send a question to the Groq API and return the response."""
    data = {
        "model": "groq-llama3-8b",
        "messages": [{"role": "user", "content": question}]
    }
    response = requests.post(API_URL, json=data, headers=HEADERS)
    
    return (
        response.json()["choices"][0]["message"]["content"]
        if response.status_code == 200
        else f"Error: {response.status_code}, {response.text}"
    )

def main():
    """Loop for user interaction until 'quit' is entered."""
    print("Welcome to the Groq chatbot! Type 'quit' to exit.")
    while (user_input := input("You: ")) != "quit":
        print("Groq:", ask_groq(user_input))
    print("Goodbye!")

if __name__ == "__main__":
    main()
