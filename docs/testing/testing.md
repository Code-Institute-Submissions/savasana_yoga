# Savasana Yoga - Testing 


## Project Testing 

### CSS Validation 

1. CSS Validation

* Test: Check the base.css file, and ensure no errors are present.
    * Result: I checked the main css file (base.css) by using W3C CSS Validator. No errors were found.
* Note: There were 13 warnings; 

    11 of which were related to an unknown vender extension for -webkit-background-size, -moz-background-size and -o-background-size. I decided to ignore these warnings. 

    The two remaining warnings were 
    * Imported style sheets are not checked in direct input and file upload modes. Which I felt was also OK to ignore. 
    * Same color for background-color and border-color for the custom checkbox. This was intended, and so I chose to ignore this warning too. 

### JavaScript Validation

1. I tested each JavaScript script in JSHint. No errors were found in any of the JS scripts used.

### Navbar 

* Test: I checked all navbar links work as expected, and direct to the correct page. 
    * Result: All navbar links work as expected, and direct users to the intended page. 

* Test: To check the cart icon, to see if directs to the correct page. 
    * Result: The cart icon directs users to the intended shopping cart page.

### Footer

* Test: Social media icons grow in size on hover, and when clicked, opens a new tab, and takes users to the correct social media website.

    * Result: Social media icons grow in size when hovered, and when clicked a new tab is opened which directs users to the correct social media website. 

* Test: If the site map links direct users to the correct page.

    * Result: Each link in the site map correctly directs users to relevant page. 

* Test: Search Bar correctly searches for products relating to name, category, or description. 

    * Result: Search functionality correctly identifies a user's search parameters by querying results via name, category, or description. 

The search functionality was tested extensively by purposefully searching for products via their name, categories, and words used in the product description. The expected products were returned and successfully searched. 

I also tested the search functionality by searching terms I know would not provide any results. 

The test was successful and correctly displays a message to users that no results were found.


### Home App

* Test: Responsiveness and column change when changing screen sizes. 

    * Result: Product cards, and about image and test change to single rows when viewed on smaller devices.

* Test: Three products with a beginner category are displayed on the home page, and when clicked, direct users to the relevant product info page. 

    * Result: Product cards are displayed as expected, and directs users to the relevant product info page when clicked. 

* Test: Latest blog post entry is displayed as a snipper to the user. 

    * Result: Latest blog post entry is displayed as a snippet to the user.

* Test: To test whether the hover effect works on product cards displayed on Home Page. 
* 
    * Result: When hovering product cards, the hover effect works as intended. 

* Test: Tested to ensure that the index view correctly rendered the home page. 

    * Result: The view correctly rendered the home page. 
 
#### Home App Validation 

* Test: HTML markup for the index.html page, using W3Validator. 
    * Result: No errors or warnings were found. 

* Test: Checked the home app code using gitpod's python validator and pep8.
    * Result: No errors found.

* Test: I have also tested the Home App URL via Django Unit Testing.
    * Result: No errors were found. 

    ```
    class TestUrls(TestCase):

        def test_home_url_is_resolved(self):
            url = reverse('home')
            print(resolve(url))
            self.assertEquals(resolve(url).func, index)   
    ```

### Products

* Test: To check Product App URLs via unit testing. 

    * Result: No errors were found.

* Test: Product template to ensure that the correct page was rendered. 

    * Result: The correct templates were rendered for each product page. 

* Test: To confirm all products in the admin database were displayed on the products page. 

    * Result:  I checked the number of products in the admin database, and confirmed that all products were being displayed on the all products page.

* Test: To check that product information in models and admin matches displayed product information.

    * Result: Confirmed that information for each product in the admin database matches the information displayed on the product cards.

* Test: Product Info page rendered the correct product.

    * Result: Correct product displayed in product Info page. 

* Test: To check the responsiveness of product cards on smaller devices.

    * Result:  On smaller screen sizes, product cards are displayed in a column rather than a row of three.

* Test: To check whether the sort selector box correctly displays intended information.

    * Result: Each sort option displays the product in the intended order. For example: by ascending price, descending price, etc.

* Test: Hover effect on product card to check if shadow effect was triggered.

    * Result:  Shadow effect triggered on product cards are triggered when hovered.

* Test: To confirm that the edit button on product cards works as intended. 

    * Result: The edit button redirects the user to the edit product page and once edited the new information is updated in both the database and on the product page. 

* Test: To confirm that the delete button on product cards works as intended. 

    * Result: The delete button triggers the modal confirmation, and confirmed that once a product is deleted it is removed from the database and no longer displays on the website.  

* Test: To ensure that edit and delete buttons can only be accessed by admin accounts.
    * Result: When a user without an admin account views the product cards, the edit and delete buttons are not visible.

* Test: To ensure that a user without an admin account is unable to navigate to add/edit/delete products via URL manipulation
    * Result: A user is redirected to the home page if they try to access the add/edit or delete URL for products.

* Test: Product card categories link to product page filtered by selected categories.
    * Result: When clicking on a product card's category it redirects to the products page with only products of the selected category shown.

* Test: Check whether the add to cart button, adds the selected product to the user's shopping cart.
    * Result: When clicking the add to cart button on a product card, the success message is triggered and displays confirmation to the user what item is currently in their cart. I also checked the cart and confirmed that the product was successfully added.

* Test: Check whether information of added product matches the information of the product in the cart.
    * Result: The product information (price, day and time information, etc) matches the product information.
    
    
#### Add Products and Edit Product Form

* Test: To check whether Add Product form renders correctly, and displays expected fields.

    * Result: Add Product form renders as expected, and displays all expected fields.

* Test: To check whether Edit Product form

    * Result: Edit Product form renders as expected, displaying all expected fields, and populates previously inputted information.

* Test: To check whether any user can access the Add and Edit Products forms.

    * Result: Regular user account is unable to access the Add and Edit Product forms.

* Test: To check if admin users can access the Add and Edit Product pages.

    * Result: Admin users can access the Add and Edit product form pages.

* Test: Defensive Measures to prevent regular account users from accessing Add and Edit Product forms. 

    * Result: When a user without an admin account tries to Add or Edit a product, they are informed they do not have access to this page, and are redirected to the home page, and an alert is displayed that store owners can only perform the intended action/access the page.
    
        If a user without an admin account, and is currently not signed into an account attempts to access the add/edit product page, they are redirected to the sign-in page. 

* Test: To check if an empty Add Product form can be submitted. 

    * Result: Form will not submit if all fields are empty. 

* Test: To check if a form will submit with some required fields are correctly populated, while others left blank. 
    * Result: A form won't submit without all required fields populated.

* Test: To attempt to submit a form with incorrect values. Example: a letter in the price field, a letter in the number of sessions field. 

    * Result: A form won't submit unless the field has the correct value. For example, a number must be entered in the price field. 

    Note: I have attempted the same process with the Edit Product form; deleting the previous values, and replacing them with incorrect values, and blank fields, and the form won't submit. 

* Test: To check that products added via the Add Products form are stored in the database and displayed on the Products Page

    * Result: Newly added products correctly display on intended pages, and in the database.

* Test: Ensure that an edited product is displayed on the all_products page, product_info page, and displays in the timetable with the updated information

    * Result: Edited products display on intended pages with correct updated information.


#### TimeTable 

* Test: To check whether the Timetable page renders as expected and correctly displays all classes currently in the database.

    * Result: The Timetable renders as expected and correctly displays all classes currently in the database. 

* Test: To check if Media Queries and Timetable responsiveness works as intended on smaller devices.

    * Result: The media query for items in the timetable changes on smaller screens, as well as the reduction of margins to ensure a better mobile experience. 

#### Product App Validation 

* Test: HTML for all pages in the Product App using the W3Validator.
    * Result: No errors or warnings found.


* Test: Checked the code using gitpod's python validator, via the command python3 -m flake8 and as well as PEP8 Online Validator.
    * Result: No errors found.


* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.

```

class TestUrls(TestCase):

    def test_products_url_is_resolved(self):
        url = reverse('products')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_products)


    def test_products_url_product_detail(self):
        url = reverse('product_info', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, product_info)


    def test_products_url_add_product(self):
        url = reverse('add_product')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_product)


    def test_products_url_edit_product(self):
        url = reverse('edit_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_product)


    def test_products_url_delete_product(self):
        url = reverse('delete_product', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_product)


    def test_products_url_timetable(self):
        url = reverse('view_timetable')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_timetable)
        

```


### Shopping Cart

* Test: To check Cart App URLs via unit testing. 

    * Result: No errors were found.

* Test: Cart template to ensure that the correct page was rendered. 

    * Result: The correct templates were rendered for the cart page.

* Test: To test that navigation to the cart page with an empty cart displays the correct message.
    * Result: Confirmed navigation to cart page when the shopping cart is empty, displays message to the user that shopping cart is currently empty, and links users to the products page.

* Test: Check quantity form works as intended.
    * Result: All users can increase or decrease the quantity of a product in their shopping cart.

* Test: To ensure validation works on the quantity input form.
    * Result: User cannot decrease quantity below 1, or above 99. 

* Test: If a user can adjust the quantity of a product by manually entering the desired amount.
    * Result: Confirmed that a user can manually enter the quantity of a product in the quantity form.

* Test: If manually entering the quantity can break quantity validation.
    * Result: A user is unable to submit a quantity form with a number below 0, or above 99.

* Test: To check that quantity change is reflected in the total price. 
    * Result: Confirmed that once the quantity is increased with the quantity selector; the change is reflected in the price. 

* Test: Change in quantity is confirmed to the user.
    * Result: Confirmed once a user increases or decreases the quantity of an item, they are displayed a toast message confirming their action.

* Test: Confirm that products in the cart can be removed.
    * Result: I confirmed that when clicking the remove link in the cart, the intended product is removed.

* Test: Removal of product from the cart is confirmed to the user.
    * Result: When a user removes a product from their cart, a toast message is displayed confirming the correct product has been removed from the cart.

* Test: Product remain in cart if a user logs out of their account. 
    * Result: Product do not remain in the shopping cart once a user logs out of their account.

* Test: Check whether the cart counter accurately reflects the number of products in the cart.
    * Result: The cart counter correctly displays the number of items in a cart. 

* Test: Ensure checkout button leads to checkout page and form.
    * Result: I confirmed that when clicking the 'checkout' button users are directed to the checkout form.


#### Cart App Validation 

* Test: HTML using W3Validator:
    * Result: No errors or warnings found.

* Test: Checked the code using gitpod's python validator, via the command python3 -m flake8 and as well as PEP8 Online Validator.
    * Result: No errors found. 

* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.

```
class TestUrls(TestCase):

    def test_cart_url_is_resolved(self):
        url = reverse('view_cart')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_cart)


    def test_cart_url_add_to_cart(self):
        url = reverse('add_to_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_to_cart)


    def test_cart_url_adjust_cart(self):
        url = reverse('adjust_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, adjust_cart)


    def test_cart_url_remove_from_cart(self):
        url = reverse('remove_from_cart', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, remove_from_cart)

```

### Checkout App

* Test: Unit test the Checkout App URLs. 
    * Result: No errors were found. All checkout URLs are correct. 

* Test: Checkout app renders correct templates.
    * Result: All templates are rendered correctly. 

* Test: To check if products in the cart are accurately reflected on the checkout page.
    * Result: I confirmed that products in the cart are correctly displayed on the checkout page when a user clicks the checkout button

* Test: Check whether a logged-in user with pre-populated profile information has the relevant information pre-filled in the checkout form.
    * Result: A user's profile information is pre-filled in the checkout form.

* Test: If a user fills out the checkout form and selects the option to 'save information to profile', that information is transferred to their profile page.
    * Result: If a user selects the 'save info' box, once checkout is completed, a user's profile information is populated with the information from the checkout form.

* Test: The validity of the checkout form. 
    * Result: All required fields are necessary to complete the checkout process. 

* Test: To check whether checkout form can be submitted with incorrect values
    * Result: The checkout form is unable to be submitted if the values of a field are incorrect.
 
* Test: Users are directed to the checkout success page after successfully submitting the checkout form
    * Result: I confirmed that once checkout is completed, a user is directed to the checkout success page. 

* Test: The checkout success page correctly displays a checkout summary.
    * Result: The Checkout success page renders the correct template

* Test: Checkout summary information matches the information from the checkout form and the products purchased
    * Result: I confirmed that the checkout summary currently matches the information inputted on the checkout form, as well as the correct products purchased.

* Test: Whether a user receives an order confirmation toast after checkout
    * Result: Once an order has been completed, a user is correctly shown a success message with an order number and a message that they will receive a confirmation email

* Test: Check whether the user receives an order confirmation email
    * Result: I confirmed that the user receives a checkout confirmation email with a brief checkout summary.

* Test: Check whether the checkout confirmation email contains the correct order number.
    * Result: The checkout confirmation email contains the correct order number. 

* Test: Whether order number on user's profile is displayed after checkout.
    * Result: I confirmed that once checkout has been successful, that the order number is visible on a user's profile.

* Test: To confirm if order history reflects the user's orders, and contains the correct information.
    * Result: I confirmed that the order history on a user's profile accurately reflects their previous orders. 

* Test: Ensure that stripe webhook is successful. 
    * Result: Confirmed that the stripe webhook was successful; and checked the stripe events page to ensure the webhook and payment were successful. 


#### Checkout App Validation 

* Test: Check the checkout.css file and ensure no errors exist.
    * Result: No errors were found.
        * Note: One warning was found, related to an unknown vender extension. I also chose to ignore this warning. 

* Test: HTML all pages in the Checkout App using W3Validator
    * Result: No errors or warnings found.

* Test: Checked the code using gitpod's python validator, via the command python3 -m flake8 and as well as PEP8 Online Validator.
    * Result: 2 errors in the  webhook hander file due to lines being too long. Unable to make line shorter without breaking the code.

* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.

```
class TestUrls(TestCase):

    def test_checkout_url_is_resolved(self):
        url = reverse('checkout')
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout)

    def test_checkout_url_checkout_success(self):
        url = reverse('checkout_success', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, checkout_success)

    def test_checkout_url_cache_checkout_data(self):
        url = reverse('cache_checkout_data')
        print(resolve(url))
        self.assertEquals(resolve(url).func, cache_checkout_data)

``` 

### Profile 

* Test: Whether the Profile app URLs work as intended.
    * Result: Profile app URLs testing with Django unit testing, and no errors were found. 
    
* Test: Profile page renders the correct template
    * Result: The profile page renders the correct template.

* Test: Profile heading matches the user's profile name.
    * Result: I confirmed that the Profile page's heading correctly displays a user's account name. 

* Test: Whether a user can edit their profile information and if the information is reflected in the checkout form.
    * Result: Confirmed that a user can edit and update their profile information, and this update is reflected in the checkout form. 

* Test: Whether a user can remove their information from their profile.
    * Result: A user can remove their information from their profile.    


#### Profile App Validation 

* Test: HTML using W3Validator:
    * Result: No errors or warnings found.

* Test: Checked the code using gitpod's python validator, via the command python3 -m flake8 and as well as PEP8 Online Validator.
    * Result: No errors found. 

* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.

```
class TestUrls(TestCase):

    def test_profiles_url_is_resolved(self):
        url = reverse('profile')
        print(resolve(url))
        self.assertEquals(resolve(url).func, profile)


    def test_profiles_url_order_history(self):
        url = reverse('order_history', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, order_history)

```

### Sign In and Sign Out Form

* Test: To attempt to log into the account with an incorrect password and correct email address.

    * Result: Unable to log in and the user is displayed message that email and/or password is incorrect. 

* Test: To attempt to log into the account with the correct password and incorrect email address

    * Result: Unable to log in and the user is displayed message that email and/or password is incorrect.

* Test: To log into the account with the correct email and correct password.

    * Result: The user successfully logs into the account, and the message is displayed to inform them log in was successful.

* Test: Sign out link directs users to sign out the form and correctly signs out the user from the session.

    * Result: User correctly logs out of the account, and displayed a message to confirm they have been logged out.


#### Sign In and Sign Out Page Validation 

* Test: HTML Sign In and Sign out pages using W3Validator:
    * Result: No errors or warnings found.

* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.

### Blog

* Test: Django Unit testing Blog App URLs.
    * Result: No error with URLs, all URLs for Checkout App are correct. 

* Test: Whether correct templates are rendered.
    * Result: All blog app templates are rendered correctly.

* Test: Whether each blog post is displayed on the all blogs page.
    * Result: All blog posts are correctly displayed on the blog page. 

* Test: The number of blog posts in the database matches the number displayed on-page.
    * Result: All blog posts in the database match the number of blog posts displayed.

* Test: To check whether each blog post is displayed as a snippet on the blog.html page.
    * Result: I confirmed that each blog is displayed as a snippet

* Test: Whether the 'Read More' button on the blog card directs users to the relevant blog post.
    * Result: Confirmed that the 'Read More' button on a blog card directs users to the relevant blog post detail page. 

* Test: Check if the format and blog information is correct. 
    * Result: Confirmed that the format and blog information is correct. I.e the date created, and the author, as well as the correct image. 

* Test: To check if all text in the blog post is displayed on the blog detail page.
    * Result: Confirmed that all text was correctly displayed on the blog detail page. 

#### Blog Comments 

* Test: The user can leave a comment without creating an account.
    * Result: A user is unable to leave a comment without being signed into their account. If a user is not signed into their account and attempts to leave a comment, they are directed to the log-in page.

* Test: 'Leave a comment' button directs logged-in users to the comment form.
    * Result: I confirmed that a logged-in user is directed to the add comment form when clicking on the leave a comment button. 

* Test: Leaving a comment redirects users to a specific blog post page.
    * Result: I confirmed that when a user leaves a comment, they are redirected to the blog detail page. 

* Test: After submitting a comment, the user is informed their comment is awaiting moderation.
    * Result: Confirmed that when a user leaves a comment they are shown a toast message that their comment is awaiting moderation. 

* Test: Whether comments awaiting moderation are visible to all users.
    * Result: I confirmed that comments awaiting moderation are not displayed under the blog post/ and other users are unable to see the comment. 

* Test: Admin users can see comments awaiting moderation
    * Result: I confirmed that when an admin user checks a blog post, they can see all comments awaiting moderation. 

* Test: If the message is displayed to admin users that no comments are awaiting moderation. 
    * Result: I also confirmed that if there are no comments awaiting moderation, the admin user will be displayed text to indicate that there are currently no messages to moderate

* Test: Whether admin users can approve or remove pending comments. 
    * Result: I confirmed that an admin user can approve or remove a pending comment 

* Test: If approved comments are visible to users.
    * Result: I confirmed that all users can see comments which have been approved by an admin. 

* Test: If removed comments are visible to users.
    * Result: I confirmed once a pending comment has been removed; it is not visible for any users, and it is removed from the database. 

* Test: Comment counter does not count comments that are pending moderation
    * Result: Confirmed that the comment counter only counts comments which have been approved by an admin. The comment counter does not take into account comments which are currently in moderation 

* Test: Whether a non-admin user can remove another user's comments.
    * Result: A non-admin user can not remove another user's comments. 

* Test: Whether a non-admin user can remove comments they created.
    * Result: A non-admin user can remove comments they created.

#### Blog App Validation 

* Test: HTML for all pages in Blog App using W3Validator:
    * Result: No errors or warnings found.

* Test: Checked the code using gitpod's python validator, via the command python3 -m flake8 and as well as PEP8 Online Validator.
    * Result: No errors found. 

* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.

```
class TestUrls(TestCase):

    def test_blog_url_is_resolved(self):
        url = reverse('view_blog')
        print(resolve(url))
        self.assertEquals(resolve(url).func, view_blog)

    def test_blog_url_blog_post_detail(self):
        url = reverse('blog_post_detail', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, blog_post_detail)

    def test_blog_url_add_blog_post(self):
        url = reverse('add_blog_post')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_blog_post)

    def test_blog_url_edit_blog_post(self):
        url = reverse('edit_blog_post', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_blog_post)

    def test_blog_url_delete_blog_post(self):
        url = reverse('delete_blog_post', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_blog_post)

    def test_blog_url_comment_approve(self):
        url = reverse('comment_approve', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, comment_approve)

    def test_blog_url_comment_remove(self):
        url = reverse('comment_remove', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, comment_remove)

    def test_blog_url_edit_comment(self):
        url = reverse('edit_comment', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, edit_comment)

```


### Contact App

* Test: To attempt to submit the form without an email address.

    * Result: Unable to submit the form without an email address. 

* Test: To attempt to submit the form with characters that exceed the max length in the name, email, and subject fields.

    * Result: Unable to submit the form if the characters exceed the max length.

* Test: To check whether a user receives an email to confirm their message was sent.

    * Result: The user successfully receives an email after they have submitted the contact form.

* Test: Whether the information in the contact form is accurate and saved in the database.

    * Result: The information in the contact form is stored in the database, and correctly matches the information the user placed in the form.

* Test: Whether the contact page loads the correct template and has the correct URL.

    * Result: The contact page loads the correct template and has the correct URL.


#### Contact App Validation 

* Test: HTML markup for the contact page using W3Validator:
    * Result: No errors or warnings found. 

* Test: Checked the code using gitpod's python validator, via the command python3 -m flake8 and as well as PEP8 Online Validator.
    * Result: No errors found.

* Test: I have also tested the App's URL via Django Unit Testing.
    * Result: No errors found.


## Testing User Stories

* Test: I want a website that allows me to book yoga classes.
    * Result: Users can add yoga classes to the shopping cart and purchase these classes via the checkout form.
        * You can view this [here](./user_stories/user-story-purchasing.png) 

* Test: I want a website that provides me information about the yoga classes.
    * Result: Each yoga class has a description that provides information on the class, as well as a category attached to the class to inform the user of its difficulty level. In addition, each product card provides days and times of the particular yoga class.
        * You can view this [here](./user_stories/user-story-description.png)

* Test: I want to be able to book multiple classes.
    * Result: A user can increase the quantity of each product in their shopping cart. In addition, a user can purchase multiple yoga classes at a time.
        * You can view this [here](./user_stories/user-story-multiple-purchase.png)

* Test: I want to be able to review and change my cart before purchasing classes.
    * Result: A user can increase or decrease the quantity of each product, and a user can also remove a product from their shopping cart.
        * You can view this [here](./user_stories/user-story-quantity.png)

* Test: I want to receive an email confirmation after booking a class.
    * Result: Each time a user completes the checkout form, they receive a confirmation email regarding their recent purchase.
        * You can view this [here](./user_stories/user-story-confirmation-email.png)

* Test: I would like a blog to read more about the yoga studio, and yoga in general.
    * Result: The website features a blog app so users can read more about the yoga studio, and other yoga-related information.
        * You can view this [here](./user_stories/user-story-blog.png)

* Test: I would like the ability to comment on blog posts.
    * Result: A logged-in user can leave a comment on any blog post.
        * You can view this [here](./user_stories/user-story-blog-comments.png) and [here](./user_stories/user-story-blog-comment-form.png)

* Test: I would like the ability to remove comments I make on a blog post.
    * Result: A logged-in user can remove the published comments they have made.
        * You can view this [here](./user_stories/user-story-comment-remove.png) 

* Test: I want the ability to filter classes between difficulty levels.
    * Result: A user can filter classes by categories, which are the difficulty levels for all yoga classes offered.
        * You can view this [here](./user_stories/user-story-class-filter.png) 

* Test: I want the ability to view a timetable or schedule for yoga classes.
    * Result: A user can see all the times and days for yoga classes offered on the timetable page.
        * You can view this [here](./user_stories/user-story-timetable.png) 

* Test: I want a website that is easily accessed on my mobile phone and tablet.
    * Result: The website was developed with a mobile-first approach and is responsive across all devices.
        * You can view this [here](./user_stories/user-story-mobile.png) 

* Test: I want a website that is easy to understand and navigate.
    * Result: All links are indicated, and icons are used where possible to help a user identify different pieces of information. In addition, many links are clearly stated and related to their purpose. Finally, a user can quickly navigate to different pages via the navigation bar or the site map in the footer. Throughout the website, there are call-to-action buttons, as well as a back button to allow a user to move between pages without using the browser buttons.
        * You can view this [here](./user_stories/user-story-navigate.png) 

* Test: I want to have my profile store my information.
    * Result: Each user that creates an account, can store their personal information on their profile.
        * You can view this [here](./user_stories/user-story-profile.png) 

* Test: I want to view my order history on my profile.
    * Result: Every time a user completes the checkout process, the order is saved on their profile, and the user can view these orders as often as they want.
        * You can view this [here](./user_stories/user-story-order-history.png) 

* Test: I want my profile to be password protected.
    * Result: A user is unable to create an account without completing the signup form which requires a password. All accounts are password protected.
        * You can view this [here](./user_stories/user-story-password.png) 

* Test: I would like to be able to follow the website's social media accounts.
    * Result: A user can follow the website's social media accounts by locating the social media icons in the footer. These are shown on every page, and when clicked, will open a new tab of the website's social media account.
        * You can view this [here](./user_stories/user-story-social-media.png) 

* Test: I would like to be able to search for classes.
    * Result: On every page, in the footer, there is a search bar. This allows users to quickly search for different yoga classes via category, name, or keywords from a classes' description.
        * You can view this [here](./user_stories/user-story-searchbar.png) 


## Other Automated Testing

I tested this project via Google Lighthouse and all pages have passed the tests for Performance, Accessibility, Best Practices and
SEO.

I have also tested this project via Google's Mobile Friendly Test. The project had passed the test, and declared a mobile friendly website.


## Troubleshooting

Throughout the development of the website, I encountered several problems and issues. Through research, and trial and error, solutions were found, or in some cases, other ideas were instead implemented.

I have documented these issues below.

1. The first major hurdle I faced when developing this project, was the product counter for the shopping cart icon. 
    I wanted the cart icon to display to the user the number of items currently in their cart in the form of a small badge number. 

    I initially added the number of products with Django templating {{ product_count }} inside a span and tried to style this to my liking. The issue I faced, was the I was unable to get the product counter to sit exactly where I wanted it to (at the top-right of the cart icon). Upon researching different ideas and implementations on StackOverflow, I found a post which assisted with the placement and CSS of this feature. 

    The trick was to use the CSS placement 'vertical-align: top;'. The StackOverflow post can be found [here](https://stackoverflow.com/questions/51304169/how-to-put-the-number-at-top-right-corner-of-cart-icon)

    With the CSS created, and the Django templating with {{ product_count }} the desired result was achieved.

2. When creating the Timetable page, I wanted to display the days of the week in the following order: Monday to Sunday. When I initially created the page, the data was ordered by the latest entry, and the days of the week were not ordered. I felt this was not a good UI. One possible solution to this was to remove the products and input them in order so the latest entry would be Monday, then Tuesday. However this did would not resolve the issue, and if a new product was created the unordered days of the week would be present. 

To solve this, I re-created the days of the week choices in the Product Model. 

```
    DAYS_OF_THE_WEEK = [
        ('1', 'Monday'),
        ('2', 'Tuesday'),
        ('3', 'Wednesday'),
        ('4', 'Thursday'),
        ('5', 'Friday'),
        ('6', 'Saturday'),
        ('7', 'Sunday')
    ]
```

Then I added a MetaClass to the Product Model: 

```
class Meta:
        ordering = ['day']

```

This allowed me to have all products displayed by the days of the week. 


3. I faced another issue with the Timetable page when trying to display the days of the week. As I had re-arranged the choice field for the days of the week, when I was creating the Timetable page and used the Django templates to target and display these days using {{ product.day }} the days of the week were displayed as '1', '2', '3', etc rather than the values of 'Monday', 'Tuesday' etc. 

I searched through the Django documentation, I came across the get_FOO_display() method. To better understand how to use this method in Django templates, I researched this method on StackOverflow and found the following post: https://stackoverflow.com/questions/4320679/django-display-choice-value

From this post, I learned that I could target the choices field values by using 

```
{{ product.get_day_display }}
```

3. I wanted to implement a maximum and minimum value for the number of sessions a yoga class could have. 

Upon researching how to implement these restrictions for the Product Model, I came across the following validators on Django's official documentation, which can be seen [here](https://docs.djangoproject.com/en/3.2/ref/validators/#maxvaluevalidator)

This provided me with the correct validation logic to implement the restrictions I desired. 

4. When I was initially creating the website, I had two apps for products: I had an app for Yoga Workshops, and I had an app for Products (books, yoga equipment, etc). I felt that this resulted in a lot of duplicated code, and templates. As a result, I decided to completely remove the Workshop App and merged the model into the Product Model. I then separated the different types of products by categories. 

However, I also felt that the project had begun to lose focus. I thought the promoting of the yoga studio, and the yoga classes were far more important than the selling of yoga equipment/books, etc. I finally decided to completely remove all products that were not yoga classes, and by doing so, the website felt much more focused.

5. I had a persistent issue with excessive overflow with some containers. As a result, the home image didn't fit as I would like it to. I initially removed the padding and margins from the container-fluid. Doing so created overflow for other container-fluid sections, so the solution was to target the specific container where the image was placed. 


```
.home-image-container {
    padding: 0px;
    margin: 0px;
}
```

In addition, there was still some excessive overflow, and I opened chrome dev tools, and targetted the excessive overflow section of the home page, and saw that there was a missing div in closing the about section container. I added the necessary closing div, and the issue was solved.

6. I had an issue when creating the navigation bar, specifically with utilizing the icons for the shopping cart, and profile. I wanted to keep the navbar brand visible on mobile devices, however, When using both the profile icon and cart icon, resulted in a squashed experience. There was very little space between the navbar brand and the icons, and the only way to create space between these items was to place the icons in the mobile dropdown menu, or else on a new line below the navbar brand. 

I decided to remove the profile icon, and instead place it as a nav-link 'Account'. This allowed me to keep the navbar brand and the shopping cart icon on mobile devices.


7. With regards to the timetable page, I faced several issues with how I wanted to achieve, and display this information. Initially, I created a separate app for the timetable and created the table with the currently offered classes for different days of the week. I felt this was not optimal, as if an admin wanted to remove, edit or add a yoga class, they would also have to make this change for the timetable model. I decided to remove the timetable app, and merge it with the Products app, and include the timetable data into the Product model. This created a streamlined experience for admin users to quickly update the yoga class timetable information, and for the timetable, page to always be updated and accurately reflect the current products being offered to users.

8. I was having issues with getting the footer to stay at the bottom of the page. While developing the website, I didn't encounter this problem as the content on each page was enough to push the footer to the bottom of the page. However, on some pages such as the forgotten password page, and an empty shopping cart page there would be a lot of space below the footer.

When attempting to have the footer stay at the bottom of the page, I first tried to use the class 'sticky footer', however, I did not like the UI and UX of a fixed footer on scroll. 

Instead, I wanted the footer to remain at the bottom of the page, regardless of content, while also not being 'sticky' and being shown to a user at all times. 

I found a solution on CSS-tricks, which can be seen [here](https://css-tricks.com/couple-takes-sticky-footer/) 

I opted to use the flexbox solution, which allowed the footer to remain responsive, and dynamic. The solution was to use flex-direction column on the body, and wrap the block content in a div with flex: 1 0 auto, and use flex-shrink: 0 on the footer.

9. I encountered an issue when adding blog posts, the issue rested with the required field in the model 'author'. Each time, a user created a blog post, they were required to select the author. If there were more than one admin account, the admin user could select an admin user as the author of a blog post, even if they were not the account that added the blog post. I felt this was not a good design, and I wanted the author to be the user who was currently in session. 

When I attempted this

```
blog_post.author = request.user
blog_post = form.save()
```

I received an error that 'blog_post' is not defined. 


I did not like this and instead wanted the author to be the current user in session. 

When I tried this, I first got an error that blog_post is not defined. Upon inspection, I realized this error occurred because the 'blog_post.author' was being referenced before the saving of the form: 'blog_post = form.save()'

I initially thought a quick fix for this would be to simply re-arrange the code to read 

```
blog_post = form.save()
blog_post.author = request.user
```

This did not solve the issue, and I encountered an error that 'blog_post.author cannot be NULL as it is a required field.

I quickly realized my mistake, and that I first need to save the form to reference the blog_post, but to not save it until after the blog_post.author is assigned as the request.user.

Upon research, I found the best way to achieve this is to use the 'commit=False' method. This method was also used on the order form.

Once I re-arranged the blog code to the following:

```
blog_post = form.save(Commit=False)
blog_post.author = request.user
blog_post = form.save()

```

The blog post is first saved without being committed to the database, then the author is assigned as the current user in session. Finally, the form is saved to the database.


10. When developing the blog, I faced a dilemma as to how I wanted the blog comments to function. I did not a user's comments to be posted automatically. I wanted an admin to be able to approve or deny a pending comment before being visible on the website. I felt that the content should be moderated and the focus of comments to be kept related to the content of the website: Yoga. 

To achieve this, I decided to place all comments in a field named 'approved_comments' with a Boolean field. In the blog views.py I set the 'approve_comments' field to False to ensure that these comments did not show. 

Initially, when I created this the following would happen: When a user leaves a comment on a blog post, they are alerted that their comment is awaiting admin approval. 

To approve a comment, an admin user must log in to the admin panel, go to the comment database, and manually approve comments from here. 

I felt this was not the best experience for an admin of the website, and so I wanted to be able to approve or deny pending comments from the specific blog post, on the website.

To achieve this I created a new variable - awaiting_approval_comments, which stored all comments with an active=False. I then created a for loop to display all comments with these parameters. From here, I created a function to change the boolean value from false to true and linked this to the approve button. 

To help with understanding how to approve or deny comments, I used a tutorial which can be seen [here](https://tutorial-extensions.djangogirls.org/en/homework_create_more_models)

When an admin is viewing a blog post, they can see if there are any pending comments awaiting admin approval, and they can approve or deny these pending comments from the blog post page.

This allowed me to create an on-site moderation functionality.

11. I experienced some issues when creating the Contact app. I created each app before deployment. However, this app was created after I had deployed it to Heroku. Once I created the contact app locally and tested it locally, I committed my changed and pushed it to Github. I then tested the contact form on Heroku. 

The form was rendered as expected, however once submitting the form I was redirected to the 500 error page. To debug this issue, I switched DEBUG to True and repeated the previous steps. After submitting the form, I received the following error message "Relation does not exist". I logged in to the admin section of the website, and when clicking on the Contact Forms, I was directed to the error again. 

I knew then that the contact app had not migrated to Heroku. The fix was to force run the models migrating to Heroku

```
heroku run python3 manage.py migrate --plan
```

I could see the contact app in the pending changes and so I entered the command 

```
heroku run python3 manage.py migrate 
```

I turned DEBUG to off and repeated the steps above. The contact form was submitted as intended, and the data was stored in the database. 


12. When testing the contact form, I noticed that users could submit the form multiple times by repeatedly clicking the submit button while the form was being submitted. To fix this I created a JavaScript script to disable the submit button when the form was being submitted. This allowed the form to be submitted once and avoided the possibility of being submitted multiple times by rapid clicks. 

```
$('#contact-form').submit( function(event) {
    // disable to avoid double submission
    $('#submit_button').attr('disabled', true);
});
```

13. I had an issue with the checkout app once I deployed the project to Heroku. When a user purchased a product, two order items were created, with one order having a grand_total of 0. 

A screenshot of the bug can be seen [here]((./testing_images/purchasing-bug.png). 

I initially thought the issue was with the webhook_handler.py file, and checked stripe events to see if I could troubleshoot the issue there. However, everything seemed fine on that end. Upon inspection, I realized there was an error in the signals.py field where both signal function were named the same. 

I changed the duplicated signal 'update_on_delete'. I then re-tested the checkout process, and confirmed that everything was working as expected. I also checked the order line items in the admin panel, and could see that the order_total and grand_total had matched.

14. A site-breaking issue was found when testing the removal of products. If a product is removed while it is currently in a user's cart, each page is then shown the 404 error page. 

I created the following code thinking this would be a temporary fix. 

```
 cart = request.session.get('cart', {})
    if product_id in list(cart.keys()):
        remove_from_cart(request, product_id)
    product.delete()
```
I wanted to check if the product is currently in the cart before deleting it. If the product is in the cart, then remove the product from the cart. And then delete the product. 

However, it would not work when tested. The same error was displayed. To further debug this, I added the following print statements to the add_to_cart view

```
print(item_id)
print(cart.keys())
```

I realized the the code above would not work as the item_id is stored as a string. 

I changed the code above to:

```
 cart = request.session.get('cart', {})
    if str(product_id) in list(cart.keys()):
        remove_from_cart(request, str(product_id))
    product.delete()

```

This method has worked fine as an immediate fix to this error. However, after speaking about this issue with Code Institute's Tutors, I realized that this solution is not ideal, because if an admin deletes a product, while it is currently in the cart of a non-admin user, the user would be shown a 404 page. 

An alternative and safer solution was presented to be Code Institute's tutor Ed. Who suggested to create a copy of my cart dictionary, loop over the new dictionary and implement an except statement for when the product no longer exists. In the end, this was the approach I implemented. 

I first created a new dictionary, looping over the key:value pairs from the cart_items dictionary. I then set the product_id variable to equal the item_id. I created a try and except statement, to check whether the product_id is in the database, and if it does not exist to remove the product from the current cart.

With this completed, I recreated the issue, and confirmed that it no longer redirects users to a 404 page.

