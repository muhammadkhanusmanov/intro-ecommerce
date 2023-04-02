# intro-ecommerce

## objective

The objective of this project is to create a simple e-commerce backend using Django.

## Database

### Tables

- `Product`
- `Company`
- `Category`

### Schema

- `Product`

    | Field | Type | Description |
    | --- | --- | --- |
    | id | int | Primary Key |
    | name | varchar | Product name |
    | color | varchar | Product color |
    | price | decimal | Product price |
    | description | varchar | Product description |
    | company | int | One to Many relationship with `Company` |

- `Company`

    | Field | Type | Description |
    | --- | --- | --- |
    | id | int | Primary Key |
    | name | varchar | Company name |

- `Category`

    | Field | Type | Description |
    | --- | --- | --- |
    | id | int | Primary Key |
    | name | varchar | Category name |
    | products | int | Many to Many relationship with `Product` |

## API

### Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/products` | Get all products |
| GET | `/api/products/<id>` | Get a product by id |
| POST | `/api/products` | Create a product |
| POST | `api/products/<id>/update` | Update a product |
| POST | `api/products/<id>/delete` | Delete a product |
| GET | `/api/companies` | Get all companies |
| GET | `/api/companies/<id>` | Get a company by id |
| GET | `/api/companies/<id>/products` | Get all products by company id |
| POST | `/api/companies` | Create a company |
| GET | `/api/categories` | Get all categories |
| GET | `/api/categories/<id>` | Get a category by id |
| GET | `/api/categories/<id>/products` | Get all products by category id |
| POST | `/api/categories` | Create a category |