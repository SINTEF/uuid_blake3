# uuid_blake3

[![CI](https://github.com/SINTEF/uuid_blake3/workflows/CI/badge.svg)](https://github.com/SINTEF/uuid_blake3/actions)
[![PyPI version](https://badge.fury.io/py/uuid_blake3.svg)](https://badge.fury.io/py/uuid_blake3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Fast, secure deterministic UUIDs using BLAKE3 hashing, with optional structured metadata support.

## Features

- **Fast & Secure**: Uses BLAKE3 instead of SHA-1 or MD5 for better performance and cryptographic security. Or simply because *SHA1* isn't cool any more
- **Deterministic**: Same inputs always produce the same UUID
- **RFC 4122 Compliant**: Generated UUIDs follow the standard format
- **Metadata Support**: Enhanced version supports structured metadata beyond simple namespace+name
- **Type Safe**: Built in Rust with Python bindings for reliability and performance

## Installation

```bash
pip install uuid_blake3
```

## Quick Start

### Basic Usage (like UUID v3/v5)

```python
import uuid_blake3

# Generate deterministic UUIDs from namespace and name
uuid1 = uuid_blake3.uuid("my-namespace", "my-resource")
uuid2 = uuid_blake3.uuid("my-namespace", "my-resource")

assert uuid1 == uuid2  # Always the same for identical inputs
print(uuid1)  # e.g., b6839270-3331-531b-99b5-e67404c687cb
```

### With Metadata

```python
import uuid_blake3

# Enhanced version with key/value metadata
metadata = {
    "version": "1.0",
    "environment": "production",
    "user_id": 12345,
    "production": False,
}

uuid_meta = uuid_blake3.uuid_with_metadata(
    namespace="my-app",
    name="user-session",
    metadata=metadata
)

print(uuid_meta)  # Deterministic UUID incorporating all metadata
```

## Why BLAKE3?

Traditional UUID v3 and v5 use MD5 and SHA-1 respectively, which have known cryptographic weaknesses. BLAKE3 offers:

- **Speed**: Significantly faster than SHA-1/SHA-256
- **Security**: Cryptographically secure with no known vulnerabilities
- **Simplicity**: Clean, modern design
- **Versatility**: Supports keyed hashing and extensible output

## Metadata Handling

The `uuid_with_metadata` function provides deterministic UUID generation with complex structured data:

```python
# All these produce the same UUID (order doesn't matter)
meta1 = {"key1": "value1", "key2": "value2"}
meta2 = {"key2": "value2", "key1": "value1"}

uuid1 = uuid_blake3.uuid_with_metadata("ns", "name", meta1)
uuid2 = uuid_blake3.uuid_with_metadata("ns", "name", meta2)
assert uuid1 == uuid2

# Supports various data types
metadata = {
    "string": "text",
    "number": 42,
    "float": 3.14,
    "boolean": True,
    "bytes": b"binary-data",
    "complex": {"nested": "objects"}  # Serialized via str()
}
```

### Supported Types

- **Strings**: UTF-8 encoded
- **Integers**: Little-endian byte representation
- **Floats**: IEEE 754 little-endian bytes
- **Booleans**: Single byte (0x00/0x01)
- **Bytes**: Direct binary data
- **Complex types**: String representation via `str()`

## API Reference

### `uuid(namespace: str, name: str) -> uuid.UUID`

Generate a deterministic UUID from namespace and name (similar to UUID v3/v5).

**Parameters:**

- `namespace`: Namespace string to scope the UUID
- `name`: Name/identifier within the namespace

**Returns:** A `uuid.UUID` object

### `uuid_with_metadata(namespace: str, name: str, metadata: dict) -> uuid.UUID`

Generate a deterministic UUID incorporating structured metadata.

**Parameters:**

- `namespace`: Namespace string to scope the UUID
- `name`: Name/identifier within the namespace
- `metadata`: Dictionary of metadata to include in hash. Nested structures are serialized to strings, so you may want to serialize to JSON first or stick to simple types.

**Returns:** A `uuid.UUID` object

**Raises:** `TypeError` if metadata is not a dictionary

*The first sixteen bits of the UUID are derived from only the namespace and the name while the remaining bits are derived from everything: namespace, name, and metadata. This means that sharing the same namespace and name will produce UUIDs that are relatively close to each other, which can be convenient if you organize data based on the UUID.*

## Security Considerations

This is **NOT** cryptographically secure. First, a standard UUID is 128 bits long with 122 actual data bits, which is clearly not enough for cryptographic purposes. Second, the library is designed to derive strings and metadata into reproducible IDs but is not designed to be a secure hashing function.

## When to Use

- **Use `uuid()`** for simple namespace+name scenarios (like traditional UUID v3/v5)
- **Use `uuid_with_metadata()`** when you need to incorporate additional context that affects uniqueness
- **Consider JSON serialization** for complex metadata to ensure consistent representation

## Development

This project uses Rust with Python bindings via PyO3 and Maturin.

```bash
# Install Rust toolchain, if you haven't already done it
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install Python dependencies
pip install maturin pytest

# Build and install in development mode
maturin develop

# Run tests
pytest
```

## Licence

MIT Licence - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions welcome! Please open an issue or submit a pull request.
