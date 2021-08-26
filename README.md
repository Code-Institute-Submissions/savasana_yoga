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

Finally, the website also provides admin features to manage the yoga classes, by editing, deleting and adding new classes, and blog posts.


## User Stories

* I want a website that allows me to book yoga classes.
* I want to receive an email confirmation after booking a class.
* I would like a blog to read more about the yoga studio, and yoga in general.
* I would like the ability to comment on blog posts.  
* I want the ability to filter classes between difficulty levels.
* I want a website that is easily accessed on my mobile phone and tablet. 
* I want a website that is easy to understand and navigate.
* I want to have my own profile to store my information, and view my order history. 
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



#### Purchasing Products

The main feature of this website was the sale and promoting of yoga classes. I have split this into multiple parts; the all products page, the individual product page, the shopping cart, the checkout page, and the booking confirmation. 

##### All Products Page 

All Products Page

The all products page features all available yoga class a user can purchase. 

I decided to display the products in individual cards. 

At first, I wanted to create an alterating col-12 with a complimentary alternating background-color for each product. 

However, it resulted in users having to scroll a lot when viewing all the products offered. I felt this wasn't a great user experience, and felt the conciseness that bootstrap cards offered was much preferred from a UI and UX standpoint. 

The product cards are filled with basic information including the name of the class, the price, a tagline to briefly describe the essence of a class. When a user hovers over a card, a box shadow effect is triggered, and if a user clicks on the card, they are directed to an individual product page where they can purchase the class, and read more information about the particular class.

In addition, if an admin user is logged in, the product cards also display an edit/delete button to allow quick product management. 

The all products page, also features a filtering system, where users can filter the products displayed by their categories (advanced classes or beginner classes).

The all products page also features a sorting system where users can sort products by ascending/descending price/category/name

##### Individual Products Page

The individual products page is created mostly with template tags, to allow the variety of information in each product to be displayed correctly. 

The page features a larger size of the product image, a product description, and information regarding the product's price, day, and times. 

The page also features a link to the timetable page, for users to look at other times which may suit them, and which classes best suit their time schedule.

Finally, the page also features an add to cart button, and a button which redirects users back to the all products page. 

##### The Shopping Cart Page

##### The Checkout Page

##### The Booking Confirmation Page


#### Timetable Page


#### Blog Page


#### User Profiles

There are a number of pages related to a User's account, and I have explained them below. 

##### Register Page

##### Login Page

##### Individual Profile Page


#### Admin Profiles

##### Product Management

###### Adding Products

###### Editing Products

###### Deleting Products

##### Blog Management

###### Adding Blog Posts

###### Editing Blog Posts

###### Deleting Blog Posts


### Future Features

In the future, I would like to optimize the booking system for yoga classes by implementing an interactive calendar, which will allow users to choose a class and times. 

In addition, I would like to implement a tracking system to display to users how many sessions they have left from a class they have booked. For instance, some products offer 10 sessions, and I'd like to have a system where after each session attended, its reflected on their profile how many sessions are remaining. 


## Database Information


## Troubleshooting


## Technologies Used


## Testing


## Deployment


### Heroku Deployment 


## Credits 


### Images 


### Text 


## References for Code


## Acknowledgements

