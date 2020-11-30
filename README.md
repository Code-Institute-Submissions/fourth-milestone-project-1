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

* First
* Second
* Third

### Future Features

* First
* Second
* Third

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

* [JavaScript/JQuery](https://jquery.com/)

  * JQuery was used to improve the user experience and make the site more interactive, as well as enabling Stripe payments.

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