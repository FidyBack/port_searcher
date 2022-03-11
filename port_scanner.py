import socket, sys, os
import threading
from queue import Queue
from time import time

print_lock = threading.Lock()
q = Queue()
ports = {}


def start(host):
	os.system('clear') if os.name == 'posix' else os.system('cls')
	hostIp = socket.gethostbyname(host)
	ports['PORTA'] = ('ESTADO', 'SERVIÇO')

	print("-" * 60)
	print(f"Procurando por portas abertas\nHost: {host}\nIp: {hostIp}")
	print("-" * 60)


def align(portList):
	alignPort = len(max(portList.keys(), key=len))+1
	alignState = len(max([i[0] for i in portList.values()], key=len))+1

	for i in portList:
		print(f"{i.ljust(alignPort, ' ')} {portList[i][0].ljust(alignState, ' ')} {portList[i][1]}")


def threader(host):
	while True:
		port = q.get()
		range_scan(port, host)
		q.task_done()


def range_scan(port, host):
	socket.setdefaulttimeout(2)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		result = sock.connect_ex((host, port))
		if result == 0:
			try:
				ports[str(port)] = ('open', socket.getservbyport(port))
			except OSError:
				ports[str(port)] = ('open', 'desconhecido')
		sock.close()
	
	except Exception as e:
		print(e)
	


def main():
	t1 = time()

	try:
		host = sys.argv[1]
		start(host)

	except IndexError:
		print (f"Erro: Argumentos Insuficienes")

	if len(sys.argv) == 2:
		for _ in range(700):
			thread = threading.Thread(target=threader, args=[host], daemon = True)
			thread.start()

	for port in range(65535):
		q.put(port)

	q.join()

	align(ports)
	t2 = time()
	print("-" * 60)
	print(f'Completo em {round(t2-t1, 2)} segundos')


if __name__ == '__main__':
	main()