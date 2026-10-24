from gecko_tts import GeckoTTS

client = GeckoTTS()
client.synthesize_to_file("speech.mp3", text="Hello from Gecko TTS.", lang="en-in", format="mp3")
print("Saved speech.mp3")
