# Zenif

Zenif (pronounced "Zenith") is a powerful and versatile Python module designed to enhance the efficiency and performance of your programs. Whether you're a seasoned developer or just starting out, Zenif offers a suite of tools to streamline your workflow and improve code management. Zenif currently enables developers with a simple yet highly customizable logger with support for multiple streams, a set of utility decorators, like `@cache` and `@rate_limiter`, a handful of tools to create a command-line interface with interactive prompts and argument handling, and easy-to-use schemas to validate your user's inputs.

- [Zenif](#zenif)
  - [Installation](#installation)
  - [Documentation](#documentation)
    - [Modules](#modules)
    - [Other](#other)
  - [Contributing](#contributing)
  - [Testing](#testing)
  - [Versioning](#versioning)
  - [License](#license)
  - [Support](#support)

## Installation

Zenif requires Python 3.12 or higher. To install the latest version, install with `pip` or your favorite PyPi package manager.

```sh
pip install zenif
```

This command will download and install Zenif along with its dependencies.

## Documentation

### Modules

- [CLI](https://github.com/DomBom16/zenif/blob/main/docs/modules/cli.md): Create command line interfaces and interactive prompts
- [Log](https://github.com/DomBom16/zenif/blob/main/docs/modules/log.md): Enhance your debugging game with a highly customizable logger
- [Decorators](https://github.com/DomBom16/zenif/blob/main/docs/modules/decorators.md): Give your functions extra functionality on the fly
- [Schema](https://github.com/DomBom16/zenif/blob/main/docs/modules/schema.md): Validate your user's inputs with intuitive syntax

### Other

- [Changelog](https://github.com/DomBom16/zenif/blob/main/docs/changelog.md): View new features, breaking changes, and more between updates

## Contributing

Contributions to Zenif are welcome! Whether you're fixing bugs, improving documentation, or proposing new features, your efforts are appreciated. Here's how you can contribute:

1. **Fork & Clone the Repository**: Start by forking the Zenif repository on GitHub. Clone your fork to your local machine for development.

   ```zsh
   git clone https://github.com/DomBom16/zenif.git
   ```

2. **Create a Branch**: Create a new branch for your feature or bug fix.

   ```zsh
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes & Test**: Implement your feature or bug fix. Be sure to test it before continuing.
4. **Update Documentation**: If your changes require it, update the README and any relevant documentation.
5. **Commit Your Changes**: Commit your changes with a clear and descriptive commit message.

   ```zsh
   git commit -m "Add feature: your feature description"
   ```

6. **Push to Your Fork**: Push your changes to your fork on GitHub.

   ```zsh
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**: Go to the Zenif repository on GitHub and create a new pull request from your feature branch.

Please ensure your code adheres to the project's coding standards and includes appropriate documentation. We appreciate your contribution!

## Testing

Zenif uses unittest for its test suite. We encourage contributors to write tests for new features and bug fixes. The `zenif/tests/decorators/test1.py` provides a good example of how to structure tests.

## Versioning

Zenif follows [Semantic Versioning](https://semver.org/). The version number is structured as MAJOR.MINOR.PATCH:

- MAJOR version increments denote incompatible API changes,
- MINOR version increments add functionality in a backwards-compatible manner, and
- PATCH version increments are for backwards-compatible bug fixes.

## License

Zenif is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

<!-- Only add acknowledgements once someone is acknowledged :( -->

<!-- ## Acknowledgements

We would like to thank all the contributors who have helped to make Zenif better. Your time and effort are greatly appreciated. -->

## Support

If you encounter any issues or have questions about using Zenif, please file an issue on the [GitHub issue tracker](https://github.com/DomBom16/zenif/issues).
