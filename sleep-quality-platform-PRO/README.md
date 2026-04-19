
# 💤 Sleep Quality Analyzer (PRO VERSION)

## 🚀 Descrizione
Sistema modulare per analisi della qualità del sonno basato su criteri percentuali.

## 🧠 Architettura
- core/ → logica business
- cli/ → interfaccia terminale
- tests/ → test automatici

## ⚙️ Esecuzione

```bash
python cli/main.py example_input.txt
```

## 🧪 Test

```bash
pytest
```

## 📊 Output
- numero sonni sopra target
- statistiche (min/max/media)
- valutazione qualità
- top 5 durate

## 🧩 Criteri
- REM ≥ 20%
- DEEP ≥ 13%
- WAKE < 15%
- durata totale ≥ target
