import copy, argparse

mx = b'\x01\x1b'
c = b'\x63'
sbox = {b'\x98': b'F', b'\xbc': b'e', b'&': b'\xf7', b'\xed': b'U', b'\xca': b't', b'\x0b': b'+', b'w': b'\xf5', b'\xfd': b'T', b'\xa5': b'\x06', b'U': b'\xfc', b'9': b'\x12', b'\xc9': b'\xdd', b'\x14': b'\xfa', b'J': b'\xd6', b'\x89': b'\xa7', b'l': b'P', b'\x04': b'\xf2', b'\xcd': b'\xbd', b'\x81': b'\x0c', b'\r': b'\xd7', b'\xc8': b'\xe8', b'n': b'\x9f', b'\xc3': b'.', b' ': b'\xb7', b'A': b'\x83', b'\x94': b'"', b'\xfe': b'\xbb', b's': b'\x8f', b'\xf6': b'B', b'-': b'\xd8', b'\xd9': b'5', b'\x9f': b'\xdb', b'D': b'\x1b', b'\x05': b'k', b'\x0f': b'v', b'}': b'\xff', b'%': b'?', b'\xde': b'\x1d', b'[': b'9', b'\xe3': b'\x11', b'\x92': b'O', b'\xd0': b'p', b'\x16': b'G', b'\x13': b'}', b'\xa7': b'\\', b'\x1c': b'\x9c', b'Y': b'\xcb', b'\x97': b'\x88', b'\x88': b'\xc4', b'#': b'&', b'_': b'\xcf', b'2': b'#', b'F': b'Z', b'\x8a': b'~', b'\xdb': b'\xb9', b'\xae': b'\xe4', b'\x8b': b'=', b',': b'q', b'o': b'\xa8', b'\x02': b'w', b'\x9b': b'\x14', b'*': b'\xe5', b'\xcb': b'\x1f', b'\xcc': b'K', b'\xf9': b'\x99', b'\xd8': b'a', b'\x03': b'{', b'\x07': b'\xc5', b'\xb8': b'l', b'\x10': b'\xca', b'\xb5': b'\xd5', b'\xba': b'\xf4', b'\xb9': b'V', b'6': b'\x05', b'\xd3': b'f', b'S': b'\xed', b'\xb2': b'7', b'\xe6': b'\x8e', b'\xea': b'\x87', b'm': b'<', b'\xb7': b'\xa9', b'd': b'C', b'\xa2': b':', b'\xaa': b'\xac', b'\x1f': b'\xc0', b'\xa0': b'\xe0', b'\x00': b'c', b'5': b'\x96', b'a': b'\xef', b'\xe0': b'\xe1', b'\x96': b'\x90', b'\xfa': b'-', b'\n': b'g', b'\xfb': b'\x0f', b'\x83': b'\xec', b'\x1a': b'\xa2', b'!': b'\xfd', b'\x1d': b'\xa4', b'\xd5': b'\x03', b'R': b'\x00', b'^': b'X', b'\x87': b'\x17', b'\xa6': b'$', b'\t': b'\x01', b'\xf8': b'A', b'\xe9': b'\x1e', b'.': b'1', b'i': b'\xf9', b';': b'\xe2', b'\xa9': b'\xd3', b'\xd7': b'\x0e', b'\xc2': b'%', b'\xaf': b'y', b'\xf5': b'\xe6', b'\x12': b'\xc9', b'\xc5': b'\xa6', b'x': b'\xbc', b'\xd6': b'\xf6', b'\xef': b'\xdf', b'r': b'@', b'\xe2': b'\x98', b'P': b'S', b'\x19': b'\xd4', b'G': b'\xa0', b'V': b'\xb1', b'C': b'\x1a', b'\xdc': b'\x86', b'\x93': b'\xdc', b'\x8e': b'\x19', b'`': b'\xd0', b'z': b'\xda', b'\xe1': b'\xf8', b'|': b'\x10', b'\x86': b'D', b'\xa3': b'\n', b'E': b'n', b'f': b'3', b'<': b'\xeb', b'\xbb': b'\xea', b'K': b'\xb3', b'h': b'E', b'{': b'!', b'+': b'\xf1', b'\xe8': b'\x9b', b'y': b'\xb6', b'\xeb': b'\xe9', b'I': b';', b'\xf3': b'\r', b'1': b'\xc7', b'\xd2': b'\xb5', b'\xab': b'b', b'\xda': b'W', b'\x8c': b'd', b'\xd1': b'>', b')': b'\xa5', b'\x0e': b'\xab', b'\xbd': b'z', b'\x1e': b'r', b'v': b'8', b'\x18': b'\xad', b'\xcf': b'\x8a', b'p': b'Q', b'\xf0': b'\x8c', b'c': b'\xfb', b'\xb6': b'N', b'\xce': b'\x8b', b'M': b'\xe3', b'?': b'u', b'@': b'\t', b'\xdd': b'\xc1', b'"': b'\x93', b'\x85': b'\x97', b'\xbf': b'\x08', b'8': b'\x07', b'\x8f': b's', b'\x9a': b'\xb8', b'\xec': b'\xce', b'O': b'\x84', b'\x1b': b'\xaf', b'\xd4': b'H', b'>': b'\xb2', b'=': b"'", b'\xad': b'\x95', b'g': b'\x85', b'\xb0': b'\xe7', b'B': b',', b'\xf1': b'\xa1', b'\x08': b'0', b'\x9c': b'\xde', b'\xc4': b'\x1c', b'3': b'\xc3', b'q': b'\xa3', b'\xc1': b'x', b'\xfc': b'\xb0', b"'": b'\xcc', b'u': b'\x9d', b'4': b'\x18', b'\xb3': b'm', b'\x82': b'\x13', b'T': b' ', b'b': b'\xaa', b'7': b'\x9a', b't': b'\x92', b'\x91': b'\x81', b'Z': b'\xbe', b'W': b'[', b'\xa1': b'2', b'\xc0': b'\xba', b'L': b')', b'k': b'\x7f', b'e': b'M', b'\x84': b'_', b'\xe7': b'\x94', b'Q': b'\xd1', b'\xc6': b'\xb4', b'\x90': b'`', b'j': b'\x02', b'\xb4': b'\x8d', b'X': b'j', b'\xff': b'\x16', b'0': b'\x04', b'\xdf': b'\x9e', b'\xa4': b'I', b'\xee': b'(', b'N': b'/', b'(': b'4', b'\xac': b'\x91', b':': b'\x80', b'\xf7': b'h', b'\x15': b'Y', b'\x9d': b'^', b'\x95': b'*', b'/': b'\x15', b'\xbe': b'\xae', b']': b'L', b'\xa8': b'\xc2', b'\xb1': b'\xc8', b'\x06': b'o', b'\xf4': b'\xbf', b'\x99': b'\xee', b'\x9e': b'\x0b', b'\x8d': b']', b'\x7f': b'\xd2', b'H': b'R', b'\xe5': b'\xd9', b'~': b'\xf3', b'\xf2': b'\x89', b'\x01': b'|', b'\x11': b'\x82', b'\xc7': b'\xc6', b'\x17': b'\xf0', b'\\': b'J', b'\x80': b'\xcd', b'$': b'6', b'\x0c': b'\xfe', b'\xe4': b'i'}
inv_sbox = {b'\x00': b'R', b'\x01': b'\t', b'\x02': b'j', b'\x03': b'\xd5', b'\x04': b'0', b'\x05': b'6', b'\x06': b'\xa5', b'\x07': b'8', b'\x08': b'\xbf', b'\t': b'@', b'\n': b'\xa3', b'\x0b': b'\x9e', b'\x0c': b'\x81', b'\r': b'\xf3', b'\x0e': b'\xd7', b'\x0f': b'\xfb', b'\x10': b'|', b'\x11': b'\xe3', b'\x12': b'9', b'\x13': b'\x82', b'\x14': b'\x9b', b'\x15': b'/', b'\x16': b'\xff', b'\x17': b'\x87', b'\x18': b'4', b'\x19': b'\x8e', b'\x1a': b'C', b'\x1b': b'D', b'\x1c': b'\xc4', b'\x1d': b'\xde', b'\x1e': b'\xe9', b'\x1f': b'\xcb', b' ': b'T', b'!': b'{', b'"': b'\x94', b'#': b'2', b'$': b'\xa6', b'%': b'\xc2', b'&': b'#', b"'": b'=', b'(': b'\xee', b')': b'L', b'*': b'\x95', b'+': b'\x0b', b',': b'B', b'-': b'\xfa', b'.': b'\xc3', b'/': b'N', b'0': b'\x08', b'1': b'.', b'2': b'\xa1', b'3': b'f', b'4': b'(', b'5': b'\xd9', b'6': b'$', b'7': b'\xb2', b'8': b'v', b'9': b'[', b':': b'\xa2', b';': b'I', b'<': b'm', b'=': b'\x8b', b'>': b'\xd1', b'?': b'%', b'@': b'r', b'A': b'\xf8', b'B': b'\xf6', b'C': b'd', b'D': b'\x86', b'E': b'h', b'F': b'\x98', b'G': b'\x16', b'H': b'\xd4', b'I': b'\xa4', b'J': b'\\', b'K': b'\xcc', b'L': b']', b'M': b'e', b'N': b'\xb6', b'O': b'\x92', b'P': b'l', b'Q': b'p', b'R': b'H', b'S': b'P', b'T': b'\xfd', b'U': b'\xed', b'V': b'\xb9', b'W': b'\xda', b'X': b'^', b'Y': b'\x15', b'Z': b'F', b'[': b'W', b'\\': b'\xa7', b']': b'\x8d', b'^': b'\x9d', b'_': b'\x84', b'`': b'\x90', b'a': b'\xd8', b'b': b'\xab', b'c': b'\x00', b'd': b'\x8c', b'e': b'\xbc', b'f': b'\xd3', b'g': b'\n', b'h': b'\xf7', b'i': b'\xe4', b'j': b'X', b'k': b'\x05', b'l': b'\xb8', b'm': b'\xb3', b'n': b'E', b'o': b'\x06', b'p': b'\xd0', b'q': b',', b'r': b'\x1e', b's': b'\x8f', b't': b'\xca', b'u': b'?', b'v': b'\x0f', b'w': b'\x02', b'x': b'\xc1', b'y': b'\xaf', b'z': b'\xbd', b'{': b'\x03', b'|': b'\x01', b'}': b'\x13', b'~': b'\x8a', b'\x7f': b'k', b'\x80': b':', b'\x81': b'\x91', b'\x82': b'\x11', b'\x83': b'A', b'\x84': b'O', b'\x85': b'g', b'\x86': b'\xdc', b'\x87': b'\xea', b'\x88': b'\x97', b'\x89': b'\xf2', b'\x8a': b'\xcf', b'\x8b': b'\xce', b'\x8c': b'\xf0', b'\x8d': b'\xb4', b'\x8e': b'\xe6', b'\x8f': b's', b'\x90': b'\x96', b'\x91': b'\xac', b'\x92': b't', b'\x93': b'"', b'\x94': b'\xe7', b'\x95': b'\xad', b'\x96': b'5', b'\x97': b'\x85', b'\x98': b'\xe2', b'\x99': b'\xf9', b'\x9a': b'7', b'\x9b': b'\xe8', b'\x9c': b'\x1c', b'\x9d': b'u', b'\x9e': b'\xdf', b'\x9f': b'n', b'\xa0': b'G', b'\xa1': b'\xf1', b'\xa2': b'\x1a', b'\xa3': b'q', b'\xa4': b'\x1d', b'\xa5': b')', b'\xa6': b'\xc5', b'\xa7': b'\x89', b'\xa8': b'o', b'\xa9': b'\xb7', b'\xaa': b'b', b'\xab': b'\x0e', b'\xac': b'\xaa', b'\xad': b'\x18', b'\xae': b'\xbe', b'\xaf': b'\x1b', b'\xb0': b'\xfc', b'\xb1': b'V', b'\xb2': b'>', b'\xb3': b'K', b'\xb4': b'\xc6', b'\xb5': b'\xd2', b'\xb6': b'y', b'\xb7': b' ', b'\xb8': b'\x9a', b'\xb9': b'\xdb', b'\xba': b'\xc0', b'\xbb': b'\xfe', b'\xbc': b'x', b'\xbd': b'\xcd', b'\xbe': b'Z', b'\xbf': b'\xf4', b'\xc0': b'\x1f', b'\xc1': b'\xdd', b'\xc2': b'\xa8', b'\xc3': b'3', b'\xc4': b'\x88', b'\xc5': b'\x07', b'\xc6': b'\xc7', b'\xc7': b'1', b'\xc8': b'\xb1', b'\xc9': b'\x12', b'\xca': b'\x10', b'\xcb': b'Y', b'\xcc': b"'", b'\xcd': b'\x80', b'\xce': b'\xec', b'\xcf': b'_', b'\xd0': b'`', b'\xd1': b'Q', b'\xd2': b'\x7f', b'\xd3': b'\xa9', b'\xd4': b'\x19', b'\xd5': b'\xb5', b'\xd6': b'J', b'\xd7': b'\r', b'\xd8': b'-', b'\xd9': b'\xe5', b'\xda': b'z', b'\xdb': b'\x9f', b'\xdc': b'\x93', b'\xdd': b'\xc9', b'\xde': b'\x9c', b'\xdf': b'\xef', b'\xe0': b'\xa0', b'\xe1': b'\xe0', b'\xe2': b';', b'\xe3': b'M', b'\xe4': b'\xae', b'\xe5': b'*', b'\xe6': b'\xf5', b'\xe7': b'\xb0', b'\xe8': b'\xc8', b'\xe9': b'\xeb', b'\xea': b'\xbb', b'\xeb': b'<', b'\xec': b'\x83', b'\xed': b'S', b'\xee': b'\x99', b'\xef': b'a', b'\xf0': b'\x17', b'\xf1': b'+', b'\xf2': b'\x04', b'\xf3': b'~', b'\xf4': b'\xba', b'\xf5': b'w', b'\xf6': b'\xd6', b'\xf7': b'&', b'\xf8': b'\xe1', b'\xf9': b'i', b'\xfa': b'\x14', b'\xfb': b'c', b'\xfc': b'U', b'\xfd': b'!', b'\xfe': b'\x0c', b'\xff': b'}'}
Nb = 4

def bytes_to_hex(arg):
	''' Turn a python bytes object into a hex-formatted string. 
		bytes_to_hex(b'asdf') -> "0x61736466" '''
	pieces = [('0' + hex(b)[2:])[-2:] for b in arg]
	return ''.join(pieces)

def rot_word(word):
	res = word.copy()
	x = res[0]
	res.append(x)
	res.remove(x)
	return res

def ff_add(x, y):
	#print('got x as:', x, 'and y as:', y)
	xi = int.from_bytes(x, 'big')
	yi = int.from_bytes(y, 'big')
	res = xi ^ yi
	return res.to_bytes(max((res.bit_length() + 7) // 8, 1), 'big')

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

def state_repr(state):
	res = [''.join([('00' + hex(b[0])[2:])[-2:] for b in r]) for r in state]
	return '\n'.join(res)

def word_repr(word):
	return ''.join(('00' + hex(b[0])[2:])[-2:] for b in word)

def m_inv(x):
	if x == b'\x00':
		return x
	for i in range(1, 256):
		b = i.to_bytes(1, 'big')
		if ff_dot(x, b) == b'\x01':
			return b

def sub_word(word):
	res = word.copy()
	for i, ff in enumerate(word):
		res[i] = sbox[ff]
	return res

def inv_sub_word(word):
	res = word.copy()
	for i, ff in enumerate(word):
		res[i] = inv_sbox[ff]
	return res

# XOR two 4-byte words
def word_xor(w1, w2):
	assert len(w1) == len(w2) == 4
	res = [ff_add(w1[i], w2[i]) for i in range(4)]
	return res

def rcon(i):
	xi = b'\x01'
	for _ in range(i - 1):
		xi = xtime(xi)
	return [xi, b'\x00', b'\x00', b'\x00']

def key_expand(key, Nk, Nr):
	w = [[b'\x00', b'\x00', b'\x00', b'\x00'] for _ in range(Nb * (Nr + 1))]
	temp = [b'\x00', b'\x00', b'\x00', b'\x00']
	
	for i in range(Nk):
		w[i] = key[i].copy()
	
	for i in range(Nk, Nb * (Nr + 1)):
		#print('when i =', i)
		temp = w[i - 1]
		#print('temp =', word_repr(temp))
		if i % Nk == 0:
			#temp = word_xor(sub_word(rot_word(temp)), rcon(i // Nk))
			temp = rot_word(temp)
			#print('after rot_word:', word_repr(temp))
			temp = sub_word(temp)
			#print('after sub_word:', word_repr(temp))
			#print('rcon[i/Nk]:', rcon(i // Nk))
			temp = word_xor(temp, rcon(i // Nk))
			#print('after XOR with Rcon:', word_repr(temp))
		elif Nk > 6 and i % Nk == 4:
			temp = sub_word(temp)
		#print('w[i-Nk]', word_repr(w[i - Nk]))
		w[i] = word_xor(w[i - Nk], temp)
		#print('w[i]=temp XOR w[i-Nk]', word_repr(w[i]))
	
	return w

def add_round_key(state, words, rnd):
	#print('words is:', words)
	state_copy = state.copy()
	iwords = words[4 * rnd : 4 * rnd + 4]
	#print('round key val is:\n' + state_repr(iwords))
	for r in range(4):
		for c in range(4):
			state_copy[r][c] = ff_add(iwords[c][r], state[r][c])
	return state_copy

def aes_128_encrypt(input_bytes, key_bytes, Nk, Nr):
	assert len(input_bytes) == 16
	assert len(key_bytes) == Nk * 4
	assert Nk in {4, 8}
	assert Nr in {10, 14}
	
	#print('enciphering:', bytes_to_hex(input_bytes))
	if Nk == 4:
		key_words = [key_bytes[0:4], key_bytes[4:8], key_bytes[8:12], key_bytes[12:16]]
	else:
		key_words = [key_bytes[0:4], key_bytes[4:8], key_bytes[8:12], key_bytes[12:16], key_bytes[16:20], key_bytes[20:24], key_bytes[24:28], key_bytes[28:32]]
	
	key = [[word[0].to_bytes(1, 'big'), word[1].to_bytes(1, 'big'), word[2].to_bytes(1, 'big'), word[3].to_bytes(1, 'big')] for word in key_words]
	#print('got key:', key)
	ks = key_expand(key, Nk, Nr)
	#print('key schedule is:', ks)

	# Load input bytes into 4 X 4 state array
	state = []
	for row in range(4):
		state.append([input_bytes[row].to_bytes(1, 'big'), input_bytes[row + 4].to_bytes(1, 'big'), input_bytes[row + 8].to_bytes(1, 'big'), input_bytes[row + 12].to_bytes(1, 'big')])
	#print('got start state:\n' + state_repr(state))
	
	state = add_round_key(state, ks, 0)
	#print('after first add_round_key, state is:\n' + state_repr(state))
	
	for rnd in range(1, Nr):
		#print('~~~~~~~~~~~~~\nRound:', rnd)
		#print('start of round:\n' + state_repr(state))
		# SubBytes step
		for r, row in enumerate(state):
			state[r] = sub_word(row)
		
		#print('after SubBytes:\n' + state_repr(state))

		# ShiftRows step
		state_copy = state.copy()
		for r in range(4):
			row = state[r]
			for _ in range(r):
				row = rot_word(row)
			state_copy[r] = row
		state = state_copy
		
		#print('after ShiftRows:\n' + state_repr(state))

		# MixColumns step
		state_copy = copy.deepcopy(state)
		for c, ff in enumerate(state[0]):
			state_copy[0][c] = ff_add(ff_add(ff_add(ff_dot(b'\x02', state[0][c]), ff_dot(b'\x03', state[1][c])), state[2][c]), state[3][c])
		for c, ff in enumerate(state[1]):
			state_copy[1][c] = ff_add(ff_add(ff_add(state[0][c], ff_dot(b'\x02', state[1][c])), ff_dot(b'\x03', state[2][c])), state[3][c])
		for c, ff in enumerate(state[2]):
			state_copy[2][c] = ff_add(ff_add(ff_add(state[0][c], state[1][c]), ff_dot(b'\x02', state[2][c])), ff_dot(b'\x03', state[3][c]))
		for c, ff in enumerate(state[3]):
			state_copy[3][c] = ff_add(ff_add(ff_add(ff_dot(b'\x03', state[0][c]), state[1][c]), state[2][c]), ff_dot(b'\x02', state[3][c]))

		#print('got state copy[0] as:\n' + word_repr(state_copy[0]))
		state = state_copy
		#print('after MixColumns:\n' + state_repr(state))

		# AddRoundKey step
		state = add_round_key(state, ks, rnd)
		#print('state after add_round_key is:\n' + state_repr(state))

	# SubBytes one more time...
	for r, row in enumerate(state):
		state[r] = sub_word(row)
		
	#print('after last sub_bytes:\n' + state_repr(state))

	# ShiftRows one more time...
	state_copy = state.copy()
	for r in range(4):
		row = state[r]
		for _ in range(r):
			row = rot_word(row)
		state_copy[r] = row
	state = state_copy
			
	#print('after last shiftrows:\n' + state_repr(state))

	# AddRoundKey one more time...
	state = add_round_key(state, ks, Nr)
	
	#print('final state is:\n' + state_repr(state))

	out = bytearray(16)
	for r in range(4):
		for c in range(4):
			out[4 * c + r] = state[r][c][0]
	#print('enciphered:', bytes_to_hex(out))
	return bytes(out)

def inv_cipher(input_bytes, key_bytes, Nk, Nr):
	#print('deciphering:', bytes_to_hex(input_bytes))
	state = []
	for row in range(4):
		state.append([input_bytes[row].to_bytes(1, 'big'), input_bytes[row + 4].to_bytes(1, 'big'), input_bytes[row + 8].to_bytes(1, 'big'), input_bytes[row + 12].to_bytes(1, 'big')])
	
	if Nk == 4:
		key_words = [key_bytes[0:4], key_bytes[4:8], key_bytes[8:12], key_bytes[12:16]]
	else:
		key_words = [key_bytes[0:4], key_bytes[4:8], key_bytes[8:12], key_bytes[12:16], key_bytes[16:20], key_bytes[20:24], key_bytes[24:28], key_bytes[28:32]]
	
	key = [[word[0].to_bytes(1, 'big'), word[1].to_bytes(1, 'big'), word[2].to_bytes(1, 'big'), word[3].to_bytes(1, 'big')] for word in key_words]
	#print('got key:', key)
	ks = key_expand(key, Nk, Nr)
	
	state = add_round_key(state, ks, Nr)
	
	for rnd in range(Nr - 1, 0, -1):
		# InvShiftRows step
		state_copy = state.copy()
		for r in range(4):
			row = state[r]
			for _ in range(4 - r):
				row = rot_word(row)
			state_copy[r] = row
		state = state_copy
		
		# InvSubBytes step
		for r, row in enumerate(state):
			state[r] = inv_sub_word(row)
		
		# AddRoundKey step
		state = add_round_key(state, ks, rnd)
		#print('state after add_round_key is:\n' + state_repr(state))
		
		# InvMixColumns step
		state_copy = copy.deepcopy(state)
		for c, ff in enumerate(state[0]):
			state_copy[0][c] = ff_add(ff_add(ff_add(ff_dot(b'\x0e', state[0][c]), ff_dot(b'\x0b', state[1][c])), ff_dot(b'\x0d', state[2][c])), ff_dot(b'\x09', state[3][c]))
		for c, ff in enumerate(state[1]):
			state_copy[1][c] = ff_add(ff_add(ff_add(ff_dot(b'\x09', state[0][c]), ff_dot(b'\x0e', state[1][c])), ff_dot(b'\x0b', state[2][c])), ff_dot(b'\x0d', state[3][c]))
		for c, ff in enumerate(state[2]):
			state_copy[2][c] = ff_add(ff_add(ff_add(ff_dot(b'\x0d', state[0][c]), ff_dot(b'\x09', state[1][c])), ff_dot(b'\x0e', state[2][c])), ff_dot(b'\x0b', state[3][c]))
		for c, ff in enumerate(state[3]):
			state_copy[3][c] = ff_add(ff_add(ff_add(ff_dot(b'\x0b', state[0][c]), ff_dot(b'\x0d', state[1][c])), ff_dot(b'\x09', state[2][c])), ff_dot(b'\x0e', state[3][c]))
		
		state = state_copy
	
	# InvShiftRows one more time
	state_copy = state.copy()
	for r in range(4):
		row = state[r]
		for _ in range(4 - r):
			row = rot_word(row)
		state_copy[r] = row
	state = state_copy
	
	# InvSubBytes one more time
	for r, row in enumerate(state):
		state[r] = inv_sub_word(row)
	
	# AddRoundKey one more time
	state = add_round_key(state, ks, 0)
	#print('Final state is:\n' + state_repr(state))
	
	out = bytearray(16)
	for r in range(4):
		for c in range(4):
			out[4 * c + r] = state[r][c][0]
	#print('deciphered:', bytes_to_hex(out))
	return bytes(out)

def main():
	parser = argparse.ArgumentParser(description='AES')
	parser.add_argument('keysize', type=int, help='4 or 8 words')
	parser.add_argument('keyfile', type=str)
	parser.add_argument('inputfile', type=str)
	parser.add_argument('outputfile', type=str)
	parser.add_argument('mode', type=str)
	
	args = parser.parse_args()
	
	with open(args.keyfile, 'rb') as f:
		key = f.read()
	with open(args.inputfile, 'rb') as f:
		input_bytes = f.read()
	mode = args.mode == 'encrypt'
	
	Nk = args.keysize
	Nr = {4: 10, 8: 14}[Nk]
	
	#print('input bytes:', input_bytes)
	#print('len(input_bytes) is:', len(input_bytes), ', len // 16:', len(input_bytes) // 16)
	input_chunks = [input_bytes[16 * x:16 * x + 16] for x in range(len(input_bytes) // 16 + 1)]
	#print('input_chunks:', input_chunks)
	if mode:
		last_chunk = input_chunks[-1]
		l = len(last_chunk)
		#print('lenght of last chunk is:', l)
		if l == 16:
			input_chunks.append(b'\x10' * 16)
		else:
			num_pad_bytes = 16 - l
			input_chunks[-1] = last_chunk + num_pad_bytes.to_bytes(1, 'big') * num_pad_bytes
			#print('padded w/', num_pad_bytes.to_bytes(1, 'big') * num_pad_bytes)
	else:
		input_chunks = input_chunks[:-1]
	res = bytearray()
	if mode:
		pct = 0
		for i, chunk in enumerate(input_chunks):
			print('\r' + str(pct) + '%', end='')
			res += aes_128_encrypt(chunk, key, Nk, Nr)
			pct = 100 * i // len(input_chunks)
	else:
		pct = 0
		for i, chunk in enumerate(input_chunks):
			print('\r' + str(pct) + '%', end='')
			res += inv_cipher(chunk, key, Nk, Nr)
			pct = 100 * i // len(input_chunks)
	
	print()
	
	if not mode:
		pad_bytes = res[-1]
		res = res[:-pad_bytes]
	
	with open(args.outputfile, 'wb') as f:
		f.write(res)

if __name__ == '__main__':
	main()

