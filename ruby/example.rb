require_relative 'gecko_tts'
GeckoTTS::Client.new.synthesize_to_file('speech.mp3', text: 'Hello from Gecko TTS.', lang: 'en-in', format: 'mp3')
puts 'Saved speech.mp3'
