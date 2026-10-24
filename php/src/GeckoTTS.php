<?php
declare(strict_types=1);
namespace GeckoTTS;
use RuntimeException;
final class GeckoTTSError extends RuntimeException { public function __construct(public readonly int $statusCode, string $message) { parent::__construct("Gecko TTS HTTP {$statusCode}: {$message}"); } }
final class GeckoTTS {
    public const DEFAULT_URL = 'https://www.isrgrajan.com/gecko/tts/index.php';
    public function __construct(private readonly string $key, private readonly string $secret, private readonly string $baseUrl = self::DEFAULT_URL, private readonly int $timeout = 90) {
        if ($key === '' || $secret === '') throw new \InvalidArgumentException('API key and secret are required.');
        if (!extension_loaded('curl')) throw new RuntimeException('PHP cURL extension is required.');
    }
    public function synthesize(array $options): string {
        $t = isset($options['text']) && $options['text'] !== ''; $s = isset($options['ssml']) && $options['ssml'] !== '';
        if ($t === $s) throw new \InvalidArgumentException('Provide exactly one non-empty text or ssml value.');
        $payload = ['format'=>$options['format'] ?? 'mp3', 'stream'=>$options['stream'] ?? true, $t ? 'text' : 'ssml'=>$t ? $options['text'] : $options['ssml']];
        if (!empty($options['lang'])) $payload['lang'] = $options['lang'];
        $ch = curl_init($this->baseUrl);
        curl_setopt_array($ch, [CURLOPT_POST=>true, CURLOPT_RETURNTRANSFER=>true, CURLOPT_CONNECTTIMEOUT=>15, CURLOPT_TIMEOUT=>$this->timeout,
            CURLOPT_HTTPHEADER=>['Content-Type: application/json','Accept: audio/*, application/octet-stream, application/json','X-API-Key: '.$this->key.':'.$this->secret],
            CURLOPT_POSTFIELDS=>json_encode($payload, JSON_THROW_ON_ERROR|JSON_UNESCAPED_UNICODE)]);
        $body = curl_exec($ch); $status = (int)curl_getinfo($ch, CURLINFO_RESPONSE_CODE); $error = curl_error($ch); curl_close($ch);
        if ($body === false) throw new RuntimeException('Gecko TTS transport error: '.$error);
        if ($status < 200 || $status >= 300) throw new GeckoTTSError($status, substr(trim((string)$body),0,1200) ?: 'Request failed');
        return (string)$body;
    }
    public function synthesizeToFile(string $path, array $options): string { $bytes=$this->synthesize($options); if (file_put_contents($path,$bytes,LOCK_EX)===false) throw new RuntimeException('Unable to write audio file.'); return $path; }
}
