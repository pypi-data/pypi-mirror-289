# pgtestkit

pgtestkit is a lightweight and easy-to-use PostgreSQL testing framework for Python, inspired by pytest.

## Features

- Seamless integration with PostgreSQL databases.
- Customizable fixtures for setting up and tearing down database environments.
- Detailed assertions specific to PostgreSQL.

## Installation

Install pgtestkit via pip:

```bash
pip install pgtestkit
```

## Usage

Here's a simple example of how to use pgtestkit:

```python
import pgtestkit

def test_user_table(pg_connection):
    pg_connection.assert_table_exists('users')
```

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

## License

pgtestkit is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Links

- Documentation:
- Source Code: https://github.com/danimarin24/pgtestkit
- Issues: https://github.com/danimarin24/pgtestkit/issues
