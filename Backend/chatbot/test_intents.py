from intents import get_intent

messages = [
    "Hi Jarvis",
    "How many seats are available?",
    "Book me a seat",
    "Cancel my booking",
    "Can you sing a song?",
    "Don't book me a seat, just tell me how many are free"
]

for message in messages:
    intent = get_intent(message)
    print(f"Message: {message}")
    print(f"Intent: {intent.name}")
    print("----------------------")

