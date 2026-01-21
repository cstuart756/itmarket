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
---
## Wireframe Images

Wireframes are stored in `docs/screenshots/wireframes/`.

### Mobile
![Mobile Wireframe](docs/screenshots/wireframes/mobile.png)
![Mobile Wireframe Variant](docs/screenshots/wireframes/mobile0.png)
![Mobile Wireframe Variant](docs/screenshots/wireframes/mobile1.png)

### Tablet
![Tablet Wireframe](docs/screenshots/wireframes/tablet.png)
![Tablet Wireframe Variant](docs/screenshots/wireframes/tablet0.png)
![Tablet Wireframe Variant](docs/screenshots/wireframes/tablet1.png)

### Laptop
![Laptop Wireframe](docs/screenshots/wireframes/laptop.png)
![Laptop Wireframe Variant](docs/screenshots/wireframes/laptop0.png)
![Laptop Wireframe Variant](docs/screenshots/wireframes/laptop1.png)

### Desktop
![Desktop Wireframe](docs/screenshots/wireframes/desktop.png)
![Desktop Wireframe Variant](docs/screenshots/wireframes/desktop0.png)
![Desktop Wireframe Variant](docs/screenshots/wireframes/desktop1.png)

### Group Concepts
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

User Stories (MoSCoW Prioritisation)
The ITMarket platform was developed using a user-centred Agile approach. Requirements were captured as user stories and prioritised using the MoSCoW framework to define scope and delivery order.
________________________________________
MUST HAVE — Core Marketplace Platform (Delivered Scope)
These stories define the Minimum Viable Product (MVP) and were fully implemented.
Authentication & Security
US-M1 — User Registration
As a visitor
I want to create an account
So that I can access marketplace features
Acceptance Criteria
•	Registration form available
•	User account created securely
•	Validation errors shown clearly
•	Success confirmation message displayed
________________________________________
US-M2 — User Login
As a registered user
I want to log in to my account
So that I can access protected functionality
Acceptance Criteria
•	Login page available
•	Credentials validated securely
•	Error messages for invalid login
•	Login state reflected in UI
________________________________________
Marketplace Product Management (CRUD)
US-M6 — View Products
As a visitor
I want to browse marketplace products
So that I can explore available listings
Acceptance Criteria
•	Product list loads successfully
•	Responsive card layout
•	Product details displayed clearly
________________________________________
US-M7 — Create Product
As a logged-in user
I want to create a product listing
So that I can sell items
Acceptance Criteria
•	Product creation form available
•	Only authenticated users can create
•	Validation enforced
•	Success message displayed
________________________________________
US-M8 — Update Product
As a product owner
I want to edit my product listing
So that I can update its details
Acceptance Criteria
•	Only owner can edit
•	Form pre-filled with product data
•	Validation applied
•	Success message displayed
________________________________________
US-M9 — Delete Product
As a product owner
I want to delete my product listing
So that I can remove unwanted items
Acceptance Criteria
•	Only owner can delete
•	Confirmation page displayed
•	Product removed from database
•	Success message displayed
________________________________________
Media Uploads (Cloudinary)
US-M11 — Upload Product Images
As a product owner
I want to upload images for my product
So that buyers can see what I am selling
Acceptance Criteria
•	Image upload form available
•	Images stored via Cloudinary
•	Image displayed on product card
________________________________________
US-M12 — Primary Product Image
As a product owner
I want to set a primary image
So that my product has a main display image
Acceptance Criteria
•	Only one primary image per product
•	New primary replaces old
•	Primary shown on product card
________________________________________
SHOULD HAVE — Enhancements (Next Iteration)
These stories improve usability but are not required for MVP.
US-S1 — Product Search
As a user
I want to search for products
So that I can find items quickly
________________________________________
US-S2 — Product Filtering
As a user
I want to filter by category and price
So that I can narrow my results
________________________________________
US-S3 — Product Sorting
As a user
I want to sort by price or newest
So that I can browse efficiently
________________________________________
US-S4 — User Profile Page
As a user
I want a profile page
So that I can view my products
________________________________________
COULD HAVE — Future Expansion
These stories represent future platform growth.
US-C1 — Product Reviews
As a buyer
I want to leave reviews
So that sellers build reputation
________________________________________
US-C2 — Wishlist
As a user
I want to save favourite products
So that I can view them later
________________________________________
US-C3 — Messaging Between Users
As a buyer
I want to message sellers
So that I can ask questions
________________________________________
US-C4 — Email Notifications
As a user
I want email notifications
So that I don’t miss updates
________________________________________
WON'T HAVE — Out of Scope (Current Project)
These features were deliberately excluded due to scope, security, and compliance constraints.
•	Online payments & checkout
•	Shipping integration
•	Real-time chat
•	Mobile app
•	AI recommendations
________________________________________
Agile Tracking
User stories were managed using GitHub Issues and tracked via a Kanban board:
Backlog → To Do → In Progress → Done
Each story is traceable to:
•	Git commits
•	Test cases
•	Deployed features



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
![Herokulive](docs/screenshots/herokulive.png)
![Admin-heroku](docs/screenshots/admin-local.png)
![Admin-local](docs/screenshots/admin-local0.png)
![Itmarket-admin](docs/screenshots/itmarket-admin.png)
![Laptop0](docs/screenshots/laptop0.png)
![Desktop](docs/screenshots/desktop.png)
![Laptop](docs/screenshots/laptop.png)
![Mobile](docs/screenshots/mobile0.png)
![Tablet](docs/screenshots/tablet0.png)
![Tablet](docs/screenshots/tablet.png)
![Mobile](docs/screenshots/mobile.png)
![JavaScript-validation](docs/screenshots/javascript-validation.png)
![CSS-validation](docs/screenshots/css-validation.png)
![HTML-validation](docs/screenshots/html-validation.png)
![View-deployed](docs/screenshots/view-deployed.png)
![Homepage (Heroku)](docs/screenshots/01-homepage-heroku.png)
![Registration Page](docs/screenshots/02-registration-page.png)
![Registration Confirmation](docs/screenshots/03-registration-confirmation.png)
![Login Page](docs/screenshots/04-login-page.png)
![Logged In State](docs/screenshots/05-logged-in-state.png)
![Create Product](docs/screenshots/06-create-product.png)
![Product Created Confirmation](docs/screenshots/07-product-created-confirmation.png)
![Product Updated Confirmation](docs/screenshots/10-product-updated-confirmation.png)
![Product Deleted Confirmation](docs/screenshots/12-product-deleted-confirmation.png)
![Homepage](docs/screenshots/homepage.png)
![Homepage (Heroku)](docs/screenshots/homepage0.png)
![User Registration](docs/screenshots/register0.png)
![Registration Confirmation](docs/screenshots/successful_login.png)
![Logged In Homepage](docs/screenshots/loggedin.png)
![Create Product](docs/screenshots/add_product.png)
![Upload Product Image](docs/screenshots/upload_image.png)
![Product Listed](docs/screenshots/product-listed.png)
![Image Loaded](docs/screenshots/image-loaded.png)
![Homepage1](docs/screenshots/homepage1.png)
![Homepage2](docs/screenshots/homepage2.png)
![Lighthouse-desktop](docs/screenshots/lighthouse-desktop.png)
![Lighthouse-mobile](docs/screenshots/lighthouse-mobile.png)







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
    Future Features & Roadmap

The current version of ITMarket delivers a complete and fully functional marketplace MVP. However, due to time, scope, and security constraints associated with an academic capstone project, several enhancements were intentionally deferred for future iterations.

The following roadmap outlines the planned evolution of the platform.

Phase 1 — Marketplace Enhancements (Short Term)

These features improve usability and browsing efficiency and would be prioritised immediately in the next release cycle.

Advanced Search & Filtering

Filter by category, price range, and seller

Keyword-based full-text search

Combined filters (e.g. phones under £500)

Product Sorting

Sort by newest

Sort by price (low → high / high → low)

Sort by popularity (views or saves)

Image Gallery & Carousel

Multiple product images per listing

Lightbox image viewer

Swipe support on mobile

User Profile Page

Public seller profiles

View all products by a seller

Profile bio and avatar

Phase 2 — Community & Engagement Features (Mid Term)

These features build trust, reputation, and interaction between users.

Product Reviews & Ratings

Buyers can leave star ratings and written reviews

Seller reputation score

Review moderation

Wishlist / Favourites

Save products for later

Personal wishlist page

Wishlist notifications for price changes

User Messaging System

Secure buyer ↔ seller messaging

Message history

Notification badges

Phase 3 — Platform Expansion (Long Term)

These features turn ITMarket into a fully-fledged commercial marketplace platform.

Admin Moderation Dashboard

Approve or remove listings

Moderate user-generated content

Flag inappropriate products

Email Notifications

Registration confirmation

New messages

Product updates

Wishlist price alerts

REST API

Public API endpoints

Mobile app integration

Third-party integrations

Out of Scope for Current Release

The following features were intentionally excluded due to security, compliance, and infrastructure requirements that exceed the scope of an academic project:

Payments & Checkout

Requires PCI compliance

Fraud protection

Refund handling

Tax handling

Shipping & Order Tracking

Carrier integration

Label generation

Delivery tracking

Real-Time Chat

WebSocket infrastructure

Message delivery guarantees

Online/offline presence

Mobile App

iOS and Android builds

Push notifications

App store deployment

Technical Roadmap

Future technical improvements include:

Redis caching for product listings

Background jobs (Celery)

Image optimisation pipeline

Rate limiting and abuse prevention

Advanced logging and monitoring

GDPR data export and deletion tools

Product Vision

The long-term vision for ITMarket is to evolve into a secure, scalable, and community-driven technology marketplace with:

Trust-based seller reputation

Rich product discovery

Real-time communication

Mobile-first experience

API-driven ecosystem

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
