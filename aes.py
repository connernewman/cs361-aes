mx = b'\x01\x1b'
c = b'\x63'
sbox = {b'\x98': b'F', b'\xbc': b'e', b'&': b'\xf7', b'\xed': b'U', b'\xca': b't', b'\x0b': b'+', b'w': b'\xf5', b'\xfd': b'T', b'\xa5': b'\x06', b'U': b'\xfc', b'9': b'\x12', b'\xc9': b'\xdd', b'\x14': b'\xfa', b'J': b'\xd6', b'\x89': b'\xa7', b'l': b'P', b'\x04': b'\xf2', b'\xcd': b'\xbd', b'\x81': b'\x0c', b'\r': b'\xd7', b'\xc8': b'\xe8', b'n': b'\x9f', b'\xc3': b'.', b' ': b'\xb7', b'A': b'\x83', b'\x94': b'"', b'\xfe': b'\xbb', b's': b'\x8f', b'\xf6': b'B', b'-': b'\xd8', b'\xd9': b'5', b'\x9f': b'\xdb', b'D': b'\x1b', b'\x05': b'k', b'\x0f': b'v', b'}': b'\xff', b'%': b'?', b'\xde': b'\x1d', b'[': b'9', b'\xe3': b'\x11', b'\x92': b'O', b'\xd0': b'p', b'\x16': b'G', b'\x13': b'}', b'\xa7': b'\\', b'\x1c': b'\x9c', b'Y': b'\xcb', b'\x97': b'\x88', b'\x88': b'\xc4', b'#': b'&', b'_': b'\xcf', b'2': b'#', b'F': b'Z', b'\x8a': b'~', b'\xdb': b'\xb9', b'\xae': b'\xe4', b'\x8b': b'=', b',': b'q', b'o': b'\xa8', b'\x02': b'w', b'\x9b': b'\x14', b'*': b'\xe5', b'\xcb': b'\x1f', b'\xcc': b'K', b'\xf9': b'\x99', b'\xd8': b'a', b'\x03': b'{', b'\x07': b'\xc5', b'\xb8': b'l', b'\x10': b'\xca', b'\xb5': b'\xd5', b'\xba': b'\xf4', b'\xb9': b'V', b'6': b'\x05', b'\xd3': b'f', b'S': b'\xed', b'\xb2': b'7', b'\xe6': b'\x8e', b'\xea': b'\x87', b'm': b'<', b'\xb7': b'\xa9', b'd': b'C', b'\xa2': b':', b'\xaa': b'\xac', b'\x1f': b'\xc0', b'\xa0': b'\xe0', b'\x00': b'c', b'5': b'\x96', b'a': b'\xef', b'\xe0': b'\xe1', b'\x96': b'\x90', b'\xfa': b'-', b'\n': b'g', b'\xfb': b'\x0f', b'\x83': b'\xec', b'\x1a': b'\xa2', b'!': b'\xfd', b'\x1d': b'\xa4', b'\xd5': b'\x03', b'R': b'\x00', b'^': b'X', b'\x87': b'\x17', b'\xa6': b'$', b'\t': b'\x01', b'\xf8': b'A', b'\xe9': b'\x1e', b'.': b'1', b'i': b'\xf9', b';': b'\xe2', b'\xa9': b'\xd3', b'\xd7': b'\x0e', b'\xc2': b'%', b'\xaf': b'y', b'\xf5': b'\xe6', b'\x12': b'\xc9', b'\xc5': b'\xa6', b'x': b'\xbc', b'\xd6': b'\xf6', b'\xef': b'\xdf', b'r': b'@', b'\xe2': b'\x98', b'P': b'S', b'\x19': b'\xd4', b'G': b'\xa0', b'V': b'\xb1', b'C': b'\x1a', b'\xdc': b'\x86', b'\x93': b'\xdc', b'\x8e': b'\x19', b'`': b'\xd0', b'z': b'\xda', b'\xe1': b'\xf8', b'|': b'\x10', b'\x86': b'D', b'\xa3': b'\n', b'E': b'n', b'f': b'3', b'<': b'\xeb', b'\xbb': b'\xea', b'K': b'\xb3', b'h': b'E', b'{': b'!', b'+': b'\xf1', b'\xe8': b'\x9b', b'y': b'\xb6', b'\xeb': b'\xe9', b'I': b';', b'\xf3': b'\r', b'1': b'\xc7', b'\xd2': b'\xb5', b'\xab': b'b', b'\xda': b'W', b'\x8c': b'd', b'\xd1': b'>', b')': b'\xa5', b'\x0e': b'\xab', b'\xbd': b'z', b'\x1e': b'r', b'v': b'8', b'\x18': b'\xad', b'\xcf': b'\x8a', b'p': b'Q', b'\xf0': b'\x8c', b'c': b'\xfb', b'\xb6': b'N', b'\xce': b'\x8b', b'M': b'\xe3', b'?': b'u', b'@': b'\t', b'\xdd': b'\xc1', b'"': b'\x93', b'\x85': b'\x97', b'\xbf': b'\x08', b'8': b'\x07', b'\x8f': b's', b'\x9a': b'\xb8', b'\xec': b'\xce', b'O': b'\x84', b'\x1b': b'\xaf', b'\xd4': b'H', b'>': b'\xb2', b'=': b"'", b'\xad': b'\x95', b'g': b'\x85', b'\xb0': b'\xe7', b'B': b',', b'\xf1': b'\xa1', b'\x08': b'0', b'\x9c': b'\xde', b'\xc4': b'\x1c', b'3': b'\xc3', b'q': b'\xa3', b'\xc1': b'x', b'\xfc': b'\xb0', b"'": b'\xcc', b'u': b'\x9d', b'4': b'\x18', b'\xb3': b'm', b'\x82': b'\x13', b'T': b' ', b'b': b'\xaa', b'7': b'\x9a', b't': b'\x92', b'\x91': b'\x81', b'Z': b'\xbe', b'W': b'[', b'\xa1': b'2', b'\xc0': b'\xba', b'L': b')', b'k': b'\x7f', b'e': b'M', b'\x84': b'_', b'\xe7': b'\x94', b'Q': b'\xd1', b'\xc6': b'\xb4', b'\x90': b'`', b'j': b'\x02', b'\xb4': b'\x8d', b'X': b'j', b'\xff': b'\x16', b'0': b'\x04', b'\xdf': b'\x9e', b'\xa4': b'I', b'\xee': b'(', b'N': b'/', b'(': b'4', b'\xac': b'\x91', b':': b'\x80', b'\xf7': b'h', b'\x15': b'Y', b'\x9d': b'^', b'\x95': b'*', b'/': b'\x15', b'\xbe': b'\xae', b']': b'L', b'\xa8': b'\xc2', b'\xb1': b'\xc8', b'\x06': b'o', b'\xf4': b'\xbf', b'\x99': b'\xee', b'\x9e': b'\x0b', b'\x8d': b']', b'\x7f': b'\xd2', b'H': b'R', b'\xe5': b'\xd9', b'~': b'\xf3', b'\xf2': b'\x89', b'\x01': b'|', b'\x11': b'\x82', b'\xc7': b'\xc6', b'\x17': b'\xf0', b'\\': b'J', b'\x80': b'\xcd', b'$': b'6', b'\x0c': b'\xfe', b'\xe4': b'i'}

def rot_word(word):
	b = bytearray(word)
	x = b[-1]
	b.insert(0, x)
	b = b[:-1]
	return bytes(b)

def ff_add(x, y):
	xi = int.from_bytes(x, 'big')
	yi = int.from_bytes(y, 'big')
	res = xi ^ yi
	return res.to_bytes((res.bit_length() + 7) // 8, 'big')

def ff_mult(x, y):
	xi = int.from_bytes(x, 'big')
	yi = int.from_bytes(y, 'big')
	bits = 0
	for bit_x in range(0, xi.bit_length()):
		if xi & (0x1 << bit_x):
			for bit_y in range(0, yi.bit_length()):
				if yi & (0x1 << bit_y):
					bits ^= (0x1 << (bit_x + bit_y))
	return bits.to_bytes((bits.bit_length() + 7) // 8, 'big')

def ff_deg(gf):
	return int.from_bytes(gf, 'big').bit_length() - 1

def ff_mod(p, m):
	if ff_deg(p) < 8:
		return p
	degree_difference = ff_deg(p) - ff_deg(mx)
	mult_by = 0x1 << degree_difference
	mult_by = mult_by.to_bytes((mult_by.bit_length() + 7) // 8, 'big')
	part = ff_mult(m, mult_by)
	q = ff_add(part, p)
	return ff_mod(q, m)

def ff_dot(x, y):
	return ff_mod(ff_mult(x, y), mx)

def xtime(x):
	return ff_dot(x, b'\x02')

def gf_repr(gf):
	gf = int.from_bytes(gf, 'big')
	res = []
	for i in range(gf.bit_length(), -1, -1):
		if gf & (0x1 << i):
			res.append('x^' + str(i))
	return ' + '.join(res)#.replace('x^1', 'x').replace('x^0', '1')

def m_inv(x):
	if x == b'\x00':
		return x
	for i in range(1, 256):
		b = i.to_bytes(1, 'big')
		if ff_dot(x, b) == b'\x01':
			return b

def aes_128_encrypt(input_bytes, key_bytes):
	Nk = 4
	Nb = 4
	Nr = 10
	assert len(input_bytes) == 16

	# Load input bytes into 4 X 4 state array
	state = []
	for row in range(4):
		state.append([[input_bytes[row], input_bytes[row + 4], input_bytes[row + 8], input_bytes[row + 12]]])

	#words = [input_bytes[4 * x:4 * x + 4] for x in range(4)]

	add_round_key(state, w[0, Nb - 1])

	for rnd in range(Nr - 1):
		# SubBytes step
		for row in state:
			for i, ff in enumerate(row):
				row[i] = sbox[ff]

		# ShiftRows step
		for j, row in enumerate(state):
			for i, ff in enumerate(row):
				row[i] = row[(i + j) % Nb]

	out = bytearray(16)
	for i in range(16):
		out[i] = state[i // 4][i % 4]
	return bytes(out)

def main():
	pass

if __name__ == '__main__':
	main()

