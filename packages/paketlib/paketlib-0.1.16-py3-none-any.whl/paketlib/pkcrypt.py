class pkDesC:
    def __init__(self, key: bytes):
        self.key = int.from_bytes(key, 'big') & 0xFFFFFFFFFFFFFFFF

    def _feistel_round(self, block: int, subkey: int) -> int:
        left = (block >> 32) & 0xFFFFFFFF
        right = block & 0xFFFFFFFF
        left ^= subkey
        return (right << 32) | left

    def _generate_subkeys(self) -> list:
        return [self.key ^ i for i in range(16)]

    def _process_block(self, block: int) -> int:
        subkeys = self._generate_subkeys()
        for subkey in subkeys:
            block = self._feistel_round(block, subkey)
        return block

    def encrypt(self, plaintext: bytes) -> bytes:
        block = int.from_bytes(plaintext, 'big')
        encrypted_block = self._process_block(block)
        return encrypted_block.to_bytes((encrypted_block.bit_length() + 7) // 8, 'big')

    def decrypt(self, ciphertext: bytes) -> bytes:
        block = int.from_bytes(ciphertext, 'big')
        decrypted_block = self._process_block(block)
        return decrypted_block.to_bytes((decrypted_block.bit_length() + 7) // 8, 'big')



    

def xor(data: bytes, key: bytes) -> bytes:
    return bytes(
        d ^ key[i % len(key)]
        for i, d in enumerate(data)
    )

l1l1l1l1ll1l1l1llllll1l1ll1l1l1l1 = b'hdasjkdsajdasjkdsadasdsaadsdasadsadsadsads'[::-1]
ll1l1l1l1l1l1l1l11l11l1l1l1l1l1ll = b'ALSDDLKASHDKAJSDHIUASHDJKAKSDHKASJDHKASJDKASD'[::-1]
l1l1ll1lll1l1l1l1l1l1l1llIl1ll1l1 = b'Khkasda7sdiasyd7asydas8d6a8sd76as8d7ads87dasyuadsy'[::-1]
l1l1l1l1l1ll1lIl1l1ll1l1l1Il1l1l1 = 'oдфыоофыдлвррыапырл3ршгвыалоывралоырвалоывалофывр'[::-1].encode()
l1l1l1l1l1l1l1l1l1l1l1l1l11111111 = b'LAKSDDDDDDDDDDJLKASJDLKASJDLAKSJDLAKSJDLAKSJD'[::-1]
llll1lll1l1l1l1l12l1l1l1l12l1llll = b';laskdpxjoiuwsdifu8wowdifu8wosdifu4wodifu840'[::-1]
IIIIl1l1l1ll1ll1ll1IIIIl1l1l1l1l1 = b';.;.;as.d;as.s;d.as;d.asd;.;ads.;ads..;sa.;dass'