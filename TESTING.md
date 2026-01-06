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
- None currently.

### Solved Bugs
- Placeholder for resolved issues during development.

---

[Back to README.md](README.md) • [Back to Top](#stocka---testing-documentation)