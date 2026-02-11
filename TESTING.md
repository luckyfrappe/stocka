# Stocka - Testing Documentation

<!-- ![alt text](documentation/testing/manual-testing/landing.png "Overview image of Stocka landing page") -->

🔗 [**Live site**](https://boutique-stocka-748274888aff.herokuapp.com/)

Testing for Stocka is an integral part of the development process to ensure functionality, responsiveness, and usability across all devices.

## Contents

- [User Stories](#user-stories)
- [Automated Testing](#automated-testing)
- [Manual Testing](#manual-testing)
- [Bugs](#bugs)
  - [Known Bugs](#known-bugs)
  - [Solved Bugs](#solved-bugs)

---

### User Stories

| User Story | Description | Status |
| :--- | :--- | :--- |
| US-01: Browse all products | As a shopper, I can browse items to rent or buy so that I can see all available options. | ✅ |
| US-02: Category Browsin | As a shopper, I can browse items by category to quickly find relevant options. | ✅ |
| US-03: Product Details | As a shopper, I can view descriptions, sizing, and pricing to decide whether to rent or buy. | ✅ |
| US-04: Product Search | As a shopper, I can search by name or description to quickly find specific items. | ✅ |
| US-05: Product Sorting | As a shopper, I can sort items by price or name to compare products easily. | ✅ |
| US-06: Purchase Options | As a shopper, I can select buy, buy pre-owned, or rent to fit my budget and needs. | ✅ |
| US-07: Size & Quantity | As a shopper, I can select size and quantity to ensure I order the correct item. | ✅ |
| US-08: View Shopping Bag | As a shopper, I can review my items, total cost, and rental duration before checkout. | ✅ |
| US-09: Edit Shopping Bag | As a shopper, I can update or remove items in my bag to correct mistakes before checkout. | ✅ |
| US-10: Secure Checkout | As a shopper, I can complete my purchase securely to place my order with confidence. | ✅ |
| US-11: Authentication | As a user, I can register and log in to manage my rentals and orders. | ✅ |
| US-12: User Profile | As a user, I can view my profile to access my personal details and rental history. | ✅ |
| US-13: Product Management | As a store owner, I can add, edit, and delete products to manage site inventory. | ✅ |
| US-14: Active Rentals | As a shopper, I can track my active rentals and subscription dates to manage my orders. | ✅ |
| US-15: Extend Rental | As a shopper, I can extend my rental period to keep an item longer with updated pricing. | ✅ |
| US-16: Rental Buyout | As a shopper, I can buy out a rented item to keep it permanently at a clear price. | ✅ |
| US-17: Buyout Calculation | As a shopper, I want the system to calculate a fair remaining buyout price based on paid rental time. | ✅ |
| US-18: Return Rental | As a shopper, I can mark an item as returned to close the rental and update my subscriptions. | ✅ |
| US-19: Legal Information | As a shopper, I can access Privacy, Terms, and Return policies to understand my rights and data handling. | ✅ |
| US-20: Save for Later | As a shopper, I can save items to a favorites list to revisit them before renting or buying. | ✅ |
| US-21: Contact Form | As a shopper, I can use a contact form with a title to get help with returns and general questions. | ✅ |
| US-22: Company Values | As a site visitor, I can read about the brand’s concept and sustainability to feel confident in my purchase. | ✅ |

---

### Automated Testing

Automated tools are used to ensure code quality, performance, and accessibility.

**Google Lighthouse:**
I have utilized Lighthouse Metrics to evaluate the site’s current technical standing. While the initial results show strong foundations in visibility and standards, there is clear room for growth regarding speed and inclusive design.

* **SEO & Best Practices:** I’ve achieved a score almost of **100** across most pages. My focus here was ensuring the site is fully discoverable and follows modern web standards.
* **Accessibility:** The site consistently passes basic accessibility checks. However, my scores are not yet uniform across the board, and I am working toward a more consistent user experience for all visitors.
* **Performance:** This is the primary area for improvement. While lighter pages perform well, I noticed significant score drops on heavy product pages. 

**Future Objectives:**
Performance and accessibility did not reach my target thresholds on every page. I will endeavor to optimize asset loading on the product-heavy sections and refine my accessibility implementation to ensure a seamless experience site-wide.

**HTML & CSS Validation:**  
HTML Validation

I used the [W3C Markup Validation Service](https://validator.w3.org/) to check all HTML files for syntax errors and compliance with web standards.

Notes on Validation:
All templates passed with no syntax errors. I fixed all unclosed tags, missing alt attributes, and deprecated elements to ensure clean markup.

CSS Validation

I used the [W3C Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) to check all static CSS files. 

Notes on Validation:
All custom stylesheets passed with no syntax errors. 

**JavaScript Validation:**  
I used [JSHint](https://jshint.com/) to validate all static JavaScript files and inline scripts. After my Python cleanup, I completed a final pass on all JavaScript to ensure the front-end logic was just as polished.

Notes on Validation:
All scripts passed with zero errors. I fixed all versioning warnings and properly defined global variables like `Stripe`, `jQuery`, and `Bootstrap` so the linter recognized them. Django Compatibility: In cases where Django tags were used inside scripts, I adjusted the formatting to make sure the code was valid for both the server and the linter.

**Python / Django Validation:**  
I used the [CI Python Linter](https://pep8ci.herokuapp.com/) and the flake8 extension to ensure my code follows PEP8 compliance. At the end of the project, I did a "grand cleanup" to fix all linting issues. 

Notes on Validation:
100% Clean: All flagged issues, including lines exceeding 79 characters and multiple statements on one line, have been resolved.

Excluded Files: I ignored files like manage.py, env.py, and the migrations/ folders. These are auto-generated by Django or contain system configurations, so I left them untouched to ensure the project stays stable.

**Accessibility Testing:**  
I implemented semantic HTML and ARIA roles to ensure a seamless experience for screen reader users, while also performing manual keyboard navigation tests to verify that the entire checkout funnel is fully accessible. I also used Lighthouse to identify and fix any accessibility issues, such as missing alt text or insufficient color contrast.

---

### Manual Testing

**Home Page Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Home Page Load** | Open the website URL | Logo, Hero Image, and Brand Marquee are displayed correctly | ✅ |
| **Navigation Menu** | Hover over "Shop" | Mega menu drops down with categories like Men, Women, and Accessories | ✅ |
| **Mobile Menu** | Tap the hamburger icon | Menu slides out with easy-to-tap sections for Clothing and Fit | ✅ |
| **Search Bar** | Type a keyword and enter | The site searches and shows me products matching that word | ✅ |
| **Shopping Bag** | Click the bag icon | Side panel opens showing added items and total price (e.g., 590 kr) | ✅ |
| **User Dropdown** | Click the user icon | Shows Profile, Subscriptions, or Admin options based on login | ✅ |
| **Product Click** | Click a product image | I am taken directly to that product's detail page | ✅ |
| **Admin Controls** | Click Edit or Delete | Buttons allow quick product updates or removal directly from home | ✅ |
| **Delete Safety** | Click Delete button | A popup asks "Are you sure?" to prevent accidental deletion | ✅ |
| **Delete Safety** | Click Delete button on items with active subscriptions | An error message appears preventing deletion to protect active subscriptions | ✅ |
| **Company Info** | Click Concept or Values | Navigate to pages explaining the brand story and sustainability | ✅ |
| **Brand Marquee** | Observe the scrolling brand list | The partner brand names (Joseph, Hope, etc.) scroll smoothly without layout breaks. | ✅ |

**Product Listing & Filter Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Sorting** | Select "Price (low to high)" from the dropdown | The list reloads immediately showing the cheapest rental options first | ✅ |
| **Smart Filters** | Click a checkbox (e.g., a specific Brand or Size) | The page submits automatically and filters the results without extra clicks | ✅ |
| **Filter Sidebar** | Click "Clear" button in the sidebar | All active filters are removed and the full product list is restored | ✅ |
| **Product Display** | View a product card | Name, Retail Price, Rental Price, and Pre-owned Price are all clearly visible | ✅ |
| **Pagination** | Click a page number at the bottom | The next set of products loads while keeping my active filters/sorting | ✅ |
| **Mobile Filters** | Tap the "Filters" button on mobile | The filter menu expands/collapses to save screen space | ✅ |
| **Back to Top** | Click the floating arrow button | The page smoothly scrolls back up to the navigation bar | ✅ |
| **Admin Tools** | Click "Edit" or "Delete" on a card | As an admin, I can modify or remove items directly from the gallery | ✅ |
| **Delete Modal** | Click the Delete button | A warning popup appears to confirm the action before any data is lost | ✅ |
| **Empty Results** | Filter by a criteria with no matches | A friendly "No products found" message appears with a link to browse all | ✅ |

**Product Detail Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Image Gallery** | Scroll or swipe through the product images | All product photos load clearly and are easy to navigate on both desktop and mobile. | ✅ |
| **Wishlist Toggle** | Click the heart icon next to the product title | The heart changes style or a notification confirms the item is saved to my favorites. | ✅ |
| **Information Tabs** | Click the "Description" accordion | The section expands to show the product details and clickable attribute badges (e.g., Brand, Material). | ✅ |
| **Purchase Options** | Click between "Buy New" and other purchase modes | The accordion switches focus smoothly, updating the price and selection details. | ✅ |
| **Size Selection** | Choose a different size from the dropdown menu | The dropdown correctly updates to my selected size (e.g., switching from S to M). | ✅ |
| **Price Accuracy** | Check the price displayed in the header vs. the button | The total price matches the selected purchase type (e.g., 1300.00 SEK for Buy New). | ✅ |
| **Add to Bag** | Click the main action button (e.g., "Add to Bag") | A toast message appears confirming the item was added, and the cart total in the navbar updates. | ✅ |
| **Responsive Layout** | View the page on a narrow mobile screen | The product info stays "sticky" or stacks logically below the images for easy reading. | ✅ |
| **Inventory Status** | View an out-of-stock item | The purchase button is disabled or clearly labeled as "Sold Out" or "Unavailable." | ✅ |
| **Security** | Try to add to bag without selecting a required size | The form prevents submission and alerts me that a size must be chosen. | ✅ |

**Shopping Bag Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Bag Visibility** | Open the Shopping Bag page | All added items appear with their correct name, size, and purchase type (e.g., NEW) | ✅ |
| **Quantity Update** | Click the "+" or "-" buttons | The number in the box changes, but the subtotal only updates after clicking "Update" | ✅ |
| **Update Link** | Click the "Update" link after changing qty | The page refreshes and the Grand Total recalculates correctly | ✅ |
| **Remove Item** | Click the "Remove" button | The item is instantly deleted from the bag and the "Bag Total" updates | ✅ |
| **Price Breakdown** | Check Bag Total vs Delivery vs Grand Total | The math adds up correctly (e.g., 1200 + 0 = 1200 SEK) | ✅ |
| **Mobile View** | View bag on a mobile phone | The table switches to a "stacked" card layout that fits the screen width | ✅ |
| **Navigation** | Click the "Keep Shopping" button | I am taken back to the main Product Listing page | ✅ |
| **Secure Checkout** | Click the "Secure Checkout" button | I am redirected to the payment/checkout page safely | ✅ |
| **Image Links** | Click the product thumbnail image | I am taken back to the Product Detail page for that specific item | ✅ |
| **Scroll to Top** | Click the floating arrow button | The page scrolls back to the top so I can see the Navigation bar | ✅ |

**Checkout Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Order Summary** | Review items in the summary | Correct product, size (L), and type (NEW) are displayed with the right subtotal. | ✅ |
| **Form Pre-fill** | Verify user details | Name, email, and address auto-populate correctly for logged-in users. | ✅ |
| **Field Validation** | Leave a required field (e.g., Phone) empty | Form prevents submission and highlights the missing required field. | ✅ |
| **Math Accuracy** | Check Grand Total logic | Grand Total correctly sums Order Total and Delivery (1200 + 0 = 1200 SEK). | ✅ |
| **Stripe Integration**| View payment element | The Stripe credit card input container loads securely without errors. | ✅ |
| **Mobile Flow** | View on mobile device | Order summary moves to the top/bottom logically to keep the form accessible. | ✅ |

**Thank You Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Messaging** | Check Order Number | UUID (AFA168...) is displayed in both the toast and the summary. | ✅ |
| **Product** | Verify Line Items | Displays "Black Amber Pants - Size L" with price "1200.00 Kr." | ✅ |
| **Logistics** | Verify Shipping Info | Recipient "Oscar Wilde" and address details (SW3 4JA) match the input. | ✅ |
| **Billing** | Check Totals | Math remains consistent: 1200.00 (Total) + 0.00 (Delivery). | ✅ |
| **UI/UX** | Success Notification | The `bg-success` toast triggers and correctly identifies the user email. | ✅ |

**Subscriptions Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Buyout Option** | Review Buyout button | Button appears allowing the customer to purchase the item permanently. If price is 0, no checkout process is initiated. | ✅ |
| **Price Logic** | Compare Buyout vs. Extension | "Extend" button disables automatically if the buyout price is lower than the weekly rate. | ✅ |
| **Subscription Info** | View Current Items | Shows "Jarvis Blouse" in Size XS with "Active" status. | ✅ |
| **Dates** | Review Timeline | Rental period correctly lists 1 week (Feb 13 to Feb 20). | ✅ |
| **Return Process** | Click "Mark as Returned" | Button is visible and correctly associated with the item for easy returns. | ✅ |
| **Extension** | Open Extension Window | Pop-up appears showing the weekly price of 590.00 SEK. | ✅ |
| **Extension** | Enter Week Count | User can successfully input the number of weeks to add. | ✅ |
| **Display** | Mobile View | Images and buttons resize to fit phone screens properly. | ✅ |

**Extension & Buyout Flow Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Bag Logic** | Initiate Extension/Buyout | Automatically clears all other items from the bag to prioritize the transaction. | ✅ |
| **Direct Flow** | Navigation Path | Redirects user immediately to the Checkout page after selecting "Extend" or "Buyout". | ✅ |
| **Transaction Lock** | Add New Item during lock | System blocks additional items from being added while an exclusive transaction is active. | ✅ |
| **Error Handling** | Cross-navigation Redirect | If a user navigates away and tries to add a new product, they are pushed back to Checkout. | ✅ |
| **User Feedback** | Toast Notification | A message displays: "Current transaction in progress. Please complete it or remove the item." | ✅ |
| **Security** | Integrity Check | Ensures the bag cannot contain a mix of "Regular Purchases" and "Extensions/Buyouts." Only one type/product is allowed at a time. | ✅ |

**Contact Form Manual Testing**

| Section | Test Action? | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Missing Info** | Leaving a field blank | The form won't send and will ask the user to fill in the missing details. | ✅ |
| **Email Accuracy** | Typing a fake email (no @) | The system recognizes it isn't a real email address and asks for a correction. | ✅ |
| **Sending Message** | Clicking "Send Message" | A "Success" message appears so the user knows their inquiry is on its way. | ✅ |
| **Mobile Ease** | Using the form on a phone | The text boxes are large enough to tap easily and the "Send" button is easy to find. | ✅ |
| **Business Info** | Checking contact details | The support email and office hours are clearly visible and easy to read. | ✅ |
| **Link Check** | Clicking social or footer links | All links in the bottom area lead the user to the correct company pages. | ✅ |

**Favorites Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Save Item** | Click Heart icon on product | Item is immediately saved and the Heart icon fills in to show it is a favorite. | ✅ |
| **Favorites List** | Open Favorites page | All specifically selected items appear in one view across all categories. | ✅ |
| **Price Sorting** | Sort by "Price (low to high)" | The list reorders so the most affordable items appear at the top. | ✅ |
| **Name Sorting** | Sort by "Name (A-Z)" | The list reorders alphabetically to help the user find specific brands/products. | ✅ |
| **Count Accuracy** | Check "Products out of X" | The total number displayed matches the actual amount of items in the list. | ✅ |

**Informational Pages Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Concept** | Click "Our Concept" in the sidebar or footer | The page loads correctly, explaining the Loop (Rent), Keep (Buyout), and Reuse (Pre-owned) programs. | ✅ |
| **Terms of Service** | Select the "Terms of Service" link | The business rules and platform usage agreement are displayed clearly for the customer. | ✅ |
| **Privacy Policy** | Select the "Privacy Policy" link | Information on data protection and customer privacy is accessible and easy to read. | ✅ |
| **Return Policy** | Select the "Return Policy" link | Customers are informed about return windows and the "final sale" status of pre-owned items. | ✅ |
| **Side Navbar** | Test all links in the sidebar navigation | Every link directs the correct header. | ✅ |
| **Mobile Display** | View any info page on a mobile device | The side navigation and long-form text adjust to fit the screen. | ✅ |

**Branding Pages Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Our Values** | Access the values page | Branding elements (Goal, Values, Hope) and the brand marquee load correctly. | ✅ |
| **About Us** | Access the about page | The company narrative and mission statement are displayed professionally. | ✅ |
| **Sustainability** | Access the sustainability page | Our commitment is clearly communicated. | ✅ |
| **Brand Marquee** | Observe the scrolling brand list | The partner brand names (Joseph, Hope, etc.) scroll smoothly without layout breaks. | ✅ |

**Profile Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Profile Access** | Click "My Profile" in the user dropdown | The user is directed to their profile dashboard with existing data populated. | ✅ |
| **Delivery Info** | Update default address fields (Street, City, Postcode) | Changes are saved to the database and correctly reflect in future checkouts. | ✅ |
| **Country Selection** | Select a country from the dropdown menu | The full list of ISO countries is available and the selection saves correctly. | ✅ |
| **CSRF Security** | Submit the profile update form | The system validates the hidden security token to prevent unauthorized form submission. | ✅ |
| **Form Validation** | Attempt to save an empty Full Name or Phone Number | The form prevents submission and provides a prompt for required information. | ✅ |
| **Navigation Sync** | View profile across mobile and desktop | The profile form remains responsive and legible on all device types. | ✅ |

**Past Order Confirmation Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Order Summary** | Review item details | Product name, Size, Type (Rent/Buy), and Rental Dates are clearly listed. | ✅ |
| **Delivery Data** | Check "Delivering To" section | Customer name and shipping address display correctly from the checkout form. | ✅ |
| **Past Order Toast** | View a historical order success page | A notification toast appears clarifying that this is a past order confirmation. | ✅ |

**Authentication Manual Testing**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **User Registration** | Sign up with a new email and password | Account is created and user is prompted for email verification if required. | ✅ |
| **Login Flow** | Enter valid business credentials | User is authenticated and redirected to their profile or the homepage. | ✅ |
| **Logout Flow** | Click "Logout" in the user dropdown | Session is terminated and user is redirected to the home/landing page. | ✅ |
| **Password Reset** | Submit "Forgot Password" request | A secure reset link is sent to the registered email address. | ✅ |
| **Validation** | Enter an incorrect password | System displays a clear error message: "Username and password do not match." | ✅ |

**Product Listing Creation Test**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Product Description** | Type a name and detailed description for the item | Text appears clearly in the boxes. | ✅ |
| **Pricing Entry** | Enter a price (e.g., 500) | The system accepts the number. | ✅ |
| **Invalid Price Check** | Try to enter letters (like "abc") into the price box | The system prevents this. | ✅ |
| **Image Upload** | Click to upload a single product photo from your computer | The file is attached, and the file name is visible next to the button. | ✅ |
| **Material Tags** | Click the "Select Attributes" or "Material" dropdown | The list opens to show options like Cotton, Wool, and Silk. | ✅ |
| **Tag Selection** | Check the boxes for "Cotton" and "Viscose" | Both boxes remain checked (allowing multiple materials to be selected). | ✅ |
| **Save Product** | Click the "Add Product" button | The page loads, and the new product is saved to the inventory. User redirected to the new product page. | ✅ |

**Product Editing Test**

| Section | Test Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Verify Product** | Open the edit page for "Ginger Spice Leopard Knit" | A notification confirms you are editing this specific product. | ✅ |
| **Update Description** | Change the existing description text | You can delete the old text and type in new details successfully. | ✅ |
| **Update Price** | Change the price to a new amount | The box accepts the new number. | ✅ |
| **Change Image** | Upload a new photo | The new file is attached. | ✅ |
| **Delete Image** | Remove a selected photo by clicking the delete button underneath the image preview | The image is removed from the product listing. | ✅ |
| **Material Tags** | Open "Change Attributes" and uncheck "Synthetic" | The checkmark is removed from "Synthetic". | ✅ |
| **New Tag Selection** | Select a new material (e.g., "Cotton") | The checkmark appears next to "Cotton" while "Synthetic" remains unchecked. | ✅ |
| **Save Changes** | Click the "Save Changes" button | The page saves changes and the product is updated in the shop. | ✅ |

**Browser & Mobile Device Testing**
Testing Scope:
* **Browsers:** Chrome, Safari, Firefox, and Edge.
* **Devices:** iPhone, iPad and Desktop.

Purchase flows, navigation, and responsive design were tested across all platforms to ensure a consistent user experience.

---

## Bugs

### Known Bugs
- No known bugs at this time.

### Solved Bugs
- Bug summary:
Shopping Bag icon and the Price text were sitting side-by-side in a horizontal row. Because the price text takes up quite a bit of width, it was pushing the icon out behind logo. 

The Fix:
I stacked the price directly underneath the icon to solve this issue.

- Bug summary:
In the mobile navigation, the collapsible submenu items were not scrollable when the content exceeded the viewport height. 

The Fix:
I added CSS styles to the navbar collapse div to set a maximum height and enable vertical scrolling.

- Bug summary:
The mobile navigation menu's maximum height was set too low, causing some submenu items to be inaccessible on smaller screens. 

The Fix:
I increased the max-height to 90vh to ensure all items are reachable.

- Bug summary:
In the mobile navigation, the submenu items were not collapsing when another submenu was opened. 

The Fix:
I added the `data-bs-parent` attribute to each submenu collapse div to ensure only one submenu is open at a time.

- Bug summary:
On the product listing page, the attribute filters were displaying all available attributes, leading to a cluttered interface. 
The Fix:
I modified the view to only fetch and display a targeted subset of attribute types (material, brand, color, length, details) for filtering.

- Bug summary:
The product listing page header had excessive top margin, causing unnecessary whitespace. 

The Fix:
I adjusted the margin to create a more balanced layout.

- Bug summary:
Broken pagination controls:

The Problem: On a fresh page, there is no ? in the URL. Adding &page=2 creates an invalid URL. It only worked when I had filters because the filters already provided the required ?.

The Fix:
I changed the links to always start with a ? and then loop through active filters. This ensures the URL is valid on a clean search and a filtered one. 

- Bug summary:
Pagination controls were not preserving existing query parameters when navigating between pages. 

The Fix:
Gemini by Copilot suggested to update the pagination links to include all current GET parameters using `request.GET.urlencode`, ensuring filters remain applied during pagination.

- Bug summary:
The Sidebar and Navbar weren't "talking" to each other. When navigating from a Navbar link, the Sidebar didn't realize a filter was already active, so it didn't check the box. When I clicked "Apply," the Sidebar form submitted only its own checked boxes, "forgetting" Navbar selection.

The Logic Fix
Global Visibility: Allowed the Sidebar to see all attribute types. Instead of filtering to a targeted few, it now has access to all. Original filter logic were to complement the Navbar, but this broke the connection.

Pre-selection: If a filter is in the URL (from a link), the checkbox pre-selects itself.

Result: When I hit "Apply," the form now includes the Navbar category because it's already checked.

- Bug summary:
Backend filtering is working, but the frontend keeps sending old filter parameters in the URL. When I uncheck a filter, the checkbox disappears visually, but its query parameter is not removed, so Django still filters by it.

Root cause:
HTML checkboxes don’t automatically remove GET params. Filter UI (forms / links / pagination) is not rebuilding a clean URL, so “removed” filters are never actually removed from the request.

Solution:
The Logic Fix: Instead of the frontend telling the backend what is selected, the Backend now tells the Frontend.

I created active_filter_slugs = [] to store the exact IDs the user clicked.

In the view, it loops through the URL parameters and extends this list with every active attribute.

This list is sent to the context, and the checkbox only stays "checked" if its specific slug exists in that clean list. The list keeps the checkbox alive, not the other way around.

The Integrated "New Arrivals" Toggle
I moved New Arrivals from a standalone link into the main filter form.

Form Integration: By adding it as a filter-checkbox, it now behaves like an attribute.

Persistent State: Using {% if 'new_arrivals' in request.GET %}checked{% endif %}, I ensure that when a user filters for "Shoes" and then clicks "New Arrivals," the shoe filter stays active because the whole form is submitted together.

Hierarchical Filtering: By placing the logic at the end of the view, the "New Arrivals" filter acts as a "final cut," showing the 100 newest items from the already filtered pool of products.

- Bug summary:
On the product detail page, the purchase options (Buy New, Rent, Pre-Owned) were not functioning correctly. The accordion flush behavior was broken after separeting into 3 separate forms, and selecting an option did not "flush" others options.

The Fix:
I wrapped all three purchase forms in a single accordion container with the ID "purchaseAccordion". Each purchase option's collapse div includes the attribute `data-bs-parent="#purchaseAccordion"`, ensuring that when one option is expanded, the others collapse automatically. This restores the intended accordion behavior across the separate forms.

- Bug summary:
On admin page for ProductAttribute, the display of attribute values was showing attribute type as number IDs instead of their actual values, making it hard to identify them.

The Fix:
I updated the `__str__` method in the AttributeValue model to return just the value string. This way, in the admin interface, attribute values are displayed clearly by their actual value rather than an ID reference.

- Bug summary:
AttributeValue model's string representation included both attribute type and value, leading to redundancy when displaying in contexts where the type is already known.
The Fix:
I modified the `__str__` method of the AttributeValue model to return only the value. This simplifies displays and avoids redundancy in contexts where the attribute type is already clear. Also adjsuted products tags to display both product type and value where needed.

- Bug summary:
On bag page, clicking the quantity update link was not submitting the form correctly, leading to no change in quantity.

The Fix:
I added if (startInput) { ... } around the rental date logic to ensure it only runs if the startInput element exists on the page. This prevents errors on pages without rental options. I also added efault:0 to the price_per_week context variable to avoid errors when the product does not have a rental price defined.

- Bug summary:
In the bag page template, the quantity update form was not correctly passing the product size to the backend when updating item quantities. Resulted in deleting other sizes of the same product when updating quantity.

The Fix:
I modified the quantity form to include a hidden input field for product_size, ensuring that when the quantity is updated, the correct size is referenced in the backend logic.

- Bug summary:
In the bag context processor, the subtotal calculation for each bag item was incorrectly using the product's retail price instead of the actual price paid (which could be rental or pre-owned price). This led to inaccurate subtotal and total calculations in the shopping bag.

The Fix:
I updated the subtotal calculation to use item.price_each (the actual price paid) multiplied by item.quantity, ensuring accurate subtotal and total amounts in the bag context.

- Bug summary:
In add_to_bag view, rental_period was not being captured in item_key, causing issues when adding multiple rental items of different durations.

The Fix:
I updated the item_key to include rental_period, ensuring that items with different rental durations of the same size are treated as separate entries in the bag.

- Bug summary:
Scroll up button was not appearing above other content, making it unclickable when overlapping with other elements like footer cards.

The Fix:
I added `z-index: 9999;` to the scroll-up button CSS to ensure it appears above all other content, making it clickable at all times.

- Bug summary:
In my original code borrowed from Boutique Ado study project, I tried to cram the entire shopping bag—product IDs, quantities, sizes, and rental dates—into Stripe's metadata field. I hit a hard limit: Stripe only allows 500 characters for metadata values. As soon as a customer tried to purchase more than 3 or 4 items, the data exceeded that limit. Stripe rejected the request, the JavaScript crashed, and the payment process couldn't even start.

The Fix:
Instead of trying to send the entire order details to Stripe and back again, I changed the logic. Now, my website stores the bag safely in its own database the moment the order is created in Django. I used the Stripe PID (payment_intent_id) as the unique "Claim Ticket." Stripe now only needs to hold that tiny PID string, which stays the same size no matter how many items are in the bag. When the webhook fires, the webhook_handler uses that PID to look up the bag in the database, marks the order as paid, and processes it normally.

- Bug summary:
In the webhook_handler, I had a process to save user profile information after a successful payment. However, if a UserProfile did not exist for the provided username (such as during a guest checkout or a sync error), it raised a UserProfile.DoesNotExist exception. This caused the entire webhook to fail and stop running before it could finish the order.

The Fix:
I added a try-except block around the UserProfile retrieval. Now, if the profile does not exist, the code simply sets the profile to None and continues without raising an exception. This prevents the webhook from failing due to missing profiles and ensures the payment confirmation logic always completes.

- Bug summary:
Buyout price calculation was not accounting for rental equity correctly, leading to incorrect buyout prices being set.

The Fix:
I adjusted the buyout price calculation to first determine the total rental equity based on weeks paid and price per week. Then, I subtracted this rental equity from the retail price to get the correct buyout base price.

- Bug summary:
When a user select several filter options the products page title just said the first filter type and value (e.g. "Material: Leather") instead of reflecting the combination of filters applied. This made it unclear to users what filters were active, especially when multiple attributes were selected.

The Fix:
I added a check if there are multiple active filters. If so, the title now displays "Filtered Results" instead of just the first filter. If only one filter is active, it continues to show the specific attribute type and value for clarity.

- Bug summary:
On info pages, the scrollspy functionality was not working correctly. When clicking on sidebar links, the page would jump to the correct section but the active link was not updating properly.

The Fix:
Scrollspy is changed to a static sidebar and scrollspy functionality can be added back in later if desired. 

---

[Back to README.md](README.md) • [Back to Top](#stocka---testing-documentation)