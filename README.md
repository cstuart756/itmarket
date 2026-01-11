## Live Site (Heroku)
Deployed application: https://itmarket-app-208bb526531b.herokuapp.com/

ITMarket – AI-Augmented Full-Stack Django Web Application
Author: Stuart Carey
Programme: AI-Augmented Full-Stack Bootcamp — Individual Capstone Project
________________________________________
Project Overview
ITMarket is a full-stack marketplace web application developed using Django 4.2.1, Python 3.13.11, Bootstrap 5, and Google Fonts. The platform enables users to register, authenticate, and manage marketplace products using secure, database-backed CRUD functionality with ownership-based access control.
The application demonstrates:
•	Secure authentication and authorisation
•	Object-oriented data modelling with Django ORM
•	Responsive and accessible user interface design
•	Automated unit and integration testing
•	Cloud deployment using Heroku
•	AI-augmented software development workflows
The system is deployed to Heroku and version-controlled using GitHub, following industry-standard DevOps practices.
This project satisfies all requirements of the AI-Augmented Full-Stack Bootcamp Individual Capstone Project and demonstrates professional full-stack development competency.
________________________________________
UX Design
Design Goals
•	Provide a clean and intuitive interface for buyers and sellers
•	Ensure full responsiveness across desktop, tablet, and mobile devices
•	Maintain WCAG-compliant accessibility standards
•	Apply a bright and vivid colour palette for strong visual identity
•	Provide consistent navigation and clear user feedback
Layout & Interface Design
•	Navigation bar displaying authentication state
•	Card-based product listing layout
•	Centrally aligned authentication and product management forms
•	Feedback messages for all user actions (registration, login, CRUD operations)
Colour Scheme
•	Primary: #FF2E63 (Vibrant Pink)
•	Secondary: #08D9D6 (Bright Teal)
•	Dark Contrast: #252A34
•	Background: #EAEAEA
Typography
•	Google Font: Poppins
•	Used consistently across headings and body text
The interface follows a mobile-first design approach and is implemented using the Bootstrap 5 responsive grid system.
________________________________________
Features
Authentication & Authorisation
•	User registration
•	Secure login and logout
•	Login state reflected in navigation bar
•	Role-based access control
•	Ownership-based permissions for product management
Marketplace Functionality
•	View all products
•	Create new products
•	Update owned products
•	Delete owned products
•	Ownership-restricted CRUD operations
Notifications & Feedback
•	Registration confirmation
•	Login confirmation
•	Product created confirmation
•	Product updated confirmation
•	Product deleted confirmation
________________________________________
Technologies Used
Front-End
•	HTML5
•	CSS3
•	Bootstrap 5
•	Google Fonts
•	Responsive grid system
•	Accessible forms and navigation
Back-End
•	Python 3.13.11
•	Django 4.2.1
•	Django ORM
•	SQLite (development)
•	PostgreSQL (production)
Tools & Platforms
•	Visual Studio Code
•	Git & GitHub
•	Heroku
•	Gunicorn
•	Whitenoise
________________________________________
Database Design
Product Model
Field	Type	Description
owner	ForeignKey(User)	Product owner
title	CharField	Product title
description	TextField	Product description
price	DecimalField	Product price
created_at	DateTimeField	Auto timestamp
The data model is implemented using Django ORM with enforced ownership relationships, database migrations, and integrity constraints.
________________________________________
Agile Methodology
Epics
1.	User Authentication & Registration
2.	Marketplace CRUD Functionality
3.	Notifications & User Feedback
4.	UX Design & Responsiveness
5.	Deployment & Security
User Stories (MoSCoW Prioritisation)
Must Have
•	User registration and login
•	Product CRUD functionality
Should Have
•	Notifications and confirmation messages
Could Have
•	Admin dashboard
•	Product image uploads
Development followed an Agile workflow using incremental delivery, GitHub issue tracking, and feature-based commits.
________________________________________
Automated Testing
Testing Strategy
Automated testing is implemented using Django’s TestCase framework.
Coverage
•	Product model tests
•	CRUD view tests
•	Authentication tests
•	Ownership permission tests
•	Notification message tests
Test Execution
python manage.py test accounts
python manage.py test marketplace
python manage.py test
All tests pass successfully, validating application integrity and user workflows.
________________________________________
Version Control
Git Strategy
•	Incremental commits with meaningful messages
•	Feature-based development workflow
•	Full development lifecycle documented
Repository:
https://github.com/cstuart756/itmarket
Security
•	.env excluded from repository
•	Environment variables for secrets
•	DEBUG disabled in production
•	No credentials committed
________________________________________
Deployment
Platform
•	Heroku with PostgreSQL database
Deployment Workflow
1.	Create Heroku application
2.	Configure environment variables
3.	Disable DEBUG in production
4.	Deploy via GitHub integration
5.	Apply database migrations
6.	Verify production functionality
Static Files
•	Managed using Whitenoise
________________________________________
AI-Assisted Development
AI tools were strategically leveraged to:
•	Generate Django boilerplate code
•	Assist with automated unit tests
•	Debug application issues efficiently
•	Optimise front-end UX and layout
•	Improve development velocity
AI significantly improved development efficiency while all architectural and implementation decisions were reviewed and validated manually.
________________________________________
Responsiveness & Accessibility
•	Mobile-first design
•	Fully responsive grid layout
•	Accessible navigation and forms
•	Semantic HTML structure
•	WCAG-compliant contrast ratios
________________________________________
Future Enhancements
•	Product image uploads
•	Search and filtering
•	Admin moderation dashboard
•	Email notifications
•	User profiles
________________________________________
References
•	Django Documentation — https://docs.djangoproject.com
•	Bootstrap Documentation — https://getbootstrap.com/docs/5.3
•	Google Fonts — https://fonts.google.com
•	WCAG Accessibility Standards — https://www.w3.org/WAI/standards-guidelines/wcag/
•	Heroku Documentation — https://devcenter.heroku.com
________________________________________
Author
Stuart Carey
AI-Augmented Full-Stack Bootcamp — Individual Capstone Project
