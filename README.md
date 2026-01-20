 # 🐄 Milk Ledger | Учет надоя – Dairy Management Simulator

A strategic cattle breeding and dairy farm simulation game with genetics, economics, and herd management mechanics.

## 📋 Features
- **Herd Management** – Breed, feed, and care for cows and bulls
- **Genetics System** – Mendelian inheritance for traits and mutations
- **Dairy Production** – Milk yield tracking and optimization
- **Market Economy** – Buy/sell animals, manage finances
- **Data Persistence** – Save/load your farm progress
- **Expandable Architecture** – Modular systems for future features

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- No external dependencies (pure Python)

### Installation
```bash
# Clone the repository
git clone https://github.com/Artemlvannikov/Milk-Ledger.git
cd Milk-Ledger

# Run the game (not available)
python src/main.py 

### Project structure
src/
├── main.py              # Entry point, launches the game
├── game.py              # Main game loop and game state
├── models/
│   ├── __init__.py
│   ├── animal.py        # Base Animal class and subclasses (Cow, Bull, Calf)
│   └── pen.py           # Base Pen class and subclasses (CowPen, BullPen)
├── systems/
│   ├── __init__.py
│   ├── market.py        # Buying/selling animals, buy food, sell milk, market prices
│   ├── breeding.py      # Breeding logic, pairing animals
│   ├── milk_production.py # Milk calculation and collection
│   ├── feeding.py       # Feeding mechanics, nutrition costs
│   └── genetics.py      # Genetics system (Mendelian inheritance)
├── data/
│   ├── __init__.py
│   ├── storage.py       # Save/load game state
│   └── save_data.json   # Save file (generated)
├── ui/
│   ├── __init__.py
│   └── interface.py     # User interface (console-based)
└── config.json            # Game constants, balance settings 


### Current Development Status

🟡 In Active Development – Core systems are functional, UI and balancing in progress