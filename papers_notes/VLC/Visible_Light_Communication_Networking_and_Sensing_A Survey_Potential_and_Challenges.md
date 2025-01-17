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

## Physical Layer

### Channel Model and Propagation Properties


#### Transmitted Power of an LED - Luminous Flux

- LED parameters
  - Photometric: brightness, color, for human eyes
  - Radiometric: radiant electromagnetic energy, determinate communication related property.
- Calculating the Luminous Flux
  - Spectral integral: 
    - Luminosity Function $V(\lambda)$: photopic vision of human, distinguish different colors 
    <img src="https://imgur.com/hKKg56z.jpg" style="width: 600px" align="center"/> 
    - Spectral Power Distribution$S_T(\lambda)$: the power of the LED at all wavelengths in the visible light spectrum
      - radiometric parameter measured in Watts/nm
    <figure><img src="https://imgur.com/unbrdJr.png" style="width: 600px" align="center"/>
    <div style='width: 600px; text-align: center;'>High radiant Power at blue and yellow</div>

    - Luminous Flux: combines luminosity function and spectral power distribution 
      - $F _ { T } = 683$ (lumens/watt) $\int _ { 380 \mathrm { nm } } ^ { 750 \mathrm { nm } } S _ { T } ( \lambda ) V ( \lambda ) d \lambda$
        - $S_T(\lambda)$ : Transmit electromagnetic power
        - $V(\lambda)$: Receive sensitivity function of Human-Eye
        - $F_T$ is the total luminous converted form electromagnetic energy.(at EYE reception)
        - 683: the maximum luminous efﬁciency, occurs at 555 nm wavelength
      - luminous efﬁciency: ratio of luminous ﬂux to the radiant ﬂux
        - how well the radiated electromagnetic energy and electricity of an LED was transformed to provide visible light illumination
        - 電轉換成光的效益多高
  - Spatial integral: LED’s spatial emission properties
    - Luminous Intensity $g_t(\theta)$: how bright the LED is in a speciﬁc direction 
      - $F _ { T } = I _ { 0 } \int _ { 0 } ^ { \theta _ { \max } } 2 \pi g _ { t } ( \theta ) \sin \theta d \theta$
      <img src="https://imgur.com/zFG19Q2.jpg" style="width: 600px" align="center"/> 
      - measured in **Candela**(cd): luminous ﬂux per unit solid angle (1 steradian(球面度))
      - Most LED sources have Lambertial beam distribution: intensity drops as the cosine of the incident angle
      - *Axial Intensity* ($I_0$): luminous intensity at $0^o$ solid angle
      - *Half Beam Angle* ($\theta_{max}$): the angle of intensity decrease 3dB.
        - $\Omega _ { \max } = 2 \pi \left( 1 - \cos \theta _ { \max } \right)$
      - Candela: 發光強度(燭光), $I = \frac { \mathrm { d } \Phi } { \mathrm { d } \Omega }$
        - 光源在給定方向上，每單位立體角內所發出的的光通量
        - https://zh.wikipedia.org/wiki/%E5%8F%91%E5%85%89%E5%BC%BA%E5%BA%A6

#### Path Loss and Received Power

- The same path loss model in both photometric($L_l$,luminous) and radiometric($L_p$,optical power) domain.
  - free space LOS propagation, loss independent to waveform $\lambda$.
  - $F _ { T } = I _ { 0 } \int _ { 0 } ^ { \theta _ { \max } } 2 \pi g _ { t } ( \theta ) \sin \theta d \theta$
- $F_{R}$ Derivation:
  - $L _ { L } = \frac { F _ { R } } { F _ { T } } = \frac { g _ { t } ( \beta ) A _ { r } \cos \alpha } { D ^ { 2 } \int _ { 0 } ^ { \theta _ { m a x } } 2 \pi g _ { t } ( \theta ) \sin \theta d \theta }$
    - $A _ { r } \cos ( \alpha ) = D ^ { 2 } \Omega _ { r }$
      - D: distance between TX/RX
      - r: Radius of RX aperture(光圈,恐)
      - $\alpha$: incident angle, angle between TX and RX
    - $F _ { R } = I _ { 0 } g _ { t } ( \beta ) \Omega _ { r }$

  <img src="https://imgur.com/j4QgdAC.jpg" style="width: 600px" align="center"/> 

- Lambertial beam distribution: most LED spatial intensity property
  - spatial luminous intensity : $g _ { t } ( \theta ) = \cos ^ { m } ( \theta )$
    - $m$: Lambertial emmission, depends on the semi-angle at half illuminance $\Phi _ { 1 / 2 }$
      - $m = \frac { \ln ( 2 ) } { \ln \left( \cos \Phi _ { 1 / 2 } \right) }$
- Path Loss of Lambertian LED: 
  - $L _ { L } = \frac { ( m + 1 ) A _ { r } } { 2 \pi D ^ { 2 } } \cos \alpha \cos ^ { m } ( \beta )$
- Received Power At LOS 
  - $P _ { R _ { O } } = \int _ { \lambda _ { r L } } ^ { \lambda _ { r H } } S _ { R } ( \lambda ) R _ { f } ( \lambda ) d \lambda$
    - $S _ { R } ( \lambda ) = L _ { P } S _ { T } ( \lambda ) = L _ { L } S _ { T } ( \lambda )$
  - $R_f(\lambda)$: optical filter response
  <img src="https://i.imgur.com/erVTAnE.png " style="width: 400px" align="center"/>
  - Factor of RX power
    - distance $D$, incident(接收) angle $\alpha$, irradiation(放射,發射) angle $\beta$
    - crucial to understand the capacity of the link
    - Example in smartphone photodiode as receiver
    <img src="https://i.imgur.com/30WDuYP.png" style="width: 600px" align="center"/> 
  

### Multipath Propagation with Reﬂected Paths

- Received total power: $P _ { R } ( \text {total} ) = \sum _ { i = 0 } ^ { N } P _ { R } ( i )$
  - $P _ { R } ( i )$ is $i$-th LOS path optical power.
- Reflation 
  - spectral reflation: $\rho ( \lambda )$
    - in different materials
  <img src="https://i.imgur.com/O7pTCoS.png" style="width: 400px" align="center"/>
- Power-delay profile
  <figure><img src="https://i.imgur.com/YghwNeK.png" style="width: 500px" align="center"/>
  <div style='width: 500px; text-align: center;'>example of non-LOS model</div>

  - $h ( t ) = \sum _ { n = 1 } ^ { N } \sum _ { k = 0 } ^ { \infty } h ^ { ( k ) } \left( t ; S _ { n } \right)$
    - $N$ LEDs
    - $S_n$: spectral power distribution
    - $k$: number of bounces
  - LOS path: $h ^ { ( 0 ) } \left( t ; S _ { n } \right) = L _ { 0 } P _ { n } r \operatorname { ect } \left( \frac { \alpha _ { 0 } } { F O V } \right) \delta \left( t - \frac { D _ { 0 } } { c } \right)$
    - $L_0=L_L$: path loss; $c$: light speed; $D_0$: distance
    - $\operatorname { rect } ( x ) = \left\{ \begin{array} { l l } { 1 } & { \text { for } | x | \leq 1 } \\ { 0 } & { \text { for } | x | > 1 } \end{array} \right.$
  - $k$-th reflcation path
    - $\begin{aligned} h ^ { ( k ) } \left( t ; S _ { n } \right) = & \int _ { s \in \mathbb { S } } \left[ L _ { 1 } L _ { 2 } \cdots L _ { k + 1 } \Gamma _ { n } ^ { ( k ) } r \operatorname { ect } \left( \frac { \alpha _ { 0 } } { F O V } \right) \times  \delta \left( t - \frac { D _ { 1 } + D _ { 2 } + \cdots + D _ { k + 1 } } { c } \right) \right] d A _ { s } \end{aligned}$
    - $L _ { 1 } = \frac { A _ { s } ( m + 1 ) \cos \alpha _ { 1 } \cos ^ { m } \beta _ { 1 } } { 2 \pi D _ { 1 } ^ { 2 } }$
    - $L _ { k + 1 } = \frac { A _ { R } \cos \beta _ { k + 1 } \cos \alpha _ { k + 1 } } { \pi D _ { k + 1 } ^ { 2 } }$
    - $\Gamma _ { n } ^ { ( k ) }$ power of the reﬂected ray: $\Gamma _ { n } ^ { ( k ) } = \int _ { \lambda } S _ { n } ( \lambda ) \rho _ { 1 } ( \lambda ) \rho _ { 2 } ( \lambda ) \ldots \rho _ { k } ( \lambda ) d \lambda$
  - Example
    - first spike from LOS and others are reflation paths
  <figure><img src="https://i.imgur.com/fpeTutx.png" style="width: 500px" align="center"/>
  <div style='width: 500px; text-align: center;'>Power delay proﬁle for 4 LED transmitters in a cubic room</div> 
  - Most of the power delay proﬁling of visible light communication rely on simulations

### Receiver Noise and SNR

- Major light noise source:
  - Ambient light noise: solar radiation and other illumination sources
    - a DC interference,
    - remains stationary over space and time(but no systemically evaluation)
    - can be mitigated by HPF
  - shot noise: 
    - inherent statistical ﬂuctuation(波動) of photons collected by the photodetector
    - the photon counting follows a **poisson** distribution: mean = $x$, std = $\sqrt{x}$
  - electrical pre-ampliﬁer noise: thermal noise
- SNR: (removing ambient noise)
  - $S N R = \frac { P _ { R _ { E } } ^ { 2 } } { \left( \sigma _ { \text {shot} } \right) ^ { 2 } + \left( \sigma _ { \text {thermal} } \right) ^ { 2 } }$
  - $\left( \sigma _ { \text {shot} } \right) ^ { 2 } = 2 q P _ { R _ { E } } B + 2 q I _ { B } I _ { 2 } B$
  - $\left( \sigma _ { \text {thermal} } \right) ^ { 2 } = \frac { 8 \pi \kappa T _ { k } } { G _ { o l } } C _ { p d } A I _ { 2 } B ^ { 2 } + \frac { 16 \pi ^ { 2 } \kappa T _ { k } \eta } { g _ { m } } C _ { p d } ^ { 2 } A ^ { 2 } I _ { 3 } B ^ { 3 }$
    - B: bandwidth
    - $\kappa$: Boltzmann’s constant
    - $I_B$: photpcurrent due to back ground radiation
    - $G_{ol}$: open loop voltage gain
    - $T_{k}$: absolute temperature
    - $C_{pd}$: capacitance of the photodetector per unit area
    - $\eta$: FET channel noise factor
    - $g_m$: FET transconductance
    - $I_2 = 0.562$, $I_3 = 0.0868$ : noise-bandwidth factors
  - Factors includes area of the photodetector,room temperature, ambient light

### Shadowing 

- VLC link shadowed by other object or humans
- Frequency shadowing
- Multiple spatial separated LEDs to mitigate the frequency shadowing
- shadowing in indoor VLC networks is not studied in literature. 

## Modulation Methods

- No phase/amplitude modulation: data can not be encoded in phase or amplitude in light signal
- IM/DD : 
  - Intensity Modulation: information encoded in varying intensity(亮度)
  - Direct Detection: direct detection at receiver
- Requirements perceived(感知) light
  - Dimming(調光): 
    - human sensitivity to the dimming of the light.
    - $ \text{Perceived light} ( \% ) = 100 \times \sqrt { \frac { \text { Measured light } ( \% ) } { 100 } }$
    - 1% decreasing of measured light cause 10% decreasing of the perceived light
    - communication should not be affected by the dimming.
  - Flicker mitigation(避免閃爍)
    - VLC should not result in human-perceivable ﬂuctuations
    - changes light intensity must faster than human eye can perceive 
    - IEEE 802.15.7 suggest > 200Hz
    - most common flicker source: long 0s and long 1s
    - Run Length Limited (RLL) codes to mitigate flicker.
    - Common used RLL: 
      - Manchester: 0->(10), 1-> (01)
      - 4B6B: 4bits to 6bit which has balanced repetition.
      - 8B10B: 8bit to 10bit
        - reduce additional bits, but performs poorly in terms of DC balancing.

### OOK

- Bits 1 and 0 are transmitted by turning the LED on and off respectively
- Most early work VLC using OOK
- Major limitation of white LED(BLUE + yellow phosphor): 
  - Bandwidth limitation to ~MHz due to slow time response of phosphor
- Transmission speed evaluation
  - first version 10Mbps -> 
  - 40Mbps by using blue filter ->
  - 100Mbps by tx blue filtering+rx analog Eqz ->
  - 230Mbps using avalanche photodiode rx.
  - 477Mbps using RGB LED, but only Red for modulation.
- 802.15.7 proposed two approaches for OOK modulation
  - Redeﬁne ON and OFF levels
  - Compensation periods: on/off level remain the same,added compensation period.
    - The duration is determined based on the desired level of dimming
    - $\gamma = \left\{ \begin{array} { l l } { ( 2 - 2 D ) \times 100 } & {: D > 0.5 } \\ { 2 D \times 100 } & {: D \leq 0.5 } \end{array} \right.$

### Pulse Modulation Methods

- OOK limitation is the data rate.
- Pulse Width Modulation (PWM): adjust dimming level to carry information by pulse width.
  - Advantage: without change intensity level,not incur color shift
  - limited data rate to 4.8kbps
- PWM+DMT(Discrete multi-tone)
  - data modulated in QAM->DMT, multiplied by a pulse width modulation
  - the duty cycle of PWM is dependent on desired level of dimming
  - used QAM on DMT subcarriers to achieve a link rate of 513 Mbps
<img src="https://i.imgur.com/E0GmFKJ.png" style="width: 600px" align="center"/> 

- Pulse Position Modulation (PPM):
  - information modulated based on pulse position
  - early adopted due to simplicity
  <img src="https://i.imgur.com/wltB7zi.png" style="width: 600px" align="center"/>
  - Variety:
    - Overlapping PPM (OPPM): overlap of different symbols in time, better spectrum efficiency than OOK/PPM
    - Multipulse PPM (MPPM): multiple pulses to be transmitted during the symbol duration, better efficiency than OPPM
    - Overlapping MPPM: furthermore improvemnet without expending bandwidth
    - Differential PPM (DPPM)
    - Expurgated PPM
    - Multi-level EPPM
    - Variable PPM (VPPM): hybrid PPM and PWM, proposed in 802.15.7
     
### OFDM 

- Single carrier modulation suffers high ISI.
- OFDM simplify the equalization design.
- VLC-OFDM need to modify to fit IM/DD system.
  - Real value system: no complex value in time domain by Hermitian symmetry constraint
  - Unipolar signals (no negative value):
    - Asymmetrically-Clipped Optical OFDM (ACO-OFDM)
      - only odd subcarriers are modulated leads symmetric in time domain
    - DC-biased Optical OFDM (DCO-OFDM)
      - positive direct current is added to make the signal unipolar
      - LED clipping more significant
  - Biggest challenge: nonlinear model current to intensity
    - OFDM PAPR effect
    - let LED operates at a small range to make drive current and optical power quasi-linear.
  - OFDM for VLC holds great potential with achievable link rates in the scale of multiple **gbps**

### Color Shift Keying (CSK)

- TriLED(TLED): Combined RGB LED
- CSK: modulated in intensity of the three colors in the TLED source
  - relays on color space chromaticity diagram
  
- Approach to CSK
  - Determine RGB constellation triangle
  <img src="https://i.imgur.com/Mx9eOjH.png" style="width: 600px" align="center"/> 
  - Mapping data bits to chromaticity values
  <img src="https://i.imgur.com/doNvHLp.png" style="width: 600px" align="center"/> 
  - Determine the intensities of RGB LEDs
  $\begin{aligned} x _ { s } =  P _ { i } x _ { i } + P _ { j } x _ { j } + P _ { k } x _ { k } \\ y _ { s } = P _ { i } y _ { i } + P _ { j } y _ { j } + P _ { k } y _ { k } \\ P _ { i } + P _ { j } + P _ { K } = 1 \end{aligned}$ 
- Advantage: flicking is not problem in CSK
- Generalization on constellation mapping: 
  - Billards equivalent disk packing algorithm
  - design techniques are designed to meet the color balance requirement
- Wavelength division multiplexing(WDM) in TLED: 
  - modulate different stream from each color LED

### IEEE 802.15.7 Physical Layer

- PHY I: low speed OOK/VPPM
<img src="https://i.imgur.com/MKZL8C2.png" style="width: 600px" align="center"/> 

- PHY II: high speed OOK/VPPM
<img src="https://i.imgur.com/npM4rf4.png" style="width: 600px" align="center"/> 

- PHY III: 
<img src="https://i.imgur.com/xszuO8b.png" style="width: 600px" align="center"/> 

### Multiple Input Multiple Output (MIMO)


- Luminaries typically contain multiple LEDs: can enable visible light MIMO communication
- MIMO system are difficult to realize compared to RF comm.
  - paths are similar, less diverse

#### MIMO Receiver

- Non-imaging receiver: 
  - independent photodiodes
  - high gain, low FOV, need careful alignment of the LOS
- Imaging receiver:
  - projection lens and large matrix of photodiodes
  - projection lens enlarge FOV
  - limited gain. advanced image process is required to create an efficiency MIMO channel.
  - ideal MIMO receiver: hybrid imaging and non-imaging sensors.
    - high gain for LOS using narrow FOV 
    - robustness by leveraging NLOS path.
  - Spherically-shaped receiver: 
    - a large number of photodiodes.
    - each has a narrow FOV and points in different direction in the room
    - incurs cost for additional hardware
  - A token-based pixel selection method: the pixels of interest are selectively scanned to speedup sampling rate.

#### VLC MIMO Techniques

- Repetition Coding (RC)
  - less restrictive but limited throughput
- Spatial Multiplexing (SMP): multiple parallel SISO streams
  - optical wireless MIMO communication with subcarrier multiplexing where zero forcing was utilized
  - **Optical beat interference** caused by multiple transmitters transmitting simultaneously
- Spatial Modulation (SM)
  - information modulated by activation of LEDs
  - receiver estimate which LEDs are activated to decode
  - power imbalance between the transmitter LEDs can improve the performance of spatial modulation especially in high correlated channel.
- imaging receiver provide higher in SPM and SM compared to non-imaging receiver.

#### Optical Beamforming

- multiple LEDs can be focused towards the receiver to create optical beamforming
- single LED can be focused in a speciﬁc target direction using Spatial Light Modulator (SLM)
- SNR improvements

## Link Layer

### Medium Access Control(MAC)

- Topology
  - P2P : suitable for highspeed NFC(near field communication)
  - Star: many bidirectional links
  - Broadcast: only received from master LED. Simple control.
   
#### CSMA : Carrier sense multiple access

- 802.15.7 defines two CSMA protocol
- un-slotted random access with CSMA
  - random backoff
  - carrier sense before transmission
  - if channel busy, random backoff and wait
- Beacon enabled slotted CSMA
  - using beacon to slot the periods.
  - Contention access period (CAP): CCA senses idle and transmission
  - contention-free period (CFP): contains multiple GTS
    - Guaranteed Time Slots (GTS): ensure medium access to devices with delay or bandwidth constrained applications
- Key issue of Hidden-node:  to avoiding collisions especially due to hidden terminals is a challenging problem. 
<img src="https://i.imgur.com/c8fFW62.png" style="width: 600px" align="center"/>

- Bidirectional communication: LED off symbol can receive data.

#### OFDMA

- Multiple user access by assignment to different resource block of an OFDM Symbol.
- Main challenge: power efficiency and decoding complexity.
- Furthermore to consider power-efficient and interference-awareness resource allocation scheme.
- Joint transmission (JT):  due to intensity modulation, it is possible to achieve much better coordination multiple point(CoMP) to RF system

#### CDMA

- OOC: optical orthogonal code for transmissions of multi-user in the same access channel
- limitation: long OOC to ensure optimal
- Code Cycle Modulation: using cyclic shift of the code to modulate M-ary information, increasing the capacity in $log_2(L)$
  - Not suitable for providing dimming support
    - achieving a different dimming level => a new set of OOC codes are required to be calculated
    - Two approach to handle this issue: BIBD(Balanced Incomplete Block Designs) and Multi-level MEPPM signal.
  - Not suitable for large user:
    - difficult to generate code.
  - Multiple reflection path cause isi degradation more than increasing fo user.
  - Combine CSK with TLED with OCDMA to multi-user VLC.
  - Hybrid CDMA and OFDM scheme that can achieve the advantages of both.

#### Multi-User MIMO 

- Early Work: multiple transmitter LEDs coordinated joint transmit to multiple user by zero-forcing precoding.
  - Block-digitalization algorithm.
    - reduce rx side complexity and power consumption.
    - high performance uncertainty, only for RX path less than tx path.
  - Tomlinson-Harashima Precoding: achieve better performance.

