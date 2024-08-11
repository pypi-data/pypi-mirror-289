# My Rust Installer

This package installs Rust and the `agg` tool from asciinema during its own installation process.

## Installation

You can install this package using pip:

```
pip install my_rust_installer
```

This will automatically:
1. Install Rust using rustup
2. Set up the Rust environment
3. Install the `agg` tool from asciinema

## Requirements

- Python 3.6+
- curl
- Internet connection

## Note

This package requires sudo privileges to install Rust and cargo. It will make changes to your system during the installation process.

## License

This project is licensed under the MIT License.