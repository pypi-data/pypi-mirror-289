from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend
import getpass

def generate_key_pair() -> tuple[str, str]:
    """
    # func > generate_key_pair

    Generates a public-private key pair for RSA encryption.

    :return: tuple (private_key: str, public_key: str)
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()

    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )

    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem.decode(), public_pem.decode()

def encrypt_with_public_key(public_pem: str, message: str) -> bytes:
    """
    # func > encrypt_with_public_key

    Encrypts a message using the provided public key.

    :param public_pem: str
    :param message: str
    :return: bytes
    """

    public_key = serialization.load_pem_public_key(
        public_pem.encode(),
        backend=default_backend()
    )

    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return ciphertext

def decrypt_with_private_key(ciphertext: bytes) -> str:
    """
    # func > decrypt_with_private_key

    Decrypts a ciphertext using the provided private key input securely.

    :param ciphertext: bytes
    :return: str
    """

    private_pem = getpass.getpass("Enter your private key:\n")

    private_key = serialization.load_pem_private_key(
        private_pem.encode(),
        password=None,
        backend=default_backend()
    )

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return plaintext.decode()