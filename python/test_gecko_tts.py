import unittest
from unittest.mock import Mock
from gecko_tts import GeckoTTS, GeckoTTSError

class Tests(unittest.TestCase):
    def setUp(self):
        self.session = Mock()
        self.client = GeckoTTS("key", "secret", "https://example.test/tts", session=self.session)
    def test_success_bytes_and_header(self):
        self.session.post.return_value = Mock(ok=True, content=b"audio")
        self.assertEqual(self.client.synthesize(text="hi"), b"audio")
        self.assertEqual(self.session.post.call_args.kwargs["headers"]["X-API-Key"], "key:secret")
    def test_http_error(self):
        self.session.post.return_value = Mock(ok=False, status_code=401, text="invalid", reason="Unauthorized")
        with self.assertRaises(GeckoTTSError): self.client.synthesize(text="hi")
    def test_exactly_one_input(self):
        with self.assertRaises(ValueError): self.client.synthesize()

if __name__ == "__main__": unittest.main()
