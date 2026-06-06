import os
import psutil

def optimizar_sistema():
    print("[*] Iniciando VORTEX Core...")
    
    # 1. CPU Performance
    print("[*] Ajustando CPU a modo Performance...")
    os.system("echo performance | sudo tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor > /dev/null 2>&1")
    
    # 2. RAM Purgue
    mem_antes = psutil.virtual_memory().available
    print("[*] Liberando caché de RAM...")
    os.system("sync && echo 3 | sudo tee /proc/sys/vm/drop_caches > /dev/null 2>&1")
    mem_liberada = (psutil.virtual_memory().available - mem_antes) // 1024 // 1024
    print(f"[+] RAM liberada: {mem_liberada} MB")
    
    # 3. SSD Trim
    print("[*] Optimizando almacenamiento (SSD)...")
    os.system("sudo fstrim -av > /dev/null 2>&1")
    
    print("[+] Optimización completa. ¡Sistema listo!")

if __name__ == "__main__":
    optimizar_sistema()
