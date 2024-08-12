![antivirus-microservice](./assets/logo2.png)

# Antivirus Microservice Python Client

This is a python client for the free and fully functional [Antivirus Microservice Server](https://github.com/ivanoff/Antivirus-Microservice). It allows you to easily integrate virus scanning capabilities into your PHP applications.

## Installation

...

## Usage

Here's a basic example of how to use the Antivirus Microservice client:

```python
if __name__ == "__main__":
    antivirus = AntivirusMicroservice()
    result = antivirus.check_file('path/to/your/file.txt')
    if result['ok']:
        print("File is clean")
    else:
        print(f"File is infected: {result['viruses']}")
```

## Error Handling

The client handles basic errors:
- If the file is not found, it returns `['ok' => false, 'viruses' => ['File not found']]`.
- If there's an error communicating with the server, it returns `['ok' => false, 'viruses' => ['Error checking file']]`.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Support

If you encounter any problems or have questions, please open an issue in the [project repository](https://github.com/ivanoff/antivirus-microservice-python).

## Created by

Dimitry Ivanov <2@ivanoff.org.ua> # curl -A cv ivanoff.org.ua
