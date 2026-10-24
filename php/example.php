<?php
declare(strict_types=1);
require __DIR__ . '/vendor/autoload.php';
$client = new \GeckoTTS\GeckoTTS(getenv('GECKO_TTS_KEY') ?: '', getenv('GECKO_TTS_SECRET') ?: '');
$client->synthesizeToFile(__DIR__.'/speech.mp3', ['text'=>'Hello from Gecko TTS.','lang'=>'en-in','format'=>'mp3']);
echo "Saved speech.mp3\n";
