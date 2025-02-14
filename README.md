# Setting Up and Activating a Virtual Environment

## Windows
### 1. Create a Virtual Environment
Run the following command to initialize a virtual environment:
```sh
python -m venv <folder-name>
```
For example:
```sh
python -m venv venv
```

### 2. Activate the Virtual Environment
Use the following command to activate it:
```sh
<folder-name>\Scripts\activate.bat
```
Example:
```sh
venv\Scripts\activate.bat
```

---

## Linux/macOS
### 1. Create a Virtual Environment
Initialize a virtual environment using:
```sh
python -m venv <folder-name>
```
Example:
```sh
python -m venv venv
```

### 2. Activate the Virtual Environment
Activate it with:
```sh
source <folder-name>/bin/activate
```
Example:
```sh
source venv/bin/activate
```

---

## Deactivating the Virtual Environment
To exit the virtual environment, run:
```sh
deactivate
