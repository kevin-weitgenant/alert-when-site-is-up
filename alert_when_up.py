import requests
import time
import webbrowser
import playsound

code = 502
maintence = True
while (code != 200 or maintence):
    
    try:
        time.sleep(5)
        response = requests.get("https://www.unicfcead.com.br/", timeout = 20)
        code = response.status_code
        print(code,"\n sleep")
        
        content = str(response.content)
        if content.find("indisponível") == -1:
            maintence = False
            print("não está em manutenção")            
        else:print("em manutenção") 

          
    except requests.exceptions.Timeout:
        print("fail")
        time.sleep(10)


print("musiquinha de alerta pois está on")
playsound.playsound('alert.mp3')






     

