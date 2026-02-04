import json
from database import add_complaint

# Load intents
with open("intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

def detect_intent(user_input):
    user_input = user_input.lower()
    for intent in intents.values():
        for keyword in intent["keywords"]:
            if keyword in user_input:
                return intent["response"]
    return None

def chatbot_response(user_input):
    # 1. Check FAQ intents
    intent_response = detect_intent(user_input)
    if intent_response:
        return intent_response

    # 2. Detect complaint
    complaint_keywords = [
        "not working", "broken", "issue", "problem",
        "complaint", "fan", "light", "water", "electricity"
    ]

    if any(word in user_input.lower() for word in complaint_keywords):
        add_complaint(user_input)
        return "🛠️ Your complaint has been registered successfully."

    # 3. Fallback response
    return (
        "🤖 I can help you with:\n"
        "• Rent & payment\n"
        "• Leave rules\n"
        "• Hostel rules\n"
        "• Registering complaints"
    )
