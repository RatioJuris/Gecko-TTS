# Gecko TTS SDKs

Multi-language client starter kit for the Gecko TTS HTTP API.

- **Endpoint:** `https://www.isrgrajan.com/gecko/tts/index.php`
- **Method:** `POST`
- **Authentication:** `X-API-Key: KEY:SECRET`
- **Request:** JSON with exactly one of `text` or `ssml`; optional `lang`, `format`, `stream`
- **Success:** raw audio bytes in the response body
- **Failure:** non-2xx HTTP response, often with a JSON error body

> Independent SDK project. Verify live API behavior and format/voice availability before publishing a stable release.

## Quick start: cURL

```bash
export GECKO_TTS_KEY='your-key'
export GECKO_TTS_SECRET='your-secret'
curl --fail-with-body --silent --show-error \\
  -X POST \\
  -H 'Content-Type: application/json' \\
  -H "X-API-Key: ${GECKO_TTS_KEY}:${GECKO_TTS_SECRET}" \\
  --data '{"text":"Hello from Gecko TTS","lang":"en-in","format":"mp3","stream":true}' \\
  'https://www.isrgrajan.com/gecko/tts/index.php' -o speech.mp3
```

## Language clients

| Language | Directory | Requirements |
|---|---|---|
| cURL | `curl/` | cURL |
| Python | `python/` | Python 3.9+, `requests` |
| PHP | `php/` | PHP 8.1+, cURL extension |
| Go | `go/` | Go 1.20+ |
| JavaScript / Node.js | `node/` | Node.js 18+, built-in `fetch` |
| Ruby | `ruby/` | Ruby 3.1+ |
| Java | `java/` | JDK 11+ |
| C# | `csharp/` | .NET 8 |
| Rust | `rust/` | Stable Rust, `reqwest` |

## Python

```bash
python -m pip install requests
export GECKO_TTS_KEY='your-key' GECKO_TTS_SECRET='your-secret'
python python/example.py
```

## PHP

```bash
export GECKO_TTS_KEY='your-key' GECKO_TTS_SECRET='your-secret'
php php/example.php
```

## Go

Replace `YOUR_GITHUB_USERNAME` in Go module/import paths, then run `go run ./examples/go` from `go/`.

## Node.js

```bash
export GECKO_TTS_KEY='your-key' GECKO_TTS_SECRET='your-secret'
node node/examples/example.mjs
```

## Request fields

| Field | Meaning |
|---|---|
| `text` | Plain text to synthesize. Use `text` or `ssml`, not both. |
| `ssml` | SSML/XML input, if supported by the deployed service. |
| `lang` | Language/voice mapping. Examples in deployment docs include `en-in`, `hi`, `ur`. |
| `format` | Requested audio format, such as `mp3` or `wav`; availability depends on deployment. |
| `stream` | Compatibility option included in gateway examples. These simple SDKs buffer the returned body before writing it. |

## Security

- Keep credentials in environment variables or a secret manager.
- Never commit `.env`, API secrets, or real credentials.
- Never embed private credentials in browser JavaScript or mobile app bundles.
- Keep public demo keys quota-limited; never put an unlimited key in public clients.
- Do not send confidential text through a public demo.
- Rotate credentials immediately if exposed.

## Error handling

The gateway returns audio bytes on success, not a JSON success object. Treat non-2xx responses as errors. SDK errors include HTTP status and a bounded response excerpt. Avoid logging secrets or full sensitive text.

## License

MIT; see `LICENSE`.
