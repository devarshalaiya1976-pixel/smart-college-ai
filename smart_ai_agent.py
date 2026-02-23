print("SMART COLLEGE AI ASSISTANT")
print("Type 'exit' to quit.")

while True:
    question = input("You: ").lower()

    if question == "exit":
        print("AI: Goodbye! Best of luck.")
        break

    elif "study" in question:
        print("AI: I suggest 45 min focused study + 10 min break method.")

    elif "stress" in question or "tension" in question:
        print("AI: Take deep breaths. Break your work into small steps.")

    elif "project" in question:
        print("AI: You can build a chatbot, attendance system, or smart reminder app.")

    elif "hello" in question or "hi" in question:
        print("AI: Hello! How can I help you today?")

    elif "ai" in question:
        print("AI: Artificial Intelligence allows machines to simulate human thinking.")

    else:
        print("AI: That sounds interesting. Tell me more.")