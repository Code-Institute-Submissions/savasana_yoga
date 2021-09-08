# Savasana Yoga

Savasana Yoga is a website to promote the benefits of yoga. The aim of this website is to promote, discover and book yoga classes offered by Savasana Yoga Studio. 

[You can view the live project here]()

![Website Overview]()

## Overview

A website for people who wish to practice yoga, and book yoga classes. The website also offers people the opportunity to learn more about the benefits of practicing yoga via blog entry posts.

The website is built with django and has an e-commerce focus, to faciliate the booking of classes. The website maintains responsiveness across all devices; desktop, tablet, and mobile. 

The website was built with a mobile-first approach as most users now visit website via their mobile.

The website features a fully functional e-commerce store, to allow users to purchase yoga classes. The website also features a register and login form, to allow users to create their own profile, which allows for a quicker booking process, and allow a user to view their order history. 


The main goal of this website is to promote the practice of yoga, highlight it's benefits, and offer classes for both beginner and advanced yogis.

The website also features a blog, which promotes the benefits of yoga, provides announcements for the yoga studio, and allows users to comment on blog posts. 

Finally, the website also provides admin features to manage the yoga classes, by editing, deleting and adding new classes, and blog posts, by adding, editing, and removing blog posts, as well as the ability to moderate by approving or removing pending user comments.


## User Stories

* I want a website that allows me to book yoga classes.
* I want to receive an email confirmation after booking a class.
* I would like a blog to read more about the yoga studio, and yoga in general.
* I would like the ability to comment on blog posts.
* I would like the ability to edit or remove comments I make on a blog post.
* I want the ability to filter classes between difficulty levels.
* I want the ability to view a timetable or schedule for yoga classes.
* I want a website that is easily accessed on my mobile phone and tablet. 
* I want a website that is easy to understand and navigate.
* I want to have my own profile to store my information.
* I want to view my order history on my profile.  
* I want my profile to be password protected.
* I would like to be able to follow the website's social media accounts.

## Project Goals

* I want to promote the yoga classes offered by Savasana Yoga Studio.
* I want to allow users to book yoga classes.
* I want to grow the website's social media presence. 
* I want users to be able to create their own profile, and view their order history.
* I want users to understand and navigate the website upon their first visit. 
* I want users to be able to filter classes based on difficulty level.
* I want to promote the benefits of yoga, and the studio's classes via blog posts.
* I want to allow users to comment on blog posts.
* I want to be able to store all bookings in a database. 
* I want to allow users to view the days and times for yoga classes.


## UX 


The practice of yoga can have many benefits, including stress management, relieiving anxiety, improving quality of sleep, fitness and flexibility. I created this website to help promote the practice of yoga, and facilitate a place where people can book yoga classes offered by Savasana Yoga Studio.


## Strategy 


The goal of this website it to offer accesible yoga classes for beginners and advanced yoga enthuastis. The website was built with a focus towards newcomers to yoga, in order to make yoga seem less intimiatding and showcase the variety of yoga classes offered.

The secondary goal of the website, is to promote Savasana's Yoga Studo by driving users to the studio's social media accounts, and promoting the studio on the website via the blog.


### Business Goals: 

* Promote booking of variety of yoga classes offered.
* A simple and easy to navigate website with a clear purpose.
* Mobile-first design to increase ease of use for those without PCs.
* Increase web-presence to grow the brand via blog and social media accounts.


### User Goals: 

* Searching for a yoga class to book.
* Clear outlines of yoga class difficulty levels.
* A profile to save my information and order history.
* A blog to read about yoga, and comment to share my thoughts.
* Mobile-friendly website as the majority of users browses via mobile. 
* An easy-to-understand and navigate website. 
* A website that allows me to filter yoga classes via difficulty.
* A password protected profile.
* To follow the website's social media accounts. 
* To view the days and times for offered yoga classes.



## Scope 

The Scope and features of this project were based on a personal interest in the practice of yoga. 

When I first became interested in yoga, I found it difficult to find a place with a number of different types of classes, and an easy-to-understand website where I can check which classes are on at certain times, and which classes best suit my experience level.

This resulted in a feeling of being overwhelemed, and unsure what to book/attend. 

As a result, I created Savasana Yoga to faciliate an easy-to-navigate and easy to understand website, that offers a wide variety of classes, and allows the filtering of classes based on a user's experience level.


## Structure 

I feel its very important to provide users with a simple, and easy-to-navigate experience and interface. The goal of the website was to feel professional, approachable and promote a user's confidence when navigating throughout the website. 

The home page features a large image, a blurb on the benefits of yoga, a call-to-action button to encourage users to book a class, and some information about the yoga studio itself. 

I have also created a footer, which allows for quick navigation via a basic site map. I have also populated the footer with social media links, and a search bar to quickly search for yoga classes. 

As there are a number of pages in this website, I have provided a summary of each page in the 'Features' section below.


## Skeleton 

All wireframes were created using Balsamiq.


## Surface 

### Images

There are two main aspects of image use throughout this app. Static and Dynamic images. 

1. Static Images 
- The first is by storing images in a static folder. I have stored the home page images here, as they will not be altered.

I choose this landing page image, as the photo is quite zoomed out, and allows a lot of space, and breathing room on the left-hand and right-hand side of the person in the image. I also choose to use this image because it had a lot of white in it, and I wanted the home page to match the background colors of the website; greys and whites.  

2. Dynmaic Images
- All product images are stored via AWS. 

Since a user with admin privileages can edit, add, and remove products, the images can be changed. I decided to use AWS to host the images, so each time an image is updated in the database it is reflected on Heroku. In addition, storing the images on AWS avoids the risk of the images being removed once the website is deployed and running on Heroku.



### Colours

Yoga is a relaxing and sometimes viewed as an elegant form of excercise. I wanted to maintain that philosophy when developing the website. I personally felt that using very little color, was a way of achieving this. 

I decided to keep the background-color and the navigation bar the same type of white (#).

In order to split the screen space up, and offer a bit of diversity, while still maintaining the feel of a clean, relaxing and elegant look, I used an off-grey(#) for the footer. I felt this added some variety, and also complimented the white background-color. 

For the buttons, I have decided to use two different kinds. 

I opted to use a a light blue (#) for the booking and checkout buttons. And a red (#) for the back buttons. 
I felt this colors were subtle, and warm without providing too much a contrast and boldness from the white background-color.


### Font 

I decided to use 'Open Sans' as the main font for this website. This font is used on all body text besides headings. I chose Open Sans because of its simplicity, elegance, and versatility. It's an easy-to-read font, but I also feel it has some character. 

For the headings, I decided to use 'Montserrat'. I chose this font becuase it paired well with Open Sans, and also maintained the simplicity and elegance that Open Sans provided. 


### Icons 

I initially decided to use a lot of icons throughout the website, however as development continued, I felt that the icon were distracting. For example, I first had an icon for the Account nav-item, but I felt the navigation bar looked cleaner without the icon. 

I have utilized icons sparingly throughout the website. On the All Products page, I used a calendar icon to indicate a link to the Timetable page. 

I have utilized Font Awesome's Social Media icons to display the yoga studio's social media accounts. These are located in the footer of the website. When a user clicks the icon, a new tab opens, directing them to the relevant social media website. Currently, these links do not direct to a real profile as the project was built for a fictional yoga studio.

I have also used Font Awesome's hamburger bars for the navigation menu on mobile devices. 

## Features


### Current Features

The website features a fully functional e-commerce store to book yoga classes, pasword-protected profiles, a dynamic timetable to display current offered yoga classes, a fully functional blog to display posts, news and updates. 

In addition, the website was developed with a mobile-first approach and is fully responsive across all devices. 

I have provided more details on the features of the website below:

#### The Navigation Menu

The navigation menu is consistent for all users, except for one small difference. Admin users have an extra menu item in the Account dropdown called 'Class Management'. This link directs admin users to a form which allows them to create a new yoga class.

The navigation menu is divided into 6 nav-items:

- Home: which links users back to the homepage.
- Classes: which is a dropdown menu to display the yoga classes categories (Beginner and Advanced classes).
- Timetable: which links users to a dynamic timetable which displays the days and times yoga classes are offered.
- Blog: which links users to the blog page, to view all blog posts. 
- Account: which is a dropdown menu that displays 'Register and Login' when a user isn't currently logged in. When a user is logged in, it displays 'Sign Out and My Profile'. The 'My Profile' directs users to their own profile page, where they can view their order history, and add/edit/remove their personal information. 

The final navigation link, the Shopping Cart, is utilized as an icon. I have decided to use an icon here, and push it to the right-hand side of the screen to separate it from the other navigation links. I have also added a counter to the icon, which displays the number of items currently in the shopping cart. When a user clicks on the Shopping Cart icon, they are directed to the shopping cart page, where they can view/edit/remove items currently in their cart.


#### The Footer Section 

Each page contains a footer, which has a basic site map that displays links for the following pages:
- Home
- Classes
- Timetable
- Blog 

The footer also contains social media links for the website's social media accounts. 

I have also created a search bar in the footer to allow users to quickly search for yoga classes. When a user searches for a yoga classes, they are directed to the products page and shown the relevant results, otherwise, they are informed that they search criteria provided no results. 


#### Home App

This app acts as the home page, and informs that user about the content and purpose of the website. This app contains a hero image, a call to action button to view products. 

This page also features an 'about' section which informs the users of the yoga studio's philosophy. 

Finally, the page also features three product cards which are filtered by the beginner category to quickly showcase to the user that beginner friendly classes that are offered. 

In addition, the home page displays the latest blog post to encourage readers to visit the studio's blog. 

#### Products App

This app facilitaes the feature to all users to see all products offered by the yoga studio. This app allows users to also view more information about a product, by visiting the product detail page. 

Finally, this app also allows admin users to create, edit, and delete all products in the database.


##### All Products Page

This page displays all product currently being offered. A user has the ability to sort products both in ascending and descending by name, price and category. 

A user also has the ability to filter products by category (for instance, beginner or advanced classes)

Finally, a user is able to search for products by name, category or a keyword search via a product's description in the search bar in the footer which is displayed on every page. 

##### Individual Product Page

The individual products page is created mostly with template tags, to allow the variety of information in each product to be displayed correctly. 

The page features a larger size of the product image, a product description, and information regarding the product's price, and timetable information. 

The page also features a link to the timetable page, for users to look at other times which may suit them, and which classes best suit their time schedule.

Finally, the page also features an add to cart button, and a button which redirects users back to the all products page. 

#### Class Management

If the user logged in is an admin user, they will have access to the dropdown menu item 'Class Management' in the Account navigation item, which allows a user to create a new product for users to purchase. 

In addition, when an admin user is viewing the All Products page, they are shown two buttons on each product card: 'Edit' and 'Remove'. The Edit link directs the user to a Product form to edit the current product. 

The 'Remove' link triggers a modal to confirm that the admin user wishes to delete the product from the database. A product is only deleted once the user confirms this action. 


#### Cart App

This app provides users with the functionality to add products to the shopping cart, allows users to adjust their shopping cart by changing the quanitity of items, as well as the ability to remove items from their cart.

Each time an action is performed by the user for instance, adding an item to the cart, adjusting the quantity, or removing an item, a toast is triggered and a preview of their shopping cart is displayed. The preview provides users with the names, images, and price of an item as well as the total price of their current shopping cart. 

#### Checkout App

The Checkout App provides users with the functionality to securely purchase the items in their shopping cart. To allow for a secure and streamlined purchasing experience I have used Stripe.

If a user is currently logged in, the checkout information will be populated from their profile (provided that they have filled out their profile information). Otherwise, a user has the ability to either save the checkout information to the profile, or to create an account. 

To create a truly streamlined experience for users when navigating the checkout app, it is also possible to purchase products without creating an account. 

Once a user has clicked the 'Complete Order' button, a loading overlay animation is triggerd to indicate to the user that the payment is in process. 

Once this is completed, a user is automatically directed to the Checkout Success page, where they are notified that a confirmation email has been sent to their email address, as well as provided with a summary of their order. 

#### Profile App

The Profile App provides users with the functionality to store their information to speed up the checkout process, as well as a place to edit their previously saved personal information. In addition, the profile page also users to view their order history. Finally, if a user has a registerd account, they can leave comments on blog posts.

##### Register 
A user can create a profile app by clicking on the dropdown-menu link 'Register' in the navigation link 'Account'. 

When registering an account, a user must input a username, their email address and a password. The password field needs to be entered twice in order to avoid typos. 

Once a user registers, they are sent a verification/confirmation email, with a link. Once a user confirms their email address, the account is created, and they can access their profile page.

##### Log In

If a user already has created an account, they can sign into their profile by using the 'Login' link.

To do so, a user needs to enter their email address or username and their password. 

If the form is valid, and the information is correct the user is redirected to their profile page, which contains their saved personal information as well as order history, if any purchases have been made.

##### Logging Out

A user can quickly log out by selecting the sign out option in the and Account Dropdown menu on the navigation menu. 

#### Blog App

The Blog App provides functionality to admin users to create, edit and delete blog posts for the website. 

For users, this app provides a place where they can read blog posts, and leave comments if they wish. 

##### All Blog Posts Page

The main blog page features a snippet of each blog post in the form of a Bootstrap card. Each card features a blog title, information about when it was created, and the name of the author. The blog post cards also features a unique snippet of text, to give a brief summary of the blog post. Each card features a button which directs users to the blog detail page, where they can read the full blog, and leave comments.

The blog page is dynamically updated always display blogs that have been created, and it displays the latest blog first.

##### The Blog Post Detail Page

This page allows users to view the full blog post, as well as user comments. 

Any user with a registered account, and currently logged in can leave a comment on a blog post. A user is also able to edit, and delete comments they have created. A modal confirmation is trigged if a user tries to delete a comment, to confirm that this action is permanent, and to confirm if they wish to delete their comment. 

A user with an admin account, can edit and remove the blog post. Like all action which may remove an item from the database, a modal is triggerd to confirm the action.

Both the edit blog (for admin users) and the edit comment (for admin users or comment author) is redirected to a form, for the user to complete to finally edit the blog post or comment. 

If a user wishes to leave a comment, they can do so in the text box beneath the blog post. Once they have submitted their comment, a message is displayed to the user that their comment is awaiting moderation. 

I have choosed to employ this feature to prevent spam, and ensure that comments are relevant to the content. 

If an admin user is logged in and viewing the blog post detail page, all comments awaiting approval are displayed, and an admin user has the ability to either approve or deny a pending comment. 

If a pending comment is approved, it is displayed under the blog post, and if is denied, the comment is removed from the database. 

#### Timetable App

The Timetable App provides users with the ability to view all yoga classes time and day's offered. This allows users to choose a class which best suits their own schedule. Each class in the timetable has a link which directs users to the product detail page of the specific class.

The timtable page is automatically updated to reflect the current products in the database. A user can see all current yoga classes, and the day and time the class is offered. 

The timteable is designed with a a bootstrap table, with added media queries for smaller devices. The timetable is created with for loops to always reflect the current offered products. 


All features have been manually tested in a variety of ways. Which can be read in more detail here:


### Future Features

In the future, I would like to optimize the booking system for yoga classes by implementing an interactive calendar, which will allow users to choose a class and times. 

In addition, I would like to implement a tracking system to display to users how many sessions they have left from a class they have booked. For instance, some products offer 10 sessions, and I'd like to have a system where after each session attended, its reflected on their profile how many sessions are remaining. 

Finally, I would to further streamline the log in and register experience for users by allowing users to log in via Social Media.


## Database Information

A wireframe for the database was created on dbdiagram.io to help in providing an overview of what will be needed for the Django models. 

When developing the website in Django the database used was SQLite. 

## Troubleshooting

Throughout the developement of the website, I encountered a number of problems which through trial & error, or research solutions were found. 

I have documented these issues below.




## Technologies Used

* This website was developed using [HTML5](https://en.wikipedia.org/wiki/HTML5), [CSS3](https://en.wikipedia.org/wiki/CSS), [JavaScript](https://en.wikipedia.org/wiki/JavaScript) , and [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
* [Django](https://www.djangoproject.com/), a Python framework to render pages, speed up development and avoid repeated code.
* [jQuery](https://jquery.com/) was used to simplify JavaScript code.
* The fonts used in this website were imported from [Google Fonts](https://fonts.google.com/).
* [SQLite](https://www.sqlite.org/index.html) was used to manage the database during the development phase of the project.
* [PostgreSQL](https://www.postgresql.org/) was used to manage the database once the project had been deployed to Heroku.
* [AWS](https://aws.amazon.com/) was used to store static and media files.
* [Stripe](https://stripe.com/) was used to process and manage card payments.
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) was used to quickly render forms.
* [All Auth](https://django-allauth.readthedocs.io/en/latest/installation.html) was used to create the login and register functionality.
* I used [Font Awesome](https://fontawesome.com/) for all icons.
I used [Unsplash](https://unsplash.com/) and [Pexels](https://www.pexels.com/) to source images used on the website.
* [Bootstrap 5](https://getbootstrap.com/) was used to structure the layout of the website and maintaining layout and responsiveness to tablet and mobile devices. I linked Bootstrap to the HTML document via [CDN](https://www.bootstrapcdn.com/).
* This website was initially designed with wireframes using [Balsamiq](https://balsamiq.com/). 
* [Git](https://git-scm.com/) version control was used to store the version of files and track the development progress. 
* The IDE used to work on this project was [Gitpod](https://www.gitpod.io/). 
* [Github](https://github.com/) was used to manage Git repositories.
* [Heroku](https://www.heroku.com/) was used to deploy the website.
* HTML code was validated with [W3C](https://validator.w3.org/). 
* [W3C CSS](https://jigsaw.w3.org/css-validator/) was used to check the validity of the CSS code in this project. 
* [Jshint](https://jshint.com/) was used to test the validity of JavaScript code. 
* [PEP8Online](http://pep8online.com/) was used to check Python code to ensure it met PEP8 requirements.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse#devtools) was used to check that the website is user-friendly.
* [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) to test the website on mobiles. 
* [Favicon.io](https://favicon.io/) was used for the website's favicon.
* [ResponsiveDesign](http://ami.responsivedesign.is/) was used to display the README's Overview Image.


## Testing

All testing can be view here: 

## Deployment


### Heroku Deployment 


## Credits 


### Images 

All Images were sourced from Unsplash and Pexels.

### Text 

All text was written by myself.

## References for Code


## Acknowledgements


