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

When I first became interested in yoga, I found it difficult to find a place with a number of different types of classes, flexible booking systems?? - and the ability to filter classes based on difficulty levels. 

This resulted in a feeling of being overwhelemed, and unsure what to book/attend. 

As a result, I created Savasana Yoga to faciliate an easy-to-navigate and easy to understand website, that offers a wide variety of classes, promotes a flexible booking system, and allows the filtering of classes based on a user's experience level. 

With this in mind, I decided to forego a popular feature when it comes to booking classes: set time slots. Instead of the traditional booking system of 'You booked Example Class at 8pm'. Instead, a class is offered twice a day; in the morning, and in the evenings. Many people have changing schedules due to family commitments, and work. So, I wanted it to be possible for a user to book a class, and freely decide if they'll attend the morning class on week 1, and the evening class on week 2 etc. 

I have reiterated this philosophy a number of times throughout the website, and also placed this information on the checkout_success page, as well as in the email booking confirmation.


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



### Icons 



## Features


