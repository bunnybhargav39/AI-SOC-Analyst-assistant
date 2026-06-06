# AI-SOC-Analyst-assistant

# AI-Powered SOC Analyst Assistant

An AI-powered SOC Analyst Assistant built using Python, Streamlit, and Gemini API to automate security log analysis and threat triage.

## Features

- Upload SOC logs from Excel files
- AI-driven threat analysis using Gemini
- Severity classification
- Threat explanation
- Remediation recommendations
- Streamlit-based web interface

## Technologies Used

- Python
- Streamlit
- Gemini API
- Pandas
- Prompt Engineering

## Project Architecture

Excel Logs
↓
Pandas
↓
Gemini AI
↓
SOC Analysis
↓
Streamlit Dashboard

## Installation

```bash
git clone https://github.com/<username>/ai-soc-analyst-assistant.git
cd ai-soc-analyst-assistant

pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Run:

```bash
streamlit run UI.py
```

## Future Enhancements

- VirusTotal integration
- MITRE ATT&CK mapping
- SIEM integration
- Threat Intelligence enrichment
- PDF incident reports
- Real-time log ingestion
