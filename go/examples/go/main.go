package main
import("context";"log";"os"; geckotts "github.com/YOUR_GITHUB_USERNAME/gecko-tts/go")
func main(){c,e:=geckotts.NewClient("","");if e!=nil{log.Fatal(e)};b,e:=c.Synthesize(context.Background(),geckotts.Request{Text:"Hello from Gecko TTS.",Lang:"en-in",Format:"mp3"});if e!=nil{log.Fatal(e)};if e=os.WriteFile("speech.mp3",b,0600);e!=nil{log.Fatal(e)};log.Println("Saved speech.mp3")}
