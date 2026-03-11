from google import genai
import speech_recognition as sr
from gtts import gTTS
import pygame
import io

# 1. Setup Gemini Client
client = genai.Client(api_key="YOUR_API_KEY") # API key
MODEL_ID = "models/gemini-flash-lite-latest" # working model ID

# 2. Setup Audio Player (Pygame)
pygame.mixer.init()

# --- GOOGLE VOICE FUNCTION ---
def speak(text):
    # Special characters hata rahe hain
    clean_text = text.replace('*', '').replace('#', '').replace('_', '').replace('\n', ' ')
    print(f"AI: {clean_text}")
    
    try:
        # Google Text-to-Speech for audio Generation
        tts = gTTS(text=clean_text, lang='en', tld='co.in') # 'co.in' for Indian English accent 
        
        # Audio saved in memory then played (No file creation needed)
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)
        
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()
        
        # wait until the audio finishes playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
    except Exception as e:
        print(f"Bolne mein error: {e}")
# -----------------------------------

def listen():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        rec.pause_threshold = 1 
        rec.adjust_for_ambient_noise(source, duration=1)
        audio = rec.listen(source)
    try:
        query = rec.recognize_google(audio, language='en-US')
        print(f"User: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return "none"
    except sr.RequestError:
        print("Network error.")
        return "none"

# --- Main Program ---
speak("Hello, I am ready. How can I help you today?")

while True:
    user_input = listen()
    
    if any(word in user_input.lower() for word in ["exit", "stop", "bye", "goodbye"]):
        speak("Goodbye! Have a great day.")
        break
    
    if user_input != "none":
        prompt = f"System: Act as a helpful AI assistant. Answer in simple plain text without any bold, italics, or markdown formatting. User says: {user_input}"
        
        try:
            response = client.models.generate_content(
                model=MODEL_ID, 
                contents=prompt
            )
            speak(response.text)
        except Exception as e:
            print(f"Error: {e}")

            speak("I encountered an error.")
