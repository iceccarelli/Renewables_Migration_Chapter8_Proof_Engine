# The Renewables Migration - Chapter 8 Proof Engine
### The De-Industrialization Pulse: From Industrial Exodus to Protocol Sovereignty

This repository contains the complete mathematical proof engine for Chapter 8 of "The Renewables Migration" by Vincenzo Grimaldi. It verifies every claim, equation, and figure related to **Industrial Resilience**, **Carbon Recovery**, and the **Relocation Math**.

## 🚀 Quick Start (Under 60 Seconds)
```bash
# Clone the repository
git clone https://github.com/iceccarelli/Renewables_Migration_Chapter8_Proof_Engine.git
cd Renewables_Migration_Chapter8_Proof_Engine

# Install dependencies
pip install -r requirements.txt

# Run the interactive dashboard
streamlit run main_interactive.py

# Run the automated proofs
PYTHONPATH=. pytest tests/test_book_numbers.py
```

## 📊 Chapter 8 Metrics Verified
- **Legacy Market Rate:** €0.20/kWh (Lethal for industry)
- **Mittelstand Death Zone:** €0.15/kWh (Survival threshold)
- **Carbon Leakage Paradox:** 1.0-1.8 t/t CO2 added per tonne of relocated steel
- **Annual Prevented Leakage:** 35 Mt CO2 via MCP retention
- **Protocol Offset (Psi_MCP):** 60% offset of the energy gap (E)
- **Sovereignty Metric (S):** 28% (2026) to 75% (2030)

## 🛠️ Package Structure
- `chapter8_core.py`: Mathematical engine for industrial resilience, carbon recovery, and relocation math.
- `main_interactive.py`: Streamlit dashboard with "Spy Mode" to highlight book claims.
- `data/book_numbers.csv`: Hardcoded metrics extracted from the book.
- `tests/test_book_numbers.py`: Pytest suite validating all book numbers.
- `notebooks/01_Prove_Chapter8.ipynb`: Jupyter notebook with step-by-step proofs and interactive sliders.
- `plots/`: Reproduced figures (Figure 8.1, 8.2).

## ⚖️ License
MIT License - Copyright (c) 2026 Vincenzo Grimaldi
