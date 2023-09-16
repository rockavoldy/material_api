# Materials API
Create new module and menu to list Materials on Odoo 14 Community

## ERD
[![Materials API dbdiagram](./img/Materials%20API.png)](https://dbdiagram.io/d/Materials-API-6505e40502bd1c4a5eb30e5b)

## Available Endpoint API
- GET `/material/`: List all materials in the DB
- GET `/material/<material_id>`: Get specific material by material_id
- POST `/material/`: Create new material; FormData format
  - `name`: varchar; mandatory
  - `material_code`: varchar; mandatory
  - `material_type`: enum of `['fabric', 'jeans', 'cotton']`; mandatory
  - `material_buy_price`: int; mandatory; must be above 100
  - `supplier_id`: int; mandatory
- PUT `/material/<material_id>`: Update specific material; FormData format
  - `name`: varchar; mandatory
  - `material_code`: varchar; mandatory
  - `material_type`: enum of `['fabric', 'jeans', 'cotton']`; mandatory
  - `material_buy_price`: int; mandatory; must be above 100
  - `supplier_id`: int; mandatory
- DELETE `/material/<material_id>`: Delete specific material