import pyautogui
import pyperclip
import time

def get_all_chrome_tab_urls():
    urls = []
    
    # 1. Attiva la finestra di Chrome
    try:
        # A seconda della tua lingua, potrebbe essere 'Google Chrome' o 'Chrome'
        chrome_window = pyautogui.getWindowsWithTitle('Google Chrome')[0] 
        chrome_window.activate()
        time.sleep(0.5) # Dai tempo alla finestra per attivarsi
    except IndexError:
        print("Finestra di Google Chrome non trovata. Assicurati che Chrome sia aperto.")
        return []

    first_url = None
    
    while True:
        # 2. Seleziona l'URL nella barra degli indirizzi (Ctrl + L)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.1)

        # 3. Copia l'URL negli appunti (Ctrl + C)
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(0.1)

        # 4. Recupera l'URL dagli appunti
        current_url = pyperclip.paste()

        # 5. Controlla se è il primo URL che abbiamo visto
        if first_url is None:
            first_url = current_url
            urls.append(current_url)
        elif current_url == first_url:
            # Abbiamo fatto un giro completo, usciamo dal ciclo
            break
        else:
            urls.append(current_url)
        
        # 6. Passa alla tab successiva (Ctrl+Tab)
        pyautogui.hotkey('ctrl', 'tab')
        time.sleep(0.5) # Dai tempo a Chrome di cambiare tab

    return urls

if __name__ == "__main__":
    print("Avvio della raccolta degli URL delle tab di Chrome...")
    all_urls = get_all_chrome_tab_urls()
    
    if all_urls:
        print("\nURL delle tab di Chrome trovate:")
        for i, url in enumerate(all_urls):
            print(f"{i + 1}. {url}")
    else:
        print("Nessun URL raccolto. Controlla che Chrome sia aperto e in primo piano.")
