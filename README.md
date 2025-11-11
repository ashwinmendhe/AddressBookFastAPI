# AddressBookFastAPI

# For commiting git set url
git remote set-url origin https://github.com/ashwinmendhe/AddressBookFastAPI.git

git push origin main


# 🏠 Address Book API (FastAPI + SQLite)

A simple FastAPI-based Address Book application supporting CRUD operations and distance-based address search.

## 🧰 Features
- Create, update, delete, and list addresses
- Store coordinates (latitude, longitude)
- SQLite database (no external setup)
- Filter addresses within a given distance
- Automatic validation with Pydantic
- Interactive docs via Swagger UI

---

## ⚙️ Installation & Run

```bash
# 1️⃣ Clone the repo
git clone https://github.com/ashwinmendhe/AddressBookFastAPI.git
cd AddressBookFastAPI

# 2️⃣ Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Run the application
uvicorn app.main:app --reload
