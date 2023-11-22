import unittest
import sys
import os
import random
import string

parent_dir = os.path.abspath(os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")), ".."))
sys.path.append(parent_dir)

from src.lab2.vigenre import encrypt_vigenere, decrypt_vigenere

class TestVigenereEncryptionDecryption(unittest.TestCase):
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(encrypt_vigenere("python", "a"), 'python')
        self.assertEqual(encrypt_vigenere("ATTACKATDAWN", "LEMON"), 'LXFOPVEFRNHR')

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("PYTHON", "A"), 'PYTHON')
        self.assertEqual(decrypt_vigenere("python", "a"), 'python')
        self.assertEqual(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"), 'ATTACKATDAWN')

if __name__ == '__main__':
    unittest.main()


    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))