# Permissions and Groups Setup

## Custom Permissions
Defined in `Book` model (`models.py`):
- `can_view`
- `can_create`
- `can_edit`
- `can_delete`

## Groups
Created via Admin or script:
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Views
Protected using `@permission_required`:
- `book_list` → requires `can_view`
- `book_create` → requires `can_create`
- `book_edit` → requires `can_edit`
- `book_delete` → requires `can_delete`

## Testing
- Create test users and assign them to groups.
- Verify access is restricted based on roles.
