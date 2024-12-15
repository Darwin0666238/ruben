import requests
import json
import tkinter as tk
from tkinter import messagebox

def fetch_repo_info():
    repo_name = entry.get()
    url = f"https://api.github.com/repos/{repo_name}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        data = response.json()
        
        # Формирование нужного JSON
        repo_info = {
            'company': None,
            'created_at': data['created_at'],
            'email': None,
            'id': data['id'],
            'name': data['name'],
            'url': data['html_url']
        }
        
        # Запись в файл
        with open(f"{repo_name.replace('/', '_')}_info.json", "w") as json_file:
            json.dump(repo_info, json_file, indent=4)
        
        messagebox.showinfo("Success", f"Информация о репозитории сохранена в {repo_name.replace('/', '_')}_info.json")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Не удалось получить информацию: {e}")

# Создание графического интерфейса
root = tk.Tk()
root.title("GitHub Repo Info Fetcher")

tk.Label(root, text="Введите имя репозитория (например, kubernetes/kubernetes):").pack(pady=10)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

fetch_button = tk.Button(root, text="Получить информацию", command=fetch_repo_info)
fetch_button.pack(pady=20)

root.mainloop()
