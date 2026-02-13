# Products API Documentation

## 1. Comprehensive Endpoint Documentation (Prompt 1)

### List Products API

Get a list of products with flexible filtering, sorting, and pagination.

#### Endpoint
`GET /api/products`

#### Description
Retrieves a paginated list of products from the database. Supports filtering by category, price range, and stock status, as well as sorting and pagination.

#### Request Query Parameters
| Parameter | Type    | Required | Description                                                        |
|-----------|---------|----------|--------------------------------------------------------------------|
| category  | String  | No       | Filter products by category                                        |
| minPrice  | Number  | No       | Minimum price (inclusive)                                          |
| maxPrice  | Number  | No       | Maximum price (inclusive)                                          |
| sort      | String  | No       | Field to sort by (default: 'createdAt')                            |
| order     | String  | No       | Sort order: 'asc' or 'desc' (default: 'desc')                      |
| page      | Number  | No       | Page number for pagination (default: 1)                            |
| limit     | Number  | No       | Number of items per page (default: 20, max: 100)                   |
| inStock   | Boolean | No       | If 'true', only show products with stock > 0                       |

#### Response
- **200 OK**
  Returns a JSON object with an array of products and pagination info.

  ```json
  {
    "products": [
      {
        "_id": "61fa9bcf5c130b2e6d675432",
        "name": "Wireless Headphones",
        "description": "High-quality wireless headphones with noise cancellation",
        "price": 89.99,
        "category": "electronics",
        "stockQuantity": 45,
        "createdAt": "2023-02-01T15:32:47Z",
        "updatedAt": "2023-03-15T09:21:08Z"
      }
    ],
    "pagination": {
      "total": 42,
      "page": 1,
      "limit": 20,
      "pages": 3
    }
  }
  ```

- **500 Internal Server Error**
  ```json
  {
    "error": "Server error",
    "message": "Failed to fetch products"
  }
  ```

#### Authentication
No authentication required.

#### Error Responses
- 400 Bad Request: Invalid query parameters
- 500 Internal Server Error: Database or server error

#### Example Requests
1. Get all products in the "electronics" category:
   ```
   GET /api/products?category=electronics
   ```
2. Get products with price between $20 and $100, sorted by price:
   ```
   GET /api/products?minPrice=20&maxPrice=100&sort=price&order=asc&page=1&limit=10
   ```

#### Notes
- All timestamps are in ISO 8601 format (UTC).
- Product IDs are MongoDB ObjectId strings.
- The maximum allowed limit per page is 100 items.

---

## 2. OpenAPI/Swagger Documentation (Prompt 2)

```yaml
openapi: 3.0.0
info:
  title: Products API
  description: API for retrieving product information with filtering, sorting, and pagination.
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /api/products:
    get:
      summary: List products
      description: Get a list of products with flexible filtering, sorting, and pagination.
      parameters:
        - in: query
          name: category
          schema:
            type: string
          description: Filter products by category
        - in: query
          name: minPrice
          schema:
            type: number
          description: Minimum price (inclusive)
        - in: query
          name: maxPrice
          schema:
            type: number
          description: Maximum price (inclusive)
        - in: query
          name: sort
          schema:
            type: string
            default: createdAt
          description: Field to sort by
        - in: query
          name: order
          schema:
            type: string
            enum: [asc, desc]
            default: desc
          description: Sort order
        - in: query
          name: page
          schema:
            type: integer
            minimum: 1
            default: 1
          description: Page number for pagination
        - in: query
          name: limit
          schema:
            type: integer
            minimum: 1
            maximum: 100
            default: 20
          description: Number of items per page
        - in: query
          name: inStock
          schema:
            type: boolean
          description: When true, only show products with stock > 0
      responses:
        '200':
          description: Successful operation
          content:
            application/json:
              schema:
                type: object
                properties:
                  products:
                    type: array
                    items:
                      $ref: '#/components/schemas/Product'
                  pagination:
                    $ref: '#/components/schemas/Pagination'
        '400':
          description: Invalid query parameters
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
        '500':
          description: Server error
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    Product:
      type: object
      properties:
        _id:
          type: string
          description: Unique identifier for the product
        name:
          type: string
          description: Product name
        description:
          type: string
          description: Product description
        price:
          type: number
          format: float
          description: Product price
        category:
          type: string
          description: Product category
        stockQuantity:
          type: integer
          description: Available quantity in stock
        createdAt:
          type: string
          format: date-time
          description: Creation timestamp
        updatedAt:
          type: string
          format: date-time
          description: Last update timestamp
    Pagination:
      type: object
      properties:
        total:
          type: integer
          description: Total number of items
        page:
          type: integer
          description: Current page number
        limit:
          type: integer
          description: Items per page
        pages:
          type: integer
          description: Total number of pages
    Error:
      type: object
      properties:
        error:
          type: string
          description: Error type
        message:
          type: string
          description: Error message
```

---

## 3. Developer Usage Guide (Prompt 3)

### Developer Guide: List Products API

This guide explains how to use the `GET /api/products` endpoint to retrieve products with filtering, sorting, and pagination.

#### 1. Authentication
No authentication is required for this endpoint.

#### 2. Formatting Requests
- Base URL: `https://api.example.com/api/products`
- Use query parameters to filter, sort, and paginate results.

##### Example Request (Fetch electronics, page 1, 10 per page):
```
GET /api/products?category=electronics&page=1&limit=10
```

##### Example Request (Price range, sorted by price ascending):
```
GET /api/products?minPrice=20&maxPrice=100&sort=price&order=asc
```

#### 3. Handling Responses
- On success (`200 OK`), you'll receive a JSON object with:
  - `products`: Array of product objects
  - `pagination`: Pagination info

###### Example Success Response
```json
{
  "products": [
    {
      "_id": "61fa9bcf5c130b2e6d675432",
      "name": "Wireless Headphones",
      "price": 89.99,
      "category": "electronics",
      "stockQuantity": 45,
      "createdAt": "2023-02-01T15:32:47Z",
      "updatedAt": "2023-03-15T09:21:08Z"
    }
  ],
  "pagination": {
    "total": 42,
    "page": 1,
    "limit": 10,
    "pages": 5
  }
}
```

#### 4. Error Handling
- `400 Bad Request`: Invalid query parameters.
- `500 Internal Server Error`: Server/database error.

###### Example Error Response
```json
{
  "error": "Server error",
  "message": "Failed to fetch products"
}
```

#### 5. Example Code (JavaScript/Node.js with axios)
```js
const axios = require('axios');

async function fetchProducts() {
  try {
    const response = await axios.get('https://api.example.com/api/products', {
      params: {
        category: 'electronics',
        minPrice: 20,
        maxPrice: 100,
        sort: 'price',
        order: 'asc',
        page: 1,
        limit: 10
      }
    });
    console.log(response.data.products);
  } catch (error) {
    if (error.response) {
      console.error('API error:', error.response.data);
    } else {
      console.error('Request failed:', error.message);
    }
  }
}
```

#### Target Audience
This guide is intended for developers with basic experience in REST APIs and JavaScript.

#### Tone
Friendly, practical, and example-driven.
