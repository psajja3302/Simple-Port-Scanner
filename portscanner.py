import socket
import re
import threading

NUM_THREADS = 400

def scanner(ip, port, ports, lock):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                with lock:
                    ports.append(port)
    except:
        pass

def main():
    #Validity Check of IP address using regex
    validip = re.compile('^((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])$')
    while True:
        ipinput = input('\nEnter the ip address you would like to scan (Ex: 192.168.23.23): ').strip()
        if validip.search(ipinput):
            break
        else:
            print('\nEnter a valid ip address.')
    #Validity Check of port ranges (0-65535)
    while True:
        portinput = input('\nEnter the range of ports you would like to scan (Ex: 23-53): ').strip()
        parts = portinput.split('-')
        min, max = parts[0], parts[1]
        if (len(parts) == 2
            and ((min.isdigit() and (0 <= int(min) <= 65535)))
            and (max.isdigit() and (0 <= int(max) <= 65535))
            and int(min) <= int(max)):
            min, max = int(parts[0]), int(parts[1])
            break
        print('Invalid range. Use format 0-65535, min must be <= max.')

    print(f'\nScanning ports {min} – {max} on {ipinput}...\n')

    #Threading Process using Scanner 
    lock = threading.Lock()
    t_list = []
    ports = []

    for port in range(min, max + 1):
        t = threading.Thread(target=scanner, args=(ipinput, port, ports, lock))
        t_list.append(t)
        t.start()
        if len(t_list) >= NUM_THREADS:
            for t in t_list:
                t.join()
            t_list.clear()
    for t in t_list:
        t.join()
    
    #Output 
    for port in ports:
          print(f'Port: {port} | Status: Open')
    if (len(ports) == 0):
        print('All ports in the provided range are closed')
    else:
        print('\nAll other ports in the provided range are closed.')


if __name__ == "__main__":
    main()