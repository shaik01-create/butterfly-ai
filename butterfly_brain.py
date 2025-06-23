import os
from dotenv import load_dotenv

load_dotenv()

def run_butterfly():
    print("🦋 Hello Sonu, I am Butterfly, your AI assistant.")
    while True:
        command = input("You: ").lower()

        if "crypto" in command or "btc" in command:
            os.system("python tasks/binance_tracker.py")
        elif "youtube" in command:
            os.system("python tasks/youtube_tracker.py")
        elif "voice" in command:
            os.system("python voice/voice_input.py")
        elif "exit" in command:
            print("Goodbye, Sonu.")
            break
        else:
            print("Sorry, I didn't get that. Try 'crypto', 'youtube', or 'voice'.")

if __name__ == "__main__":
    run_butterfly()

