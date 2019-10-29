# Visible Light Communication, Networking and Sensing: A Survey, Potential and Challenges

## Introduction

- LED replacement incandescent bulb and fluorescent bulb 
  - power saving: 200 lumens/watt in 2020 (forecast)
  - lifespan: 25000~50000 hours life time
  - reduced usage of harmful materials
- LED serves illumination and **communication**
  - LED able to switching to different light intensity(強度) level in very fast rate
    - human eye can not detect.
    - application for communication.
  - Photo-detector (光感測器)/image sensor receive the modulated signals and decode the data
- VLC able to achieve very high speed communication
  - 802.15.7 100Mbps
  - multi-Gbps in researching
- VLC importance
  - complement the RF-based mobile communication systems 
    - exponential increase of mobile data trafﬁc identiﬁed the limitations of RF-only
    - scarce RF spectrum
    - **license free** bandwidth for visible light spectrum in ~X00 terahertz 
    <img src="https://imgur.com/7gMtjZU.jpg" style="width: 600px" align="center"/>
  - cannot penetrate through most objects and walls
    -  **no inter-cell interference** issues beyond the walls and partitions
    - increase the **capacity** of available wireless channel dramatically
    - an inherent wireless communication **security**
  - Reuse of existing lighting infrastructure
    - less effort and low cost
- Brief History of VLC
  - in 2000, Keio University in Japan, the use of white LED in homes for building an access network
  - in Nov. 2003, formation of Visible Light Communications Consortium (VLCC)
  - 2007, VLCC proposed communication system standard(JEITA CP-1221) and ID system standard(JEITA CP-1222)
  - 2009, VLCC proposed IrDA
  - 2009, European Union, hOME Gigabit Access project (OMEGA)
  - 2014,  VLCC -> VLCA
  - 2011, 802.15.7
  - currently, Gigabyte VLC in research
- Systematic view of VLC research
  - Components: Transmitter and receiver.
  - Physical layer: channel, modulation, coding, and MIMO
  - Link Layer: multiple user access, issues
  - System design,
  - Visible light sensing and applications: indoor location, human computer iteraction,device-to-device comm., vehicular-comm.

## VLC System Overview

### Transmitter

- LED luminaire(燈): LED lamp(燈), ballast(鎮流器), housing(殼) and other components
  - LED lamp: 
    - one or more LEDs, 
    - driver circuit control LEDs brightness by current ﬂowing.
      - modified for modulation in communication application: example OOK, on for 1, off for 0
  - VLC performance is depending on how the LED luminaires are designed.
  - Compose white light:
    - most common used because object closely resemble the color as natural light.
    - Two approach to White light
      - Blue LED with Phosphor(磷): Blue LED + yellow phosphor coating(塗層), $
        - most common used due to $
        - phosphor coating **limits** the communication speed at which LED can switched to a few MHz
        - various solutions to alleviate this limitation
      - RGB Combination: proper mixing of red, green and blue light, higher cost($$).
        - **preferable for communication**
        - able to use color-shift-keying
         
### VLC Receiver 

- photodetector: photodiode
  - light into current.
  - commercial photodetector easily sample the received visible light in tens of MHz
- imaging sensor: camera sensor
  - the potential to convert the mobile devices
  - consists of many photodetectors in matrix structure.
  - high resolution reduce the frame per second. ~ 40fps => low data rate
  - "rolling shutter" : used to receive the data at a faster rate
    - originally, one row read at a time row-by-row read. speedup the image output date rate.
    - Example of using "rolling shutter" to speed data communication
      - each column convert to binary data. => achieve ~Kbps.
    <img src="https://imgur.com/GfVkdOr.jpg" style="width: 600px" align="center"/> 

### VLC Mode of Communication

- Infrastructure-to-device
- Device-to-device : 
  - screen-to-camera streaming: LED pixel on mobile display communicated to another mobile thru camera.
    - 2D bar-code !