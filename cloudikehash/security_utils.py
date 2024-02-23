import hashlib


class Hasher:
    """
    A utility class for hashing data with different algorithms.

    Attributes:
        algorithm (callable): The hashing algorithm to use.

    Args:
        use_sha256 (bool): Determines whether to use SHA-256 (True) or MD5 (False) as the default hashing algorithm.
    """

    def __init__(self, use_sha512=True):
        """
        Initializes the hasher with the specified algorithm.
        """
        self.algorithm = hashlib.sha512 if use_sha512 else hashlib.md5

    def get_hash(self, data, force_sha1=False):
        """
        Calculates the hash of the given data.

        Args:
            data (str or bytes): The data to hash.
            force_sha1 (bool): If True, SHA-1 will be used regardless of the default algorithm.

        Returns:
            str: The hexadecimal digest of the hash.
        """
        if force_sha1:
            algorithm = hashlib.sha1
        else:
            algorithm = self.algorithm

        if isinstance(data, str):
            data = data.encode('utf-8')

        hasher = algorithm()
        hasher.update(data)
        return hasher.hexdigest()

    def get_hash_bytes(self, data):
        """
        Calculates the hash of the given data and returns it as bytes.

        Args:
            data (str or bytes): The data to hash.

        Returns:
            bytes: The byte digest of the hash.
        """
        if isinstance(data, str):
            data = data.encode('utf-8')
        hasher = self.algorithm()
        hasher.update(data)
        return hasher.digest()

    def get_hasher(self):
        """
        Returns the current hashing algorithm.

        Returns:
            callable: The current hashing algorithm used by the hasher.
        """
        return self.algorithm
