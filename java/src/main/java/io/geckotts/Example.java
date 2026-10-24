package io.geckotts;
import java.nio.file.Path;
public class Example { public static void main(String[] args) throws Exception { GeckoTTS c=new GeckoTTS(System.getenv("GECKO_TTS_KEY"),System.getenv("GECKO_TTS_SECRET")); c.synthesizeToFile(Path.of("speech.mp3"),"Hello from Gecko TTS.","en-in","mp3"); System.out.println("Saved speech.mp3"); } }
