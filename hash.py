

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size  # Initialize an empty hash table
        self.deleted = object()     # Unique marker for deleted items

    def hash_function(self, key):
        """Hash function that computes an index for a given key."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert a key-value pair into the hash table using linear probing."""
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None and self.table[index] is not self.deleted:
            if self.table[index][0] == key:
                self.table[index] = (key, value)  # Update existing key
                return
            index = (index + 1) % self.size  # Linear probing to next slot
            if index == initial_index:  # Full table, can't insert
                raise Exception("Hash table is full")

        # Insert new key-value pair
        self.table[index] = (key, value)

    def search(self, key):
        """Search for a value by key using linear probing."""
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                return self.table[index][1]  # Return the value associated with the key
            index = (index + 1) % self.size  # Linear probing to next slot
            if index == initial_index:  # Came full circle, key not found
                break

        return None  # Key not found

    def delete(self, key):
        """Delete a key-value pair from the hash table using linear probing."""
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None:
            if self.table[index] is not self.deleted and self.table[index][0] == key:
                self.table[index] = self.deleted  # Mark as deleted
                return True
            index = (index + 1) % self.size  # Linear probing to next slot
            if index == initial_index:  # Came full circle, key not found
                break

        return False  # Key not found


# Example usage
hash_table = HashTable(size=7)  # Small table size for demonstration
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
hash_table.insert("orange", 15)

print("Search for 'apple':", hash_table.search("apple"))  # Output: 10
print("Search for 'banana':", hash_table.search("banana"))  # Output: 20

hash_table.delete("apple")
print("Search for 'apple' after deletion:", hash_table.search("apple"))  # Output: None


def custom_hash_function(input_string):
    # Initialize a large prime number for modular arithmetic
    prime = 31_069_811_923
    # Initialize hash value with a prime seed
    hash_value = 5381

    # Process each character in the input string
    for char in input_string:
        # Bitwise manipulation: XOR with the character's ASCII value, then shift left
        hash_value = (hash_value * 33) ^ ord(char)
        # Keep the hash value within bounds by using modulus with a large prime
        hash_value %= prime

    # Return the resulting hash as a fixed-length integer
    return hash_value


# https://realpython.com/python-data-structures/

def hash_function(key):
     return sum(
        index * ord(character)
        for index, character in enumerate(repr(key), start=1)
     )

def hash_function(key):
    prime_multiplier = 33
    return sum(
        prime_multiplier ** index * ord(character)
        for index, character in enumerate(repr(key))
    )


custom_hash_function("Tiny") % 5
custom_hash_function('iTny') % 5



