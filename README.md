# Elsi-Belsi-Handmade-Angular-Django-Project
Project with Angular (frontend) and Django (backend) for handmade shop.

Perform test to the end-points of the backend (DJANGO):
Public Part:
POSTMAN:
http://127.0.0.1:8000/api/auth/register/ - registered user petko2@andreev.it (SUCCESS)
http://127.0.0.1:8000/api/auth/login/ - login of user petko2@andreev.it (SUCCESS)
http://127.0.0.1:8000/api/auth/logout/ - logout of user petko2@andreev.it (SUCCESS)
-- PROFILE
http://127.0.0.1:8000/api/auth/profile/11/ - GET request to the profile of user petko2@andreev.it (SUCCESS)
http://127.0.0.1:8000/api/auth/profile/10/ - PUT, PATCH and DELETE requests with no logged in user on user profile of petko1@andreev.it (id=10) - return errors (Authentication required) (ERROR)
-- PRODUCTS
http://127.0.0.1:8000/api/products/ - GET request - list all products (SUCCESS)
http://127.0.0.1:8000/api/products/ - POST request - return errors (Authentication required) (ERROR)
http://127.0.0.1:8000/api/products/7/ - GET request - return product details (SUCCESS)
http://127.0.0.1:8000/api/products/11/ - PUT, PATCH and DELETE requests with no logged in user - return errors (Authentication required) (ERROR)
http://127.0.0.1:8000/api/products/7/add-to-favorites/ - POST request with no logged in user - return errors (Authentication required) (ERROR)
http://127.0.0.1:8000/api/products/7/likes/ - POST request with no logged in user - return errors (Authentication required) (ERROR)

Private (required logged in user) Part:
http://127.0.0.1:8000/api/auth/profile/10/ - PUT, PATCH and DELETE requests with logged in user petko2@andreev.it (id=11) on user petko1@andreev.it (id=10) - return errors (You're not owner of this profile...) (ERROR)
http://127.0.0.1:8000/api/auth/profile/12/ - PUT, PATCH and DELETE requests with logged in user petko2@andreev.it (id=11) on user petko2@andreev.it (id=11) - in the delete request the profile and user were removed from DB. (SUCCESS)
http://127.0.0.1:8000/api/products/ - GET request - list all products (SUCCESS)
http://127.0.0.1:8000/api/products/ - POST request with logged in user petko2@andreev.it (id=12 - it were recreated after deletion) - create product with id 11 (SUCCESS)
http://127.0.0.1:8000/api/products/7/ - GET request - return product details (SUCCESS)
http://127.0.0.1:8000/api/products/11/ - PUT, PATCH and DELETE requests with logged in user petko1@andreev.it (id=10 and who is NOT the owner of the product) - return errors (You're not owner of this product...) (ERROR)
http://127.0.0.1:8000/api/products/11/ - PUT, PATCH and DELETE requests with logged in user petko2@andreev.it (id=12 and who is the owner of the product) - operations were performed (SUCCESS)
http://127.0.0.1:8000/api/products/7/add-to-favorites/ - POST request with no logged in user petko@andreev.it (id=9 and who is the owner of the product) - return errors (You are not the owner of the product) (ERROR)
http://127.0.0.1:8000/api/products/7/add-to-favorites/ - POST request with logged in user petko1@andreev.it (id=10 and who is NOT the owner of the product) - add and remove from favorites (SUCCESS)
http://127.0.0.1:8000/api/products/7/likes/ - POST request with no logged in user petko@andreev.it (id=9 and who is the owner of the product) - return errors (You are not the owner of the product) (ERROR)
http://127.0.0.1:8000/api/products/7/likes/ - POST request with logged in user petko1@andreev.it (id=10 and who is NOT the owner of the product) - add and remove like from likes (SUCCESS)
