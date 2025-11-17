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
# 1 Clone the repo
git clone https://github.com/ashwinmendhe/AddressBookFastAPI.git
cd AddressBookFastAPI

# 2 Create and activate virtual environment
python3.13 -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# 3 Install dependencies
python3.13 -m pip install -r requirements.txt

# 4 Run the application
uvicorn app.main:app --reload

# 5 Api Endpoints

## 1. To Get all list 
GET http://127.0.0.1:8000/addresses/

## 2. To Create new entry 
POST http://127.0.0.1:8000/addresses/

## 3. To Get single data using address_id
GET http://127.0.0.1:8000/addresses/{address_id}


## 3. To Get single object using address_id
GET http://127.0.0.1:8000/addresses/{address_id}

## 4. To Update single object using address_id
PUT http://127.0.0.1:8000/addresses/{address_id}

## 4. To Delete object using address_id
DELETE http://127.0.0.1:8000/addresses/{address_id}

## 5. To get address using nearby coordinates
GET http://127.0.0.1:8000/addresses/nearby
lat = -40
log = -120
radius_kn = 100

