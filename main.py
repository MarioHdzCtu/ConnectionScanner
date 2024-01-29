"""
    Este script es una replica del creado por 'stackoverknow' en YT. https://www.youtube.com/watch?v=BCk9wFHamdg
    No es de mi autoría, en caso de modificar el script lo especificaré en un comentario anexo a este

"""

import psutil
from  ip2geotools.databases.noncommercial import DbIpCity

def network_monitor():
    processess = psutil.net_connections(kind='inet')

    for process in processess:
        if process.status == 'ESTABLISHED' and process.raddr.ip != '127.0.0.1':
            print('===================')
            print('Connection found')
            get_process_details(process.pid)
            print(f'Scanning details in remote host ({process.raddr.ip})')
            get_remote_details(process.raddr.ip)

def get_process_details(pid): 
    try:
        process = psutil.Process(pid)
    except Exception as e:
        print(f'There was a problem accessing the process. {e}')
    else:
        print(f'[+] Process Name: {process.name}')
        print(f'[+] Process IS: {process.pid}')
        print(f'[+] Process Status: {process.status}')


def get_remote_details(ip):
    res = DbIpCity.get(ip, api_key='free')
    print(f'IP Address: {ip}')
    print(f'Location: {res.city} {res.region} {res.country}')
    print(f'Coordinates: Lat: {res.latitude}, Lng: {res.longitude}')

if __name__ == '__main__':
    network_monitor()