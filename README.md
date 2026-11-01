# Analysis of OFDMA, Modulation and Coding in Wi-Fi 6/6E Networks

**A Lecture-Hall Capacity Study** — IEEE-format technical report

**Authors:** Aditya Joshi (Roll No. 30, 124BTEX1019) · Bhavya Kundhadia (Roll No. 35, 124BTEX1005)
**Institution:** Shah & Anchor Kutchhi Engineering College, Mumbai · Academic year 2026–2027

---

## Overview

Dense wireless LANs are limited by **airtime**, not headline PHY rate. This project studies how
**OFDMA**, **high-order QAM** and **FEC coding** jointly determine capacity, latency and reliability in
IEEE 802.11ax (Wi-Fi 6) and its 6 GHz extension (Wi-Fi 6E). A **120-seat lecture hall** is the running
design scenario.

The report covers:

- OFDM → OFDMA, the resource-unit (RU) hierarchy and per-RU data rates
- The 802.11ax rate equation and the full MCS 0–11 table for 20–160 MHz
- Analytical uncoded BER for 16- to 1024-QAM and the SNR cost of each modulation order
- Link adaptation: why the highest MCS is not always the fastest
- An airtime-overhead model comparing single-user OFDM round-robin with trigger-based OFDMA
- Wi-Fi 6E spectrum, simulation methodology (MATLAB WLAN Toolbox), metrics, and lecture-hall design guidelines

## Repository structure

```
.
├── report/
│   ├── IEEE_Report_WiFi6_OFDMA.pdf    # final report (7 pages, two-column IEEE style, A4)
│   └── IEEE_Report_WiFi6_OFDMA.docx   # editable Word version
├── figures/                           # all 13 figures (PNG, 300 dpi)
├── src/
│   ├── figs.py                        # generates every figure + computed values (res.json)
│   └── build.py                       # assembles the .docx report
└── README.md
```

## Key results

| Finding | Value |
|---|---|
| 4 × 200 B packets, 20 MHz MCS 7 — channel time, round-robin vs OFDMA | 848 µs vs 370 µs (**2.3×** less airtime) |
| OFDMA break-even point (airtime model) | 2 stations |
| Es/N0 for uncoded BER 10⁻³ — 16 / 64 / 256 / 1024-QAM | 16.5 / 22.5 / 28.4 / 34.3 dB |
| Peak 1-SS rate, MCS 11, 0.8 µs GI — 80 MHz / 160 MHz | 600.5 / 1201.0 Mb/s |

## Evidence status — please read

Results in the report are tagged by provenance:

- **Computed** — MCS and RU data rates, analytical BER curves, channel counts.
- **Assumed-parameter models** — link-adaptation SNR thresholds and MAC timing values in the airtime model. These are stated in the paper and are *not* measurements.
- **Illustrative** — the BER and goodput tables inherited from the project draft. They are synthetic and **must not be cited as measured Wi-Fi 6 results**.

No MATLAB/WLAN Toolbox simulation output is included yet; replacing the illustrative and assumed
items with simulator results is the main planned future work (see Section IX of the report).

## Reproducing the report

Requirements: Python 3.10+, and optionally LibreOffice for PDF conversion.

```bash
pip install numpy scipy matplotlib python-docx pillow

cd src
python figs.py      # regenerates figures/ and src/res.json
python build.py     # writes report/IEEE_Report_WiFi6_OFDMA.docx

# optional: convert to PDF
soffice --headless --convert-to pdf --outdir ../report ../report/IEEE_Report_WiFi6_OFDMA.docx
```

Figures use the *Liberation Serif* font if available (falls back to DejaVu Serif).

## Figures

| # | Figure | # | Figure |
|---|---|---|---|
| 1 | Wi-Fi 6/6E feature set | 8 | Simulation processing chain |
| 2 | RU hierarchy (20 MHz) | 9 | Airtime timeline, OFDM vs OFDMA |
| 3 | Channel counts, 2.4/5/6 GHz | 10 | Goodput vs stations (airtime model) |
| 4 | QAM constellations with AWGN | 11 | Draft goodput comparison (illustrative) |
| 5 | Analytical BER vs Es/N0 | 12 | Lecture-hall layout |
| 6 | MCS rate heatmap | 13 | Design trade-off matrix |
| 7 | Link-adaptation envelope | | |

## References

1. IEEE Std 802.11ax-2021, *Enhancements for High-Efficiency WLAN*.
2. E. Khorov et al., "A tutorial on IEEE 802.11ax high efficiency WLANs," *IEEE Commun. Surveys Tuts.*, 2019.
3. B. Bellalta, "IEEE 802.11ax: High-efficiency WLANs," *IEEE Wireless Commun.*, 2016.
4. R. van Nee and R. Prasad, *OFDM for Wireless Multimedia Communications*, Artech House, 2000.
5. J. G. Proakis and M. Salehi, *Digital Communications*, 5th ed., McGraw-Hill, 2008.
6. MathWorks WLAN Toolbox documentation — 802.11ax OFDMA system-level and link-level simulation examples (full URLs in the report).

## License

Add a license of your choice (e.g. MIT for code, CC BY 4.0 for the report) before publishing.
