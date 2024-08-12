# ActivatedNotebookImporter

ActivatedNotebookImporter is a Python package developed by Activated AI (https://activated-ai.com) that allows you to import Jupyter notebooks as Python modules. It provides functionality to import notebooks from files or string representations, with support for parameter substitution.

## Installation

You can install ActivatedNotebookImporter using pip:

```
pip install activated-notebook-importer
```

## Usage

Here's a basic example of how to use ActivatedNotebookImporter:

```python
from activated_notebook_importer import import_notebook

# Import a notebook from a file
module = import_notebook('path/to/your/notebook.ipynb')

# If your notebook defines a function 'greet', you can now use it:
result = module.greet('World')
print(result)  # Output: Hello, World!

# You can also import a notebook with parameter substitution:
module = import_notebook('path/to/your/notebook.ipynb', {'name': 'Alice'})
```

For more detailed usage instructions and API documentation, please refer to our [documentation](https://docs.activated-ai.com/activated-notebook-importer).

## Contributing

We welcome contributions! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## About Activated AI

ActivatedNotebookImporter is developed and maintained by Activated AI. Visit our website at https://activated-ai.com to learn more about us.