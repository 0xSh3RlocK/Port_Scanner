#!/usr/bin/env python3
import argparse
import socket # for connecting
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue
import time
import pyfiglet
import os
import sys
import socks
from requests import ConnectionError
import json
import requests
proxies = {
    'http': 'socks5://localhost:9050',
    'https': 'socks5://localhost:9050'
}

# some colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
BLUE = Fore.BLUE


def Design_small():
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    # print({BLUE})
    print(f'{BLUE} {ascii_banner}')

def Design():
    os.system('clear')
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    # print({BLUE})
    print(f'{BLUE} {ascii_banner}')
    time.sleep(0.5)
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    print(ascii_banner)
    time.sleep(0.5)
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    print(ascii_banner)
    time.sleep(0.5)
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    print(ascii_banner)
    time.sleep(0.5)
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    print(ascii_banner)
    time.sleep(0.5)
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    print(ascii_banner)
    time.sleep(0.5)
    ascii_banner = pyfiglet.figlet_format("TEAM  19991")
    print(ascii_banner)
    time.sleep(0.5)
    os.system('clear')


# number of threads, Kol ma tzodha tsr3

# thread queue
q = Queue()
print_lock = Lock()

def port_scan(port):

    try:

        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
        s = socket.socket()
        s.connect((host, port))
       # raise KeyboardInterrupt
    except KeyboardInterrupt:
        print(f'You pressed CTRL +  C\n')
        print("GooodBye")
       # s.close()
    except:
        with print_lock:
            print(f"{GRAY}{host:15}:{port:5} is closed  {RESET}", end='\r')
    else:
        with print_lock:
            print(f"{GREEN}{host:15}:{port:5} is open    {RESET}")
    finally:
        s.close()


def scan_thread():
    global q
    while True:
        # get the port number from the queue
        ahmed = q.get()
        # y3mel scan
        port_scan(ahmed)
        # tells the queue al scan 5ls

        q.task_done()


def main(host, ports):
    global q
    for t in range(N_THREADS):
        # for each thread, start it
        t = Thread(target=scan_thread)

        t.daemon = True
        # start the daemon thread
        t.start()
    for ahmed in ports:
        # kol port, put that port into the queue
        # 3shan al scanning
        q.put(ahmed)
    # wait the threads ( port scanners ) to finish
    q.join()


if __name__ == "__main__":
    # parse some parameters passed
    parser = argparse.ArgumentParser(description="Team 19991 port scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default is 1-65535 (all ports)")
    parser.add_argument("--proxy", default='127.0.0.1:9050', type=str, help="Set Tor proxy (default: 127.0.0.1:9050)")
    parser.add_argument("--design", "-D", default="2",help="Choose the design you want D1 or D2")
    parser.add_argument("--speed", "-T", default="2",help="Increasing the threads to increase speed Defult T2")
    parser.add_argument("--output", "-O",  default=False, help="Make output file True or False")
#    parser.add_argument("--output", help="Return results as json/txt")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range
    #output = True
    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]
    # Tor proxy
    proxy = args.proxy
    session = requests.session()
    session.proxies = {'http': 'socks5h://{}'.format(proxy), 'https': 'socks5h://{}'.format(proxy)}

    if (args.speed == "1"):
        N_THREADS = 100

    elif (args.speed == "2"):
        N_THREADS = 200

    elif (args.speed == "3"):
        N_THREADS = 250

    elif (args.speed == "4"):
        N_THREADS = 300

    elif (args.speed == "5"):
        N_THREADS = 400
    else:
        print("Maximum input argument 5  press -h for information ")


    if (args.design == "1"):
        Design()

    else:
        Design_small()

    try:
        main(socket.gethostbyname(host), ports)

    except KeyboardInterrupt:
        print ('\n\nYou pressed CTRL + C \n')
        print('Good BYE \n')
        sys.exit(0)

if (args.output == "True"):
    os.system(f'python3 PORT_SCANNER.py {host} > output.txt')
else:
    pass
