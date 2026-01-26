# Stocka - Testing Documentation

<!-- ![alt text](documentation/testing/manual-testing/landing.png "Overview image of Stocka landing page") -->

<!-- 🔗 [**Live site**](https://_to_be_defined_) -->

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

<!-- Below is a summary confirming that each user story was manually tested across desktop and mobile devices.

**Story 1: Guest Browsing & Restricted Features**

**Test Summary:**  
Guests can browse products, view categories, and search items. Features such as adding items to cart, renting, or buyout options are hidden until login.

**Result:** Pass  

![Guest Browsing Test](documentation/testing/manual-testing/guest-browsing.png)

**Story 2: User Registration & Login**

**Test Summary:**  
Users can register and log in using email or social accounts. Incorrect credentials trigger proper error messages. Sessions persist until logout.

**Result:** Pass  

![Auth Test](documentation/testing/manual-testing/sign-in.png)
![Auth Test](documentation/testing/manual-testing/sign-up.png)

**Story 3: Product Purchase / Rent / Buyout**

**Test Summary:**  
Logged-in users can choose to **buy new**, **rent**, or **buy pre-owned** (if available). Stock availability and rental duration validations work correctly.

**Result:** Pass  

![Product Interaction Test](documentation/testing/manual-testing/product-detail.png)

**Story 4: Favorites / Wishlist**

**Test Summary:**  
Users can add items to a wishlist. Favorited items are stored in user profile and visible across devices.

**Result:** Pass  

![Favorites Test](documentation/testing/manual-testing/favorites.png)

**Story 5: Checkout Flow**

**Test Summary:**  
Cart and checkout process were tested for purchases and rentals. Payment and confirmation pages display correct totals, taxes, and shipping information.

**Result:** Pass  

![Checkout Test](documentation/testing/manual-testing/checkout.png) -->

---

### Automated Testing

Automated tools are used to ensure code quality, performance, and accessibility.

**Google Lighthouse:**
<!-- | Page | Screenshot |
|------|------------|
| Landing Page (Guest) | ![alt text](documentation/testing/automated-testing/lighthouse/landing-guest.png "Landing Page Guest") |
| Landing Page (Logged In) | ![alt text](documentation/testing/automated-testing/lighthouse/landing-loggedin.png "Landing Page Logged In") |
| Product List | ![alt text](documentation/testing/automated-testing/lighthouse/products-list.png "Product List") |
| Product Detail | ![alt text](documentation/testing/automated-testing/lighthouse/product-detail.png "Product Detail") |
| Favorites | ![alt text](documentation/testing/automated-testing/lighthouse/favorites.png "Favorites") |
| Cart & Checkout | ![alt text](documentation/testing/automated-testing/lighthouse/checkout.png "Checkout") | -->

**HTML & CSS Validation:**  
<!-- - Validate HTML using **W3C validator**.  
- Validate CSS using **W3C CSS validator**.  
- Tailwind classes may trigger warnings (acceptable).   -->

**JavaScript Validation:**  
<!-- - Use **JSHint / ESLint** to ensure clean JS code and correct logic.   -->

**Python / Django Validation:**  
<!-- - Use **PEP8 / flake8** to check Python files for style and syntax compliance. -->

**Accessibility Testing:**  
<!-- - Use **WAVE** to check contrast, semantic structure, alt text, and keyboard navigation.  
- Test both public and authenticated pages (base template ensures consistent accessibility). -->

---

### Manual Testing

**1. Global Layout & Navigation**

<!-- | Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 001 | Header & footer render on all pages | Visible, consistent across pages | pass |
| 002 | Navigation links work | All nav links go to correct pages | pass |
| 003 | Mobile menu works | Opens/closes correctly | pass |
| 004 | Responsive layout | All pages adjust on mobile/tablet/desktop | pass |
| 005 | Flash messages | Display correctly + dismissable | pass |
| 006 | No console errors | No JS errors in browser console | pass | -->

**2. Authentication**

<!-- | Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 101 | Sign-in/out links work | Redirects correctly | pass |
| 102 | Auth-required features blocked for guests | Rent, purchase, buyout, wishlist hidden | pass | -->

**3. Product Listing & Filtering**

<!-- | Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 201 | Products load | Images, titles, prices, status visible | pass |
| 202 | Category filters | Filters update displayed products | pass |
| 203 | Search function | Returns correct results | pass |
| 204 | Responsive grid | Adjusts to mobile/tablet/desktop | pass | -->

**4. Product Detail Page**

<!-- | Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 301 | Images load | All product images visible | pass |
| 302 | Buy / Rent / Buyout buttons | Visible and functional if allowed | pass |
| 303 | Add to wishlist | Works for logged-in users | pass |
| 304 | Responsive layout | Works on all breakpoints | pass | -->

**5. Checkout & Payment**

<!-- | Test # | Description | Expected Result | Pass/Fail |
|-------|-------------|----------------|-----------|
| 401 | Cart updates | Items added/removed correctly | pass |
| 402 | Price calculation | Correct totals, discounts, taxes | pass |
| 403 | Payment process | Successful transaction | pass |
| 404 | Confirmation page | Shows correct order summary | pass | -->

**6. Cross-Browser & Device Testing**

<!-- Tested on **Chrome, Safari, Firefox, Edge**, on devices like **iPhone, iPad, MacBook**.

| Test # | Description | Result |
|-------|-------------|--------|
| 501 | Layout & navigation | pass |
| 502 | Responsive images & grids | pass |
| 503 | Buttons & modals | pass |
| 504 | File uploads (if any) | pass |
| 505 | No console errors | pass | -->

---

## Bugs

### Known Bugs


### Solved Bugs
- Shopping Bag icon and the Price text were sitting side-by-side in a horizontal row. Because the price text takes up quite a bit of width, it was pushing the icon out behind logo. I stacked the price directly underneath the icon to solve this issue.
- In the mobile navigation, the collapsible submenu items were not scrollable when the content exceeded the viewport height. I added CSS styles to the navbar collapse div to set a maximum height and enable vertical scrolling.
- The mobile navigation menu's maximum height was set too low, causing some submenu items to be inaccessible on smaller screens. I increased the max-height to 90vh to ensure all items are reachable.
- In the mobile navigation, the submenu items were not collapsing when another submenu was opened. I added the `data-bs-parent` attribute to each submenu collapse div to ensure only one submenu is open at a time.
- On the product listing page, the attribute filters were displaying all available attributes, leading to a cluttered interface. I modified the view to only fetch and display a targeted subset of attribute types (material, brand, color, length, details) for filtering.
- The product listing page header had excessive top margin, causing unnecessary whitespace. I adjusted the margin to create a more balanced layout.
- Broken pagination controls:

The Problem: On a fresh page, there is no ? in the URL. Adding &page=2 creates an invalid URL. It only worked when I had filters because the filters already provided the required ?.

The Fix: I changed the links to always start with a ? and then loop through active filters. This ensures the URL is valid on a clean search and a filtered one. 

- Pagination controls were not preserving existing query parameters when navigating between pages. Gemini by Copilot suggested to update the pagination links to include all current GET parameters using `request.GET.urlencode`, ensuring filters remain applied during pagination.

-The Problem:
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

---

[Back to README.md](README.md) • [Back to Top](#stocka---testing-documentation)