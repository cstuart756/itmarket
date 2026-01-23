# ITMarket — AI-Augmented Full-Stack Django Marketplace

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.2_LTS-092E20?logo=django&logoColor=white" alt="Django 4.2 LTS">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white" alt="Python 3.11">
  <img src="https://img.shields.io/badge/Heroku-Deployed-430098?logo=heroku&logoColor=white" alt="Deployed on Heroku">
</p>

<p align="center">
  <strong>A secure, responsive marketplace for buying and selling modern technology products.</strong>
</p>

<p align="center">
  <a href="https://itmarket-app-208bb526531b.herokuapp.com">Live Site</a> •
  <a href="https://github.com/cstuart756/itmarket">Repository</a>
</p>

---

## Project Overview

ITMarket is a full-stack marketplace web application built with **Django 4.2 (LTS)**, **Python 3.11**, **Bootstrap 5**, and **Cloudinary**.

It enables users to register, authenticate, and manage marketplace products using secure, database-backed CRUD workflows with ownership-based access control.

The platform is designed for buying and selling modern technology products including consoles, phones, tablets, laptops, desktops, gaming PCs, and accessories.

### Key Capabilities

- Full-stack Django (MTV) architecture
- Secure authentication and authorisation
- Media uploads using Cloudinary (production-safe storage)
- Responsive UI across desktop, laptop, tablet, and mobile
- Cloud deployment with Heroku + Postgres
- Agile workflow using GitHub Issues and Projects (Kanban)
- AI-augmented engineering workflow (with manual validation)

This project satisfies the requirements of the **AI-Augmented Full-Stack Bootcamp – Individual Capstone Project**.

---

## Table of Contents

- UX Design
- Wireframes
- Data Model (ERD)
- Features
- Technologies Used
- User Stories (MoSCoW)
- Agile Methodology
- Automated Testing
- Version Control
- Deployment (Heroku)
- Bug Fix Log
- Screenshots
- Lighthouse Performance Audits
- Project Management
- AI-Assisted Development
- Future Features & Roadmap
- References
- Author
- Declaration

---

## UX Design

### Design Goals

- Clean, intuitive interface for buyers and sellers
- Fully responsive across desktop, laptop, tablet, and mobile
- Accessibility-aware design with clear navigation and readable forms
- Bright and vivid colour palette for visual engagement
- Consistent feedback messages for all user actions

### Colour Scheme

| Purpose | Colour |
|------|------|
| Primary | `#FF2E63` |
| Secondary | `#08D9D6` |
| Dark Contrast | `#252A34` |
| Background | `#EAEAEA` |

### Typography

- Google Font: **Poppins**
- Applied consistently to headings and body text

---

## Wireframes

Wireframes illustrate the responsive design approach across device sizes.  
All wireframes are stored under:

docs/screenshots/wireframes/


### Mobile

<img src="docs/screenshots/wireframes/mobile.png" style="max-width:360px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/mobile0.png" style="max-width:360px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/mobile1.png" style="max-width:360px;width:100%;height:auto;">

### Tablet

<img src="docs/screenshots/wireframes/tablet.png" style="max-width:600px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/tablet0.png" style="max-width:600px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/tablet1.png" style="max-width:600px;width:100%;height:auto;">

### Laptop

<img src="docs/screenshots/wireframes/laptop.png" style="max-width:720px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/laptop0.png" style="max-width:720px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/laptop1.png" style="max-width:720px;width:100%;height:auto;">

### Desktop

<img src="docs/screenshots/wireframes/desktop.png" style="max-width:900px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/desktop0.png" style="max-width:900px;width:100%;height:auto;">
<img src="docs/screenshots/wireframes/desktop1.png" style="max-width:900px;width:100%;height:auto;">

---

## Data Model (ERD)

The Entity Relationship Diagram defines the database structure and relationships.

<img src="docs/erd.png" style="max-width:900px;width:100%;height:auto;">

---

## Features

### Authentication & Authorisation

- User registration, login, logout
- Authentication state reflected in the navbar
- Ownership-based access control (only owners can edit or delete products)

### Marketplace

- View products in a responsive card layout
- Create, update, and delete products (authenticated users)
- Category assignment and display
- Cloudinary-backed image uploads
- Primary image selection logic
- Search by title, description, category, or seller

### Notifications

- Registration confirmation messages
- Product create, update, and delete confirmations
- Image upload and delete confirmations

---

## Technologies Used

### Front-End
- HTML5
- CSS3
- Bootstrap 5
- Google Fonts (Poppins)

### Back-End
- Python 3.11
- Django 4.2 (LTS)
- Django ORM

### Database
- SQLite (development)
- Heroku Postgres (production)

### Media & Static
- Cloudinary
- Whitenoise

### Tools & Platforms
- VS Code
- Git & GitHub
- Heroku
- Gunicorn

---

## User Stories (MoSCoW)

### MUST HAVE — Delivered
- User registration and login
- Browse products
- Create, update, and delete products
- Upload product images
- Primary image selection

### SHOULD HAVE
- Product search
- Category filtering
- Sorting
- User profiles

### COULD HAVE
- Reviews and ratings
- Wishlist
- Messaging
- Email notifications
- Public API

### WON’T HAVE (Current Scope)
- Payments and checkout
- Shipping and order tracking
- Real-time chat
- Mobile applications
- AI recommendations

---

## Agile Methodology

- GitHub Issues for user stories
- GitHub Projects for Kanban tracking
- Workflow: Backlog → To Do → In Progress → Done
- Incremental delivery with traceable commits

---

## Automated Testing

Django `TestCase` suite covering:

- Models
- Views
- Permissions
- CRUD workflows
- Messages
- Image rules

Run locally:

```bash
python manage.py test

Version Control

    Regular, incremental commits

    Meaningful commit messages

    .env excluded via .gitignore

    Secrets stored in Heroku Config Vars

Deployment (Heroku)
Stack

    Heroku web dyno

    Heroku Postgres

    Gunicorn

    Whitenoise

    Cloudinary

Production Settings

    DEBUG=False

    HTTPS enforced

    Secure cookies

    HSTS enabled

Bug Fix Log

Authentication Template Resolution

    Ensured TEMPLATES['DIRS'] includes BASE_DIR / "templates"

    Added templates/registration/login.html

    Correctly wired django.contrib.auth.urls

Result: Authentication pages render correctly locally and in production.

Database Persistence

    Migrated from SQLite to Heroku Postgres

    Enforced DEBUG=False

    Used persistent database storage

Result: Product and image data persists across dyno restarts.
## Screenshots

The following screenshots demonstrate core application functionality, user authentication, product management workflows, and production readiness.

---

### Application Interface & User Flows

#### 1. Homepage (Deployed on Heroku)
<img src="docs/screenshots/01-homepage-heroku.png" style="max-width:900px;width:100%;height:auto;">

#### 2. User Registration Page
<img src="docs/screenshots/02-registration-page.png" style="max-width:720px;width:100%;height:auto;">

#### 3. Registration Confirmation
<img src="docs/screenshots/03-registration-confirmation.png" style="max-width:720px;width:100%;height:auto;">

#### 4. Login Page
<img src="docs/screenshots/04-login-page.png" style="max-width:720px;width:100%;height:auto;">

#### 5. Logged-In User State
<img src="docs/screenshots/05-logged-in-state.png" style="max-width:900px;width:100%;height:auto;">

---

### Product Management

#### 6. Create Product Form
<img src="docs/screenshots/06-create-product.png" style="max-width:720px;width:100%;height:auto;">

#### 7. Product Created Confirmation
<img src="docs/screenshots/07-product-created-confirmation.png" style="max-width:720px;width:100%;height:auto;">

#### 8. Product Listed Successfully
<img src="docs/screenshots/product-listed.png" style="max-width:900px;width:100%;height:auto;">

#### 9. Product Image Loaded Correctly
<img src="docs/screenshots/image-loaded.png" style="max-width:900px;width:100%;height:auto;">

---

## Lighthouse Performance Audits

Lighthouse audits were conducted in the production environment to validate performance, accessibility, best practices, and SEO across desktop and mobile devices.

#### 10. Desktop Audit – High Performance
<img src="docs/screenshots/lighthouse-desktop0.png" style="max-width:900px;width:100%;height:auto;">

#### 11. Desktop Audit – Optimised State
<img src="docs/screenshots/lighthouse-desktop1.png" style="max-width:900px;width:100%;height:auto;">

#### 12. Mobile Audit
<img src="docs/screenshots/lighthouse-mobile0.png" style="max-width:900px;width:100%;height:auto;">

#### 13. Mobile Audit – Alternative Run
<img src="docs/screenshots/lighthouse-mobile1.png" style="max-width:900px;width:100%;height:auto;">

---

## Project Management

Agile project management was carried out using GitHub Issues and Projects, following a Kanban workflow.

#### GitHub Kanban Board
<img src="docs/screenshots/kanban.png" style="max-width:900px;width:100%;height:auto;">

AI-Assisted Development

AI tools were used to assist with boilerplate generation, test creation, debugging, and UX decisions.
All outputs were reviewed, adapted, and validated via automated testing and manual verification.
Future Features & Roadmap
Phase 1

    Advanced search and filtering

    Sorting

    Image gallery

    User profiles

Phase 2

    Reviews and ratings

    Wishlist

    Messaging

Phase 3

    Admin dashboard

    Email notifications

    Public REST API

References

    Django Docs — https://docs.djangoproject.com/

    Bootstrap Docs — https://getbootstrap.com/docs/

    Cloudinary Docs — https://cloudinary.com/documentation

    Heroku Dev Center — https://devcenter.heroku.com/

    WCAG Guidelines — https://www.w3.org/WAI/standards-guidelines/wcag/

Author

Stuart Carey
AI-Augmented Full-Stack Bootcamp — Individual Capstone Project
Declaration

This project is my own original work.
AI tools were used strictly as development assistants. All architecture, security decisions, business logic, and implementation choices were designed, reviewed, and validated independently.