LibraryProject
#bookshelf

# Permissions and Groups Setup

## Custom Permissions

We have defined custom permissions in the `YourModel` model to control actions like viewing, creating, editing, and deleting.

- `can_view`: Can view items
- `can_create`: Can create items
- `can_edit`: Can edit items
- `can_delete`: Can delete items

## Groups

- `Editors`: Can create and edit items.
- `Viewers`: Can view items only.
- `Admins`: Can view, create, edit, and delete items.

## Views

- `view_items`: Restricted to users with the `can_view` permission.
- `create_item`: Restricted to users with the `can_create` permission.
- `edit_item`: Restricted to users with the `can_edit` permission.
- `delete_item`: Restricted to users with the `can_delete` permission.
