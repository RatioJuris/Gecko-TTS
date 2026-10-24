using GeckoTTS;
using var client=new GeckoTTSClient();
await client.SynthesizeToFileAsync("speech.mp3",text:"Hello from Gecko TTS.",lang:"en-in",format:"mp3");
Console.WriteLine("Saved speech.mp3");
