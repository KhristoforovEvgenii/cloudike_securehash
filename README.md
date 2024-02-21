
# Cloudikehash Library

Cloudikehash is a Python library that provides a simple interface for hashing data with various algorithms, including SHA-256, MD5, and SHA-1. It is designed to make it easy for developers to work with different hashing algorithms for their projects.

## Features

- Easy to use interface for hashing data.
- Support for SHA-256, MD5, and SHA-1 hashing algorithms.
- Methods for generating hex and byte format hashes.
- Customizable hashing algorithm preference.

## Installation

You can install Cloudikehash using pip:

```bash
pip install git+https://github.com/KhristoforovEvgenii/cloudikehash.git
```

## Usage

Here's a quick example of how to use Hasher:

```python
from hasher import Hasher

# Initialize the hasher with SHA-256
hasher = Hasher(use_sha256=True)

# Hash some data
data = "Hello, world!"
hash_hex = hasher.get_hash(data)
print(f"Hexadecimal Hash: {hash_hex}")

# Hash some data and get bytes
hash_bytes = hasher.get_hash_bytes(data)
print(f"Bytes Hash: {hash_bytes}")

# Force SHA-1 hashing
hash_sha1 = hasher.get_hash(data, force_sha1=True)
print(f"SHA-1 Hash: {hash_sha1}")
```
