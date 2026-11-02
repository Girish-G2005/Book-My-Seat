from enum import Enum
import ollama
import json

class Intent(Enum):
    GREETING = "GREETING"
    CHECK_AVAILABILITY = "CHECK_AVAILABILITY"
    BOOK_SEAT = "BOOK_SEAT"
    CANCEL_BOOKING = "CANCEL_BOOKING"
    OTHER = "OTHER"


def get_intent(message):
    schema = {
        "type": "object",
        "properties": {
            "intent": {
                "type": "string",
                "enum": [intent.value for intent in Intent]
            }
        },
        "required": ["intent"],
        "additionalProperties": False
    }

    response = ollama.chat(
        model = "jarvis:latest",
        messages = [
            {
                "role": "system",
                "content": (
                        "You are an intent classifier for a seat-booking application. "
                        "Classify the user's message into exactly one of these intents: "

                        "GREETING: Basic greetings and casual pleasantries. "

                        "CHECK_AVAILABILITY: Asking about the number of free or available seats. "

                        "BOOK_SEAT: Explicitly requesting to book a random available seat. "

                        "CANCEL_BOOKING: Requesting cancellation of their current booking. "

                        "OTHER: Unrelated requests or messages that do not match the above intents. "

                        "Understand the user's actual intention, not just individual keywords. "
                        "Pay attention to negation. For example, "
                        "'Don't book me a seat, just tell me how many are free' "
                        "must be classified as CHECK_AVAILABILITY. "

                        "Return only the intent in the required JSON format."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ],
        format = schema,
        think = False
    )

    try:
        result = json.loads(response.message.content)
        return Intent(result["intent"])
    except (json.JSONDecodeError, KeyError, ValueError, TypeError):
        return Intent.OTHER