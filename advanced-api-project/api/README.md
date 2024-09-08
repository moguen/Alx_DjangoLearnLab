# Advanced API Project

## API Endpoints

### List and Create Books

- **URL:** `/books/`
- **Methods:** `GET`, `POST`
- **GET**: Retrieve a list of all books.
- **POST**: Create a new book. Requires authentication.

### Retrieve, Update, and Delete Books

- **URL:** `/books/<int:pk>/`
- **Methods:** `GET`, `PUT`, `DELETE`
- **GET**: Retrieve a single book by ID.
- **PUT**: Update a book instance. Requires authentication.
- **DELETE**: Delete a book instance. Requires authentication.

### Permissions

- **ListView:** Available to unauthenticated users for listing books.
- **DetailView:** Available to unauthenticated users for viewing book details.
- **CreateView, UpdateView, DeleteView:** Restricted to authenticated users.
