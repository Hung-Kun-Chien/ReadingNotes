# A Survey of Indoor Localization Systems and Technologies

- Authors:
  - Faheem Zafari, Athanasios Gkelias, kin K. Leung(Fellow)

- Reference : [https://arxiv.org/abs/1709.01015](https://arxiv.org/abs/1709.01015)

- Abstract:
  - techniques:
    - Angle of Arrival (AoA)
    - Time of Flight (ToF)
    - Return Time of Flight (RTOF)
    - Received Signal Strength (RSS)
  - systems:
    - WiFi 
    - Radio Frequency Identiﬁcation Device (RFID)
    - Ultra Wideband (UWB)
    - Bluetooth
  - other aspects：
    - energy efﬁciency
    - availability
    - cost 
    - reception range
    - latency 
    - scalability 
    - tracking accuracy
  
###### tags:`Paper Study` `Communication` `Wi-Fi` `Indoor Localization`, `Location Based Services`,`Internet of Things`

## INTRODUCTION

- The process of obtaining a device or user location in an indoor setting or environment.
- Indoor location is less than a decade
  - wide-scale proliferation of smart phones and wearable devices
  - location and tracking of device = location and tracking of user
- Applications: health sector, industry, disaster(災難) management, building management, surveillance
- Benefit to IoT, smart architecture(city), smart building, machine type communication
- IoT: 
  - numerous heterogeneous technologies and communication standards that intend to provide end-to-end connectivity to billions of devices.
  - Long range machine-to-machine (mMTC)
  - short/medium range: BT, WiFi, ZigBee,(UWB).
  - Range/power consumption and bandwidth tradeoff made devices utilizes several communication interfaces.
- Long range IoT provide global location information
  - not support indoor positioning
  - accuracy is poor, especially indoor env.
  - collaboration of short/long positioning is need.
- Deﬁnitions
  - Device based localization (DBL): 
    - device uses **reference nodes** (RN) or **anchor** nodes to obtain its relative location
    - primarily used for navigation
  - Monitor based localization (MBL)
    - a set of anchor nodes or RNs passively obtains the position of the user
    - used for tracking the user and then accordingly providing different services
  - Proximity Detection
    - estimating the distance between a user and a Point of Interest (PoI)
    - a reliable and cost effective solution for context aware services
- Location based Services evaluation
  - 1st generation: Network-centric approach
  - 2nd generation: User-centric approach
    - Both service providers and end users can beneﬁt from LBS and Proximity based Services (PBS).
    - For example, in mall, the users can use navigation and tracking services to get to their desired location.
- Key Contributions
  - detailed survey of different indoor localization systems 
  - detailed discussion on different Technologies
  - exhaustive discussion on different techniques that can be used with a number of technologies for indoor localization
  - provide a primer on IoT and highlight indoor localization induced challenges for IoT
  - some of the emerging IoT technologies that are optimized for connecting billions of IoT devices
  - evaluation framework that can be used to assess different localization systems
  - discusses some of the existing and potential applications of indoor localization


## LOCALIZATION TECHNIQUES

### Received Signal Strength Indicator (RSSI)

- Received signal strength (RSS): usually in dBm or mW
- Used to (approximate) estimate distance between TX and Rx
  - higher RSS shorter range
- RSSI: RSS indicator, a **relative** measurement of the RSS that has arbitrary units and is mostly deﬁned by each chip vendor
- Simple path loss model: 
  - $RSSI= -10 n \log_{10}(d)+A$
  - n: path loss exponent in 2(free space) to 4(indoor)
- DBL case: 
  - use RSS at device point
  - trilateration(三角定位) or N-point-lateration
  - one device and N(>=3) reference points
<img src="https://imgur.com/zXdjRmZ.png" style="width: 600px" align="center"/> 

- MBL case:
  - use RSS at reference points
  - a central controller to collects RSSs of the user from different reference points
- Proximity based services
  - a single reference node to create a **geofence**(地理圍欄)
  - estimate the proximity of the user to the anchor node using estimated distance from the reference
point.
- Pros/cons:
  - (+)simple and cost efﬁcient
  - (-)poor localization accuracy(non-LOS, fading condition)
    - filters or averaging mechanisms used to mitigate these effects.
    - still poor...

### Channel State Information (CSI)

- Channel impulse response(CIR) and channel frequency response(CFR) provides higher guarantees of accuracy than CSI.
- many IEEE 802.11 NICs provides subcarrier level CSI from OFDM system.
- (no detail techniques description for CSI-based measurement......)

### Fingerprinting/Scene Analysis

- Using the online RSSI or CSI measurements to map the user/device position on a discrete grid; each point is measured offline
  - Offline phase: collect different RSSI measurement from different position once when system deployed.
  - Online phase: real-time measure results matching to results from offline measured database to estimate user location.
  - collections can be RSSI or CSI
  - very susceptible to changes of the environment over time since offline measured model will change due to environment changes.
- Algorithms:
  - Probabilistic methods: likelihood estimator
    - $P \left( L _ { j } | O \right) > P \left( L _ { k } | O \right)$
      - $O$ : observed vector of the user real-time
      - $L _ { j }$ : location candidates (fingerprint database)
    - if assume equal probability of $L _ { j }$ for all $j,k,...$
      - $P \left( L _ { j } | O \right) > P \left( L _ { k } | O \right) == P \left( O| L _ { j } \right) > P \left(O| L _ { k } \right)$
    - using histogram or kernel approach
    - Multiple RNs: jointly decision by products of the likelihood functions.
    - Theoretically increasing the grid size will increase the resolution. However, the RSSI measurement noise will bound the accuracy.
      - A tradeoff between position granularity and the successful probability estimation.
  - Artiﬁcial Neural Networks
    - Training NN in offline:  using the RSSI and the corresponding coordinates
    - Inference online: obtain the user location based on the online RSSI measurements
  - k-Nearest Neighbor (kNN)
    - online RSSI to obtain the k-nearest matches to the offline measured databases of the known locations using RMSE. Averaging to obtain location estimation.
  - Support Vector Machine (SVM)

### Angle of Arrival (AoA)

- Using Array antenna to estimate the direction of the transmitted waveform propagation using the difference of arrival time of each antenna
- Key advantage: minimum require 2 RNs/Monitors for 2-D environments and 3 RNs/Monitors for 3-D environments
- For short transmitter-receiver distance , need more complicated HW and calibration to accurate estimate the AoA.
- It assumes LOS transmission for accurate estimation, but in indoor, typically a multi-path environment.
<img src="https://imgur.com/AjIYKJ5.png" style="width: 600px" align="center"/> 

### Time of Flight (ToF)

- Time of Arrival
- Distance = ToF $\times$ C(=3e8 m/sec)
  - $t_{t,i}$ : transmitted timestamp
  - $t_{r,j}$ : arrival timestamp
  - $d_{i,j} = (t_{r,j} - t_{t,i})\times c$
- TOF based UE(user equipment) location
- Estimation accuracy depends on the channel bandwidth and sampling rate.
- Frequency domain super resolution technique is used to estimate ToF using CFR(CSI)
- Cannot eliminate location error or estimation bias when the LOS path is blocked.(not available)
<img src="https://imgur.com/elXiqhv.png" style="width: 600px" align="center"/> 
- Requires the synchronization between TXs and RX

### Time Difference of Arrival (TDoA)

- (TDoA) exploits the difference
in signals propagation times from different transmitters, measured at the receiver

- Hyperbola equations
$\begin{aligned} L _ { D ( i , j ) } & = \sqrt { \left( X _ { i } - x \right) ^ { 2 } + \left( Y _ { i } - y \right) ^ { 2 } + \left( Z _ { i } - z \right) ^ { 2 } } \\ & - \sqrt { \left( X _ { j } - x \right) ^ { 2 } + \left( Y _ { j } - y \right) ^ { 2 } + \left( Z _ { j } - z \right) ^ { 2 } } \end{aligned}$ 
- At least 3 RNs

<img src="https://imgur.com/rikx5KB.png" style="width: 600px" align="center"/>

- Strict Synchronization is required,but only need synchronization between TXs

### Return Time of Flight (RToF)

- Measures the round-trip signal propagation time to estimate the distance between Tx and Rx
- Benefit: Relative moderate time sync requirement.
- Affect the same accuracy factor twice as ToF (i.e. nonLoS, sampling rate, bandwidth...)
- Response delay highly depends on RX electronics and protocol overhead.
- Distance: $D _ { i j } = \frac { \left( t _ { 4 } - t _ { 1 } \right) - \left( t _ { 3 } - t _ { 2 } \right) } { 2 } \times v$
  - $t_2(@A) = t_1(@B) + t_p + \Delta_t$, $t_4(@B) = t_3(@A)+t_p - \Delta_t$
  - $\Delta_t$ is clock offset between A and B

### Phase of Arrival (PoA)

## TECHNOLOGIES FOR LOCALIZATION

## LOCALIZATION AND INTERNET OF THINGS

## EVALUATION FRAMEWORK

## LOCALIZATION SYSTEMS

## APPLICATIONS OF LOCALIZATION