# rtsp-decoder

This is a bunch of code to make and RPi decode a video stream from a TCP/IP 
Connection to its HDMI port.

## Elements:
  
  ### Encoder:  
    Name: U8Vision H.264 HDMI Video Encoder
    IP: 192.168.1.10
    Protocol: RTSP/RTMP/UDP/RTP/HTTP
    Link: [Aliexpres Encoder](https://www.aliexpress.com/item/32834043039.html?spm=a2g0n.orderlist-amp.item.32834043039&aff_trace_key=&aff_platform=msite&m_page_id=7936amp--azL20pxfLT-uFa3m-x5ew1591212845867&browser_id=61577cdab90c4525a1d011dc9aeb4a78&is_c=Y)
    Stream: rtsp://192.169.1.10:8554/0
  
  ### Decoder
    Name: RPi
    IP: 192.168.1.9
    Protocol: RTSP/RTMP/UDP/RTP/HTTP
    Video Output: HDMI-port
    Link: [Raspberry Pi](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/)
    Stream: rtsp://192.169.1.10:8554/0

## Steps:
- Configure an sdcard with the latest raspbian available [Download](https://www.raspberrypi.org/downloads/)

- Use the [Raspi os](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

- Take the sd card and [change the IP and Enable ssh](https://learn.sparkfun.com/tutorials/headless-raspberry-pi-setup/ethernet-with-static-ip-address):
 - Add this lines of code at the end of */etc/dhcpcd.conf*
```
interface eth0

static ip_address=192.168.1.9/24
static routers=192.168.1.1
static domain_name_servers=192.168.1.1
```
- To enable ssh add an empty file called *ssd* in the *boot* directory, you can use the command *touch ssh* inside the boot directory

- Add the folowing line on the */etc/rc.local* before the *exit 0* command
```
sudo python /home/pi/decoder.py
```
- Finally copy the *decoder.py* file on the *home/pi* directory, 
- Place the sd card on the raspberry
- From other computer on the same network long into the Raspberry Pi (default user and pass, *pi* and *raspberry*) and install *omxplayer*
```
sudo apt-get install omxplayer
```
- From the next boot the RPi should decode.

## Test
- Configure PC with this IP 192.168.1.10.
- Make a simple source of video stream for instance, use [VLC to stream](https://www.howtogeek.com/118075/how-to-stream-videos-and-music-over-the-network-using-vlc/) now the streaming source will be "rtsp://192.168.1.10:8554/"
- On the RPi test if it gets the streaming using the following command
```
  omxplayer -o both rtsp://192.168.1.101:8554/
```


