# IEEE 802.11be — Extremely High Throughput: The Next Generation of Wi-Fi Technology Beyond 802.11ax

https://arxiv.org/pdf/1902.04320

###### tags: `Paper Study` `Wi-Fi`


## Key features 

- Support 6G band
- 320MHz maximum BW
- Coordinated Communication 
- 16 Spatial stream 
- implicit CSI sounding 
- Hybrid ARQ 
- Full duplex communication
- data aggregation 
 
## Objective and  Standard development time frame

### Objectvie

- Enabling new MAC and PHY to maximum throughput(at least) **30Gbps**
- 4x data service access wrt 802.11ax
- Using frequencies between 1 to 7.125 GHz
- backward support 11g/n/ac/ax in 2.4,5 and 6GHz

### Time-frame

![Imgur](https://i.imgur.com/ZclFM2d.png)


## Candidate Technical Features

- 320MHz BW and more efficiently of non-contiguous spectrum
  - adoption of **160** MHz and **320** MHz communication bandwidth per AP in the 6 GHz band as mandatory and optional features
  - Moreover, a **minimum channel size** of **40** or even **80** MHz in the 6 GHz band.
  - Always schedule uplink transmissions in the 6 GHz band

- Multi-channel/multi-band aggregation and operation
  - Multi-band data aggregation: aggregation of 5G and 6G band data transmission
    - require device sync start of TXOP in different band
  - Simultaneous transmission and reception in different bands
    - multi-band full duplex
    - reducing latency and enhancing the throughput by enabling an asynchronous and simultaneous up-link/downlink operation in separate bands
  - Simultaneous transmission and reception in the same band
    - in-band full duplex operation for Wi-Fi
  - Data and control plane separation
    - unprecedented opportunity of separating the data and management planes
    - immediate status feedback is possible in data and control plane separation.
    - reliable feedback channel on control plan is possible.
  - 16 spatial streams and multiple-input multiple-output (MIMO) protocol enhancements
    - possible high speed back-haul provided by ﬁber-to-the-home (FTTH) solutions and the rich scattering in the indoor environments
    - implicit sounding procedure to solve hugh channel sounding feedback data rate 
  - Multi-access point coordination Communication
  ![Imgur](https://i.imgur.com/fOpoVZ7.png) 
    - Coordinated OFDMA
    - Coordinated Null Steering
      - APs can also leverage their antennas to place spatial radiation nulls from and towards non-associated devices in their neighbor-hoods
    - Distributed MIMO (D-MIMO) 
      - multiple non-collocated APs perform a joint data transmission and/or reception
from multiple STAs
  - Enhanced link adaptation and retransmission protocol
     - hybrid ARQ (HARQ) capabilities

### System performance comparison to 11ac

- Benefit
  - More bandwidth
  - More antenna and spatial stream
  - implicit CSI acquisition

![Imgur](https://i.imgur.com/2fVaR82.png)


- Throughput enhance:
  - 3.2x enhance in 50% CDF, 
  - 4.6x enhance in worst 5% CDF

- Throughput Comparison
![Throughput Compare](https://i.imgur.com/jr3QrS3.png)