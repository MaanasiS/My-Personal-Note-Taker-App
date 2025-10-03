📝 My Personal Note Taker App



A simple Notes application built using **Flask** and **SQLite**.  

This app allows users to **create, view, edit, and delete notes** with a clean, vintage-style UI.



---



🚀 Features

\- Add new notes  

\- View all notes  

\- View single note details  

\- Edit existing notes  

\- Delete notes  

\- Vintage-style UI with responsive design (CSS included)  



---



📂 Project Structure



My-Personal-Note-Taker-App/

│── app.py # Main Flask application

│── requirements.txt # Python dependencies

│── README.md # Project documentation

│── notes.db (auto) # SQLite database (created automatically)

│

├── static/

│ └── styles.css # CSS for styling

│

└── templates/

├── index.html # Home page (list + add notes)

├── note.html # View single note

└── edit.html # Edit note page





---



⚙️ Installation \& Setup (Local)



1\. Clone the repository



git clone https://github.com/MaanasiS/My-Personal-Note-Taker-App

cd My-Personal-Note-Taker-App



2\. Create a virtual environment (optional but recommended)



python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\\Scripts\\activate      # Windows



3\. Install dependencies



pip install -r requirements.txt





4\. Run the app



python app.py





Now open your browser and go to 👉 http://127.0.0.1:5000


🛠️ Requirements

Python 3.8+

Flask

SQLite (comes with Python)





