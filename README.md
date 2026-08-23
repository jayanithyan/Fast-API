## Features

- Create items
- Get all items
- Get item by ID
- Update items
- Delete items
- Search items
- Filter items by price
- Sort items
- Pagination
- Item statistics
## Installation

```bash
pip install -r requirements.txt
## Run

```bash
uvicorn Main:app --reload
## Example

### Create Item

POST `/items/`

```json
{
    "name": "Laptop",
    "price": 50000,
    "description": "Programming laptop",
    "offer": 10
}