import { GeckoTTS } from '../src/index.js';
const client = new GeckoTTS();
await client.synthesizeToFile('speech.mp3', { text: 'Hello from Gecko TTS.', lang: 'en-in', format: 'mp3' });
console.log('Saved speech.mp3');
