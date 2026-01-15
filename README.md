# ITMarket – AI-Augmented Full-Stack Django Web Application

[![Django](https://img.shields.io/badge/Django-4.2%20LTS-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![Deployment](https://img.shields.io/badge/Deployed-Heroku-430098?logo=heroku&logoColor=white)](https://www.heroku.com/)
[![Media](https://img.shields.io/badge/Media-Cloudinary-3448C5?logo=cloudinary&logoColor=white)](https://cloudinary.com/)

## Live Site (Heroku)
Deployed application: https://itmarket-app-208bb526531b.herokuapp.com

## Repository
GitHub repository: https://github.com/cstuart756/itmarket

---

## Project Overview

**ITMarket** is a full-stack marketplace web application built with **Django 4.2 (LTS)**, **Python 3.11**, **Bootstrap 5**, and **Cloudinary**. It enables users to register, authenticate, and manage marketplace products with secure, database-backed **CRUD** workflows and ownership-based access control.

The platform is designed for buying and selling modern technology products such as **consoles, phones, tablets, laptops, desktops, gaming PCs, and accessories**.

### Key Capabilities
- Full-stack Django architecture (MTV pattern)
- Secure authentication & authorisation
- Media uploads using Cloudinary (production-safe storage)
- Responsive UI across desktop, laptop, tablet, and mobile
- Cloud deployment with Heroku
- Agile development workflow using GitHub Issues + Projects (Kanban)
- AI-augmented software engineering workflow (with manual validation)

This project satisfies the requirements of the **AI-Augmented Full-Stack Bootcamp Individual Capstone Project**.

---

## Table of Contents
- [UX Design](#ux-design)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Model](#data-model)
- [Agile Methodology](#agile-methodology)
- [Automated Testing](#automated-testing)
- [Version Control](#version-control)
- [Deployment (Heroku)](#deployment-heroku)
- [Bug Fix Log](#bug-fix-log)
- [Screenshots](#screenshots)
- [AI-Assisted Development (Reflection)](#ai-assisted-development-reflection)
- [Future Enhancements](#future-enhancements)
- [References](#references)
- [Author](#author)
- [Declaration](#declaration)

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
|---|---|
| Primary | `#FF2E63` (Vibrant Pink) |
| Secondary | `#08D9D6` (Bright Teal) |
| Dark Contrast | `#252A34` |
| Background | `#EAEAEA` |

### Typography
- Google Font: **Poppins**
- Applied consistently to headings and body text

### Wireframes (Design Documentation)

Wireframes were produced to plan the responsive layout of the ITMarket marketplace application across major device form factors. They define:
- Layout structure
- Content hierarchy
- Navigation behaviour
- Interaction patterns

The designs follow a **mobile-first approach** and scale progressively using **Bootstrap’s responsive grid system**.

#### Device Layouts

**Desktop**
- Full-width navigation bar with authentication state
- Multi-column product grid (3–4 cards per row)
- Category and sorting controls above listings
- Prominent product images and action buttons

**Laptop**
- Reduced-width navigation bar
- Three-column product grid
- Centralised filters and controls
- Card-based layout with ownership action buttons

**Tablet**
- Collapsible navigation menu
- Two-column stacked product layout
- Touch-friendly buttons and spacing
- Optimised form layout for portrait orientation

**Mobile**
- Hamburger navigation menu
- Single-column product layout
- Large touch targets
- Stacked form inputs
- Optimised typography and spacing for small screens

## Wireframe Images

Wireframes are stored in `docs/screenshots/wireframes/` and document the responsive UI design across mobile, tablet, laptop, and desktop breakpoints.

### Mobile Wireframes
![Mobile Wireframe](docs/screenshots/wireframes/mobile.png)
![Mobile Wireframe Variant](docs/screenshots/wireframes/mobile0.png)
![Mobile Wireframe Variant](docs/screenshots/wireframes/mobile1.png)

### Tablet Wireframes
![Tablet Wireframe](docs/screenshots/wireframes/tablet.png)
![Tablet Wireframe Variant](docs/screenshots/wireframes/tablet0.png)
![Tablet Wireframe Variant](docs/screenshots/wireframes/tablet1.png)

### Laptop Wireframes
![Laptop Wireframe](docs/screenshots/wireframes/laptop.png)
![Laptop Wireframe Variant](docs/screenshots/wireframes/laptop0.png)
![Laptop Wireframe Variant](docs/screenshots/wireframes/laptop1.png)

### Desktop Wireframes
![Desktop Wireframe](docs/screenshots/wireframes/desktop.png)
![Desktop Wireframe Variant](docs/screenshots/wireframes/desktop0.png)
![Desktop Wireframe Variant](docs/screenshots/wireframes/desktop1.png)

### Group Layout Concepts
![Group Layout](docs/screenshots/wireframes/group.png)
![Group Layout Variant](docs/screenshots/wireframes/group0.png)
![Group Layout Variant](docs/screenshots/wireframes/group1.png)
![Group Layout Variant](docs/screenshots/wireframes/group2.png)



Assessment Mapping (Wireframes)
Learning Outcome	Evidence
LO1.1	Responsive layout across desktop, laptop, tablet, and mobile
LO1.5	Documented UX design process using wireframes
LO1	Accessibility-aware layout planning
LO2	UI designed around CRUD workflows
LO3	Navigation reflects authentication state
Features
Authentication & Authorization

    User registration

    Login and logout

    Authentication state reflected in navbar

    Ownership-based access control:

        Only owners can edit or delete their products

Marketplace Functionality

    View all products in a responsive card layout

    Create new products (authenticated users)

    Update and delete owned products only

    Category assignment and display

    Cloudinary-backed image upload

    Primary image logic

    Product carousel with device-based imagery

Notifications (Django Messages)

    Registration confirmation

    Product created confirmation

    Product updated confirmation

    Product deleted confirmation

    Image upload confirmation

    Image deletion confirmation

Technologies Used
Front-End

    HTML5

    CSS3

    Bootstrap 5

    Google Fonts (Poppins)

Back-End

    Python 3.11

    Django 4.2 (LTS)

    Django ORM

Database

    SQLite (development)

    Heroku Postgres (production)

Media & Static Files

    Cloudinary (media storage)

    Whitenoise (static files)

Tools & Platforms

    VS Code

    Git & GitHub

    Heroku

    Gunicorn

Data Model
Product Model

    owner — ForeignKey to User

    category — ForeignKey to Category (nullable)

    title — CharField

    description — TextField

    price — DecimalField

    created_at — DateTimeField

    updated_at — DateTimeField

Category Model

    name — unique category name

    slug — unique slug

    created_at — timestamp

ProductImage Model

    product — ForeignKey to Product

    uploaded_by — ForeignKey to User

    image — CloudinaryField

    alt_text — accessibility alt text

    is_primary — primary image flag

    created_at — timestamp

ERD Diagram

docs/erd.png

![ERD Diagram](docs/erd.png)

Relationships

    User → Product (one-to-many)

    Category → Product (one-to-many)

    Product → ProductImage (one-to-many)

    User → ProductImage (one-to-many)

Primary image resolution is handled via ordering:
(-is_primary, -created_at)
Agile Methodology
Epics

    User Authentication & Registration

    Marketplace CRUD Functionality

    Media Uploads (Cloudinary)

    Notifications & User Feedback

    UX Design & Responsiveness

    Deployment & Security

    Automated Testing

    Documentation & Evidence

User Stories (MoSCoW)

Must Have

    Register/Login

    CRUD products

    Ownership security

    Deployment

Should Have

    Notifications

    Images

Could Have

    Filters/search

    Admin enhancements

Won’t Have (current scope)

    Payments/checkout

Kanban Tracking

Project tracked using GitHub Issues + GitHub Projects (Kanban).

Workflow:
Backlog → To Do → In Progress → Done

Incremental development with traceable commits.
Automated Testing
Testing Approach

Automated tests using Django TestCase covering:

    Models

    Views

    Permissions

    CRUD workflows

    Messages

    Image rules

Automated Test Coverage (Examples)
Area	What is tested	Evidence
Product List	Page loads and displays listing	test_product_list_page_loads
Create Product	Login required, creation works	test_owner_can_create_product_and_sees_message
Update Product	Owner can update	test_owner_can_update_product_and_sees_message
Delete Product	Owner can delete	test_owner_can_delete_product_and_sees_message
Image Upload	Upload works	test_owner_can_upload_image_and_sees_message
Primary Image Rule	Only one primary image	test_primary_image_rule_unsets_previous_primary
Image Security	Non-owner blocked	test_non_owner_cannot_delete_image
Running Tests

python manage.py test

Version Control
Git Strategy

    Regular commits reflecting incremental progress

    Meaningful commit messages

    Traceable Agile development history

Secure Code Management

    .env excluded via .gitignore

    Secrets stored in Heroku Config Vars

    Production runs with DEBUG=False

Deployment (Heroku)
Platform

    Heroku web hosting + Heroku Postgres

Deployment Steps

    Create Heroku app

    Add Heroku Postgres add-on

    Set Config Vars:

        SECRET_KEY

        DEBUG=False

        CLOUDINARY_URL

    Connect GitHub repo and enable auto deploy

    Run migrations

    Collect static files

    Verify production behaviour

Production Settings

    DEBUG=False

    Environment variables for secrets

    Whitenoise for static files

    Gunicorn production server

    Cloudinary for persistent media storage

Bug Fix Log
Authentication Template Resolution Fix

Resolved template discovery and authentication-related 500 errors by:

    Ensuring TEMPLATES['DIRS'] includes BASE_DIR / "templates"

    Ensuring login template exists at templates/registration/login.html

    Wiring django.contrib.auth.urls correctly

Result: Authentication workflows render reliably locally and on Heroku.
Screenshots

## Screenshots

Screenshots are stored in `docs/screenshots/`:

![Homepage (Heroku)](docs/screenshots/01-homepage-heroku.png)
![Registration Page](docs/screenshots/02-registration-page.png)
![Registration Confirmation](docs/screenshots/03-registration-confirmation.png)
![Login Page](docs/screenshots/04-login-page.png)
![Logged In State](docs/screenshots/05-logged-in-state.png)
![Create Product](docs/screenshots/06-create-product.png)
![Product Created Confirmation](docs/screenshots/07-product-created-confirmation.png)
![Product Updated Confirmation](docs/screenshots/10-product-updated-confirmation.png)
![Product Deleted Confirmation](docs/screenshots/12-product-deleted-confirmation.png)


AI-Assisted Development (Reflection)

AI tools were used strategically to:

    Generate Django boilerplate aligned to project goals

    Produce unit tests for CRUD flows and security

    Debug deployment and template resolution issues

    Improve UX implementation decisions

    Accelerate iteration while maintaining quality

All AI-generated outputs were reviewed, adapted, and validated through automated testing and manual verification.
Future Enhancements

    Advanced search and filtering

    Product image galleries (enhanced browsing experience)

    Admin moderation dashboard

    Email notifications

    User messaging system

References

    Django Documentation — https://docs.djangoproject.com/

    Bootstrap Documentation — https://getbootstrap.com/docs/

    Google Fonts — https://fonts.google.com/

    WCAG Guidelines — https://www.w3.org/WAI/standards-guidelines/wcag/

    Heroku Dev Center — https://devcenter.heroku.com/

    Cloudinary Documentation — https://cloudinary.com/documentation

Author

Stuart Carey
AI-Augmented Full-Stack Bootcamp – Individual Capstone Project
Declaration

This project is my own original work. AI tools were used strictly as development assistants. All architecture, security decisions, business logic, and implementation choices were designed, reviewed, and validated independently.
