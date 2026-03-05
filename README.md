# IPCheck

A lightweight CLI-based IP reputation tool powered by the [AbuseIPDB](https://www.abuseipdb.com/) API. Built for quick reputation checks without leaving the terminal.

```
|---------------------------------|
| IPCheck - Powered by AbuseIPDB  |
|---------------------------------|

[-] Enter IP: 1.2.3.4

----------------------------------------------------------------------------
| IP Address:        1.2.3.4                                               |
| Country:           CN                                                    |
| ISP:               Some ISP                                              |
| Domain:            N/A                                                   |
| Total Reports:     142                                                   |
| Last Reported:     2025-12-01                                            |
| Confidence Score:  97                                                    |
| Verdict:           Malicious                                             |
----------------------------------------------------------------------------
```

## Features

- Clean, formatted CLI output
- Verdict based on AbuseIPDB confidence score and report count
- Save results to file for logging/reporting
- Validates that the IP is public before querying

## Verdict Thresholds

| Confidence Score | Verdict |
|-----------------|---------|
| ≥ 85 | Malicious |
| ≥ 50 | Suspicious |
| ≥ 10 | Low risk — possibly abused |
| < 10 | Clean |

## Requirements

- Python 3.x
- A free [AbuseIPDB API key](https://www.abuseipdb.com/register)

```bash
pip3 install requests
```

## Installation

```bash
git clone https://github.com/erik-dzibela/IPCheck
cd IPCheck
pip3 install requests
```

## Setup

Open `ipcheck.py` and replace the placeholder with your AbuseIPDB API key:

```python
'Key': 'Your_AbuseIPDB_API_Key'
```

## Usage

```bash
python3 ipcheck.py
```

You'll be prompted to enter an IP. After the result is displayed, you can optionally save it to `IPCheck_lookups.txt` for future reference.

## Planned Features

- Bulk IP checking (multiple IPs in one run)
- CSV export
- CLI argument support (non-interactive mode)

## Disclaimer

This tool is intended for legitimate security research and SOC/analyst workflows. Always ensure you have authorisation before investigating IPs in a professional context.
