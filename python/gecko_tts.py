"""Minimal synchronous Gecko TTS client."""
import os
from pathlib import Path
import requests

DEFAULT_URL = "https://www.isrgrajan.com/gecko/tts/index.php"

class GeckoTTSError(RuntimeError):
    def __init__(self, status_code, message):
        super().__init__(f"Gecko TTS HTTP {status_code}: {message}")
        self.status_code = status_code

class GeckoTTS:
    def __init__(self, key=None, secret=None, base_url=None, timeout=90, session=None):
        self.key = key or os.getenv("GECKO_TTS_KEY")
        self.secret = secret or os.getenv("GECKO_TTS_SECRET")
        self.base_url = base_url or os.getenv("GECKO_TTS_URL", DEFAULT_URL)
        self.timeout = timeout
        self.session = session or requests.Session()
        if not self.key or not self.secret:
            raise ValueError("Set key/secret or GECKO_TTS_KEY and GECKO_TTS_SECRET.")

    def synthesize(self, *, text=None, ssml=None, lang=None, format="mp3", stream=True):
        has_text = isinstance(text, str) and bool(text)
        has_ssml = isinstance(ssml, str) and bool(ssml)
        if has_text == has_ssml:
            raise ValueError("Provide exactly one non-empty text or ssml value.")
        payload = {"text" if has_text else "ssml": text if has_text else ssml,
                   "format": format, "stream": stream}
        if lang: payload["lang"] = lang
        response = self.session.post(self.base_url, json=payload, timeout=self.timeout, headers={
            "X-API-Key": f"{self.key}:{self.secret}",
            "Accept": "audio/*, application/octet-stream, application/json"})
        if not response.ok:
            raise GeckoTTSError(response.status_code, response.text[:1200].strip() or response.reason)
        return response.content

    def synthesize_to_file(self, path, **kwargs):
        target = Path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(self.synthesize(**kwargs))
        return target
