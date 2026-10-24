```bash
curl --fail-with-body --silent --show-error \\
  -X POST -H 'Content-Type: application/json' \\
  -H "X-API-Key: ${GECKO_TTS_KEY}:${GECKO_TTS_SECRET}" \\
  --data '{"text":"Hello from Gecko TTS","lang":"en-in","format":"mp3","stream":true}' \\
  "${GECKO_TTS_URL:-https://www.isrgrajan.com/gecko/tts/index.php}" -o speech.mp3
```
