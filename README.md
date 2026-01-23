<!-- ========================= -->
<!-- COVER BANNER -->
<!-- ========================= -->

<p align="center">
  <img src="docs/screenshots/cover-banner.png" style="max-width:1100px;width:100%;height:auto;border-radius:12px;">
</p>

<h1 align="center">ITMarket — AI-Augmented Full-Stack Django Marketplace</h1>

<p align="center">
  A secure, responsive marketplace for buying and selling modern technology products.
</p>

<p align="center">
  <a href="https://itmarket-app-208bb526531b.herokuapp.com">Live Site</a> •
  <a href="https://github.com/cstuart756/itmarket">Repository</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Django-4.2%20LTS-092E20?logo=django&logoColor=white">
  <img src="https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Bootstrap-5-7952B3?logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/Deployment-Heroku-430098?logo=heroku&logoColor=white">
  <img src="https://img.shields.io/badge/Media-Cloudinary-3448C5?logo=cloudinary&logoColor=white">
</p>

---

## Live Site (Heroku)

🔗 **https://itmarket-app-208bb526531b.herokuapp.com**

---

## Repository

🔗 **https://github.com/cstuart756/itmarket**

________________________________________

## Project Overview

ITMarket is a full-stack marketplace web application built with **Django 4.2 (LTS)**, **Python 3.11**, **Bootstrap 5**, and **Cloudinary**.

It enables users to register, authenticate, and manage marketplace products with secure, database-backed CRUD workflows and ownership-based access control.

The platform is designed for buying and selling modern technology products such as consoles, phones, tablets, laptops, desktops, gaming PCs, and accessories.

### Key Capabilities

•   Full-stack Django (MTV) architecture  
•   Secure authentication & authorisation  
•   Media uploads using Cloudinary (production-safe storage)  
•   Responsive UI across desktop, laptop, tablet, and mobile  
•   Cloud deployment with Heroku + Postgres  
•   Agile workflow using GitHub Issues + Projects (Kanban)  
•   AI-augmented engineering workflow (with manual validation)

This project satisfies the requirements of the **AI-Augmented Full-Stack Bootcamp — Individual Capstone Project**.

________________________________________

## Table of Contents

•   UX Design  
•   Wireframes  
•   Features  
•   Technologies Used  
•   Data Model  
•   User Stories (MoSCoW)  
•   Agile Methodology  
•   Automated Testing  
•   Version Control  
•   Deployment (Heroku)  
•   Bug Fix Log  
•   Screenshots  
•   Lighthouse Performance Audits  
•   Project Management  
•   AI-Assisted Development  
•   Future Features & Roadmap  
•   References  
•   Author  
•   Declaration  

________________________________________

## UX Design

### Design Goals

•   Clean, intuitive interface for buyers and sellers  
•   Fully responsive across desktop, laptop, tablet, and mobile  
•   Accessibility-aware design with clear navigation and readable forms  
•   Bright and vivid colour palette for visual engagement  
•   Consistent feedback messages for all user actions  

### Colour Scheme

| Purpose | Colour |
|------|------|
| Primary | `#FF2E63` |
| Secondary | `#08D9D6` |
| Dark Contrast | `#252A34` |
| Background | `#EAEAEA` |

### Typography

•   Google Font: **Poppins**  
•   Applied consistently to headings and body text  

________________________________________

## Wireframes

---

### Planning & User Flow Groups

![](docs/screenshots/wireframes/group.png)

![](docs/screenshots/wireframes/group0.png)

![](docs/screenshots/wireframes/group1.png)

![](docs/screenshots/wireframes/group2.png)

---

### Mobile Wireframes

![](docs/screenshots/wireframes/mobile.png)

![](docs/screenshots/wireframes/mobile0.png)

![](docs/screenshots/wireframes/mobile1.png)

---

### Tablet Wireframes

![](docs/screenshots/wireframes/tablet.png)

![](docs/screenshots/wireframes/tablet0.png)

![](docs/screenshots/wireframes/tablet1.png)

---

### Laptop Wireframes

![](docs/screenshots/wireframes/laptop.png)

![](docs/screenshots/wireframes/laptop0.png)

![](docs/screenshots/wireframes/laptop1.png)

---

### Desktop Wireframes

![](docs/screenshots/wireframes/desktop.png)

![](docs/screenshots/wireframes/desktop0.png)

![](docs/screenshots/wireframes/desktop1.png)


________________________________________

## Features

### Authentication & Authorisation

•   User registration, login, logout  
•   Authentication state reflected in navbar  
•   Ownership-based access control (only owners can edit/delete their products)

### Marketplace

•   View products in responsive card layout  
•   Create, update, and delete products (authenticated users)  
•   Category assignment and display  
•   Cloudinary-backed image uploads  
•   Primary image logic  
•   Search by title, description, category, or seller

### Notifications (Django Messages)

•   Registration confirmation  
•   Product create/update/delete confirmations  
•   Image upload/delete confirmations  

________________________________________

## Technologies Used

### Front-End

•   HTML5  
•   CSS3  
•   Bootstrap 5  
•   Google Fonts (Poppins)

### Back-End

•   Python 3.11  
•   Django 4.2 (LTS)  
•   Django ORM  

### Database

•   SQLite (development)  
•   Heroku Postgres (production)

### Media & Static

•   Cloudinary (media)  
•   Whitenoise (static files)

### Tools & Platforms

•   VS Code  
•   Git & GitHub  
•   Heroku  
•   Gunicorn  

________________________________________

## Data Model

### Product

•   owner → User  
•   category → Category (nullable)  
•   title, description, price  
•   created_at, updated_at

### Category

•   name (unique)  
•   slug (unique)  
•   created_at  

### ProductImage

•   product → Product  
•   uploaded_by → User  
•   image → CloudinaryField  
•   alt_text (field exists in model; not used for README images)  
•   is_primary  
•   created_at

### ERD

<img src="docs/erd.png" style="max-width:900px;width:100%;height:auto;">

### Relationships

•   User → Product (one-to-many)  
•   Category → Product (one-to-many)  
•   Product → ProductImage (one-to-many)  
•   User → ProductImage (one-to-many)

Primary image resolution is handled via ordering: `(-is_primary, -created_at)`.

________________________________________

## User Stories (MoSCoW Prioritisation)

Requirements were captured as user stories and prioritised using the MoSCoW framework.

### MUST HAVE — Core Marketplace Platform (Delivered)

**US-M1 — User Registration**  
As a visitor, I want to create an account so that I can access marketplace features.  
Acceptance: Registration form, secure account creation, clear validation, success message.

**US-M2 — User Login**  
As a registered user, I want to log in so that I can access protected functionality.  
Acceptance: Login page, secure validation, error messages, UI reflects login state.

**US-M6 — View Products**  
As a visitor, I want to browse products so that I can explore listings.  
Acceptance: Product list loads, responsive cards, clear details.

**US-M7 — Create Product**  
As a logged-in user, I want to create a product listing so that I can sell items.  
Acceptance: Auth-only access, validation, success message.

**US-M8 — Update Product**  
As a product owner, I want to edit my listing so that I can update details.  
Acceptance: Owner-only edit, prefilled form, validation, success message.

**US-M9 — Delete Product**  
As a product owner, I want to delete my listing so that I can remove items.  
Acceptance: Owner-only delete, confirmation page, success message.

**US-M11 — Upload Product Images**  
As a product owner, I want to upload images so buyers can see what I’m selling.  
Acceptance: Upload form, Cloudinary storage, image displayed.

**US-M12 — Primary Image**  
As a product owner, I want to set a primary image so my product has a main display.  
Acceptance: One primary per product, new primary replaces old.

### SHOULD HAVE — Enhancements (Next Iteration)

•   Product search  
•   Filtering by category and price  
•   Sorting by price or newest  
•   User profile page  

### COULD HAVE — Future Expansion

•   Product reviews & ratings  
•   Wishlist / favourites  
•   Messaging between users  
•   Email notifications  
•   Public REST API  

### WON’T HAVE — Out of Scope (Current Project)

•   Payments & checkout  
•   Shipping & order tracking  
•   Real-time chat  
•   Mobile app  
•   AI recommendations  

________________________________________

## Agile Methodology

•   GitHub Issues (user stories)  
•   GitHub Projects (Kanban)  
•   Workflow: Backlog → To Do → In Progress → Done  
•   Incremental delivery with traceable commits  

________________________________________

## Automated Testing

Django TestCase suite covering:

•   Models  
•   Views  
•   Permissions  
•   CRUD workflows  
•   Messages  
•   Image rules  

Run locally:

```bash
python manage.py test
Version Control

• Regular, incremental commits
• Meaningful commit messages
• .env excluded via .gitignore
• Secrets stored in Heroku Config Vars

Deployment (Heroku)
Platform

• Heroku web dyno
• Heroku Postgres
• Gunicorn
• Whitenoise
• Cloudinary

Steps

Create Heroku app

Add Heroku Postgres add-on

Set Config Vars: SECRET_KEY, DEBUG=False, DATABASE_URL, CLOUDINARY_URL

Connect GitHub repo (auto-deploy)

Run migrations and collect static

Verify production behaviour

Production Settings

• DEBUG=False
• Environment variables for secrets
• HTTPS enforced
• Secure cookies
• HSTS enabled

Bug Fix Log
Authentication Template Resolution

• Ensured TEMPLATES['DIRS'] includes BASE_DIR / "templates"
• Added templates/registration/login.html
• Wired django.contrib.auth.urls correctly

Result: Authentication pages render reliably locally and on Heroku.

Database Persistence

• Migrated from SQLite to Heroku Postgres
• Enforced DEBUG=False in production
• Used persistent DB storage

Result: Product and image data persists across dyno restarts.

## Screenshots

---

### Deployed Application

![](docs/screenshots/01-homepage-heroku.png)

![](docs/screenshots/herokulive.png)

![](docs/screenshots/homepage.png)

![](docs/screenshots/homepage0.png)

![](docs/screenshots/homepage1.png)

![](docs/screenshots/homepage2.png)

![](docs/screenshots/view-deployed.png)

---

### Authentication & User State

![](docs/screenshots/02-registration-page.png)

![](docs/screenshots/register0.png)

![](docs/screenshots/03-registration-confirmation.png)

![](docs/screenshots/04-login-page.png)

![](docs/screenshots/successful_login.png)

![](docs/screenshots/loggedin.png)

![](docs/screenshots/05-logged-in-state.png)

---

### Product CRUD Workflow

![](docs/screenshots/06-create-product.png)

![](docs/screenshots/add_product.png)

![](docs/screenshots/07-product-created-confirmation.png)

![](docs/screenshots/09-edit-product.png)

![](docs/screenshots/10-product-updated-confirmation.png)

![](docs/screenshots/12-product-deleted-confirmation.png)

![](docs/screenshots/product-listed.png)

---

### Media Uploads

![](docs/screenshots/upload_image.png)

![](docs/screenshots/image-loaded.png)

---

### Admin & Management

![](docs/screenshots/itmarket-admin.png)

![](docs/screenshots/admin-local.png)

![](docs/screenshots/admin-local0.png)

---

### Validation

![](docs/screenshots/html-validation.png)

![](docs/screenshots/css-validation.png)

![](docs/screenshots/javascript-validation.png)

---

### Lighthouse Performance Audits

![](docs/screenshots/lighthouse-desktop.png)

![](docs/screenshots/lighthouse-desktop0.png)

![](docs/screenshots/lighthouse-desktop1.png)

![](docs/screenshots/lighthouse-mobile.png)

![](docs/screenshots/lighthouse-mobile0.png)

![](docs/screenshots/lighthouse-mobile1.png)

---

### Responsive Design

![](docs/screenshots/mobile.png)

![](docs/screenshots/mobile0.png)

![](docs/screenshots/tablet.png)

![](docs/screenshots/tablet0.png)

![](docs/screenshots/laptop.png)

![](docs/screenshots/laptop0.png)

![](docs/screenshots/desktop.png)

---

### Project Management

![](docs/screenshots/kanban.png)


AI-Assisted Development

AI tools were used to:

• Generate Django boilerplate aligned to project goals
• Produce unit tests for CRUD and security
• Debug deployment and template resolution issues
• Improve UX implementation decisions
• Accelerate iteration while maintaining quality

All AI outputs were reviewed, adapted, and validated via automated tests and manual verification.

Future Features & Roadmap
Phase 1 — Marketplace Enhancements (Short Term)

• Advanced search & filtering (category, price range)
• Sorting (newest, price)
• Image gallery & lightbox
• User profile pages

Phase 2 — Community & Engagement (Mid Term)

• Reviews & ratings
• Wishlist / favourites
• Buyer ↔ seller messaging

Phase 3 — Platform Expansion (Long Term)

• Admin moderation dashboard
• Email notifications
• Public REST API

Out of Scope (Current Release)

• Payments & checkout (PCI compliance)
• Shipping & order tracking
• Real-time chat (WebSockets)
• Mobile app (iOS/Android)
• AI recommendations

References

• Django Docs — https://docs.djangoproject.com/

• Bootstrap Docs — https://getbootstrap.com/docs/

• Cloudinary Docs — https://cloudinary.com/documentation

• Heroku Dev Center — https://devcenter.heroku.com/

• WCAG Guidelines — https://www.w3.org/WAI/standards-guidelines/wcag/

Author

Stuart Carey
AI-Augmented Full-Stack Bootcamp — Individual Capstone Project

Declaration

This project is my own original work.

AI tools were used strictly as development assistants. All architecture, security decisions, business logic, and implementation choices were designed, reviewed, and validated independently.