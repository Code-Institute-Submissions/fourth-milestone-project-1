# Miss Pan's Bakery - Full Stack Frameworks with Django Milestone Project
<https://miss-pans-bakery.herokuapp.com/>
## Overview
For the fourth and final project of my Code Institute Full Stack Web Developer course, I was tasked with building a full-stack site using the Django web framework. The project required
business logic and a user authentication system, which allow the user to create a log in and pay for services using Stripe. The final project was the largest and combined elements
from the previous three projects, with the significant addition being the use of Django. In Django, I needed to split my work into different apps and make use of the model-template-views
pattern. This meant designing a relational database backend, writing views in Python and creating frontend templates in HTML featuring template logic.

I decided to build a bakery website, with its primary purpose being to sell products from its shop. The shop app allows users to browse products and view details about them.
This also meant building a shopping cart and an orders app, allowing users to add products to their cart and submit an order after completing a payment using Stripe. Furthermore, users
can add product reviews for products if they have purchased the product.

In addition to the shop and ordering functionality, there is a recipes app where users can browse and create recipes, and click the heart button to save them to their user profile.
There is also a videos app where admins can add embedded YouTube videos for users to watch on the site, and a gallery app where admins can upload images to an image gallery and users
can switch between viewing the uploaded images and images of products in the shop. Users also have their own profile where they can view order history, their created and hearted recipes,
and update their default delivery information.

The website is responsive across devices, largely due to use of the Bootstrap CSS framework. I have also made use of JQuery to improve the user experience. Media and static files are
stored externally in an Amazon Web Services S3 bucket, and the website is deployed to Heroku [here](https://miss-pans-bakery.herokuapp.com/).

## UX
My full UX documentation can be found in the ux-design folder, which can be found [here](ux-design).
This includes documents detailing my thoughts on the strategy and scope planes of this project, plus the basic structure and my skeleton wireframes.

### User Stories

* As a fan of cakes and cookies, I want to go online and purchase some for delivery to my house.
* As a repeat customer of Miss Pan's, I want to save my delivery information for quick checkout next time.
* As a customer of Miss Pan's, I want to write reviews of their products and read reviews written by others.
* As an avid baker, I want to find new recipes and share my own.
* As a fan of Miss Pan's, I want to check out their social media pages.
* As someone with an interest in baking, I want to watch or look at content that Miss Pan's is showcasing.

## Features
### Existing Features

* A navbar for accessing the main hubs of the site, as well as links to log in and register or links to the logged in user's account.
* A user authentication system that allows a user to register and create an account, powered by Django Allauth. Users should be sent a verification email after registering. Logged in
users have access to features that anonymous users do not.
* Logged in users have a user profile, where they can view their order history, update their default delivery info and view any recipes they have created or hearted.
* A shop where users can search by keyword or view different pages that filter products by category.
* A shopping cart system, that allows users to add products to their cart from the shop or product page before checkout.
* A checkout system that allows users to place orders for different quantities of product. All orders require payment by credit or debit card using Stripe. Users can update their default
delivery info at checkout if logged in.
* A product review system. Logged in users who have purchased an item can submit a review for the item and give it a rating, which then appears on the product details page.
* A recipes hub. Logged in users can submit, edit or delete their own recipes. Recipes approved by the website admins appear on the recipes page for all users. Recipes can be selected for showcase and appear at the top of list.
Recipes can be hearted by logged in users, and then appear on their hearted recipes page.
* Website admins can add, edit and delete products on the shop.
* Products have a stock number that decreases when orders are placed. A low stock or out of stock message appears if stock is too low, and out of stock products cannot be purchased.
The cart system should adapt and prevent adding more of the product than the available stock.
* A gallery that uses scrollreveal to display images. Users can switch between images uploaded directly by website admins, or images of each shop product. Clicking on an image should
enlarge it, or direct you to the product.
* A video hub, where website admins can add, edit or delete embedded YouTube videos. Users can watch these videos on the site.
* Pages that feature lists of content should also feature pagination, so the items are split onto different pages.
* The website should be responsive and adapt to different devices and screen sizes.
* Some buttons such as the place order button should change to a spinning icon when the page loads, to give visual feedback to users.

### Future Features

* More comprehensive sorting of products and recipes.
* Information on delivery times to keep users up to date about their orders. An email should be sent with order confirmation.
* Implementation of a Stripe webhook was started but not completed. This should be finished to prevent orders being placed without updating the system.
* Users should be able to access their reviews from their user profile.
* Reviews and more detailed ratings for recipes. The ability to view all recipes by a particular user.
* More categories of item for the shop.
* An alert or toast system to provide feedback to users when changes are made.

## Technologies Used
* [HTML5](https://www.w3.org/TR/2017/REC-html52-20171214/)

  * Used to create the template structure of each page.

* [CSS3](https://www.w3.org/Style/CSS/)

  * Custom styling to the HTML - including font, layout and colours.

* [Django](https://www.djangoproject.com/)

  * The open source Python web framework that the site is based on. A fundamental requirement. I used a number of Django packages, including allauth, crispy forms and storages.
  A full list can be found in requirements.txt.

* [Python3](https://www.python.org/)

  * The programming language that Django is based on. Used to create the models, views, settings etc files for Django. I used a number of Python packages installed with pip,
  such as Pillow and Gunicorn - a full list can be found in requirements.txt.

* [Bootstrap](https://getbootstrap.com/)

  * An open source CSS framework focused on responsive, mobile-first development. A number of Bootstrap classes and components were used, such as the navbar and carousel.

* [JavaScript/jQuery](https://jquery.com/)

  * jQuery was used to improve the user experience and make the site more interactive, as well as enabling Stripe payments.

* [Stripe](https://stripe.com/gb)

  * Used as the payment system.

* [Heroku](https://heroku.com/)

  * Used to deploy the final version of the project.

* [Amazon Web Services](https://aws.amazon.com/)

  * Used to host my static and media files for my deployed site. Using S3 and IAM.

* [Git](https://git-scm.com/)

  * Used for version control and committing changes to GitHub.

* [GitHub](https://github.com/)

  * Used to host and publish my project files.

* [Google Chrome/Developer Tools](https://www.google.com/intl/en_uk/chrome/)

  * My internet browser. 
  The Developer Tools were used to troubleshoot, edit the layout, and preview changes, as well as test the responsiveness of the page.

* [GitPod IDE](https://gitpod.io/)

  * The application I used to develop the project - the production environment.

* [Font Awesome](https://fontawesome.com/)

  * Used to source the icons, e.g. the shopping cart, social media icons etc.

* [Google Fonts](https://fonts.google.com/)
  
  * Used to provide the Josefin Sans font.

* [ScrollReveal](https://scrollrevealjs.org/guide/hello-world.html)
  
  *  A JavaScript library for easily animating elements as they scroll into view, used in the gallery app.

## Testing
My full testing documentation can be found in the testing folder, which can be found [here](testing).

## Deployment
To create my development workspace, I first created a new GitHub repo and made sure to install the GitPod browser extension. I then clicked the GitPod button to generate my
GitPod workspace.

To deploy to Heroku, I followed the following steps:

1. Create a new Heroku app on [Heroku](https://dashboard.heroku.com/), giving it an appropriate name and region.
2. On the Resource tab of the new Heroku app, search for the addon Heroku Postgres and select it. Use the free plan.
3. Install the dj_database_url, psycopg2-binary and gunicorn packages using pip3. Freeze these to a requirements.txt file `pip3 freeze > requirements.txt`.
4. Import dj_database_url in your settings.py file. Comment out your existing DATABASES sqlite3 config and instead point it at `dj_database_url.parse('')`. Go to your config vars in your new Heroku
app and copy the value of the DATABASE_URL, then paste it into the quotes inside the brackets of `dj_database_url.parse('')` and save the file.
5. Run migrations and it will set up the new Postgres database. You should also set up a superuser for the new database using `python3 manage.py createsuperuser`.
6. Uncomment the old DATABASE config. Create an if statement in your settings.py file to check if DATABASE_URL exists in the os.environ, and move the new DATABASES postgres config inside the if statement. Create
an else statement and set that as the old DATABASES config.
7. Replace the postgres config you copied and pasted from the DATABASE_URL variable, and replace it with `os.environ.get('DATABASE_URL)` so that the config is not captured by version control.
8. Create a file in your directory called Profile, and add `web: gunicorn miss_pans_bakery.wsgi:application`.
9. In your Heroku app, set the config variable DISABLE_COLLECTSTATIC to 1, to disable collection of static files.
10. Add the host name of your Heroku app to ALLOWED_HOSTS in your settings.py file, as well as localhost.
11. Commit and push your changes to GitHub. Log into the the Heroku CLI, then use `git push heroku master` to push to Heroku. Make sure the app is selected if you
have more than one.
12. The website should deploy to Heroku. You can now switch on automatic deploys by connecting to your GitHub repo in the Deploy settings of your Heroku app.
13. Update your config vars with a new Django secret key called SECRET_KEY, which you can generate using an online generator. Then update your SECRET_KEY in settings.py to look for a variable called
SECRET_KEY. Make sure your development workspace also has a environment variable for SECRET_KEY.
14. Add an environment variable to your development workspace called DEVELOPMENT with value of true, and set your DEBUG value in look for that variable. DEBUG will only be true in
the development workspace.
15. Set up an AWS S3 bucket which allows public access. Make sure to create a user that has access to it using IAM.
16. Install boto3 and django-storages with pip3 and refreeze the requirements.txt. Add storages to the list of installed apps in settings.py.
17. Add a config var in Heroku called USE_AWS as true. Create an if statement to look for USE_AWS and set the AWS_STORAGE_BUCKET_NAME and AWS_S3_REGION_NAME.
18. Set more config vars in Heroku for the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. Remove the DISABLE_COLLECTSTATIC config var.
19. Update the USE_AWS if statement with os.environ.get() statements to find the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY. Add the AWS_S3_CUSTOM_DOMAIN.
20. Create a new file called custom_storages.py that uses S3Boto3 to find the static and media files locations. This is available in my project files.
21. Then update settings.py with a new location for static and media files, pointing at the custom_storages file. Set new STATIC_URL and MEDIA_URL to use the custom AWS domain. Make sure
all of the above is set within the USE_AWS if statement.
22. Commit and push your changes to GitHub. Heroku should now collect static and media files from your project files.
23. Make sure to sign into the new Postgres Django Admin pages and set the superuser email address as verified.
24. Add the Stripe public and secret keys to Heroku as new config vars. Update the webhook in Stripe to send to the new Heroku endpoint.
25. Deployment is complete.

## Credits
### Content
Text for products was written by myself.
Text for recipes was sourced from an old recipe book.
### Media
The brand logo was created by myself.
The images were sourced from Pexels and Unsplash.
Credit to:
[David Jakab](https://www.pexels.com/photo/cakes-chocolate-close-up-cupcakes-959079/)
[tabitha turner](https://unsplash.com/photos/Ns2aJ5OXKds)
[Sara Sperry](https://unsplash.com/photos/-EMvlQ5n8n0)
[Brigitte Tohm](https://www.pexels.com/photo/bowl-dessert-food-macaroons-239578/)

### Acknowledgements
My design was inspired by the Boutique Ado website shown in the course, as well as the [Anna Cake Couture website](https://www.thisisanna.co.uk/)
and the [Bettys website](https://www.bettys.co.uk/).

The changing website logo on scroll animation was inspired by the same animation of the [Bettys website](https://www.bettys.co.uk/). I inspected the code of that website
and used a very similar method to recreate it. It was achieved by applying css classes on scroll using jQuery, which changes which logo is shown and applies an animation.

Much of my shopping cart app functionality was taken from Chapter 7 of "Django 3 By Example" by Antonio Melé, including much of the code in cart.py and cart views.py.
The chapter also prompted my use of product and category slugs and methods to get URLs in my shop models.py.

I also used a fair amount of functionality demonstrated in the Boutique Ado website course content. This includes the Stripe payment and webhook functionality, the general outline of the ordering process,
the functionality to send emails via Django, and the functionality to link to an AWS S3 bucket.

I made frequent use of [Stack Overflow](https://stackoverflow.com/) when stuck.

To create the box shadow effects, I used the following online tool: [Here](https://www.cssmatic.com/box-shadow).
