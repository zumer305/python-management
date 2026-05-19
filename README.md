# 📌 Project Management API (Django REST Framework)

## 🚀 Overview

This project is a **backend REST API system** built with Django and Django REST Framework for managing projects and tasks. It includes secure JWT authentication, strict ownership-based access control, and advanced features like filtering, searching, ordering, and pagination.

The system is designed to simulate a real-world project management tool similar to Jira/Trello (simplified backend version).

---

## 🧩 Features

- 🔐 JWT Authentication (Access + Refresh Tokens)
- 👤 User Registration & Profile Management
- 📁 Project CRUD (Create, Read, Update, Delete)
- 📝 Task CRUD under Projects
- 🛡️ Strict Ownership-Based Access Control
- 🔍 Filtering (status, priority, dates, etc.)
- 🔎 Search (title, description)
- 🔃 Ordering (created date, priority, due date)
- 📄 Pagination (page size control)
- ⚙️ Automatic task completion logic
- 🧑‍💻 Admin panel customization

---

## 🏗️ Project Structure

```
myproject/
│
├── accounts/           # Authentication & user profile
├── projects/           # Project management
├── tasks/              # Task management
├── myproject/          # Settings & configuration
├── manage.py
└── README.md
```

---

## 🔐 Authentication System

This project uses **JWT (JSON Web Tokens)** for authentication.

### Authentication Flow:

1. User registers via `/api/auth/register/`
2. User logs in via `/api/auth/login/`
3. Server returns:
   - Access Token (short-lived)
   - Refresh Token (long-lived)
4. Access Token is used for all protected API requests
5. Use Refresh Token to get a new Access Token when expired

---

## 👤 User Model Fields

- `username` - Unique username
- `email` - User email address
- `password` - Hashed password (never stored in plain text)
- `first_name` - User's first name
- `last_name` - User's last name

---

## 📁 Project Model

### Fields:

| Field         | Type       | Description                           |
| ------------- | ---------- | ------------------------------------- |
| `title`       | String     | Project name                          |
| `description` | Text       | Project details                       |
| `status`      | Choice     | Planned, Active, Completed, Cancelled |
| `priority`    | Choice     | Low, Medium, High, Urgent             |
| `start_date`  | Date       | Project start date                    |
| `end_date`    | Date       | Project end date                      |
| `created_by`  | ForeignKey | Project owner (User)                  |
| `created_at`  | DateTime   | Creation timestamp                    |
| `updated_at`  | DateTime   | Last update timestamp                 |

### Validation Rules:

- ✅ End date must not be earlier than start date
- ✅ Each project belongs to a single user (owner)
- ✅ Only project owner can view/edit/delete

---

## 📝 Task Model

### Fields:

| Field          | Type       | Description                                 |
| -------------- | ---------- | ------------------------------------------- |
| `project`      | ForeignKey | Associated project                          |
| `title`        | String     | Task name                                   |
| `description`  | Text       | Task details                                |
| `status`       | Choice     | To Do, In Progress, Review, Done, Cancelled |
| `priority`     | Choice     | Low, Medium, High, Urgent                   |
| `due_date`     | Date       | Task deadline                               |
| `is_completed` | Boolean    | Auto-managed based on status                |
| `assigned_to`  | ForeignKey | Assigned user (optional)                    |
| `created_by`   | ForeignKey | Task creator                                |
| `created_at`   | DateTime   | Creation timestamp                          |
| `updated_at`   | DateTime   | Last update timestamp                       |

### Business Logic Rules:

- ✅ Task must belong to user's own project
- ✅ Due date cannot be in the past
- ✅ Status "Done" automatically sets `is_completed = True`
- ✅ Status not "Done" automatically sets `is_completed = False`

---

## 🛡️ Permissions & Access Control

- **User-Level Isolation**: Users can only access their own data
- **Object-Level Ownership**: Enforced at API endpoint level
- **Strict Authorization**: Unauthorized access returns `403 Forbidden` or `401 Unauthorized`
- **No Cross-User Access**: Impossible to view/edit other users' projects or tasks

---

## 🔍 Filtering & Search

### Projects API:

**Filters:**

- `status` - Filter by project status
- `priority` - Filter by priority level
- `start_date_from` / `start_date_to` - Filter by start date range
- `end_date_from` / `end_date_to` - Filter by end date range

**Search:**

- Search by `title` and `description`

**Ordering:**

- Order by `created_at`, `priority`, `end_date`

### Tasks API:

**Filters:**

- `status` - Filter by task status
- `priority` - Filter by priority level
- `project` - Filter by project ID
- `is_completed` - Filter by completion status
- `due_date_from` / `due_date_to` - Filter by due date range

**Search:**

- Search by `title` and `description`

**Ordering:**

- Order by `created_at`, `due_date`, `priority`

---

## 📄 Pagination

- **Global Pagination Enabled**: All list endpoints are paginated
- **Page Size**: 5 records per page (configurable)
- **Navigation**: `next`, `previous` links in response
- **Total Count**: Total number of records available

### Example Response:

```json
{
  "count": 15,
  "next": "http://api.example.com/api/projects/?page=2",
  "previous": null,
  "results": [...]
}
```

---

## ⚙️ Tech Stack

| Technology                | Purpose              |
| ------------------------- | -------------------- |
| **Python**                | Programming language |
| **Django**                | Web framework        |
| **Django REST Framework** | REST API framework   |
| **SimpleJWT**             | JWT authentication   |
| **django-filter**         | Advanced filtering   |

---

## 🧑‍💻 Admin Panel

### Projects in Admin:

Displays:

- title
- status
- priority
- created_by
- created_at

Features:

- ✅ Filtering by status & priority
- ✅ Search by title
- ✅ List display customization
- ✅ Inline editing

### Tasks in Admin:

Displays:

- title
- status
- priority
- project
- created_by
- due_date

Features:

- ✅ Filtering by status, priority & project
- ✅ Search by title
- ✅ List display customization
- ✅ Inline editing

---

## 🧪 Testing Coverage

The API includes comprehensive test cases for:

- ✅ User registration & authentication
- ✅ JWT token generation and refresh
- ✅ Project CRUD operations
- ✅ Task CRUD operations
- ✅ Ownership restrictions enforcement
- ✅ Validation rules (dates, status, etc.)
- ✅ Filtering, search & ordering functionality
- ✅ Unauthorized access handling
- ✅ Error responses and status codes

---

## 📈 Future Improvements (Optional)

- 🔲 Role-based access control (Admin, Manager, User roles)
- 🔲 Task comments & collaborative discussions
- 🔲 File attachments for projects/tasks
- 🔲 Real-time notifications system
- 🔲 Frontend integration (React / Vue / Next.js)
- 🔲 Email notifications on task assignment
- 🔲 Activity logging & audit trail
- 🔲 API documentation with Swagger/OpenAPI

---

## 📌 Security Highlights

- 🔒 JWT-based stateless authentication
- 🔒 Ownership-based access control (IsOwner permissions)
- 🔒 No cross-user data access possible
- 🔒 Secure password hashing (Django's default PBKDF2)
- 🔒 Protected API endpoints (permission_classes required)
- 🔒 Input validation & sanitization
- 🔒 SQL injection prevention (Django ORM)
- 🔒 CSRF protection enabled

---

## 👨‍💻 Author

Built as an internship task project using Django REST Framework best practices.

---

## 🏁 Project Status

- ✅ Core features completed
- ✅ API fully tested
- ✅ Ready for submission / production deployment

---

## 💡 Additional Resources

**Want more?** We can create:

- 🔥 GitHub repository structure with proper commits
- 🔥 `.env` file configuration guide
- 🔥 Deployment setup (Render / Railway)
- 🔥 Interview Q&A based on this project
- 🔥 Postman API collection for testing
- 🔥 API documentation with code examples

---

## 📝 License

This project is open source and available under the MIT License.

---

**Last Updated:** May 2026
