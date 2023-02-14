import vlc
from threading import Event

print("""
1-) Alem FM         11-) Power Pop
2-) Power Türk FM   12-) Show Radyo
3-) Kafa Radyo      13-) Pal FM
4-) Kral FM         14-) Pal Station
5-) Kral Pop        15-) Power FM
6-) Joy Turk        16-) Virgin Radyo
7-) Slow Türk       
8-) Süper FM        
9-) Number One Türk 
10-) Best FM       
""")
secim = input(""" (Eğer radyoda sorun varsa Github deposu üzerinden ISSUE bildirin.)

Radyo kanalı seçiniz: """)

match secim:
    case "1":
        alemfm = vlc.MediaPlayer("http://turkmedya.radyotvonline.net/alemfmaac")
        alemfm.play()
        Event().wait()

    case "2":
        powerturkfm = vlc.MediaPlayer("https://live.powerapp.com.tr/powerturk/abr/powerturk/128/playlist.m3u8")
        powerturkfm.play()
        Event().wait()

    case "3":
        kafaradyo = vlc.MediaPlayer("https://moondigitalmaster.radyotvonline.net/kafaradyo/playlist.m3u8")
        kafaradyo.play()
        Event().wait()

    case "4":
        kralfm = vlc.MediaPlayer("http://46.20.3.204/;")
        kralfm.play()
        Event().wait()

    case "5":
        kralpop = vlc.MediaPlayer("http://kralpopwmp.radyotvonline.com/;")
        kralpop.play()
        Event().wait()

    case "6":
        joyturk = vlc.MediaPlayer("https://playerservices.streamtheworld.com/api/livestream-redirect/JOY_TURK_SC?/;")
        joyturk.play()
        Event().wait()

    case "7":
        slowturk = vlc.MediaPlayer("https://radyo.duhnet.tv/ak_dtvh_slowturk")
        slowturk.play()
        Event().wait()

    case "8":
        superfm = vlc.MediaPlayer("https://playerservices.streamtheworld.com/api/livestream-redirect/SUPER_FM_SC?/;")
        superfm.play()
        Event().wait()

    case "9":
        numberoneturk = vlc.MediaPlayer("https://n10101m.mediatriple.net/numberoneturk")
        numberoneturk.play()
        Event().wait()

    case "10":
        bestfm = vlc.MediaPlayer("http://46.20.7.126/bestfmmp3")
        bestfm.play()
        Event().wait()

    case "11":
        powerpop = vlc.MediaPlayer("http://46.20.7.126/bestfmmp3")
        powerpop.play()
        Event().wait()

    case "12":
        showradyo = vlc.MediaPlayer("http://46.20.3.229/;")
        showradyo.play()
        Event().wait()

    case "13":
        palfm = vlc.MediaPlayer("http://shoutcast.radyogrup.com:1030/;")
        palfm.play()
        Event().wait()

    case "14":
        palstation = vlc.MediaPlayer("https://fmradiohub.in/play?url=http://shoutcast.radyogrup.com:1020/;")
        palstation.play()
        Event().wait()

    case "15":
        powerfm = vlc.MediaPlayer("https://live.powerapp.com.tr/powerfm/abr/playlist.m3u8")
        powerfm.play()
        Event().wait()

    case "16":
        virginradyo = vlc.MediaPlayer("https://playerservices.streamtheworld.com/api/livestream-redirect/VIRGIN_RADIO_SC?/;")
        virginradyo.play()
        Event().wait()
