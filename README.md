# Building an E-commerce Website With Django and Vue

## In this tutorial, we will create an e-commerce website with Django and Vue. We will use Django Rest Framework to build a RESTful API for our backend and Vue for the frontend

Before we begin, make sure you have the following installed

1. Python 3
2. pip3
3. Node.js
4. npm

### Step 1: Create a Virtual Environment

Creation of a virtual environment is a crucial step in the development process. To create a virtual environment, use the following command: $ virtualenv venv. Then activate the virtual environment using $ source venv/Scripts/activate.

After activating the virtual environment, you need to install Django and other required libraries. Use the following commands to install Django and its libraries:

### Step 2: Install Django and Required Libraries

1. $ pip3 install Django
2. $ pip3 install django-rest-framework     (for Web browsable API, Authentication policies, Serialization, and regular function-based views.)
3. $ pip3 install django-cors-headers       (for security between API and backend.)
4. $ pip3 install djoser                    (for token Authentication user.)
5. $ pip3 install pillow                    (for the Python library to resize images.)
6. $ pip3 install stripe                    (for the payment method library.)

### Step 3: Create a New Django Project

Now, create a new Django project using the command django-admin startproject project_ecommerce. You can use the manage.py file to run administrative tasks and initialize the database. It also helps to create a superuser. Inside the project_ecommerce folder, you will find an __init__.py file that tells Python how to handle this package. The asgi.py and wsgi.py files are the entry points to the web server. The settings.py file contains global configurations for the entire project, and urls.py is like the table of contents of all the pages in the backend.

### Step 4: Configure Django

To inform Django about the installed package, go to settings.py and add the following lines of code:

`INSTALLED_APPS = [
'rest_framework', 'rest_framework.authtoken', 'corsheaders', 'djoser'
]`

To configure the corsheaders, add the following code above CommonMiddleware in the MIDDLEWARE section:

`'corsheaders.middleware.CorsMiddleware',`

### Step 5: Include URLs

Now, go to urls.py and include API fonts, djoser, and include Pods (which represents a single instance of a running process in your cluster) by adding the following code:
`path('api/v1/', include('djoser.urls')), path('api/v1/', include('djoser.urls.authtoken')),`

These functionalities allow you to create users' Authentication tokens.

### Step 6: Initialize the Database

When create the first models, initialize the database by running the following commands:

`$ python manage.py makemigrations $ python manage.py migrate`

Step 6: Create a Superuser

To create a superuser, use the command:

`python manage.py createsuperuser`

### Step 7: Run the server

Finally, run the server using the command:

`python manage.py runserver`

### Set up Vue

To install and set up Vue, a JavaScript framework for building user interfaces, you need to follow the steps below

1. Install nodejs.
2. Install the Vue CLI using the command $ npm install -g @vue/cli.
3. Create a project using the following command: $ vue create e-commerce_vue. Select "Manually select features" and choose the features that you will use to transcribe the code into real JavaScript, such as babel, router, vuex, CSS Pre-processors, and remove linter. Choose the 3x version for Vue.js, use history mode for router, use dart-sass, store in dedicated config files, and save as e-commerce_vue.
4. Change to the e-commerce_vue directory using the command cd e-commerce_vue.
5. Install axios to talk to the backend using the command npm install axios.
6. Install bulma (CSS framework) using the command npm install bulma.
7. Run the server using the command `npm run server

### Note from vue frontend part two

To implement a loading bar, we need to make some changes to our store, mutations, and components. In store/index.js, we'll define a new mutation called setIsLoading that takes a status parameter and updates the isLoading state accordingly. We'll use this mutation to set the loading status to true when a request is being made, and false when the request is complete.

In Product.vue, we'll define a new method called setLoading that commits the setIsLoading mutation with a value of true. We'll call this method before making a request to the API, and call it again with a value of false when the request is complete.

To display the loading bar, we'll add a new div element to App.vue with a class of loading-bar. We'll use CSS to style this element and position it at the bottom of the page. The CSS will also define an animation that fills the loading bar from left to right as the isLoading state changes.

To set the document title for all pages, we'll update the document.title property in the mounted hook of each component. In Product.vue, we'll set the title to the product name followed by " | Petstore". In Home.vue, we'll set the title to "Home | Petstore".

To view categories, we'll define a new API endpoint in views.py called CategoryDetail. This endpoint will return the details for a specific category, along with a list of products that belong to that category. We'll also define a new serializer called CategorySerializer to serialize the category data.

In urls.py (product), we'll add a new path for the CategoryDetail view, importing it from views. We'll also update the existing products path to include the category_slug parameter.

In the vue views, we'll create a new component called Category.vue. This component will display a list of products for a specific category. We'll use the ProductBox component to display each product.

To add search functionality, we'll define a new API endpoint in views.py called search. This endpoint will accept a search query via a POST request and return a list of products that match the query. We'll decorate the view with @api_view(['POST']) to specify the HTTP method.

In urls.py, we'll add a new path for the search view above the existing category_slug path.

In App.vue, we'll add a new button to the navigation bar for searching. When the button is clicked, we'll display a search box where the user can enter their query.

To view the cart, we'll create a new component called Cart.vue. This component will display the contents of the user's cart and allow them to increment or decrement the quantity of each item.

To make it possible to sign up, we'll create a new component called MyAccount.vue. We'll change the "Log in" button on the account page to say "My Account", and clicking it will display the MyAccount component.

To create a checkout page, we'll create a new component called Checkout.vue. This component will display the user's cart contents and allow them to enter their shipping and billing information.

Finally, we'll create a new component called Success.vue to display a message to the user when their order has been successfully processed.
