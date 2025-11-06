import random

class NeuralCore:
    def __init__(self):
        self.responses = [
            "System secure.",
            "Threat level minimal.",
            "Connection stable.",
            "Anomaly detected. Initiate scan?",
        ]

    def analyze_input(self, user_input):
        with open("log.txt", "a") as log_file:
            log_file.write(f"User Input: {user_input}\n")
        user = user_input.lower()
        if "scan" in user:
            return "Initiating full system scan..."
        elif "status" in user:
            return random.choice(self.responses)
        elif "shutdown" in user:
            return "Shutting down neural core..."
        else:
            return "Input not recognized. Please try again."