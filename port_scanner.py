import socket, sys

class Scanner:
	def full_scanner(host, inter=None):
		if inter == None:
			for port in range(1, 65535):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				conn = s.connect_ex((host, port))
				if conn == 0:
					try:
						print(f"Porta {port} Aberta, Serviço: {socket.getservbyport(port)}")
						s.close()
					except OSError:
						print(f"Porta {port} Aberta, Serviço: desconhecido")

		else:
			for port in range(inter[0], inter[1]):
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				conn = s.connect_ex((host, port))
				if conn == 0:
					try:
						print(f"Porta {port} Aberta, Serviço: {socket.getservbyport(port)}")
						s.close()
					except OSError:
						print(f"Porta {port} Aberta, Serviço: desconhecido")
		
		print("Fim do escaneamento")


	def port_scanner(host, port):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		try:
			port = int(port)
			conn = s.connect_ex((host, port))
			if conn == 0:
				try:
					print(f"Porta {port} Aberta, Serviço: {socket.getservbyport(port)}")
					s.close()
				except OSError:
					print(f"Porta {port} Aberta, Serviço: desconhecido")
			else:
				print("Porta Fechada")
			print("Fim do escaneamento")

		except ValueError:
			if '-' in port:
				ports = port.split("-")
				try:
					i1 = int(ports[0])
					i2 = int(ports[1])
					Scanner.full_scanner(host, (i1, i2))

				except ValueError as e:
					raise Exception(e)
			else:
				raise Exception ("Formatação inconsistente")

			

def main():
	if len(sys.argv) <= 1:
		raise Exception("Argumentos Insuficientes")

	elif len(sys.argv) == 2:
		ipAddress = sys.argv[1]
		Scanner.full_scanner(ipAddress)

	elif len(sys.argv) == 3:
		ipAddress = sys.argv[1]
		port = sys.argv[2]
		Scanner.port_scanner(ipAddress, port)


if __name__ == '__main__':
	main()