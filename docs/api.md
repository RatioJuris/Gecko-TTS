# API contract

`POST https://www.isrgrajan.com/gecko/tts/index.php`

Headers: `Content-Type: application/json`, `X-API-Key: KEY:SECRET`.

Example body:

```json
{"text":"Hello from Gecko TTS","lang":"en-in","format":"mp3","stream":true}
```

Supply exactly one of `text` or `ssml`. Successful responses contain audio bytes, not a JSON success object. Non-2xx responses should be treated as errors. Actual voices, formats, quotas, and authentication policies are controlled by the deployment.
