import os
import time
import tkinter as tk
import psutil

def get_cpu_frequency():
    cpu_info = os.popen('cat /proc/cpuinfo').read()
    frequency = 0.0

    for line in cpu_info.split('\n'):
        if 'cpu MHz' in line:
            frequency = float(line.split(':')[-1].strip()) / 1000
            break

    return frequency

def get_cpu_temperature():
    temperature = psutil.sensors_temperatures()['coretemp'][0].current
    return temperature

def get_gpu_temperature():
    temperature_info = os.popen('nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits').read()
    temperature = float(temperature_info.strip())
    return temperature

def get_gpu_usage():
    usage_info = os.popen('nvidia-smi --query-gpu=utilization.gpu --format=csv,noheader,nounits').read()
    usage = float(usage_info.strip())
    return usage

def get_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    return usage

def get_memory_usage():
    memory = psutil.virtual_memory().percent
    return memory

def update_info_labels():
    cpu_frequency = get_cpu_frequency()
    cpu_temperature = get_cpu_temperature()
    gpu_temperature = get_gpu_temperature()
    gpu_usage = get_gpu_usage()
    cpu_usage = get_cpu_usage()
    memory_usage = get_memory_usage()

    frequency_label.config(text=f'Frequência atual do CPU é {cpu_frequency:.2f} GHz', fg='green')
    cpu_temp_label.config(text=f'Temperatura da CPU é {cpu_temperature}°C', fg='green')
    gpu_temp_label.config(text=f'Temperatura da GPU é {gpu_temperature}°C', fg='green')
    usage_label.config(text=f'Uso da GPU é {gpu_usage}%, \n\nUso da CPU é {cpu_usage}%, \n\nUso de Memória é {memory_usage}%', fg='green')

    frequency_label.after(1000, update_info_labels)

# Criação da janela principal
window = tk.Tk()
window.title("Monitor de Hardware")
window.configure(bg='black')

# Centralizar a janela na área de trabalho
window_width = 400
window_height = 300
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Criação dos rótulos para exibir as informações
frequency_label = tk.Label(window, text="Frequência atual do CPU é 0.00 GHz", font=("Arial", 12), bg='black', fg='green')
frequency_label.pack(pady=10)

cpu_temp_label = tk.Label(window, text="Temperatura da CPU é 0°C", font=("Arial", 12), bg='black', fg='green')
cpu_temp_label.pack(pady=10)

gpu_temp_label = tk.Label(window, text="Temperatura da GPU é 0°C", font=("Arial", 12), bg='black', fg='green')
gpu_temp_label.pack(pady=10)

usage_label = tk.Label(window, text="Uso da GPU é 0%, Uso da CPU é 0%, Uso de Memória é 0%", font=("Arial", 12), bg='black', fg='green')
usage_label.pack(pady=10)

# Inicia a atualização das informações
update_info_labels()

# Execução da janela principal
window.mainloop()
