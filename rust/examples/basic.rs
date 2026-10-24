use gecko_tts::GeckoTTS;
fn main()->Result<(),Box<dyn std::error::Error>>{let c=GeckoTTS::new(None,None)?;c.synthesize_to_file("speech.mp3","Hello from Gecko TTS.",Some("en-in"),"mp3")?;println!("Saved speech.mp3");Ok(())}
