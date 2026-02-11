# Stocka — A Modern Fashion Marketplace

Stocka is a modern fashion marketplace exploring alternative ways to engage with fashion.  
The platform combines **buying new**, **renting**, **buying pre-owned**, and **rental buyouts** into a single, thoughtful shopping experience focused on flexibility, longevity, and reduced waste.

Rather than treating fashion as strictly disposable or permanent, Stocka allows customers to choose how they want to engage with each item — whether that means owning it outright, using it temporarily, or keeping it after a rental period.

This project is built as an educational study project, demonstrating how a traditional e-commerce flow can be extended to support rental economies, circular fashion models, and sustainable design principles.

<!-- ![alt text](> _To be defined._ "Mockup image of Stocka marketplace on different devices") -->

<!-- 🔗 [**Live site**](https:> _To be defined._) -->

Test Checkout (Stripe Sandbox)

This store uses **Stripe’s test environment** to simulate the purchasing process.  
No real payments are processed and **no orders will be fulfilled**.

**Use the Stripe dummy card details below**

- **Card number:** `4242 4242 4242 4242`
- **Expiration date:** Any future date (`MM/YY`)
- **CVC:** Any 3 digits
- **Postcode:** Any 5 digits

No money will be charged or transferred — this is a **simulated checkout** for testing and demonstration purposes only.

> ⚠️ **Important**
> - Do **not** use a real card as this integration is in test mode only.
> - This is a **fictional / student project**  
> - Orders placed here will **not** be delivered

For more information about Stripe test payments, see the official documentation:

👉 [Stripe Test Cards & Payments](https://stripe.com/docs/testing)


## Contents

- [User Experience (UX)](#user-experience-ux)
  - [Business Goals](#business-goals)
  - [Scope](#scope)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Database Schema & Data Engineering](#database-schema--data-engineering)
- [Features](#features)
  - [Core Features](#core-features)
  - [Page-Specific Features](#page-specific-features)
  - [Future Implementations](#future-implementations)
  - [Accessibility Considerations](#accessibility-considerations)
- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
- [Deployment](#deployment)
- [Local Development](#local-development)
  - [Cloning and Forking](#cloning-and-forking)
    - [Cloning](#cloning)
    - [Forking](#forking)
    - [Local vs Deployed Version](#local-vs-deployed-version)
- [Agile Development Process](#agile-development-process)
- [Testing](#testing)
- [Credits](#credits)
  - [Data Sources](#data-sources)
  - [Acknowledgments](#acknowledgments)


## User Experience (UX)

### Business Goals

- Provide a **unified fashion platform** where users can **buy new**, **rent**, **purchase pre-owned**, or **keep items after rental** (buyout).
- Promote **sustainable fashion consumption** by offering flexible options without restricting user choice.
- Demonstrate how **rental, resale, and traditional e-commerce** can seamlessly coexist.
- Deliver a **clean, intuitive, and distraction-free shopping experience** focused on user decision-making.
- Establish a foundation for **personalized recommendations** based on user preferences and behaviors.

### Scope

This project focuses on demonstrating a **fashion marketplace** that supports
buying, renting, pre-owned purchasing, and rental buyouts within a single
e-commerce flow.

The implementation prioritizes **core user journeys, UX clarity, and system
structure** over commercial completeness. Real payments, logistics, and
automation are intentionally excluded as this is an educational project.

### Target Audience
Stocka is designed for fashion-forward, sustainability-conscious users who want flexible ways to enjoy clothing. Our primary audience includes:  

- **Age:** 18–30, fashion-savvy and tech-friendly  
- **Interests:** Sustainable fashion, circular economy, renting, reselling, eco-conscious shopping  
- **Behaviors:** Interested in trying new styles without commitment, willing to explore rental and pre-owned options, active online shoppers  
- **Values:** Flexibility, longevity, personalization, and reduced environmental impact

### User Stories

All user stories are listed in the [**GitHub Project board**](https://github.com/users/luckyfrappe/projects/10).


## Design

### Color Scheme




### Typography


### Imagery


### Wireframes

<details>

<summary>Home Page</summary>

A clean, modern homepage featuring a full-width hero with headline and CTA, followed by program highlights (Buy New, Rent, Pre-owned) and a mini-catalogue of featured items (popular or curated products). On mobile, the hero scales, product cards stack, buttons stay tappable, and carousels are swipeable.

![Desktop Home Page](documentation/images/wireframes/desktop-home.png)
![Mobile Home Page](documentation/images/wireframes/mobile-home.png)

</details>

<details>

<summary>Shop All Page</summary>

A grid-based product listing page with filtering and sorting options. The layout adapts to different screen sizes, ensuring easy navigation and product discovery on both desktop and mobile devices.

Since real stock levels are not implemented, sizes in filters are showing real stock for pre-owned items only. Ideally it should show sizes available across all options (new, rent, pre-owned).

![Desktop Home Page](documentation/images/wireframes/desktop-all.jpg)
![Mobile Home Page](documentation/images/wireframes/mobile-all.jpg)

</details>

<details>

<summary>Navbar</summary>

A responsive navigation bar that collapses into a hamburger menu on mobile devices. The navbar includes links to key sections of the site, a search bar, and user account access.

![Desktop Home Page](documentation/images/wireframes/desktop-navbar.png)
![Mobile Home Page](documentation/images/wireframes/mobile-navbar.png)
</details>

<details>

<summary>About Page</summary>

A clean, informative about page that highlights the brand's mission.

![Desktop Home Page](documentation/images/wireframes/desktop-about.png)
![Mobile Home Page](documentation/images/wireframes/mobile-about.png)
</details>

<details>

<summary>Concept page</summary>

A step-by-step guide explaining the process of buying, renting, and purchasing pre-owned items. 
![Desktop Home Page](documentation/images/wireframes/desktop-how.png)
![Mobile Home Page](documentation/images/wireframes/mobile-how.png)
</details>

<details>

<summary>Returns & Refunds</summary>

A clear and concise returns and refunds page that outlines the policies and procedures for returning items. 

![Desktop Home Page](documentation/images/wireframes/desktop-return.png)
![Mobile Home Page](documentation/images/wireframes/mobile-return.png)
</details>

<details>

<summary>FAQ's page (not implemented)</summary>

A well-organized FAQ page that addresses common questions and concerns. Questions will be hidden in collapsible sections for easy navigation on both desktop and mobile devices.

To save time, this page is not implemented in the project but wireframes have been created.

![Desktop Home Page](documentation/images/wireframes/desktop-faq.png)
![Mobile Home Page](documentation/images/wireframes/mobile-faq.png)
</details>

<details>

<summary>Terms of Service page</summary>

A comprehensive terms of service page that outlines the legal agreements between the user and the platform. 

![Desktop Home Page](documentation/images/wireframes/desktop-terms.png)
![Mobile Home Page](documentation/images/wireframes/mobile-terms.png)
</details>

<details>

<summary>Privacy page</summary>

A comprehensive privacy page that outlines the legal agreements between the user and the platform. 

![Desktop Home Page](documentation/images/wireframes/desktop-privacy.png)
![Mobile Home Page](documentation/images/wireframes/mobile-privacy.png)
</details>

<details>

<summary>Contact page</summary>

A user-friendly contact page featuring a form for inquiries and support requests.

![Desktop Home Page](documentation/images/wireframes/desktop-contact.png)
![Mobile Home Page](documentation/images/wireframes/mobile-contact.png)
</details>

<details>

<summary>Sustainability page</summary>

A dedicated sustainability page highlighting the brand's commitment to eco-friendly practices and circular fashion principles.

![Desktop Home Page](documentation/images/wireframes/desktop-sustainability.png)
![Mobile Home Page](documentation/images/wireframes/mobile-sustainability.png)
</details>

<details>

<summary>Values page</summary>

A dedicated values page highlighting the brand's commitment to eco-friendly practices and circular fashion principles.

![Desktop Home Page](documentation/images/wireframes/desktop-values.png)
![Mobile Home Page](documentation/images/wireframes/mobile-values.png)
</details>

<details>

<summary>Product detail page</summary>

A detailed product page showcasing multiple images, descriptions and pricing options (Buy New, Rent, Buy Pre-Owned).

![Desktop Home Page](documentation/images/wireframes/desktop-details.png)
![Mobile Home Page](documentation/images/wireframes/mobile-details.png)
</details>

<details>

<summary>Bag drawer</summary>

A slide-out bag drawer that provides a quick overview of selected items, quantities, and total cost. 

![Desktop Home Page](documentation/images/wireframes/desktop-bag.png)
![Mobile Home Page](documentation/images/wireframes/mobile-bag.png)
</details>

<details>

<summary>Bag review page</summary>

A dedicated bag review page that allows users to review their selected items, adjust quantities, and proceed to checkout.

![Desktop Home Page](documentation/images/wireframes/desktop-adjust.png)
![Mobile Home Page](documentation/images/wireframes/mobile-adjust.png)
</details>

<details>

<summary>Checkout page</summary>

A streamlined checkout page that collects shipping, payment, and rental details (borrowed from Code Insitute eCommerce walkthrough).

![Desktop Home Page](documentation/images/wireframes/desktop-checkout.png)
![Mobile Home Page](documentation/images/wireframes/mobile-checkout.png)
</details>

<details>

<summary>Thank you page</summary>

A confirmation page that thanks users for their purchase or rental and provides order details.

![Desktop Home Page](documentation/images/wireframes/desktop-thanks.png)
![Mobile Home Page](documentation/images/wireframes/mobile-thanks.png)
</details>

<details>

<summary>User account pages</summary>

A set of user authentication and account management pages will be powered by django-allauth templates, including login, registration, password reset, and profile management using crispy-forms for styling and adjusted to suit the site design.

</details>

<details>

<summary>My profile</summary>

A user profile page where users can view and manage their personal information and order history.

![Desktop Home Page](documentation/images/wireframes/desktop-profile.png)
![Mobile Home Page](documentation/images/wireframes/mobile-profile.png)

</details>

<details>

<summary>Subscriptions</summary>

A subscriptions management page where users can view and manage their subscriptions.

![Desktop Home Page](documentation/images/wireframes/desktop-subscriptions.png)
![Mobile Home Page](documentation/images/wireframes/mobile-subscriptions.png)

</details>

<details>

<summary>Product management</summary>

Product management pages will be borrowed from Code Insitute eCommerce walkthrough with adjustments for the project.

</details>

<details>

<summary>Favorites</summary>

A favorites / wishlist page where users can view and manage their favorite items.

![Desktop Home Page](documentation/images/wireframes/desktop-favorites.png)
![Mobile Home Page](documentation/images/wireframes/mobile-favorites.png)

</details>

Wireframes will focus on:
- Product browsing
- Product detail views
- Rental / purchase option selection
- User account flows

### Database Schema & Data Engineering

![Database Schema](documentation/images/database/erd-1.png)

The Stocka database is built to support a flexible, scalable marketplace. While the system is centered around a core `Product` model, the most critical part of the work was transforming and structuring over 18,000 rows of semi-structured data from the Vibrent Kaggle Dataset into a clean, relational format.

<details>

<summary>The Challenge: Structuring Semi-Structured Data</summary>

The original dataset stored key product information as fragmented string-based lists (for example: `outfit_tags = "['Yellow', 'Silk']"` and `tag_categories = "['Color', 'Material']"`).  
To convert this into a searchable and extensible system, an `AttributeType` and `AttributeValue` model structure was introduced.

This approach pairs each category with its corresponding value and connects them to products through a dedicated `ProductAttribute` join table. The result is a normalized data model that remains flexible while avoiding duplication and hard-coded logic.

</details>

<details>

<summary>Import Script (`import_data.py`)</summary>

This script acts as the structural backbone of the data layer, responsible for assembling the full product graph. Successfully connected 15,000+ products with over 150,000 attribute relations and their associated images.

This step established the foundational structure on which all filtering, categorization, and future features are built.

Note: The `time_created` field was not populated during this initial import so the patch script was created to update this field.

</details>

<details>

<summary>Date creation Patch (`patch_time.py`)</summary>

Restored accurate creation dates for all 15,649 products, enabling correct “Newest Arrivals” sorting without reprocessing the full dataset.

</details>

<details>

<summary>Data Architecture & Integrity</summary>

The product database is structured as a flat-file inventory system, mirroring the source outfits.csv data. In this model, every physical item is treated as a unique entity with its own SKU, even if they share the same product name. This approach was intended to maintain 1:1 traceability of rental assets. However, in current state it is used as product catalog only and in the catalog view, I utilized PostgreSQL’s .distinct('name') method to group identical items, preventing visual clutter. This does not reflect actual stock levels or availability for specific sizes for new and rentals. Future iterations will involve refactoring into a Parent-Child (Product-Variant) model to better handle stock and size availability.

</details>

## Features

This website uses CRUD for some features (Create, Read, Update, Delete) to manage products and favorites.

### Core Features

- Responsive navigation bar with:
  - Logo linking to home
  - Search bar
  - Links to key pages 
    - Shop
      - Browse All
      - Categories
    - Concept
    - Company
      - About
      - Values
      - Sustainability
      - FAQs
      - Contact
  - User account access (login, profile)
  - Bag icon with item count
  - Hamburger menu on mobile
  - Sticky behavior on scroll
  - Favorites / wishlist access
- View detailed product pages with:
  - Multiple images
  - Description and pricing options
- Select engagement options per product:
  - Buy New
  - Rent (when available)
  - Buy Pre-Owned (when available)
- Favorites / wishlist view
- Shopping bag with add, remove, and quantity adjustment
- Subscription management (active)
  - Rental-specific flows (user-facing):
    - Rental period selection at checkout
    - Rental Page Actions:
      - **Extend Rental**: Opens modal asking how many weeks to extend; quick-select buttons for 1, 2, or 3 weeks; checkout new order; updates rental end date & total price
      - **Mark as Returned**: Opens confirmation modal ("I confirm I have posted the item"); after confirmation, rental is removed from active rentals
      - **Keep Item (Buyout)**: Displays buyout price; allows user to convert rental into purchase
      - **Risk-Free Rental**: Return item within allowed window if size does not suit, no penalty
- Secure checkout using Stripe (test mode only)
- Order confirmation and thank-you pages
- User account management:
  - Login, logout, password reset
  - Profile management
  - View order & rental history
- Footer links duplicated for easy access:
  - Home, Shop, About, Concept, Contact, FAQs, Returns & Refunds, Privacy, Terms of Service
- Notifications for user actions (success, error messages)
- Custom 404 and 500 error pages with return-to-home buttons
- Concept page explaining buying, renting, and buyout processes
- Side bar for Info / Concept pages
- Dynamic sustainability image stays fixed on page
- Filters for browse/shop page remain sticky


### User Feature Access

| Feature | Guest | Registered User |
|---------|-------|-----------------|
| Home page | ✅ Visible | ✅ Visible |
| About page | ✅ Fully accessible | ✅ Fully accessible |
| Shop / Browse products | ✅ Visible | ✅ Visible |
| Search, filter & sort products | ✅ Can search | ✅ Can search |
| Product detail page | ✅ Viewable | ✅ Viewable |
| Bag drawer (quick bag preview) | ✅ Accessible | ✅ Accessible |
| Add items to bag | ⚠️ Only new and pre-owned items | ✅ Can add items |
| Favorites / wishlist | ⚠️ Prompted to log in | ✅ Can add, view & manage |
| Rent items | ⚠️ Prompted to log in | ✅ Can rent |
| Add products | ⚠️ Not visible for guests or registered users | ⚠️ Visible to admins only |
| Edit products | ⚠️ Not visible for guests or registered users | ⚠️ Visible to admins only |
| Delete products | ⚠️ Not visible for guests or registered users | ⚠️ Visible to admins only |
| Buy new items | ✅ Can purchase | ✅ Can purchase |
| Buy pre-owned items | ✅ Can purchase | ✅ Can purchase |
| Extend active rentals | ❌ Not allowed | ✅ Can extend |
| Rental buyout (keep item) | ❌ Not allowed | ✅ Can buy out |
| Mark rental as returned | ❌ Not allowed | ✅ Can confirm posted item |
| Checkout (Stripe test mode) | ✅ Can checkout | ✅ Can checkout |
| Thank you / order confirmation page | ✅ Viewable after checkout | ✅ Viewable after checkout |
| User account pages (auth) | ❌ Not accessible | ✅ Login, logout, password reset |
| User registration (auth) | ✅ Fully accessible | ❌ Not accessible |
| My profile | ❌ Not accessible | ✅ View & manage profile |
| View order & rental history | ❌ Not accessible | ✅ Can view history |
| Manage subscriptions | ❌ Not accessible | ✅ Available to subscribed users |
| Concept page | ✅ Fully accessible | ✅ Fully accessible |
| Sustainability page | ✅ Fully accessible | ✅ Fully accessible |
| Values page | ✅ Fully accessible | ✅ Fully accessible |
| Returns & Refunds page | ✅ Fully accessible | ✅ Fully accessible |
| Contact page | ✅ Fully accessible | ✅ Fully accessible |
| Privacy Policy page | ✅ Fully accessible | ✅ Fully accessible |
| Terms of Service page | ✅ Fully accessible | ✅ Fully accessible |
| Custom 404 page | ✅ Visible | ✅ Visible |
| Custom 500 page | ✅ Visible | ✅ Visible |


### Admin Feature Access

| Feature | Notes |
|---------|-------|
| Add / edit / delete products | ✅ Django Admin and website CRUD functionality |
| Manage product images and pricing options | ✅ Django Admin |
| View and manage orders | ✅ Django Admin |
| View and manage rentals | ✅ Django Admin |
| View user profiles and activity | ✅ Django Admin |
| Manage subscriptions | ✅ Django Admin |
| Manage static site content | ✅ Django Admin |
| Delete confirmation modal | ✅ Website functionality – shows prompt before deletion |


### Page-Specific Features

- **Home** — Hero section, featured categories
- **Shop** — Product listing with filtering and sorting  
- **Product Detail** — Image gallery, pricing options, engagement selection  
- **Favorites** — Saved items and quick access  
- **Bag / Checkout** — Quantity adjustment, checkout flow
- **Thank You** — Order confirmation details
- **Authentication** — Login, registration, password reset (django-allauth)
- **Product Management** — Add, edit, delete products (website)
- **Bag drawer** — Quick view of selected items
- **Profile** — User details, order history, rental overview  
- **Subscriptions** — Active and past subscription management  
- **Concept** — Explanation of buying, renting, buyout flows 
- **Sustainability** — Circular fashion principles, fixed dynamic image  
- **About** — Brand story and mission  
- **Values** — Brand values and vision  
- **Contact** — User inquiries and support form  
- **Notifications** — Success and error messages for user actions
- **Legal Pages** — Terms of Service, Privacy Policy, Returns & Refunds
- **Custom 404 / 500** — Friendly error pages, return-to-home buttons  


### Future Implementations

- Smart product recommendations (logic-based using tags, favorites, cart behavior)  
- Availability-aware rental logic  
- Sustainability insights (estimated reuse impact)  
- Users' rental history and lifecycle tracking  
- Enhanced admin rental management tools  
- Social media sharing options for products  
- Multi-language support  
- Advanced search with autocomplete  
- User notifications for rental due dates and promotions  
- Mobile app version for iOS and Android
- Overhauled FAQ page with accordion sections
- Overdue logic that updates server every day for rentals that have not been marked as returned after end date
- Better express item handling as separate flow instead of blocking all other items in bag
- Divide subscriptions page into active and past subscriptions for better UX
- Add sorting options to subscriptions page (newest, oldest, product name, overdue, etc.)
- A known limitation of the current prototype is the disconnect between the simulated size selection and actual stock availability for specific SKUs. A future refactoring of the database into a Parent-Child relationship (Product-Variant model). 

This would involve:
Product Model: Housing global attributes (description, base imagery).
Variant Model: Housing specific SKU data (exact size, availability, and physical condition for rentals/pre-owned items).

### Accessibility Considerations

- Semantic HTML structure  
- Accessible form labels and inputs  
- Alt text for all images  
- Keyboard navigable components  
- Sufficient color contrast 
- ARIA roles and attributes where necessary  
- Responsive design for various screen sizes


## Technologies Used

### Languages Used

- **HTML**
- **CSS**
- **JavaScript**
- **Python**

### Frameworks, Libraries & Programs Used

- **[Git & GitHub](https://github.com/)** – Version control and hosting.
- **[Google DevTools](https://developer.chrome.com/docs/devtools/)** – Development & debugging.
- **[FigJam](https://www.figma.com/figjam/)** - Flowcharts
- **[Font Awesome](https://fontawesome.com/)** – Icons via CDN. 
- **[Favicon.io](https://favicon.io/)** – Favicon generation.
- **[Polypane](https://polypane.app/)** – Responsive device previews.
- **[Autoprefixer](https://autoprefixer.github.io/)** – Vendor prefixes for CSS.
- **[HTML Validator](https://validator.w3.org/)** – Markup Validation Service.
- **[CSS Validator](https://jigsaw.w3.org/css-validator/)** – CSS Validation Service.
- **[JSHint](https://jshint.com/)** – JavaScript validation.
- **[Bootstrap 5](https://getbootstrap.com/)** – CSS framework for responsive, mobile-first front-end development.
- **[Adobe Color](https://color.adobe.com/)** – Color scheme generation and inspiration.
- **[Prettier](https://prettier.io/)** – Code formatter that ensures consistent style across your JavaScript, CSS, JSON, and other files.
- **[Lucidchart](https://www.lucidchart.com/)** – Database schema design and ERD creation.
- **[ChatGPT (OpenAI)](https://chat.openai.com/)** and **[Gemini (Google)](https://gemini.google.com/)** were used for generating service descriptions, debugging support, exploring different solutions, and clarifying code concepts.
- **[Django](https://www.djangoproject.com/)** – High-level Python web framework powering the backend of the application.  
- **[Gunicorn](https://gunicorn.org/)** – Python WSGI HTTP server for running Django apps in production.
- **dj-database-url** – Simplifies database configuration in Django by allowing the database URL to be parsed and set as Django settings.
- **psycopg2** – Adapter for Python, enabling Django to communicate with a PostgreSQL database.
- **[WhiteNoise](http://whitenoise.evans.io/en/stable/)** – Simplifies static file serving in Django for production environments.
- **[PostgreSQL](https://www.postgresql.org/)** – Open-source relational database system used for storing structured application data.  
- **[django-allauth](https://django-allauth.readthedocs.io/en/latest/)** – Integrated Django app for authentication, registration, and account management with support for social logins and email verification.
- **[Google Workspace (Gmail SMTP)](https://mail.google.com/)** – Configured to send transactional emails through Gmail’s secure SMTP service, used for account verification, password resets, and contact forms.
- **[Stripe](https://stripe.com/)** – Payment processing platform used to handle secure transactions during checkout (test mode only).
- **[Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)** – Django app for rendering forms in a DRY way with support for Bootstrap styling.
- **[Pillow](https://python-pillow.org/)** – Python Imaging Library (PIL) fork used for image processing tasks within Django.
- **[Django Storages](https://django-storages.readthedocs.io/en/latest/)** – Collection of custom storage backends for Django, used here to interface with cloud storage solutions.
- **[Heroku](https://www.heroku.com/)** – Cloud platform used for deploying and hosting the web application.
- **[VS Code](https://code.visualstudio.com/)** – Source-code editor used for writing and editing code.
- **[Figma](https://www.figma.com/)** – UI/UX design and prototyping tool used for creating wireframes and mockups.
- **[Kaggle](https://www.kaggle.com/)** – Platform for data science and machine learning, used here to source the Vibrent Clothes Rental Dataset.
- **[ngrok](https://ngrok.com/)** – Tool to expose local servers to the internet for testing webhooks and external integrations during development.


## Deployment

**Deployment Guide (Heroku + Django)**

This project is deployed using **Heroku**. Follow the steps below to host and configure the application.

**Create and Configure a Heroku App**

Create a Heroku account  
If you do not already have a Heroku account, create one first.

- Log in to the Heroku Dashboard:  
  https://dashboard.heroku.com/

Create a new app  
1. Click **New** in the top-right corner  
2. Select **Create new app**

App configuration  
- **App Name**: Enter a unique name for your project  
- **Region**: Choose either **United States** or **Europe**

Click **Create app** to finalize.

**Environment Variables (Config Vars)**

To allow the application to communicate with the database, environment variables must be configured in Heroku.

Steps  
1. Open your Heroku application  
2. Navigate to the **Settings** tab  
3. Locate **Config Vars** and click **Reveal Config Vars**  
4. Add the following variables:

| Key            | Value               |
|----------------|---------------------|
| `DATABASE_URL` | Your PostgreSQL URL |
| `SECRET_KEY` | Your Django Secret Key |

**Django Database Configuration**

In your envonmet file, add you database URL as follows:

```bash
os.environ['DATABASE_URL'] = 'your-database-url-here'
```

**Verify Database Connection**

Run the following command:

```bash
python3 manage.py showmigrations
```

If the connection is successful, a list of migrations will appear **without any checkmarks**, indicating a fresh database.

---

**Apply Database Migrations**

Migrate all database models to the new database:

```bash
python3 manage.py migrate
```

**Primary Data Import**

Populate the database with the core product catalog and metadata, including SKUs, descriptions, pricing, and attribute mapping.

```bash
python manage.py shell < dataset/import_data.py
```

Note  
Due to the large dataset size, this process may take significant time (up to several hours) depending on your database connection.  
Ensure your system does not enter sleep mode during execution or connection interruptions.

**Time-Based Data Patching**

After the primary import is complete, apply product creation updates to restore accurate timestamps for sorting and filtering purposes.:

```bash
python manage.py shell < dataset/patch_time.py
```

**Administrative Access**

Create a superuser to access the Django Admin panel:

```bash
python manage.py createsuperuser
```

Follow the on-screen prompts to set your username and password.  
The email field can be left blank.

**Add allowed hosts**

In your Django settings, add the Heroku app URL to the `ALLOWED_HOSTS` list:

```python
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'your-heroku-app-name.herokuapp.com',
]
```

**Deploying the app**

Assuming you have already initialized a Git repository in your project directory, committed your code and connected GitHub to your Heroku app, you can deploy the project using the following steps:

On your Heroku app dashboard, select the Deploy tab.

Here, we will connect our Heroku app to our GitHub repository and deploy our project. Scroll to the Deployment method and select GitHub

Search for your repository name, then click Connect

Click the Enable Automatic Deploys button. This will ensure that any time you push new code to your GitHub repository, Heroku will deploy the updated application.

Click Deploy Branch to deploy your project.

Watch the build log as it runs. You can view the build output in the application's Activity tab in the dashboard. This build may take several minutes to complete. If all goes well, the log should look like this when completed.

Click the Open app button at the top of the page to open your app. You can also access your app at the URL `https://your-heroku-app-name.herokuapp.com/`.

**S3 Bucket Configuration (Optional)**
If you are using an S3 bucket for static and media file storage, ensure that your AWS credentials and bucket information are set as environment variables in Heroku:

| Key                | Value                         |
|--------------------|-------------------------------|
| `USE_AWS`           | Set to any value to enable AWS S3 storage |
| `AWS_ACCESS_KEY_ID` | Your AWS Access Key ID        |
| `AWS_SECRET_ACCESS_KEY` | Your AWS Secret Access Key    |
| `AWS_STORAGE_BUCKET_NAME` | Your S3 Bucket Name          |
| `AWS_S3_REGION_NAME` | Your S3 Bucket Region (e.g., us-east-1) |

Ensure that your S3 bucket permissions are configured to allow public read access for static and media files.

**Uploading Static and Media Files**
If using S3, your static files will be automatically uploaded to the bucket when you run `collectstatic` during deployment or after deploying project on heroku. Ensure that your Django settings are configured to use S3 for static storage.

Media folder can be obtained here https://www.kaggle.com/datasets/kaborg15/vibrent-clothes-rental-dataset?select=images

I found it usefull to upload the media folder to the S3 bucket using the AWS CLI tool for large file uploads. You can do this with the following command:

If MAC os or Linux, you can install AWS CLI using Homebrew:

```bash
brew install awscli
```

Verify installation:

```bash
aws --version
```

Configure AWS credentials

```bash
aws configure
```

You’ll be asked for:
AWS Access Key ID
AWS Secret Access Key
Default region (e.g. eu-north-1)
Output format → json

Upload media folder to S3 bucket:

```bash
aws s3 sync media/ s3://boutique-stocka/media/ --acl public-read
```



## Local Development



## Cloning and Forking

### Cloning



### Forking



### Local vs Deployed Version


## Agile Development Process

This project follows an Agile-inspired workflow using **GitHub Projects**.  
User stories were tracked on a Kanban board with columns for **Backlog**, **Todo**, **In progress**, and **Done**.  

Features were prioritized using a simplified **MoSCoW approach**:  
- **Must Have:** Core marketplace functionality (browse, buy, rent, buyout).  
- **Should Have:** Enhancements like search, filters, and wishlists.  
- **Could Have:** Optional UI improvements or future features.  
- **Won’t Have:** Deferred or stretch goals for future iterations.  

This setup provided clear visibility, focus on priorities, and iterative progress during development.

### Sprints & Milestones

I have broken the project into sprints with buffer days to guide development and account for planning, debugging, and testing.  

The goal is to complete the full project within one month, while allowing a few extra days for unforeseen delays.

| Sprint | Dates | Focus / Milestone | Notes |
|--------|-------|-------------------|-------|
| Sprint 0 | Jan 6–Jan 12 | Project Planning | Initialize Django project, Wireframes, Database Schema, repo setup, initial research |
| Sprint 1 | Jan 13–Jan 19 | **Milestone 1: Core Product Browsing** | Browse all products, category filters, product detail pages, basic responsive UI, dataset adjustments, DB models, basic templates |
| Sprint 2 | Jan 20–Jan 26 | **Milestone 2: Checkout & User Account** | Bag, Orders, Authentication, Profile, Stripe test payments |
| Sprint 3 | Jan 27–Feb 1 | **Milestone 3: Rental Management** | Subscriptions, extend rentals, buyouts, mark returned, rental logic |
| Sprint 4 | Feb 2–Feb 7 | **Milestone 4: Stretch / Nice-to-Have Features** | Favorites/wishlist, optional recommendations, admin metrics |
| Sprint 5 | Feb 8–Feb 10 | Testing & Deployment | QA, bug fixing, cross-browser & mobile, deployment, documentation |

View all [Milestones](https://github.com/luckyfrappe/stocka/milestones)

Each sprint has been given buffer days to accommodate planning, debugging, or unexpected delays while staying within a one-month timeframe.


## Testing

See **[TESTING.md](TESTING.md)** for test cases, known issues, and resolved bugs.


## Credits

### Code Used

- **[Typewriter on Scroll](https://codepen.io/calebmisclevitz/pen/MGZVbd)** – Code snippet for typing text effect on about page.


### Data Sources

- [Vibrent Clothes Rental Dataset (Kaggle)](https://www.kaggle.com/datasets/kaborg15/vibrent-clothes-rental-dataset?select=images)  
- Academic reference:  
  *[A Dataset for Adapting Recommender Systems to the Fashion Rental Economy](https://dl.acm.org/doi/10.1145/3640457.3688174)* (RecSys 2024)  **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
-[Adobe Colors](https://stock.adobe.com/se/images/flat-lay-with-woman-fashion-accessories-in-yellow-colors-fashion-blog-summer-style-shopping-and-trends-idea/315730695) – Colors inspiration.

### Content

The textual content and platform descriptions for this fictional fashion marketplace were created in collaboration with AI tools such as ChatGPT and Gemini. Page copy, product descriptions, and UX narratives were AI-assisted and inspired by real-world fashion e-commerce and rental platforms.

### Media

#### General Imagery

- **[Woman in blue bralette holding sunglasses putting on her eyes](https://unsplash.com/photos/woman-in-blue-bralette-holding-sunglasses-putting-on-her-eyes-_KaMTEmJnxY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)** – Photo by Atikh Bana on Unsplash.
      

### Acknowledgments


Website style and feel were inspired by:

- [Framer Marketplace - Nivest Template](https://www.framer.com/marketplace/templates/nivest/)
- Most of the models for order, checkout, backend logic, and the overall site structure were inspired by **Boutique Ado** by Code Institute. This project acted as a skeleton for my site, and I adapted and adjusted aspects of it to create the project as it is now. [GitHub Repository – Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1)

This project is developed as part of a full-stack web development course and serves as a learning and experimentation platform.

[Back to Top](#stocka-—-a-modern-fashion-marketplace)