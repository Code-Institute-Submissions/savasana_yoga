# Savasana Yoga - Testing 

## General Troubleshooting 


Throughout the developement of the website, I encountered a number of problems and issues. Through research, and trial and error, solutions were found, or in some cases other ideas were instead implemented.

I have documented these issues below.

1. The first major hurdle I faced when developing this project, was the product counter for the shopping cart icon. 
    I wanted the cart icon to dispaly to the user the amount of items currently in their cart in the form of a small badge number. 

    I initially added the number of products with django templating {{ product_count }} inside a span, and tried to style this to my liking. The issue I faced, was the I was unable to get the product counter to sit exactly where I wanted it to (at the top-right of the cart icon). Upon researching different ideas and implementations on StackOverflow, I found a post which assisted with the placement and css of this feature. 

    The trick was to use the css placement 'vertical-align:top;'. The StackOverflow post can be found [here](https://stackoverflow.com/questions/51304169/how-to-put-the-number-at-top-right-corner-of-cart-icon)

    With the css created, and the django templating with {{ product_count }} the desired result was achieved.

2. When creating the Timetable page, I wanted to display the days of the week in the following order: Monday to Sunday. When I initially created the page, the data was ordered by the latest entry, and the days of the week were not ordered. I felt this was not a good UI. One possible solution to this was to remove the products and input them in an order so the latest entry would be Monday, then Tuesday. However this did would not resolve the issue, and if a new product was created the unordered days of the week would be present. 

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

Then I added a Meta Class to the Product Model: 

```
class Meta:
        ordering = ['day']

```

This allowed me to have all products displayed by the days of the week. 


3. I faced another issue with the Timetable page when trying to display the days of the week. As I had re-arranged the choice field for the days of the week, when I was creating the Timetable page, and used the django templates to target and display these days using {{ product.day }} the days of the week were displayed as '1', '2', '3', etc rather than the values of 'Monday', 'Tuesday' etc. 

I searched through the Django documentation, I came across the get_FOO_display() method. To better understand how to use this method in django templates, I researched this method on StackOverflow, and found the following post: https://stackoverflow.com/questions/4320679/django-display-choice-value

From this post, I learnt that I could target the choices field values by using 

```
{{ product.get_day_display }}
```

3. I wanted to implement a maximum and minimum value for the number of sessions a yoga class could have. 

Upon researching how to implement these restrictions for the Product Model, I came across the following validators on Django's official documentation, which can be seen [here](https://docs.djangoproject.com/en/3.2/ref/validators/#maxvaluevalidator)

This provided me with the correct validation logic to implement the restrictions I desired. 

4. When I was initially creating the website, I had two apps for products: I had an app for Yoga Workshops, and I had a app for Products (books, yoga equipment etc). I felt that this resulted in a lot of duplicated code, and templates. As a result, I decided to completely remove the Workshop App, and merged the model into the Product Model. I then separated the different types of products by categories. 

However, I also felt that the project had began to lose focus. I thought the promoting of the yoga studio, and the yoga classes were far more important than the selling of yoga equipment/books etc. I finally decided to completely remove all products that were not yoga classes, and by doing so, the website felt much more focused.

5. I had a persistent issue with excessive overflow with some containers. As a result, the home image didn't fit as I would like it to. I initially removed the padding and margins from the container-fluid. Doing so created created overflow for other container-fluid sections, so the solution was to target the specfic container where the image was placed. 


```
.home-image-container {
    padding: 0px;
    margin: 0px;
}
```

In addition, there was still some excessive overflow, and I opened chrome dev tools, and targetted the excessive overflow section of the home page, and saw that there was a missing div in closing the about section container. I added the necessary closing div, and the issue was solved.

6. I had an issue when creating the navigation bar, specifically with utilizing the icons for the shopping cart, and profile. I wanted to keep the navbar brand visible on mobile devices, however, When using both the profile icon, and cart icon, resulted in a squashed experience. There was very little space between the navbar brand and the icons, and the only way to create space between these items was to place the icons in the mobile dropdown menu, or else on a new line below the navbar brand. 

I decided to remove the profile icon, and instead place it as a nav-link 'Account'. This allowed me to keep the navbar-brand and the shopping cart icon on mobile devices.


7. With regards to the timetable page, I faced a number of issues which required to re-think how I wanted to achieve, and display this information. Initially, I created a separete app for the timetable, and created the table with the current offered classes for different days of the week. I felt this was not optimal, as if an admin wanted to remove, edit or add a yoga class, they would also have to make this change for the timetable model. I decided to remove the timetable app, and merge it with the Products app, and include the timetable data into the Product model. This created a streamlined experience for admin users to quickly update the yoga class timetable information, and for the timetable page to always be updated and accuratley reflect the current products being offered to users.

8. I was having issues with getting the footer to stay at the bottom of the page. While developing the website, I didnt encounter this problem as the content on each page was enough to push the footer to the bottom of the page. However, on some pages such as the forgotten password page, and an empty shopping cart page there would be a lot of empty space below the footer.

When attempting to have the footer stay at the bottom of the page, I first tried to use the class 'sticky footer', however, I did not like the UI and UX of a fixed footer on scroll. 

Instead I wanted the footer to  remain at the bottom of the page, regardless of content, while also not being 'sticky' and being shown to a user at all times. 

I found a solution on css-tricks, which can be seen [here](https://css-tricks.com/couple-takes-sticky-footer/) 

I opted to use the flexbox solution, which allowed the footer to remain responsive, and dynamic. The solution was to use flex-direction column on the body, and wrap the block content in a div with a flex: 1 0 auto, and use flex-shrink: 0 on the footer.

9. I encountered an issue when adding blog posts, the issue rested with the required field in the model 'author'. Each time, a user created a blog post, they were required to select the author. If there were more than one admin account, the admin user could select an admin user as the author of a blog post, even if they were not the account which added the blog post. I felt this was not a good design, and I wanted the author to be the user who was currently in session. 

When I attempted this

```
blog_post.author = request.user
blog_post = form.save()
```

I recieved an error that 'blog_post' is not defined. 


I did not like this, and instead wanted the author to the current user in session. 

When i tried this, i first got an error that blog_post is not defined. Upon inspection, I realized this error occured because the 'blog_post.author' was being referenced before the saving of the form: 'blog_post = form.save()'

I initially thought a quick fix for this would be to simply re-arrange the code to read 

```
blog_post = form.save()
blog_post.author = request.user
```

This did not solve the issue, and I encountered an error that 'blog_post.author cannot be NULL as it is a required field.

I quickly realized my mistake, and that I first need to save the form to reference the blog_post, but to actually not save it until after the blog_post.author is assigned as the request.user.

Upon research, I found the best way to achieve this is to use the 'commit=False' method. This method was also used on the order form.

Once I re-arranged the blog code to the following:

```
blog_post = form.save(Commit=False)
blog_post.author = request.user
blog_post = form.save()

```

The blog post is first saved without being committed to the database, then the author is assigned as the current user in session. Finally, the form is saved to the database.


10. When developing the blog, I faced a dilema as to how I wanted the blog comments to function. I did not user comments to be posted automatically. I wanted an admin to be able to approve or deny a pending comment before being visible on the website. I felt that the content should be moderated and the focus of comments to be kept related to the content of the website: Yoga. 

To achieve this, I decided to place all comments in a field named 'approved_comments' with a Boolean field. In the blog views.py I set the 'approve_comments' field to False to ensure that these comments did not show. 

Initially, when I created this the following would happen: When a user leaves a comment on a blog post, they are alerted that their comment is awaiting admin approval. 

To approve a comment, an admin user must log into the admin panel, go to the comment database, and manually approve comments from here. 

I felt this was not the best experience for an admin of the website, and so I wanted to be able to approve or deny pending comments from the specific blog post, on the website.

To achieve this I created a new variable - awaiting_approval_comments, which stored all comments with an active=False. I then created a for loop to display all comments with these parameteres. From here, I created a function to change the boolean value from false to true, and linked this to the approve button. 

To help with understanding how to approve or deny comments, I used a tutorial which can be seen [here](https://tutorial-extensions.djangogirls.org/en/homework_create_more_models)

When an admin is viewing a blog post, they can see if there are any pending comments awaiting admin approval, and they can approve or deny these pending comments from the blog post page.

This allowed me to create an on-site moderation functionality. 

11. 
