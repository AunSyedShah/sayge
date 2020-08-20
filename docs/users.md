#Django Application

This is the backend application of Sayge-ai, written in python using Django restframework.

#Dependencies 

Details about project's dependencies and environment setup can be found in python.md

#Project Structure

sayge-ai folder contains basic configurations and settingsof Project. 

Users app manages creating new Tenants and Stores and also user's creation and authentication. We are using Djoser third party app for authentication and
registration purposes. Models have Tenant model which creates each tenant, Store model for each store of a corresponding
tenant, User model for each user of tenant, Role model for assigning role
to each User.

