# Stocka — A Modern Fashion Marketplace

Stocka is a modern fashion marketplace exploring alternative ways to engage with fashion.
The platform combines buying new, renting, buying pre-owned, and rental buyouts into a single, thoughtful shopping experience focused on flexibility, longevity, and reduced waste.

Rather than treating fashion as strictly disposable or permanent, Stocka allows customers to choose how they want to engage with each item — whether that means owning it outright, using it temporarily, or keeping it after a rental period.

This project is built as an educational study project, demonstrating how a traditional e-commerce flow can be extended to support rental economies, circular fashion models, and sustainable design principles.

![alt text](documentation/images/user-journey/home.png "Mockup image of Stocka marketplace on different devices")

🔗 [**Live site**](https://boutique-stocka-748274888aff.herokuapp.com/)

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
- [The User Journey](#the-user-journey)
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

The color palette for Stocka is inspired by the natural tones of sustainable fashion and the modern, minimalist aesthetic of contemporary design. Brand colors are used strategically to create a cohesive and inviting atmosphere while allowing the products to take center stage. 

![Color Palette](documentation/images/design/color-theme.jpeg)

### Typography

The main font used across the site is **[Tenor Sans](https://fonts.google.com/specimen/Tenor+Sans)**, a versatile typeface that balances modernity with approachability. It is used for headings, navigation, and key UI elements to create a cohesive and stylish look.

The body text is set in **[Inter](https://fonts.google.com/specimen/Inter)**, a clean and highly legible font that ensures readability across all devices and screen sizes. This combination of fonts helps to establish a clear visual hierarchy while maintaining a friendly and accessible tone.

### Imagery

The design of Stocka focuses on a clean, modern aesthetic that allows the products to shine. The color palette is neutral and minimal, with soft accents to create a welcoming atmosphere. Typography is chosen for readability and style, complementing the overall brand identity.

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

### Database Schema & Data Engineering

![Database Schema](documentation/images/database/erd-1.png)

1. Product Management & Inventory
The core tables managing the catalog, including the normalized attribute system for handling complex product variations.

**Model: `Product`**
The central entity representing a stock item available for rent or sale.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK**, Unique ID |
| `sku` | CharField | Stock Keeping Unit (Unique Identifier) |
| `name` | CharField | Product Name |
| `description` | TextField | Full product details |
| `retail_price` | DecimalField | Original RRP |
| `price_per_week` | DecimalField | Rental cost per week |
| `time_created` | DateTimeField | Timestamp of creation (Patched via script) |

**Model: `ProductImage`**
Allows multiple images per product with ordering capabilities.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `product` | ForeignKey | Related **Product** |
| `image` | ImageField | Upload path / URL |
| `sort_order` | PositiveIntegerField | Determines display order in gallery |

**Model: `AttributeType`**
Defines the category of a product characteristic (e.g., "Color", "Material", "Size").
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `name` | CharField | Category Name |
| `slug` | SlugField | URL-friendly identifier |

**Model: `AttributeValue`**
Specific values within a category (e.g., "Red", "Silk").
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `attribute_type` | ForeignKey | Related **AttributeType** |
| `value` | CharField | Display value |
| `slug` | SlugField | URL-friendly identifier |

**Model: `ProductAttribute`**
Junction table linking Products to their Attributes (Many-to-Many relationship).
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `product` | ForeignKey | Related **Product** |
| `attribute_value` | ForeignKey | Related **AttributeValue** |

---

2. Commerce & Transactions
Tables handling the checkout process, order history, and recurring billing logic.

**Model: `Order`**
Represents a single checkout transaction containing customer details and payment status.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `order_number` | CharField | Unique, generated order reference |
| `userprofile` | ForeignKey | Linked **UserProfile** (Optional for guest checkout) |
| `full_name` | CharField | Billing Name |
| `email` | CharField | Billing Email |
| `phone_number` | CharField | Contact Number |
| `country` | CountryField | Standardized Country Code |
| `town_or_city` | CharField | City |
| `street_address1` | CharField | Address Line 1 |
| `street_address2` | CharField | Address Line 2 |
| `county` | CharField | County/State |
| `postcode` | CharField | Postal Code |
| `date` | DateTimeField | Transaction Timestamp |
| `order_total` | DecimalField | Total amount before taxes and discounts |
| `original_bag` | DecimalField | Original bag value |
| `delivery_cost` | DecimalField | Delivery cost |
| `grand_total` | DecimalField | Final amount charged |
| `stripe_pid` | CharField | Stripe Payment Intent ID |
| `payment_confirmed` | BooleanField | True if webhook/callback verified |

**Model: `OrderLineItem`**
Individual items within an order, capturing the specific state (price/size) at time of purchase.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `order` | ForeignKey | Parent **Order** |
| `product` | ForeignKey | Related **Product** |
| `product_size` | CharField | Selected Size |
| `quantity` | IntegerField | Count purchased |
| `lineitem_total` | DecimalField | Calculated subtotal |
| `purchase_type` | CharField | Choices: BUY, RENT, PREOWNED, etc. |
| `rental_period` | PositiveIntegerField | Duration (if rental) |
| `start_date` | DateField | Rental start (if applicable) |

**Model: `Subscriptions`**
Manages active rentals and recurring engagement.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `user` | ForeignKey | Related User |
| `product` | ForeignKey | Related Product |
| `order_line_item` | ForeignKey | Source transaction item |
| `start_date` | DateField | Subscription Start |
| `end_date` | DateField | Subscription End |
| `status` | CharField | Choices: active, returned, bought_out, overdue |
| `duration_weeks` | PositiveIntegerField | Total active weeks |

---

3. User Management & Engagement
Tables storing user preferences, profiles, and direct communications.

**Model: `UserProfile`**
Extended profile for storing default delivery information and order history.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `user` | OneToOneField | Links to standard Django User model |
| `default_full_name` | CharField | Saved default name |
| `default_phone_number` | CharField | Saved default phone |
| `default_street_address1`| CharField | Saved default address |
| `default_street_address2`| CharField | Saved default address line 2 |
| `default_town_or_city` | CharField | Saved default city |
| `default_county` | CharField | Saved default county |
| `default_postcode` | CharField | Saved default postcode |
| `default_country` | CountryField | Saved default country |
| `marketing_opt_in` | BooleanField | User consent for emails |

**Model: `Wishlist`**
Allows users to save products for later.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `user` | ForeignKey | Owner of the wishlist |
| `product` | ForeignKey | Saved Product |

**Model: `ContactMessage`**
Stores inquiries from the "Contact Us" form.
| Field | Type | Notes / Constraints |
| :--- | :--- | :--- |
| `id` | AutoField | **PK** |
| `name` | CharField | Sender Name |
| `email` | CharField | Sender Email |
| `subject` | CharField | Message Subject |
| `message` | TextField | Message Body |
| `created_at` | DateTimeField | Timestamp of message |
| `is_resolved` | BooleanField | Admin status flag |

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

## The User Journey

I designed the application to guide users through a circular fashion lifecycle: from discovery to checkout, and finally, to managing their rentals. The user journey is structured to be intuitive and flexible, allowing users to easily explore their options and make informed decisions about how they want to engage with each product.

This website uses CRUD for some features (Create, Read, Update, Delete) to manage products and favorites.

### Phase 1: Discovery & Navigation
*The entry point where users understand the brand value and find products.*

![alt text](documentation/images/user-journey/home.png "Mockup image of Stocka marketplace on different devices")

**Key Interactions:**
* **Responsive Navigation:** Users can navigate via a sticky navbar that adapts to mobile (hamburger menu) or desktop.

Hero image includes a clear headline and CTA to guide users to the shop.

1. The **Shop** dropdown provides quick access to product categories and featured collections. Categories are mirrored from the attribute system for consistency.
New arrivals turns query param to filter by creation date. I was inspired by modern e-commerce sites that prioritize ease of navigation and product discovery. At the top level, 3 main tags Men, Women, All Products are shown for quick access. Although website is made only for female products, men section is mostly for gifts to him.
On mobile device accordions are used for better UX. To save space on screen, only one accordion can be open at a time and the rest are flushed closed.
![alt text](documentation/images/user-journey/desktop-shop-dropdown.png "Mockup image of Stocka shop dropdown on desktop")
![alt text](documentation/images/user-journey/mobile-shop-dropdown.png "Mockup image of Stocka shop dropdown on desktop")

2. Concept link in navbar leads to a dedicated page explaining the buying, renting, and pre-owned flows.

3. Company dropdown includes About, Values, Sustainability and Contact pages to build brand trust. On desktop verison there are background images to make it more visually appealing.
![alt text](documentation/images/user-journey/companies-dropdown.png "Mockup image of Stocka company dropdown on desktop")
![alt text](documentation/images/user-journey/mobile-companies-dropdown.png "Mockup image of Stocka company dropdown on mobile")

**User Profile Access:** Users can access their profile the navbar. The profile page allows users to manage their personal information, view order history manage rentals.

If guest user, it displays Sign Up and Sign In options. If logged in:
Product Management link is only visible to admin users and leads to a page where they can add a product.
My Profile,
Subscriptions,
Logout

**Favorites / Wishlist:** A heart icon on product cards and detail pages allows users to view and manage their favorite items. This feature is designed to encourage users to save products they are interested in for later consideration. 

If user is not logged in, clicking the heart icon will prompt them to log in or create an account to access the wishlist feature. Once logged in, users can click the heart icon to add items to their favorites list, which can be accessed from their profile page.

If wishlist is empty, a friendly message encourages users to explore products and add favorites. User redirects back to the original page.

* **Search:** A global search bar allows for quick lookup of products by name or description.
Search bar expands on click to provide a larger input area and better UX on desktop. On mobile it stretches to full width for easier typing and attached to the bottom of hamburger menu for better accessibility.

![alt text](documentation/images/user-journey/desktop-search.png "Mockup image of Stocka search bar on desktop")
![alt text](documentation/images/user-journey/desktop-search-expand.png "Mockup image of Stocka search bar on mobile")

![alt text](documentation/images/user-journey/mobile-search-bar.png "Mockup image of Stocka search bar on mobile")
![alt text](documentation/images/user-journey/mobile-search-bar-expanded.png "Mockup image of Stocka search bar on mobile")

* **Brand Marquee:** A rotating banner on the homepage and Values page shows brands from the actual dataset to build authenticity and connection to real products.

![alt text](documentation/images/user-journey/marquee.png "Mockup image of Stocka brand marquee on different devices")

<details>

<summary>Home page content</summary>

Main content of the home page is to provoke interest and guide users to the shop. Berlow the hero section, there are 6 sections that highlight the core value propositions of the platform. 

1. **Spring collection** — A seasonal collection to entice users to prepare for spring. This sections displays products filtered by the "Spring" tag in the dataset. This is a dynamic section that can be updated with different tags for future seasons or promotions depending on the marketing strategy.
![alt text](documentation/images/user-journey/image.png "Mockup image of Stocka spring collection on different devices")
![alt text](documentation/images/user-journey/image-1.png)
2. **Stocka Loop banner** - A visual representation of the circular fashion lifecycle.
![alt text](documentation/images/user-journey/image-2.png)
![alt text](documentation/images/user-journey/image-3.png)
3. **Everydyay essentials** — A collection of staple items that are versatile and timeless. This section is filtered by the "Everyday" tag in the dataset, showcasing products that are perfect for daily wear and can be styled in various ways.
![alt text](documentation/images/user-journey/image-4.png)
![alt text](documentation/images/user-journey/image-5.png)
4. **Stocka Reuse banner** - A dynamic banner that highlights the environmental impact of reusing fashion items. On the right side of the banner is a image of smiling woman giving the good vibes of a happy customer. 
![alt text](documentation/images/user-journey/image-6.png)
![alt text](documentation/images/user-journey/image-7.png)
5. **Reviews carousel** - A rotating carousel of customer reviews to build trust and social proof. This section is designed to show real feedback from users, enhancing credibility and encouraging new customers to engage with the platform.
![alt text](documentation/images/user-journey/image-8.png)
![alt text](documentation/images/user-journey/image-9.png)
6. **FAQ section** - A preview of frequently asked questions to address common concerns and guide users to the full FAQ page for more information. (Full FAQ page is not implemented but wireframes have been created for future development.)
FAQ section uses accordions to keep the layout clean and organized, allowing users to easily find answers to their questions without overwhelming them with information.
![alt text](documentation/images/user-journey/image-10.png)
![alt text](documentation/images/user-journey/image-11.png)
**Footer:** The footer includes links to legal pages (Terms of Service, Privacy Policy, Returns & Refunds), contact, concept, FAQ, brand pages (About, Values, Sustainability) and social media icons. The footer is designed to be consistent across all pages, providing easy access to important information and additional resources. It also features 3 main shop links (Men, Women, All Products) for quick navigation.

Social links opens in a new tab to avoid losing the user’s place on the site.

The footer has 4 cards with advantages of shopping with Stocka, eco-friendly packaging; quick shipping, reliable brands and 30 day returns. This section is designed to reinforce the brand's value propositions and build trust with potential customers by highlighting key benefits of shopping with Stocka. Cards are stocking into 2 columns on tablet view and 1 column on mobile devices. 

At the very bottom of the footer, there is a small copyright notice and accepted credit card icons to build trust and provide reassurance about payment security.

![alt text](documentation/images/user-journey/image-12.png)
![alt text](documentation/images/user-journey/image-13.png)
![alt text](documentation/images/user-journey/image-14.png)
</details>

### Phase 2: Evaluation & Engagement
*How users interact with products and decide between Buying vs. Renting.*

<details>
<summary>Products page content</summary>
![alt text](documentation/images/user-journey/image-38.png)
![alt text](documentation/images/user-journey/image-39.png)

**Key Interactions:**
* **Dynamic Page Headers:** Depending on the applied filters, the Shop page header updates to reflect the current view (e.g., Products, New Arrivals, Category: Blouses, etc.). If several filters are applied, the header will show Filtered Results to avoid overwhelming the user with too much information. If search query is applied, it will show Search Results for "query" to provide clear feedback on the search action. If search query is applied with filters, it will display a message below "Refining your search for "bo" with selected filters." This dynamic header system is designed to provide users with clear context about their current browsing state, enhancing navigation and helping them understand how their actions are affecting the product display.
![alt text](documentation/images/user-journey/image-15.png)
![alt text](documentation/images/user-journey/image-16.png)
![alt text](documentation/images/user-journey/image-17.png)
![alt text](documentation/images/user-journey/image-18.png)
![alt text](documentation/images/user-journey/image-19.png)
![alt text](documentation/images/user-journey/image-37.png)
* **Filtering & Sorting:** On the Shop page, users can filter by attributes (color, material, size) and sort by name and price. User can also explore only New Arrivals by toggling the "New Arrivals" filter which sorts products by creation date and displays the latest 100 items. Filters are build dynamically based on the attributes in the dataset, allowing for flexibility and scalability as new products and attributes are added. On mobile devices, filters are accessible via a dedicated button that opens a full-screen filter menu for better usability. The clear buttons allow users to easily reset their filters and start a new search, enhancing the overall user experience and encouraging exploration. Brand section has in scrolling carousel to accommodate a large number of brands.
![alt text](documentation/images/user-journey/image-30.png)
![alt text](documentation/images/user-journey/image-32.png)
![alt text](documentation/images/user-journey/image-31.png)
![alt text](documentation/images/user-journey/image-34.png)
![alt text](documentation/images/user-journey/image-33.png)
* **Product Cards:** Each product card displays the name, price, and available options (Buy New, Rent, Buy Pre-Owned). Hovering over a card on desktop zooms in on the image for smoother browsing. Pre-owned price is calculated as a discount off the retail price. On mobile, there are 2 columns of product cards to optimize screen space.
![alt text](documentation/images/user-journey/image-23.png)
![alt text](documentation/images/user-journey/image-24.png)
* **Edit and Delete Buttons:** For admin users, Edit and Delete buttons are visible on product cards, allowing for quick management of inventory directly from the shop page. These buttons are hidden from regular users to prevent unauthorized access to product management features. If user clicks edit button, they are redirected to the product management page where they can update the product information. If user clicks delete button, a confirmation modal appears to prevent accidental deletion of products. This feature is designed to streamline the admin workflow while maintaining security and integrity of the product catalog.
![alt text](documentation/images/user-journey/image-25.png)
![alt text](documentation/images/user-journey/image-26.png)
* **Pagination:** The shop page is paginated to show 20 products per page, with navigation controls to move between pages. This ensures that the page loads quickly and remains user-friendly, even with a large inventory. Pagination controls are designed to be intuitive and accessible on both desktop and mobile devices, allowing users to easily navigate through the product catalog without feeling overwhelmed.
![alt text](documentation/images/user-journey/image-27.png)
![alt text](documentation/images/user-journey/image-28.png)
* **Back to top button:** A floating button appears on long pages, allowing users to quickly return to the top of the page. This feature enhances navigation and improves user experience.
![alt text](documentation/images/user-journey/image-29.png)
* **Products count:** The total number of products is displayed at the top of the shop page, providing users with a sense of the breadth of the inventory and encouraging exploration. This count updates dynamically based on applied filters and search queries, giving users real-time feedback on how their actions are affecting the product selection. If there are no products found based on the current filters or search query, a friendly message is displayed to encourage users to adjust their criteria and continue exploring the catalog.
![alt text](documentation/images/user-journey/image-35.png)
![alt text](documentation/images/user-journey/image-36.png)
</details>

<details>

<summary>Product Detail Page content</summary>

![alt text](documentation/images/user-journey/image-40.png)
![alt text](documentation/images/user-journey/image-41.png)
* **Product Description with Clickable Tags:** The product detail page features a comprehensive description along with clickable tags for attributes like color, material, and size. Clicking on a tag takes users to the shop page filtered by that specific attribute, allowing for easy exploration of similar products. This interconnected tagging system enhances product discovery and encourages users to browse the catalog based on their preferences.
![alt text](documentation/images/user-journey/image-42.png)
* **Flexible Consumption:** On the Product Detail Page, users are presented with a choice:
![alt text](documentation/images/user-journey/image-43.png)
    * **Buy New:** Standard purchase with select size and quantity.
    ![alt text](documentation/images/user-journey/image-44.png)
    * **Rent:** (Requires Login) Select a rental period.
    Users can still select size and quantity for rentals, but the price updates to reflect the rental cost based on the selected duration.
    ![alt text](documentation/images/user-journey/image-46.png)
    Rentals are allowed only for logged in users to ensure that the system can register products under user subscriptions page and track rental durations effectively. If user click rent button while not logged in, they are prompted to log in or create an account.
    ![alt text](documentation/images/user-journey/image-56.png)
    Rental period window provides 4 options (1-4 weeks) with clear pricing for each duration.
    ![alt text](documentation/images/user-journey/image-45.png)
    Start dates for rentals can be selected at least 3 days in advance to allow for processing and shipping. The date picker is designed to prevent selection earlier than 3 days from the current date.
    ![alt text](documentation/images/user-journey/image-47.png)
    End date and total rental cost are calculated based on the selected start date and rental duration.
    ![alt text](documentation/images/user-journey/image-48.png)
    * **Buy Pre-Owned:** A discounted purchase option for used items, clearly marked to differentiate from new purchases. This option allows users to make more sustainable choices while still enjoying the products they love.
    ![alt text](documentation/images/user-journey/image-49.png)
    The select size size and quantity are simulated to display 1 product and size available. In a real implementation, this would be based on actual stock levels for pre-owned items per size.
    * **Keep shopping:** Users can easily return to browsing.
    ![alt text](documentation/images/user-journey/image-50.png)
    * **FAQs:** A small faq section.
    ![alt text](documentation/images/user-journey/image-51.png)
    * **Edit/Delete Buttons:** For admin users, Edit and Delete buttons are visible on the product detail page. If user clicks edit button, they are redirected to the product management page. If user clicks delete button, a confirmation modal appears to prevent accidental deletion.
    ![alt text](documentation/images/user-journey/image-52.png)
    ![alt text](documentation/images/user-journey/image-53.png)
* **Visuals:** High-quality image galleries and detailed sizing guides.
![alt text](documentation/images/user-journey/image-54.png)
On mobile devices, the image gallery is designed to be swipeable with a small part of a next image visible to indicate more content, enhancing the user experience and encouraging interaction with the product visuals.
![alt text](documentation/images/user-journey/image-55.png)
* **Wishlist:** If user is logged in, they can favorite items for later consideration (saved to their profile). If not, clicking the heart icon prompts them to log in or create an account to access the wishlist feature. After adding to favorites, users receive a confirmation toast.
![alt text](documentation/images/user-journey/image-57.png)
![alt text](documentation/images/user-journey/image-58.png)
* **Adding to Bag:** After adding to the bag, appropriate toast messages are shown. Toasts are showing if new item added or updated quantity of an existing item in the bag. It also separetes rentals from new or pre-owned items. New items are separeted by size.
Rentals are separeted by size, rental period and start date to avoid confusion with regular purchases. This achieved by unique key generation for each type of item in the bag.
![alt text](documentation/images/user-journey/image-59.png)
![alt text](documentation/images/user-journey/image-60.png)
</details>

### Phase 3: The Transaction

<details>

<summary>Bag and Checkout content</summary>

![alt text](documentation/images/user-journey/image-67.png)
![alt text](documentation/images/user-journey/image-68.png)
**Key Interactions:**
* **Bag Drawer:** A non-intrusive side drawer allows users to check their total without leaving the shopping page.
If there are items in the bag, total price is calculated and displayed in the navbar for easy reference. If bag is empty, it shows no price.
![alt text](documentation/images/user-journey/image-61.png)
![alt text](documentation/images/user-journey/image-62.png)
![alt text](documentation/images/user-journey/image-63.png)
By clicking on the bag icon, users can access a detailed view of their selected items, quantities, and total cost. 
![alt text](documentation/images/user-journey/image-64.png)
If bag is empty, the bag drawer displays a friendly message encouraging users to shopping.
![alt text](documentation/images/user-journey/image-65.png)
It also displays a free delivery treshold message to encourage users to add more items to their bag for free shipping.
* **Bag adjustments:** Users can adjust quantities or remove items directly from the bag drawer, with real-time price updates. This allows for a seamless shopping experience without needing to navigate away from the current page.
![alt text](documentation/images/user-journey/image-66.png)
* **Total Calculation:** The bag calculates subtotals for each item, applies any discounts (e.g., pre-owned), and provides a clear total before checkout.
![alt text](documentation/images/user-journey/image-69.png)

**Checkout Process:** The checkout page collects necessary information for both purchases and rentals.
![alt text](documentation/images/user-journey/image-70.png)
![alt text](documentation/images/user-journey/image-71.png)

**Stripe Integration:** The checkout process is integrated with Stripe for secure payment processing. Users can enter their payment details, and the system handles the transaction while providing feedback on success or failure. 

**Save Info Option:** During checkout, users have the option to save their information for future purchases, which is stored in their user profile for a faster checkout experience next time. If user is not logged in, they are prompted to log in or create an account to access this feature. 
![alt text](documentation/images/user-journey/image-72.png)

**Order summary:** A summary of the order is displayed during checkout, including item details, rental periods (if applicable), and the total cost. This allows users to review their order before finalizing the purchase.
![alt text](documentation/images/user-journey/image-73.png)

**Thank You Page:** After a successful transaction, users are redirected to a thank you page that confirms their order and provides details about the next steps (e.g., shipping information, rental start dates, etc.).


### Phase 4: Retention (The Rental Lifecycle)
*The post-purchase experience where the complex logic lives.*

![User Dashboard and Active Rentals](path/to/your/image.png)

**Key Interactions:**
* **Dashboard:** The user profile aggregates Order History and Active Rentals.
* **Rental Management:** This is the core logical engine where users can:
    1.  **Extend:** Add 1-4 weeks to a rental (updates price automatically).
    2.  **Buyout:** "Fall in love" with an item? Users can pay the difference to keep it.
    3.  **Return:** A "Mark as Returned" flow removes the item from active duty.
* **Risk-Free:** Logic exists to handle immediate returns if the fit isn't right.

---

### Phase 5: Admin & Operations
*The backend tools used to manage the business.*

![Admin Dashboard](path/to/your/image.png)

**Key Interactions:**
* **Product Management:** Full CRUD capability for inventory.
* **Order Oversight:** Admins can view active rentals and flag users or items.

### Others
**500 & 404 Pages:** Custom error pages provide a branded experience even when things go wrong.
![alt text](documentation/images/user-journey/image-74.png)

* **Safety:** Confirmation modals prevent accidental deletion of inventory or user data.

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
- Adjust buttons layout and sizes for consistency across pages and better UX

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

**HTML5** – Standard markup language for creating web pages.
**CSS3** – Style sheet language used for describing the presentation of the web application.
**JavaScript** – Programming language used for client-side interactivity and handling Stripe elements.
**Python** – The core programming language used for back-end development with Django.
**SQL** – Used for managing and querying the PostgreSQL relational database.
**Django Template Language (DTL)** – A specialized syntax used within HTML files to bridge the back-end Python data with the front-end display.
**Markdown** – Used for project documentation files.

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
- **[Flake8 / Pylint](https://flake8.pycqa.org/)** – Python linting tools used to enforce PEP 8 style guides and code quality.
- **[Prettier](https://prettier.io/)** – Code formatter ensuring consistent syntax style across the project.
- **[Prettier](https://prettier.io/)** – Code formatter that ensures consistent style across your JavaScript, CSS, JSON, and other files.
- **[Lucidchart](https://www.lucidchart.com/)** – Database schema design and ERD creation.
- **[ChatGPT (OpenAI)](https://chat.openai.com/)** and **[Gemini (Google)](https://gemini.google.com/)** were used for generating service descriptions, debugging support, exploring different solutions, and clarifying code concepts.
- **[Django](https://www.djangoproject.com/)** – High-level Python web framework powering the backend of the application.  
- **[Gunicorn](https://gunicorn.org/)** – Python WSGI HTTP server for running Django apps in production.
- **psycopg2** – Adapter for Python, enabling Django to communicate with a PostgreSQL database.
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
- **[ngrok](https://ngrok.com/)** – Tool to expose local servers to the internet for testing webhooks and external integrations during 
development.
- **[AWS S3](https://aws.amazon.com/s3/)** – Cloud object storage used for hosting static and media files in production.
- **[AWS IAM](https://aws.amazon.com/iam/)** – Used to manage access keys and permissions for S3 integration.
- **[AWS CLI](https://aws.amazon.com/cli/)** – Command-line tool used to upload and sync large media files to S3.
- **[django-storages](https://django-storages.readthedocs.io/)** – Provides custom Django storage backends, used to integrate AWS S3 for static and media file storage.
- **[boto3](https://boto3.amazonaws.com/)** – AWS SDK for Python, required by `django-storages` to communicate with S3 services.
- **[dj-database-url](https://pypi.org/project/dj-database-url/)** – Parses database URLs from environment variables and configures Django database settings automatically.
- **[django-countries](https://pypi.org/project/django-countries/)** – Provided standardized country dropdowns for shipping and billing addresses.
- **[CI Python Linter](https://pep8ci.herokuapp.com/)** – Continuous integration tool used to enforce PEP 8 style guidelines on Python code.

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

In your environment file, add your database URL as follows:

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

**If not using S3 or Other storage solutions**, make sure to add key `DISABLE_COLLECTSTATIC` with value `1` to your Heroku Config Vars to prevent Heroku from running `collectstatic` during deployment.

**Stripe Configuration**

Set up Stripe API keys as environment variables in Heroku:
| Key                 | Value                         |
|---------------------|-------------------------------|
| `STRIPE_PUBLIC_KEY`  | Your Stripe Public Key        |
| `STRIPE_SECRET_KEY`  | Your Stripe Secret Key        |
| `STRIPE_WH_SECRET`   | Your Stripe Webhook Secret    |

**Webhook Setup**
To handle Stripe events (e.g., payment confirmations), set up a webhook endpoint in your Heroku app:

1. In the Heroku Dashboard, navigate to your app and select the **Settings** tab.
2. Click on **Reveal Config Vars** and ensure `STRIPE_WH_SECRET` is set. 
3. In your Stripe Dashboard, go to **Developers > Webhooks**.
4. Click **Add endpoint** and enter your Heroku app URL followed by `/checkout/wh/` (e.g., `https://your-heroku-app-name.herokuapp.com/checkout/wh/`).

**Email Configuration (Gmail SMTP)**
To enable email functionality (e.g., account verification, password resets), configure Gmail SMTP settings in Heroku:

| Key                 | Value                         |
|---------------------|-------------------------------|
| `EMAIL_HOST_USER`   | `smtp.gmail.com`              |
| `EMAIL_HOST_PASS`   | Your Gmail App Password       |

ATTN: For Gmail SMTP, you may need to set up an App Password if you have 2-Step Verification enabled on your Google account. Follow Google's instructions to create an App Password and use it as the value for `EMAIL_HOST_PASS`. 

Stripe webhooks and email functionality will not work properly until these configurations are in place.

**Deploying the app**

Assuming you have already initialized a Git repository in your project directory, committed your code and connected GitHub to your Heroku app, you can deploy the project using the following steps:

On your Heroku app dashboard, select the Deploy tab.

Here, we will connect our Heroku app to our GitHub repository and deploy our project. Scroll to the Deployment method and select GitHub

Search for your repository name, then click Connect

Click the Enable Automatic Deploys button. This will ensure that any time you push new code to your GitHub repository, Heroku will deploy the updated application.

Click Deploy Branch to deploy your project.

Watch the build log as it runs. You can view the build output in the application's Activity tab in the dashboard. This build may take several minutes to complete. If all goes well, the log should look like this when completed.

Click the Open app button at the top of the page to open your app. You can also access your app at the URL `https://your-heroku-app-name.herokuapp.com/`.

**Uploading Static and Media Files**
If using S3, your static files will be automatically uploaded to the bucket after deploying project on heroku.

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

To run the project locally, follow the steps below.

**Create a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Environment variables

Create a `.env` file in the root of your project and add the following variables:

```bash
import os

os.environ['DEVELOPMENT'] = 'True'
os.environ['DATABASE_URL'] = 'your-database-url-here'
os.environ['EMAIL_HOST_USER'] = 'your-email@gmail.com'
os.environ['EMAIL_HOST_PASS'] = 'your-email-app-password'
os.environ['STRIPE_WH_SECRET'] = 'your-stripe-webhook-secret'
os.environ['STRIPE_PUBLIC_KEY'] = 'your-stripe-public-key'
os.environ['STRIPE_SECRET_KEY'] = 'your-stripe-secret-key'
os.environ['SECRET_KEY'] = 'your-django-secret-key'

# If using S3 for static and media file storage, add the following variables:
os.environ['USE_AWS'] = 'True'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'Your AWS Secret Access Key'
os.environ['AWS_ACCESS_KEY_ID'] = 'Your AWS Access Key ID'
os.environ['AWS_STORAGE_BUCKET_NAME'] = 'Your S3 Bucket Name'
os.environ['AWS_S3_REGION_NAME'] = 'Your S3 Region Name (e.g., us-east-1)'
```

The setup above includes all necessary environment variables for local development with connected production database, email settings, Stripe API keys and AWS S3 services if applicable. Make sure to replace the placeholder values with your actual credentials and configuration details.

Run migrations

```bash
python manage.py migrate
```

Create a superuser

```bash
python manage.py createsuperuser
```

Start the development server

```bash
python manage.py runserver
```

The application will be available at:
http://127.0.0.1:8000/

## Cloning and Forking

### Cloning

To clone the repository, run:

```bash
git clone https://github.com/your-username/your-repo-name.git
```

Navigate into the project directory:

```bash
cd your-repo-name
```

### Forking

1. Navigate to the GitHub repository
2. Click the Fork button in the top-right corner
3. Clone your forked repository locally using the steps above

### Local vs Deployed Version

**Local Version**

Used for development and testing
- Runs with DEBUG=True
- Uses local environment variables
- May use SQLite or a local PostgreSQL database if configured
- Static files served locally
- Media files might be stored locally or on S3 depending on configuration

**Deployed Version (Heroku)** (is deployed to Heroku and accessible to the public)

- Runs with DEBUG=False
- Uses Heroku Config Vars
- Static and media files are served via AWS S3 (if enabled)

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
- [Framer Marketplace - Nivest Template](https://www.framer.com/marketplace/templates/nivest/) – Inspiration for overall design and layout.
- [GitHub Repository – Boutique Ado](https://github.com/Code-Institute-Solutions/boutique_ado_v1) - Most of the models for order, checkout, backend logic, and the overall site structure were inspired and partially copied from **Boutique Ado** by Code Institute. This project acted as a skeleton for my site, and I adapted and adjusted aspects of it to create the project as it is now. 


### Data Sources

- [Vibrent Clothes Rental Dataset (Kaggle)](https://www.kaggle.com/datasets/kaborg15/vibrent-clothes-rental-dataset?select=images)  
- Academic reference:  
  *[A Dataset for Adapting Recommender Systems to the Fashion Rental Economy](https://dl.acm.org/doi/10.1145/3640457.3688174)* (RecSys 2024)  **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- [Adobe Colors](https://stock.adobe.com/se/images/flat-lay-with-woman-fashion-accessories-in-yellow-colors-fashion-blog-summer-style-shopping-and-trends-idea/315730695) – Colors inspiration.

### Content

The textual content and platform descriptions for this fictional fashion marketplace were created in collaboration with AI tools such as ChatGPT and Gemini. Page copy, product descriptions, and UX narratives were AI-assisted and inspired by real-world fashion e-commerce and rental platforms.

### Media

#### General Imagery

- **[Woman in blue bralette holding sunglasses putting on her eyes](https://unsplash.com/photos/woman-in-blue-bralette-holding-sunglasses-putting-on-her-eyes-_KaMTEmJnxY?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)** – Photo by Atikh Bana on Unsplash.

- **The main images were taken from the Vibrent Clothes Rental Dataset for the website styling.**
      

### Acknowledgments

I’m grateful to the creators of the Vibrent Clothes Rental Dataset for making this project possible.

Thanks to the Django community and the open-source libraries used in this project.

Special thanks to Code Institute for the Boutique Ado walkthrough and ongoing support, which formed the foundation of this work.

Finally, thanks to my closest friend and my cat James for emotional support and occasional “debugging” assistance 🐾

[Back to Top](#stocka-—-a-modern-fashion-marketplace)
