# 💻 Micro-IT-Internship

## 🔐 Password Generator Web App

A modern and responsive web application built with **Flask** and **Tailwind CSS** to generate secure passwords based on customizable options.
---


## 🌟 Features

- Select password length (4–32 characters)
- Choose character types:
  - ✅ Uppercase letters
  - ✅ Lowercase letters
  - ✅ Numbers
  - ✅ Symbols
- Live password strength indicator
- "Copy to clipboard" button
- Responsive UI with Tailwind CSS
---


## 📸 Preview

> Add a screenshot named `preview.png` in your project directory and it will appear here:

![Password Generator Preview](static/images/preview.png)

---


## 📁 Project Structure

```

password-generator/
│
├── app.py                    # Flask backend
├── templates/
│   └── index.html            # Frontend with Tailwind CSS
├── static/
│   └── images/
│       └── preview\.png       # Optional screenshot or assets
├── README.md                 # Project documentation

```



### 🛠️ Installation & Setup

### 🔧 Prerequisites

- Python 3.7 or higher
- Flask

### 📦 Steps

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/password-generator.git
cd password-generator
````

2. **(Optional) Create a virtual environment**

``` 
python -m venv venv
# For macOS/Linux
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

### 3. **Install dependencies**

``` bash
pip install flask
```

4. **Run the Flask application**

```bash
python app.py
```

5. **Open in browser**

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔁 API Details

### Endpoint: `/generate`

* **Method:** POST
* **Content-Type:** `application/json`

### 📨 Request Example

```json
{
  "length": 16,
  "uppercase": true,
  "lowercase": true,
  "numbers": true,
  "symbols": true
}
```

### 📤 Response Example

```json
{
  "password": "gH#7ek9@Wd1!"
}

```

### 🧠 Password Strength Logic

Password strength is calculated based on:

* Length
* Uppercase characters
* Lowercase characters
* Digits
* Symbols

**Strength Levels:**

* Very Weak
* Weak
* Moderate
* Strong
* Very Strong

---

## 📌 Notes

* The generated password **always includes at least one character** from each selected type.
* If **no character types** are selected, an **empty password** is returned.

---

## 📜 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
