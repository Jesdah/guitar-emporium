# Guitar Emporium.
## An online guitar shop, check out our range or contact us and we will build your dream guitar!

Welcome to Guitar Emporium! This is a page for all music lovers, check out our exclusive range of guitars, if you don't find what you are looking for, get in touch and we will build your dream guitar according to your wishes. Create a profile and sign up for our newsletters.

### Home.
![screenshot of Home screen](/docs/readme_images/guitar-emporium-home.png)<br>
On the home, which is the home page, the user is met by a header, page quote and a footer.
<br>
The content of the page mainly consists of a large background image where we see a rock star who is on his way to the stage and in the center is a quote from Bob Dylan and a button that takes the user to the guitar page.
The aim is to trigger curiosity in the user and give an impression of quality and seriousness.


### Guitars Page.
![screenshot of guitars page.](/docs/readme_images/guitar-emporium-guitars.png)<br>
On the guitar page we see cards with a linked image, title, price, category and if you are a superuser there is a link to edit and delete.
On the page, it is possible to sort the assortment according to certain criteria. At the top it shows how many guitars match the search, to go back to the standard page there is a link that resets the search.

### Edit Guitar.
![Screenshot of edit guitar page](/docs/readme_images/guitar-emporium-edit-guitar.png)<br>

On the page, old information is already entered and a superuser can then freely change the fields without going through the admin panel.

### Delete Guitar.
![Screenshot of delete message.](/docs/readme_images/guitar-emporium-delete-guitar.png)<br>
If the user presses Delete, a pop-up window appears asking the user if they want to delete this guitar, if the user presses yes, the guitar is deleted, if the user presses no, the process is canceled.

### Guitar Details.
![Screenshot of guitar detail page](/docs/readme_images/guitar-emporium-guitar-details.png)<br>
When the user clicks on one of the guitars, the reader is taken to the detailed page. Here we only see a guitar with a picture and a detailed description, at the bottom the user can add the product to the shopping cart or see reviews. Superusers can edit or delete an item and a logged in user can leave a review.

### Add Guitar.
![Screenshot of the add guitar page](/docs/readme_images/guitar-emporium-add-guitar.png)<br>
If the user is a superuser, the user can press "Product Management" in the navigation tab and the user will be taken to a page to add a product. The user writes in the fields and adds an image and presses "add" and the user is taken back to the guitar page.

### Add a Review.
![Screenshot of add a review page](/docs/readme_images/guitar-emporium-add-review.png)<br>
A logged in user can add a review which is accessible through the details page and anonymous users can see the reviews.

### Profile.
![Screenshot of the profile page](/docs/readme_images/guitar-emporium-profile.png)<br>
If the user is logged in, the user gets access to a profile page that can be found in the navigation tab. Here, the user can view and update their information and keep track of the order history and which items have been added to the wish list.

### Order History.
![Screenshot of order history](/docs/readme_images/guitar-emporium-order-history.png)<br>
On the profile page, in the order history section, there is a link that takes you to a page that shows the entire order including email, address, what you have bought and price as some examples.

### Custom Workshop.
![Screenshot of Custom workshop page](/docs/readme_images/guitar-emporium-custom.png)<br>
In the navigation tab we find the "Custom" link and it takes us to the "Custom Workshop" page. Here, users can submit their information to receive a booked consultation for a special order to build the customer's dream guitar.

### Shopping Cart.
![Screenshot of shopping cart](/docs/readme_images/guitar-emporium-shopping-cart.png)<br>
All items that the customer has added to their shopping cart are collected here. Here the customer can add or remove items and when the customer feels satisfied, the customer presses "Secure Checkout".

### Checkout.
![Screenshot of checkout page](/docs/readme_images/guitar-emporium-checkout.png)<br>
Here the customer can fill in their information and see their shopping cart, if the customer wants to change something, the customer can quickly go back to the shopping cart page or the customer can complete their payment through STRIPE.

### Header.
![Screenshot of header](/docs/readme_images/guitar-emporium-header.png)<br>
It consists of Title, navigation tab with home, guitars, profile and custom links after which comes a search field followed by a shopping cart.
<br>
The Header is identical on all pages.

### Footer.
![Screenshot of the footer](/docs/readme_images/guitar-emporium-footer.png)<br>
My Footer is brown and transparent and in the footer there is a field so the customer can register to receive newsletters, here there is also a link to the Custom workshop page and a link to the company's Facebook page.
<br>
The footer is identical on all pages.

### Reminder.
![Screenshot of the reminder](/docs/readme_images/guitar-emporium-reminder.png)<br>
If the user is inactive for 1 minute, a modal pops up reminding the user that the company also offers specially designed guitars and that the form can be found under the Custom link.

### Facebook Page.
![Screenshot of Facebook page](/docs/readme_images/facebook-1.png)<br>
![Screenshot of Facebook page](/docs/readme_images/facebook-2.png)<br>
![Screenshot of Facebook page](/docs/readme_images/facebook-3.png)<br>


### Userstories.
You can find my userstories [here](/docs/AGILE.md).

### Lucidchart.
![Screenshot of Lucidchart](/docs/readme_images/guitar-emporium-lucidshart.png)<br>
Lucidchart has been used at an early stage to facilitate an overview of how data should flow between the various apps.

### Balsamiq.
![Screenshot of balsamiq mobile concept](/docs/readme_images/guitar-emporium-balsamiq-mobile.png)<br>
![Screenshot of balsamiq products concept](/docs/readme_images/guitar-emporium-balsamiq-products.png)<br>
![Screenshot of balsamiq products detail concept](/docs/readme_images/guitar-emporium-balsamiq-product-detail.png)<br>
![Screenshot of balsamiq color concept](/docs/readme_images/guitar-emporium-balsamiq-colors.png)<br>
Balsamiq has been used at an early stage to facilitate an overview of how the site will look like.

### Existing features.
* Responsive design
* Views 
* Models
* Forms
* modal
* Authentication
* sign in/sign out
* sign up
* Add data
* Change data
* Delete data
* STRIPE
* webhooks
* Mail Chimp Newsletter
* AWS Bucket

### Features left to implement.

### Technologies.
* HTML
    * The structure of the Website was developed using HTML as the main language.
* CSS
    * The website was styled using css in a seperate file.
* Git
    * Used to commit and push code during the development of the Website
* Git hub
    * Source code is hosted on GitHub.
* JavaScript
    * The site was scripted using JavaScript.
* Django
    * The site was built using Django as a framework.
* Bootstrap
    * The site was styled and made responsive using Bootstap as a framewok.
* Python
    * The site was developed using Python.
* Heroku
    * The site was delpoyed using Heroku App.
* STRIPE
    * Stripe has been used to make finactial transactions.
* Mail Chimp
    * Mail chimp has been used to let users sign up for newsletters.
* AWS Bucket
    * Used for storage of static files

# Testing.

You can find the tests [here](/docs/TESTING.md).

### Bugs.
When I created a new account I got the following error message: "no such table: socialaccount_socialapp"<br>
I solved it by clearing all the migrations and the data base and then migrated again.

### Unfixed Bugs
No unfixed bugs.

### Deployment.
The following git commands were used throughout development to push code to the remote repo:

```git add <file>``` - This command was used to add the file(s) to the staging area before they are committed.<br>
```git commit -m “commit message”``` - This command was used to commit changes to the local repository queue ready for the final step.<br>
```git push``` - This command was used to push all committed code to the remote repository on github.

### Deployment
- Use the following steps to deploy the poject to Heroku:
1. Use the "pip freeze -- local > requirements.txt" command in the gitPod terminal; to save any libraries that need to be installed to the project files in Heroku.
2. Login or create a Heroku account.
3. Click the "New" button in the upper right corner and select "Create New App".
4. Choose an app name and your region and click "Create App". Note: the app name must be unique.
5. Go to the "Settings" tab, add the python build pack and then the node.js build pack. This is to ensure the project functions correctly with the Code Institute pre-installed template.
6. Create a "Config VAR" with the 'CREDS' key and the enter the value of the creds.json file.
7. Create a second "Config VAR" with the key of 'PORT' and value of '8000'
8. Go to the "Deploy" tab and pick GitHub as a deployment method.
9. Search for a repository to connect to.
10. Click enable automatic deploys and then deploy branch.
11. Wait for the app to build and then click on the "View" link. 

The live link can be found [here](https://guitar-emporium-8025a898f08c.herokuapp.com/).

### Clone the Repository Code Locally
Navigate to the GitHub Repository you want to clone to use locally:
- Click on the code drop down button
- Click on HTTPS
- Copy the repository link to the clipboard
- Open your IDE of choice (git must be installed for the next steps)
- Type git clone copied-git-url into the IDE terminal
The project will now been cloned on your local machine for use.

### Credit.
* I found the Date picker [here](https://stackoverflow.com/questions/3367091/whats-the-cleanest-simplest-to-get-running-datepicker-in-django)

* I got the styling for .accept-btn [here](https://www.sliderrevolution.com/resources/css-button-hover-effects/)

* The hover effect for the detail image comes from [this site](https://thebrandsmen.com/css-image-hover-effects/).

* The boxshadow i got from [here](https://getcssscan.com/css-box-shadow-examples)

* When user is inactive a modal will be displayed reminding the user about the [custom service](https://stackoverflow.com/questions/53108336/show-popup-when-user-is-inactive-after-5-minutes).

* I have used StackOverflow for tips and tricks.

* I have read alot of [Django](https://www.djangoproject.com/)