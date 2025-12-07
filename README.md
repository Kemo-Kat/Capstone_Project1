cityParties – Event Management API
Project Overview
cityParties is a backend Event Management API built using Django and Django REST Framework (DRF). The goal of this project is to design and implement a real-world RESTful API that allows users to create, manage, and discover events happening in their city.
The system simulates a modern event management platform by handling user authentication, event ownership, permissions, and upcoming event discovery, while following industry best practices in API design and deployment.
________________________________________
Project Objectives
The main objectives of the cityParties project are:
1. Build a RESTful Event Management API
•	Design and implement a backend API that supports Create, Read, Update, and Delete (CRUD) operations for events.
•	Follow REST principles by using appropriate HTTP methods (GET, POST, PUT, DELETE).
•	Ensure clean, maintainable, and scalable API structure.
________________________________________
2. User Management and Authentication
•	Implement user registration and authentication using Django’s built-in authentication system.
•	Ensure each user has a unique username and email.
•	Restrict sensitive operations so that only authenticated users can create, update, or delete events.
•	Enforce ownership rules so users can only manage events they created.
________________________________________
3. Event Discovery and Upcoming Events
•	Provide an endpoint to retrieve upcoming events only (events scheduled for future dates).
•	Allow optional filtering by:
o	Event title
o	Location
o	Date range
•	Support pagination to efficiently handle large numbers of events.
________________________________________
4. Event Capacity Management
•	Assign a maximum capacity to each event.
•	Prevent registrations once an event reaches full capacity.
•	Prepare the system for optional features such as waitlists or attendee tracking.
________________________________________
5. Practical Backend Development Experience
•	Gain hands-on experience with:
o	Django ORM for database interactions
o	Django REST Framework for API development
o	Authentication and permission handling
o	Data validation and error handling
•	Simulate a real-world backend development workflow from planning to deployment.
________________________________________
6. Deployment and Real-World Readiness
•	Deploy the API to Heroku or PythonAnywhere.
•	Configure the application for production environments.
•	Ensure the deployed API is accessible and functional.
________________________________________
Learning Outcomes
By completing this project, the developer aims to:
•	Strengthen backend development skills using Django and DRF.
•	Understand how to model real-world problems using relational databases.
•	Apply best practices in API security, validation, and permissions.
•	Build confidence in deploying and maintaining backend systems.
