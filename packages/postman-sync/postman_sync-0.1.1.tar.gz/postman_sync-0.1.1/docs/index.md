
# postman_sync Documentation

## Overview

`postman_sync` is a tool designed to synchronize Postman collections with Swagger (OpenAPI) specifications. It automates the process of keeping your API documentation in sync between Postman and Swagger, making it easier to manage and update your API documentation.

## Features

- Extract endpoints from Swagger specifications.
- Update existing Postman collections with new or modified endpoints.
- Create new Postman collections from Swagger specifications.
- Cleanup old endpoints from Postman collections.
- Supports both Swagger 2.0 and OpenAPI 3.0 specifications.

## Installation

To install `postman_sync`, you can use pip:

```sh
pip install postman_sync
```

## Usage

### Command Line Interface

You can use the command line interface to synchronize your Postman collections with Swagger specifications. Here are some examples:

#### Sync a new Swagger specification with a new Postman collection

```sh
postman_sync --swagger-url http://example.com/swagger.json --postman-api-key YOUR_POSTMAN_API_KEY
```

#### Update an existing Postman collection with a Swagger specification

```sh
postman_sync --swagger-url http://example.com/swagger.json --postman-api-key YOUR_POSTMAN_API_KEY --collection-id YOUR_COLLECTION_ID
```

### Library Usage

You can also use `postman_sync` as a library in your Python code:

```python
from postman_sync.helper_functions import create_collection_json, update_collection_json

swagger_url = 'http://example.com/swagger.json'
api_key = 'YOUR_POSTMAN_API_KEY'
collection_id = 'YOUR_COLLECTION_ID'

# Create a new collection
new_collection_id = create_collection_json(swagger_url, api_key)
print(f'New collection created with ID: {new_collection_id}')

# Update an existing collection
update_success = update_collection_json(swagger_url, api_key, collection_id)
if update_success:
    print(f'Collection {collection_id} updated successfully')
else:
    print(f'Failed to update collection {collection_id}')
```

## Configuration

### API Keys

To use `postman_sync`, you need a Postman API key. You can generate an API key from your Postman account settings.

### Swagger URL

The Swagger URL should point to a valid Swagger (OpenAPI) JSON specification. Ensure that the URL is accessible and returns a valid JSON response.

## Development

### Setting up the Development Environment

1. Clone the repository:

```sh
git clone https://github.com/BlazinArtemis/postman-swagger-automatic-sync.git
cd postman-swagger-automatic-sync
```

2. Create a virtual environment and install dependencies:

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Run the tests to ensure everything is set up correctly:

```sh
python -m unittest discover tests
```

### Contributing

We welcome contributions to `postman_sync`. If you would like to contribute, please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Write tests to cover your changes.
4. Ensure all tests pass.
5. Submit a pull request with a detailed description of your changes.

## License

`postman_sync` is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or issues, please open an issue on GitHub or contact us at [oluwaseyinexus137@gmail.com](oluwaseyinexus137@gmail.com).
```

