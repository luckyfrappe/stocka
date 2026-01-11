# Stocka — A Modern Fashion Marketplace

Stocka is a modern fashion marketplace exploring alternative ways to engage with fashion.  
The platform combines **buying new**, **renting**, **buying pre-owned**, and **rental buyouts** into a single, thoughtful shopping experience focused on flexibility, longevity, and reduced waste.

Rather than treating fashion as strictly disposable or permanent, Stocka allows customers to choose how they want to engage with each item — whether that means owning it outright, using it temporarily, or keeping it after a rental period.

This project is built as an educational study project, demonstrating how a traditional e-commerce flow can be extended to support rental economies, circular fashion models, and sustainable design principles.

<!-- ![alt text](> _To be defined._ "Mockup image of Stocka marketplace on different devices") -->

<!-- 🔗 [**Live site**](https:> _To be defined._) -->

---

## Contents

- [User Experience (UX)](#user-experience-ux)
  - [Business Goals](#business-goals)
  - [Target Audience](#target-audience)
  - [Marketing Strategy](#marketing-strategy)
  - [User Stories](#user-stories)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Sitemap & Database Schema](#sitemap--database-schema)
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

---

## User Experience (UX)

### Business Goals

- Provide a **unified fashion platform** where users can **buy new**, **rent**, **purchase pre-owned**, or **keep items after rental** (buyout).
- Promote **sustainable fashion consumption** by offering flexible options without restricting user choice.
- Demonstrate how **rental, resale, and traditional e-commerce** can seamlessly coexist.
- Deliver a **clean, intuitive, and distraction-free shopping experience** focused on user decision-making.
- Establish a foundation for **personalized recommendations** based on user preferences and behaviors.

### Target Audience
Stocka is designed for fashion-forward, sustainability-conscious users who want flexible ways to enjoy clothing. Our primary audience includes:  

- **Age:** 18–30, fashion-savvy and tech-friendly  
- **Interests:** Sustainable fashion, circular economy, renting, reselling, eco-conscious shopping  
- **Behaviors:** Interested in trying new styles without commitment, willing to explore rental and pre-owned options, active online shoppers  
- **Values:** Flexibility, longevity, personalization, and reduced environmental impact

<!-- ### Marketing Strategy
Stocka’s marketing approach focuses on building awareness, trust, and engagement with users who care about sustainable fashion:

1. **Content Marketing**  
   - Blog posts highlighting rental trends, circular fashion, and sustainability tips
   - Social media content showcasing featured items, rental experiences, and pre-owned finds

2. **Social Media Marketing**  
   - **Platforms:** Instagram, TikTok, Pinterest  
   - **Strategies:** Visual campaigns, unboxing-style posts, influencer partnerships, interactive polls  

3. **Email Marketing**  
   - Newsletter with new arrivals, rental highlights, sustainability insights, and exclusive offers  
   - Automated sequences for new user onboarding, rental reminders, and purchase follow-ups  

4. **Search Engine Optimization (SEO)**  
   - Optimized product pages with relevant keywords such as "sustainable fashion marketplace," "clothing rental platform," and "pre-owned clothing online"  
   - Structured data for product availability, reviews, and rental options  

5. **Paid Advertising (Future)**  
   - Targeted social media and Google Ads campaigns focusing on eco-conscious fashion shoppers  
   - Retargeting for users who browse items without completing rentals or purchases   -->


### User Stories

All user stories are listed in the [**GitHub Project board**](https://github.com/users/luckyfrappe/projects/10).

---

## Design

### Color Scheme

> _To be defined._

### Typography

> _To be defined._

### Imagery

> _To be defined._

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

<summary>How it works page</summary>

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

<summary>FAQ's page</summary>

A well-organized FAQ page that addresses common questions and concerns. Questions will be hidden in collapsible sections for easy navigation on both desktop and mobile devices.

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

A detailed product page showcasing multiple images, descriptions, pricing options (Buy New, Rent, Buy Pre-Owned), and user reviews.

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

> _To be defined._

Wireframes will focus on:
- Product browsing
- Product detail views
- Rental / purchase option selection
- User account flows

### Sitemap & Database Schema

> _To be defined._

Initial planning will include:
- Product and image relationships
- Rental availability logic
- User interactions (favorites, orders, rentals)

---

## Features

### Core Features

- Browse fashion products by category and gender
- View detailed product pages with multiple images
- Choose between **Buy New**, **Rent**, or **Buy Pre-Owned** (when available)
- Favorites / wishlist functionality
- Basic cart and checkout flow (educational scope)

### Page-Specific Features

> _To be defined._

Planned pages include:
- Home
- Shop
- Product Detail
- Favorites
- About
- Values
- Locations
- Newsroom
- Contact
- FAQs
- Legal pages (Terms, Privacy, Returns)
- Custom 404

### Future Implementations

- Rental extensions and buy-out options
- Smart product recommendations
- Availability-aware rental logic
- Sustainability insights (e.g. estimated reuse impact)
- User rental history and item lifecycle tracking

---

### Accessibility Considerations

- Semantic HTML structure
- Accessible form labels and inputs
- Alt text for all images
- Keyboard navigable components
- Sufficient color contrast

---

## Technologies Used

### Languages Used

- **HTML**
- **CSS**
- **JavaScript**
- **Python**

### Frameworks, Libraries & Programs Used

- **[Git & GitHub](https://github.com/)** – Version control and hosting.
- **[Google DevTools](https://developer.chrome.com/docs/devtools/)** – Development & debugging.
<!-- - **[FigJam](https://www.figma.com/figjam/)** - Flowcharts -->
<!-- - **[Font Awesome](https://fontawesome.com/)** – Icons via CDN. -->
<!-- - **[Favicon.io](https://favicon.io/)** – Favicon generation. -->
<!-- - **[TinyPNG](https://tinypng.com/)** – Image optimization. -->
- **[Polypane](https://polypane.app/)** – Responsive device previews.
<!-- - **[Autoprefixer](https://autoprefixer.github.io/)** – Vendor prefixes for CSS. -->
<!-- - **[HTML Validator](https://validator.w3.org/)** – Markup Validation Service. -->
<!-- - **[CSS Validator](https://jigsaw.w3.org/css-validator/)** – CSS Validation Service. -->
<!-- - **[WAVE](https://wave.webaim.org/)** – Web Accessibility Evaluation Tools. -->
<!-- - **[JSHint](https://jshint.com/)** – JavaScript validation. -->
<!-- - **[ESLint](https://eslint.org/)** – JavaScript linter for finding and fixing code issues, enforcing consistent style, and preventing bugs. -->
- **[Prettier](https://prettier.io/)** – Code formatter that ensures consistent style across your JavaScript, CSS, JSON, and other files.
<!-- - **[Canva](https://www.canva.com/create/logos/)** was used for creating the collage assets and favicon design. -->
- **[ChatGPT (OpenAI)](https://chat.openai.com/)** and **[Gemini (Google)](https://gemini.google.com/)** were used for generating service descriptions, debugging support, exploring different solutions, and clarifying code concepts.
- The virtual environment was installed following Code Institute’s setup instructions.
- **[Django](https://www.djangoproject.com/)** – High-level Python web framework powering the backend of the application.  
<!-- - **[Gunicorn](https://gunicorn.org/)** – Python WSGI HTTP server for running Django apps in production. -->
<!-- - **dj-database-url** – Simplifies database configuration in Django by allowing the database URL to be parsed and set as Django settings.   -->
<!-- - **psycopg2** – Adapter for Python, enabling Django to communicate with a PostgreSQL database. -->
<!-- - **[WhiteNoise](http://whitenoise.evans.io/en/stable/)** – Simplifies static file serving in Django for production environments.   -->
- **[PostgreSQL](https://www.postgresql.org/)** – Open-source relational database system used for storing structured application data.  
- **[django-allauth](https://django-allauth.readthedocs.io/en/latest/)** – Integrated Django app for authentication, registration, and account management with support for social logins and email verification.
<!-- - **[Google Workspace (Gmail SMTP)](https://mail.google.com/)** – Configured to send transactional emails through Gmail’s secure SMTP service, used for account verification, password resets, and contact forms. -->
<!-- - **[FilePond](https://pqina.nl/filepond/)** – Used for modern, user-friendly file uploads with drag-and-drop support, live image previews, and file validation. Configured to behave like a regular Django file input using `storeAsFile: true`, so uploaded files are submitted together with the form. -->

---

## Deployment

> _To be defined._

---

## Local Development

> _To be defined._

---

## Cloning and Forking

### Cloning



### Forking



### Local vs Deployed Version

---

## Agile Development Process

This project follows an Agile-inspired workflow using **GitHub Projects**.  
User stories, tasks, and bugs were tracked on a Kanban board with columns for **Backlog**, **Todo**, **In progress**, and **Done**.  

Features were prioritized using a simplified **MoSCoW approach**:  
- **Must Have:** Core marketplace functionality (browse, buy, rent, buyout).  
- **Should Have:** Enhancements like search, filters, and wishlists.  
- **Could Have:** Optional UI improvements or future features.  
- **Won’t Have:** Deferred or stretch goals for later iterations.  

This setup provided clear visibility, focus on priorities, and iterative progress during development.

---

## Testing

See **[TESTING.md](TESTING.md)** for test cases, known issues, and resolved bugs.

---

## Credits

### Data Sources

- [Vibrent Clothes Rental Dataset (Kaggle)](https://www.kaggle.com/datasets/kaborg15/vibrent-clothes-rental-dataset?select=images)  
- Academic reference:  
  *[A Dataset for Adapting Recommender Systems to the Fashion Rental Economy](https://dl.acm.org/doi/10.1145/3640457.3688174)* (RecSys 2024)  

**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### Acknowledgments


Website style and feel were inspired by:

- [Framer Marketplace - Nivest Template](https://www.framer.com/marketplace/templates/nivest/)

This project is developed as part of a full-stack web development course and serves as a learning and experimentation platform.

[Back to Top](#stocka-—-a-modern-fashion-marketplace)