## REST API Best Practices

- REST APIs should accept JSON for request payload and also send responses to JSON.
- To make sure that when our REST API server responds with JSON that clients interpret it as such, we should set `Content-Type` in the response header to `application/json` after the request is made.
- We shouldn't use verbs in our endpoint paths. Instead, we should use the nouns which represent the entity that the endpoint that we're retrieving or manipulating as the pathname.
  - This is because our HTTP request method already has the verb. Having verbs in our API endpoint paths isn’t useful and it makes it unnecessarily long since it doesn’t convey any new information. The chosen verbs could vary by the developer’s whim. For instance, some like ‘get’ and some like ‘retrieve’, so it’s just better to let the HTTP GET verb tell us what and endpoint does.
  - We should create routes like `GET /articles/` for getting news articles. Likewise, `POST /articles/` is for adding a new article , PUT `/articles/:id` is for updating the article with the given id. DELETE `/articles/:id` is for deleting an existing article with the given ID.
- When designing endpoints, it makes sense to group those that contain associated information. That is, if one object can contain another object, you should design the endpoint to reflect that. This is good practice regardless of whether your data is structured like this in your database. In fact, it may be advisable to avoid mirroring your database structure in your endpoints to avoid giving attackers unnecessary information.
  - For example, if we want an endpoint to get the comments for a news article, we should append the `/comments` path to the end of the `/articles` path (`GET method on the path /articles/:articleId/comments`)
- Handle errors gracefully and return HTTP response codes that indicate what kind of error occurred.
- **Common error HTTP status codes include**:
  - 200 OK - the request was successful and the response contains the requested data.
  - 201 Created - the request was successful and a new resource was created
  - 400 Bad Request - the request was invalid or missing required parameters
  - 401 Unauthorized - This means the user isn't not authorized to access a resource. It usually returns when the user isn't authenticated.
  - 403 Forbidden - This means the user is authenticated, but it's not allowed to access a resource.
  - 404 Not Found - This indicates that a resource is not found.
  - 500 Internal server error - This is a generic server error. It probably shouldn't be thrown explicitly.
  - 502 Bad Gateway - This indicates an invalid response from an upstream server.
  - 503 Service Unavailable - This indicates that something unexpected happened on server side (It can be anything like server overload, some parts of the system failed, etc.).
- We also need ways to paginate data so that we only return a few results at a time. We don't want to tie up resources for too long by trying to get all the requested data at once.
  - Filtering and pagination both increase performance by reducing the usage of server resources. As more data accumulates in the database, the more important these features become.
  - `GET /posts?limit=10&offset=0` - retrieves the first 10 posts
  - `GET /posts?limit=10&offset=10` - retrieves the second 10 posts
  - `GET /posts?limit=10&offset=20` - retrieves the third 10 posts,
- Use in-memory caching to improve the response time.
- Version the APIs. Versioning is usually done with /v1/, /v2/, etc. added at the start of the API path.
  - For example `GET /v1/employees` and `GET /v2/employees`.
  - Another approach to versioning in REST API design is to include the version number in a custom HTTP header.
- Use an URL like `https://api.example.com/products/1234` instead of `https://api.example.com/getProduct?id=1234`.
  - `GET /customers` - retrieves a list of all customers
  - `GET /customers/{id}` - retrieves a specific customer by ID
  - `POST /customers` - creates a new customer
  - `PUT /customers/{id}` - updates an existing customer by ID
  - `DELETE /customers/{id}` - deletes a customer by ID
- Rate limit the APIs.
- Protect sensitive APIs using JSON web tokens.

## More about HTTP Requests

- Different Methods

  - GET (idempotent): Requests data from a specified resource. GET requests should only retrieve data and should not have any other effect on the data.
  - POST (non idempotent): Submits data to be processed to a specified resource. POST requests may lead to the creation of a new resource or the updating of existing resources.
  - PUT (idempotent): Uploads a representation of the specified resource. If the resource already exists, it will be replaced; if it does not exist, it will be created. We provide the complete data for the resource.
  - DELETE (idempotent): Deletes the specified resource.
  - PATCH (non idempotent): Applies partial modifications to a resource. We only provide the data that is being updated.
  - HEAD (idempotent): Requests the headers of the specified resource without returning the actual resource body. This is often used to check if a resource exists or to retrieve metadata about a resource.

- `Content-Type` is an important header which indicates the media type of data in the body.
  - This is generally set by the client to tell the server what type of content is present in the body of the request.
  - This parameter is also specified by the API servers when they want to indicate the media type of data in the response body so that it can be easily intepreted by the clients.
- Some common content types:

  - `application/json`: This content type is used when _sending JSON data in the request body or receiving JSON data in the response body_.
  - `application/x-www-form-urlencoded`: This content type is used when _submitting HTML form data to a server_. In this format, the data is URL-encoded, meaning that special characters are replaced with percent-encoded representations (e.g., spaces become %20 or +). The key-value pairs are concatenated using the ampersand symbol (&), resulting in a string of data.
  - `multipart/form-data`: This content type is used when submitting binary data or files, such as images or documents, along with other form fields.
  - `text/plain`: This content type is used for plain text data.
  - `application/octet-stream`: This content type is used for arbitrary binary data. It's often used when transferring files or other binary data where the specific format is not important to the server.

- Difference between `application/x-www-form-urlencoded` vs `application/json`
  - The first case is telling the server that we are sending data as `Name=John+Smith&Age=23` and the second case is telling the server we are sending data as `{"Name": "John Smith", "Age": 23}`.

## References

- https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/
- https://medium.com/@bubu.tripathy/best-practices-for-designing-rest-apis-5b1809545e3c
- https://www.baeldung.com/postman-form-data-raw-x-www-form-urlencoded
