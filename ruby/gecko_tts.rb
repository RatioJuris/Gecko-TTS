require 'net/http'; require 'uri'; require 'json'
module GeckoTTS
 DEFAULT_URL='https://www.isrgrajan.com/gecko/tts/index.php'
 class Error < StandardError; attr_reader :status; def initialize(status,message);@status=status;super("Gecko TTS HTTP #{status}: #{message}");end;end
 class Client
  def initialize(key:ENV['GECKO_TTS_KEY'],secret:ENV['GECKO_TTS_SECRET'],base_url:ENV['GECKO_TTS_URL']||DEFAULT_URL,timeout:90)
   raise ArgumentError,'API key and secret required' if key.to_s.empty?||secret.to_s.empty?;@key,@secret,@uri,@timeout=key,secret,URI(base_url),timeout
  end
  def synthesize(text:nil,ssml:nil,lang:nil,format:'mp3',stream:true)
   t=text.is_a?(String)&&!text.empty?;s=ssml.is_a?(String)&&!ssml.empty?;raise ArgumentError,'Provide exactly one non-empty text or ssml' if t==s
   p={t ? :text : :ssml => t ? text : ssml,format:format,stream:stream};p[:lang]=lang if lang
   r=Net::HTTP::Post.new(@uri);r['Content-Type']='application/json';r['X-API-Key']="#{@key}:#{@secret}";r['Accept']='audio/*, application/octet-stream, application/json';r.body=JSON.generate(p)
   res=Net::HTTP.start(@uri.hostname,@uri.port,use_ssl:@uri.scheme=='https',open_timeout:15,read_timeout:@timeout){|h|h.request(r)}
   raise Error.new(res.code.to_i,res.body.to_s[0,1200]) unless res.is_a?(Net::HTTPSuccess);res.body
  end
  def synthesize_to_file(path,**options);File.binwrite(path,synthesize(**options),perm:0600);path;end
 end
end
