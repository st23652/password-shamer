# Password Strength Shamer 🔥

A fun and cheeky web app that evaluates password strength and roasts you with hilarious insults if your password is weak!  
Choose between three roast levels — **mild**, **savage**, and **nuclear** — for escalating levels of brutal honesty.  
Share your roast results with friends or copy a shareable link.

---

## Features

- **Password strength evaluation** using custom logic combined with OpenAI-generated roasts
- Three roast levels:
  - Mild 🔥 — Light teasing  
  - Savage 🔥🔥 — Brutal burns  
  - Nuclear 🔥🔥🔥 — Maximum destruction  
- Shareable roast links for social fun  
- Copy roast text and share link with a single click  
- Simple and clean UI with dark mode support  



## Getting Started

### Prerequisites

- Python 3.8+
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- Git

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/st23652/password-shamer.git
   cd password-shamer

   # Create and activate a virtual environment
   python -m venv venv

   source venv/bin/activate      # Linux/macOS
   venv\Scripts\activate         # Windows PowerShell

   # Install dependencies
   pip install -r requirements.txt

   # Create a .env file in the project root and add your OpenAI API key
   OPENAI_API_KEY=your_openai_api_key_here

   # Run the Flask app
   python app.py
   ```
- Open your browser at http://localhost:5000

## Usage
- Enter a password you want to test
- Select the roast level
- Click Roast Me!
- View your roast and copy the roast or share the link with friends


## Technologies Used
- Python & Flask
- OpenAI API (GPT-4o) for generating roasts
- HTML, CSS (with dark mode)
- JavaScript (copy to clipboard and sharing)
   
