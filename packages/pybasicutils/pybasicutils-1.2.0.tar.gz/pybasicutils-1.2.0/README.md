
# pybasicutils V 1.0.1

Pybasicutils focuses adding functions that are used generally in development. This allows programmers to stop writing lines that they use in many places and allows them to just use a simple function

## Changelog

- Added many more features

- Added usage sections

- Fixed grammar in README.md

- Changed the long description on [PyPi](https://pypi.org/project/pybasicutils/) incl.
setup.py for the same.

## Usage

> Clear Screen

- Directly call function

```python
import pybasicutils as pbu

pbu.clearScreen()
```

- Use alias function

```python
import pybasicutils as pbu

pbu.clsScreen()
```

> Maths

- Add numbers

```python
import pybasicutils as pbu

z = pbu.add(1, 1)
print(z)
```

- Subtracting numbers

```python
import pybasicutils as pbu

z = pbu.sub(1, 1)
print(z)
```

- Multiplying numbers

```python
import pybasicutils as pbu

z = pbu.mul(1, 1)
print(z)
```

- Divide numbers

```python
import pybasicutils as pbu

z = pbu.div(1, 1)
print(z)
```

- Area of square

```python
import pybasicutils as pbu

z = pbu.area.square(5)
print(z)
```

- Area of Rectangle

```python
import pybasicutils as pbu

z = pbu.area.rect(5, 5)
print(z)
```

- Area of Circle

```python
import pybasicutils as pbu

z = pbu.area.circ(5)
print(z)
```

- **NEW** Area of Triangle 

```python
import pybasicutils as pbu

z = pbu.area.tri(5, 5, 5)
print(z)
```

> **NEW SECTION** Jsoned

- **NEW** Read Data

```python
import pybasicutils as pbu

print(pbu.read_json("path/to/file.json"))
```

- **NEW** Write Data

```python
import pybasicutils as pbu

data = {"Data": True}
pbu.write_json("path/to/file.json", data) # Indentation option also available. Indent is 4 by default.
```

> **NEW SECTION**File Size

- **NEW** In MB

```python
import pybasicutils as pbu

print(pbu.fileSizeMB("path/to/file.txt"))
```

- **NEW** In GB

```python
import pybasicutils as pbu

print(pbu.fileSizeGB("path/to/file.txt"))
```

> **NEW SECTION** Encryption and Decryption(RSA)

- **NEW** Generate Key Pairs

```python
import pybasicutils as pbu

private_pem, public_pem = pbu.generate_key_pair()
print("Private Key:\n", private_pem)
print("Public Key:\n", public_pem)
```

- **NEW** Encryption with Public Key

```python
import pybasicutils as pbu

message = "Hello, World!"
public_pem = """-----BEGIN PUBLIC KEY-----
... (public key content here) ...
-----END PUBLIC KEY-----"""

encrypted_message = pbu.encrypt_with_public_key(public_pem, message)
print("Encrypted message:", encrypted_message)
```

- **NEW** Decryption with Private Key

```python
import pybasicutils as pbu

# Generate key pairs
private_pem, public_pem = pbu.generate_key_pair()
print("Private Key:\n", private_pem)
print("Public Key:\n", public_pem)

# Encrypt a message using the public key
message = "Hello, World!"
encrypted_message = pbu.encrypt_with_public_key(public_pem, message)
print("Encrypted message:", encrypted_message)

# Decrypt the encrypted message using the private key
# Note: In an actual implementation, the private key should be securely input.
decrypted_message = pbu.decrypt_with_private_key(encrypted_message)
print("Decrypted message:", decrypted_message)
```

## 🚀 About Me

**ORC ID: 0009-0009-4487-4686**

Hi, I'm ItzSCodez1467 A.K.A. Srijal Dutta. I consider myself an intermediate programmer. In usually work with python for backend and for the frontend which I rarely add to my projects I have made quite a few projects, but I don't want to really share them as they are not really that important. I'll keep adding some projects over time.


## License

[pybasicutils](https://github.com/ItzSCodez1467/pybasicutils) © 2024 by [Srijal Dutta](https://github.com/ItzSCodez1467) is licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/?ref=chooser-v1).

The license file is also available with the project.