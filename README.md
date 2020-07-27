# profiles-api

An example of REST API project using django REST framework. The project includes:
* User profile 
  * A OneToOne relation with django User that include applicative information on the user.
  * Signals - Creating a profile once a new user is created
  * Avatar - image
* Authentication and permmisions
  * Configuration for session authentication and token authentication
  * Using features from django rest_auth and from django allauth
  * A client examples for API calls for registreation and authenticate
* Views examples with ViewSet
* Router for urls
* Test examples
