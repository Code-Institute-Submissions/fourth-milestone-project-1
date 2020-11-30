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

* First
* Second
* Third

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


## Credits
### Content
text
### Media
images

### Acknowledgements
inspiration etc

I made frequent use of [Stack Overflow](https://stackoverflow.com/)  

To create the background gradient, text shadow, and box shadow effects, I used the following online tools: [Here](https://cssgradient.io/), [Here](https://html-css-js.com/css/generator/text-shadow/) and [Here](https://www.cssmatic.com/box-shadow).