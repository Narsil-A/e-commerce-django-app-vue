# e-commerce-django-app-vue
### Recipe: E-commerce Website With Django and Vue Tutorial (Django Rest Framework)
 
- Install and setup django: #Done
  - Creation of virtual environment: $ virtualenv venv1, $ source venv1/Scripts/activate. 
  - Install django and libraries: $ pip3 install Django, $ pip3 install django-rest-framework(Web browsable API, Authentication policies, Serialization, regular function-based views), 
    $ pip3 install django-cors-headers(security between API and backend), $ pip3 install djoser (token Authentication user),
    $ pip3 install pillow(python library for resize image), $ pip3 install stripe (payment method library)
  - Create a new django project: django-admin startproject project_ecommerce: 
    manage.py to run administrative task and initialize the database, create superuser, into the folder project_ecommerce we found 
    a __init__.py that tell python how handle this as package. asgi.py and wsgi.py are the entry point to the web server. 
    setting.py globally configuration for the whole project. And, urls.py is like the table contents of all the pages in the backend. 
  - Tell django abouth this package installed, so, go to setting.py, INSTALLED_APPS = [ 'rest_framework', 'rest_framework.authtoken', 
    'corsheaders', 'djoser'].
  - Configuration of course headers: add bellow INSTALLED_APPS = [], CORS_ALLOWED_ORIGINS = [ "http://localhost:8080", ]
    this will be the address to the front, later you will neeed to change to the live server address
  - In the MIDDLEWARE section , above of CommonMiddleware, put, 'corsheaders.middleware.CorsMiddleware',
  - Go to the urls.py and include API fonts, djoser, include Pods (represents a single instance of a running process in your cluster).
    path('api/v1/', include('djoser.urls')), path('api/v1/', include('djoser.urls.authtoken')),. this functionalities allow create
    users Authentication tokens. 
  - initialize the database, $ python manage.py makemigrations, $ python manage.py migrate. 
  - create the superuser. $ python manage.py createsuperuser  
  - run the server: $ python manage.py runserver

- Install and setup (Vue): JavaScript framework for building user interfaces
                           -Declarative Rendering: Vue extends standard HTML with a template syntax that allows us to 
                                        declaratively describe HTML output based on JavaScript state.
                           -Reactivity: Vue automatically tracks JavaScript state 
                                        changes and efficiently updates the DOM when changes happen.                      

  - Install nodejs
  - Install Vue cli $ npm install -g @vue/cli
  - create a projct:$ Vue create e-commerce_vue
    - select: Manually select features, select the features that going to use to transcribe the code in real JavaScript.
              Manual features for this app: babel, router, vuex, CSS Pre-processors, and remove linter, choose 3x versior for vue.js,
                                            use history mode for router, use dart-sass, store in dedicated config files, 
                                            saved as e-commerce_vue. 
  - cd e-commerce_vue, npm install axios (to talk to the back-end), npm install bulma (CSS framework)
  - npm run serve http://localhost:8080/, Network: http://192.168.0.103:8080/ 
  
- Include Fond Awesome: put in the index.html (public folder, for icons) bellow <title><%=htmlwebpackpuglin.option,title %></title> 
                        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.2/css/all.min.css">

- Set up the base template: remove the styles css and put - @import '../node_modules/bulma';
                            bellow <template> put <div id="wrapper">, create a navbar <nav class="navbar is-dark">, <div class="navbar-brand">
                            add section and buttons. log in, and cart. 

   -inspect the browser for mobile view. Modify App.vue: navbar...@click="showMobileMenu = !showMobileMenu">, v-bind:class="{'is-active' : showMobileMenu}">,                

-Back-end: 
        - creating django app and models for products.
        - python manage.py startapp 
          - models.py: where we describe to the database the types of infotmation, 
            - class category: name, slug, 
              - class meta: ordering data(tuple), __string__ represetantions,
                get_absolute_url.
            - class product: name, slug, description, price, image, thumbnail, date_added. 
              - class Meta: ordering data(tuple), __string__ represetantions, get_absolute_url, get_image, 
                get_thumbnail, make_thumbnail. 
            - register app (models) admin.py 
            - Add in settings.py: MEDIA_URL = '/media/',  MEDIA_ROOT = BASE_DIR / 'media/', 
            - Add in urls.py: + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

            
- create serializer and views for the products> get info from the database and retrive in json
   - create a serealizers.py:
               import django-rest-framework, and .models, 
               create the class ProductSerializer, create a class meta and make a model to get the information, and later, configure what field, 
               with a tuple with the information we will retrive. 
   - create a urls.py in the product app. 
                                     
- create a simple front page: go to the home.
  - home.Vue: header welcome, list of products.

- view a product: 

- Sette opp vuex/state: src-store-index.js add cart items, Authentication, login. 

- Make it possible to add to the cart: 

    - Add funtionalities to the vuex, mutations create initializestore(state). 
                                       to store items in the local store of the web. 

    - initialize store in app.vue: beforeCreated() computed function 
    
    - add button to product page: computed function

    - install bullma toast

- implement a loading bar: store/index.js mutations: setIsLoading(state, status),
                           product.vue methods: store.commit setisloading true. in the final, we set set loading is false. 
                           app.vue, add div for loading bar. add styling, go donw the bottom. 

- set document title to all pages: product.vue bellow axios: document.title = this.product.name + ' | Petstore' 
                                   home.vue: mounted: document.title = ' Home | Petstore' 
- view categories: views.py: class CategoryDetail(APIView). 
                   serializers.py: class CategorySerializer
                   urls.py(product): import products path views.CategoryDetail

                   view(vue): create a Category.vue
        