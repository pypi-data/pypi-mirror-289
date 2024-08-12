![antivirus-microservice](./assets/logo2.png)

## Antivirus Microservice Python Client

This is a Python client for the free and fully functional [Antivirus Microservice Server](https://github.com/ivanoff/Antivirus-Microservice). It allows you to easily integrate virus scanning capabilities into your Python applications.

## Table of Contents

- [Antivirus Microservice Python Client](#antivirus-microservice-python-client)
- [Table of Contents](#table-of-contents)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Configuration](#configuration)
- [Error Handling](#error-handling)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)
- [Created by](#created-by)

## Installation

You can install this package via pip:

```bash
pip install antivirus-microservice
```

## Usage

Here's a basic example of how to use the Antivirus Microservice client:

```python
from antivirus_microservice import AntivirusMicroservice

antivirus = AntivirusMicroservice('http://localhost:3000')
result = antivirus.check_file('/path/to/your/file.txt')

if result['ok']:
    print("File is clean")
else:
    print(f"File is infected: {result['viruses']}")
```

## API

The `AntivirusMicroservice` class provides the following method:

- `check_file(file_path)`: Scans the provided file for viruses. Returns a dictionary with:
  - `ok`: boolean indicating whether the file is clean (`True`) or infected (`False`)
  - `viruses`: a list of detected virus names (only present if `ok` is `False`)

## Configuration

When initializing the `AntivirusMicroservice` class, you can specify the URL of your Antivirus Microservice server. By default, it uses `http://localhost:3000`.

```python
antivirus = AntivirusMicroservice('http://your-custom-url:port')
```

## Error Handling

The client handles basic errors:
- If there's an error communicating with the server, it returns `{'ok': False, 'viruses': ['Error checking file']}`.
- The specific error message is printed to the console.

## Requirements

- Python 3.6 or higher
- requests library

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Support

If you encounter any problems or have questions, please open an issue in the [project repository](https://github.com/ivanoff/antivirus-microservice-python).

## Created by

Dimitry Ivanov <2@ivanoff.org.ua> # curl -A cv ivanoff.org.ua
