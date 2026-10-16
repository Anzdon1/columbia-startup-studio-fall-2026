from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math, subprocess, json, hashlib, shutil, os

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT / 'assets'
TMP = Path('/private/tmp/restroom-tiktok-render')
TMP.mkdir(exist_ok=True)
FF = os.environ.get('FFMPEG_BIN') or shutil.which('ffmpeg')
if not FF:
    try:
        import imageio_ffmpeg
        FF = imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        raise SystemExit('Set FFMPEG_BIN or install imageio-ffmpeg in the active Python environment.')
W,H,FPS,DURATION = 720,1280,24,18
BG='#EEF2F3'; INK='#1E2A30'; MUTED='#56666E'; BLUE='#2B59C3'; TINT='#D9E3E8'
SANS='/System/Library/Fonts/Helvetica.ttc'
MONO='/System/Library/Fonts/SFNSMono.ttf'
def font(size, mono=False): return ImageFont.truetype(MONO if mono else SANS,size)
def text(draw,xy,content,size=30,fill=INK,mono=False,spacing=8):
    draw.multiline_text(xy,content,font=font(size,mono),fill=fill,spacing=spacing,stroke_width=0)
def rounded(im,xy,fill='white',outline=None,r=18,width=1):
    ImageDraw.Draw(im).rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=width)
def contain(im,w,h):
    im=im.copy();im.thumbnail((w,h),Image.Resampling.LANCZOS);return im
def paste_alpha(im,asset,xy):
    if asset.mode=='RGBA':im.paste(asset,xy,asset)
    else:im.paste(asset,xy)
illustration=Image.open(ASSETS/'nyc-illustration.png').convert('RGB')
illustration=illustration.resize((W,H),Image.Resampling.LANCZOS)
logo=contain(Image.open(ASSETS/'brand-lockup.png').convert('RGBA'),326,64)
mark=contain(Image.open(ASSETS/'brand-mark.png').convert('RGBA'),106,106)
screen=Image.open(ASSETS/'finder-mobile.png').convert('RGB')
screen=contain(screen,390,630)
def base():
    im=Image.new('RGB',(W,H),BG);d=ImageDraw.Draw(im)
    for x in range(0,W,30):d.line((x,0,x,H),fill='#E5EBEE')
    for y in range(0,H,30):d.line((0,y,W,y),fill='#E5EBEE')
    paste_alpha(im,logo,(56,78))
    return im
def progress(im,scene,t):
    d=ImageDraw.Draw(im)
    for j in range(5):d.rounded_rectangle((56+j*114,1153,160+j*114,1157),radius=2,fill=BLUE if j<=scene else '#CBD6DB')
def scene(idx,t):
    if idx==0:
        im=illustration.copy();d=ImageDraw.Draw(im)
        rounded(im,(40,63,586,553),fill='#FFFFFF',r=20)
        paste_alpha(im,logo,(65,94));d=ImageDraw.Draw(im)
        text(d,(65,196),'NEW YORK CITY',21,BLUE,True)
        text(d,(60,253),'Need a\nrestroom?',71,INK,True,spacing=7)
        text(d,(65,451),'A pin is only the start.',28)
        # Required provenance stays readable but secondary to the message.
        rounded(im,(56,1077,360,1121),fill='#FFFFFF',r=8)
        text(ImageDraw.Draw(im),(70,1089),'AI-generated illustration',17,MUTED)
    elif idx==1:
        im=base();d=ImageDraw.Draw(im)
        text(d,(56,190),'PUBLIC WEB FINDER',20,BLUE,True)
        text(d,(52,238),'Start with\nthe map.',61,INK,True,spacing=4)
        y=415-int(10*math.sin(min(1,t/0.7)*math.pi/2))
        rounded(im,(162,y-12,162+screen.width+24,y+screen.height+12),fill=INK,r=27)
        im.paste(screen,(174,y))
        text(ImageDraw.Draw(im),(56,1071),'Browse without signing in.',25)
    elif idx==2:
        im=base();d=ImageDraw.Draw(im)
        text(d,(56,190),'BEFORE YOU WALK',20,BLUE,True)
        text(d,(52,238),'Check three\nthings.',59,INK,True,spacing=4)
        rows=[('01','Entry rules','Can I enter?'),('02','Route inside','How do I reach it?'),('03','Report date','When was it reported?')]
        for j,(n,title,sub) in enumerate(rows):
            y=430+j*186-int(10*min(1,max(0,(t-j*0.15)/0.7)))
            rounded(im,(56,y,610,y+161),fill='white',outline='#9FB0B8',r=16)
            d=ImageDraw.Draw(im);text(d,(78,y+23),n,22,BLUE,True)
            text(d,(137,y+20),title,35);text(d,(137,y+83),sub,25,MUTED)
    elif idx==3:
        im=base();d=ImageDraw.Draw(im)
        text(d,(56,190),'DATES MATTER',20,BLUE,True)
        text(d,(52,238),'Check the\ndate.',64,INK,True,spacing=4)
        rounded(im,(56,450,610,690),fill='white',outline='#9FB0B8',r=16)
        d=ImageDraw.Draw(im);text(d,(82,482),'Dated city data',35)
        text(d,(82,549),'Not a live availability\ncheck.',29,MUTED,spacing=10)
        rounded(im,(56,729,610,966),fill='white',outline='#9FB0B8',r=16)
        d=ImageDraw.Draw(im);text(d,(82,761),'Missing details?',31)
        d.rectangle((82,833,515,911),outline=MUTED,width=2)
        text(d,(106,855),'Not reported',30,MUTED,True)
        text(d,(56,1048),'Unknown stays unknown.',27)
    else:
        im=base();d=ImageDraw.Draw(im)
        paste_alpha(im,mark,(58,246))
        text(d,(52,420),'Know before\nyou go.',65,INK,True,spacing=8)
        text(d,(56,676),'NYC restroom discovery',29,MUTED)
        rounded(im,(56,771,610,865),fill=BLUE,r=12)
        text(ImageDraw.Draw(im),(83,801),'Explore Restroom Ready',29,'white')
        text(ImageDraw.Draw(im),(56,928),'nyc.imfinethanku.me',29,INK,True)
        text(ImageDraw.Draw(im),(56,989),'See the website for details.',25,MUTED)
    progress(im,idx,t)
    return im

STARTS=[0,3,6,10,14];ENDS=[3,6,10,14,18]
def frame(t):
    idx=max(i for i,s in enumerate(STARTS) if t>=s)
    im=scene(idx,t-STARTS[idx])
    if idx>0 and t<STARTS[idx]+0.22:
        old=scene(idx-1,ENDS[idx-1]-STARTS[idx-1])
        im=Image.blend(old,im,(t-STARTS[idx])/0.22)
    return im

voice=[
 ('Looking for a restroom in New York?',0),
 ('Start with the map.',3.22),
 ('Check entry rules, the route inside, and report dates.',6.22),
 ('City data is dated. Unknown details stay unknown.',10.22),
 ('Restroom Ready. Know before you go.',14.3),
]
for i,(line,start) in enumerate(voice):
    subprocess.run(['/usr/bin/say','-v','Samantha','-r','174','-o',str(TMP/f'voice-{i}.aiff'),line],check=True)
args=[FF,'-y','-hide_banner']
for i in range(len(voice)):args+=['-i',str(TMP/f'voice-{i}.aiff')]
filters=[]
for i,(_,start) in enumerate(voice):filters.append(f'[{i}:a]aresample=48000,adelay={int(start*1000)}:all=1[a{i}]')
filters.append(''.join(f'[a{i}]' for i in range(len(voice)))+'amix=inputs=5:duration=longest:normalize=0,apad,atrim=0:18,loudnorm=I=-16:TP=-1.5:LRA=7[out]')
args+=['-filter_complex',';'.join(filters),'-map','[out]','-c:a','pcm_s16le',str(TMP/'voiceover.wav')]
subprocess.run(args,check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

frame(1.5).save(ROOT/'cover.png')
for sec in [0,1.5,4.5,8,12,16.5,17.96]:frame(sec).save(TMP/f'frame-{str(sec).replace(".","-")}.png')
contact=Image.new('RGB',(720,3*640),'white')
for n,sec in enumerate([1.5,4.5,8,12,16.5,17.96]):
    img=frame(sec).resize((360,640),Image.Resampling.LANCZOS)
    contact.paste(img,((n%2)*360,(n//2)*640))
contact.save(ROOT/'storyboard.png')
cmd=[FF,'-y','-hide_banner','-loglevel','warning','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','pipe:0','-i',str(TMP/'voiceover.wav'),'-c:v','libx264','-preset','medium','-crf','20','-pix_fmt','yuv420p','-c:a','aac','-ar','48000','-b:a','128k','-t',str(DURATION),'-movflags','+faststart',str(ROOT/'restroom-ready-tiktok.mp4')]
proc=subprocess.Popen(cmd,stdin=subprocess.PIPE)
for n in range(FPS*DURATION):proc.stdin.write(frame(n/FPS).tobytes())
proc.stdin.close()
if proc.wait()!=0:raise RuntimeError('Video encode failed')
subprocess.run([FF,'-y','-hide_banner','-loglevel','error','-i',str(ROOT/'restroom-ready-tiktok.mp4'),'-vn','-c:a','pcm_s16le',str(ROOT/'voiceover.wav')],check=True)
meta={'width':W,'height':H,'durationSeconds':DURATION,'framesPerSecond':FPS,'frameCount':FPS*DURATION,'videoCodec':'H.264','audioCodec':'AAC','pixelFormat':'yuv420p','voice':'macOS Samantha text to speech','voiceRateWordsPerMinute':174,'generatedIllustration':'assets/nyc-illustration.png','music':'none','status':'local draft, not published','sha256':hashlib.sha256((ROOT/'restroom-ready-tiktok.mp4').read_bytes()).hexdigest()}
(ROOT/'video-metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
print(json.dumps(meta))
