mx = b'\x01\x1b'

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
	print('Multiplying', hex(x[0])[2:], 'and', hex(y[0])[2:])
	res = bytearray(2)
	bits = 0
	for bit_x in range(0, 8):
		if x[0] & (0x1 << bit_x):
			for bit_y in range(0, 8):
				if y[0] & (0x1 << bit_y):
					bits ^= (0x1 << (bit_x + bit_y))
	print('Got bits:', bits)
	return bits

def print_GF(gf):
	gf = int.from_bytes(gf, 'big')
	res = []
	for i in range(gf.bit_length(), -1, -1):
		if gf & (0x1 << i):
			res.append('x^' + str(i))
	return ' + '.join(res)

def aes_128_encrypt(input_bytes, key_bytes):
	assert len(input_bytes) == 16
	state = []
	for row in range(4):
		state.append(bytes([input_bytes[row], input_bytes[row + 4], input_bytes[row + 8], input_bytes[row + 12]]))
	words = [input_bytes[4 * x:4 * x + 4] for x in range(4)]

	out = bytearray(16)
	for i in range(16):
		out[i] = state[i // 4][i % 4]
	return bytes(out)

def main():
	pass

if __name__ == '__main__':
	main()

