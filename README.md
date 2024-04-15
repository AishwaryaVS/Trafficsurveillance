# Live Traffic Camera Analysis for Improved Navigation

## Installation

### Server
```bash
cd server
python3 -m venv venv
source venv/bin/activate # for windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Client
```bash
cd client
npm install
```

## Running the Application

### Server
```bash
cd server
source venv/bin/activate # for windows: venv\Scripts\activate
flask run # --debug for auto-reload
```

### Client
```bash
cd client
npm run dev
```