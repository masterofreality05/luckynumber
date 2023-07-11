### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
REST which stands for representational state transfer, refers to the connection between the client and the server side. Hypertext Transfer Protocol (HTTP) verbs such as get, post, put and delete are communicated via routes on the client side into CRUD actions on the server side (create, read, update, delete)

RESTful routes refer to a convential pattern that is adhered to when a HTTP request is made from the client side. 


- What is a resource?
A resource in relation to the web, is anything that can be obtained from the world wide web. These are commonly seen in the case of URLs, (Universal Resource Locator) or URI (Uniform Resource Indicator). Resources can be used to retrieve data, media.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
This is advised as to prevent security issues. This suggestion is based upon the principle of seperation of concerns. In other words it is advisable that each component of a system should be responsible for one individual task. When dealing with a JSON api, the form rendering and submission should be handled by the client side, this allows for further validation such as CSRF, and other input validators to be implemented. Then once posted to the server side, the server can be exclusively concerned with processing the submitted information. 


- What does idempotent mean? Which HTTP verbs are idempotent?
Idempotency is the concept of an action, that when performed many times (on the same data) will return the same result as if it has only been performed once. 
For example 

2 x 1 = 2
(2 x 1) x 1 x 1 x 1 x1 x1 x1 x1 x1 = 2

The HTTP verbs which are idempotent are GET, PUT/PATCH, and DELETE
POST is not idempotent, as with each POST request, new information will be (added) to the data set. 

- What is the difference between PUT and PATCH?

PUT and PATCH at surface level both mean to replace a piece of data. However more specifically PUT means to replace the entire piece of data, where if a specific property of that data is not included in the PUT request it will be nulled out in the replaced data. 

PATCH on the other hand means to replace the data with an "updated" version, where if the information send by the PATCH is present in the data, it will be updated, and if it is missing in the PATCH request, will not be deleted or affected in the targeted data of the API. 

- What is one way encryption?

One way encryption refers to encrypted information (passwords for example) where there is no known way or indentiable reverse engineering or decryption. This ensures security, and is achieved through hashing the password, which involves converting your password (or other data) into a short string of encrypted characters using an algorythm, when combined with a salt this makes a very difficult to decode password. Ensuring security for sensitive purposes. We will look at what a salt is in the next question. 

- What is the purpose of a `salt` when hashing a password?

A salt is a generated string of characters that is used as a component of the hashing procedure. The inputted password (or other data) is passed into a hashing function in combination with a generated salt (which is customizable as to how many salt rounds (hashing repitions) take place.) using an algorythm within the hashing function. The higher the amount of salt rounds, the more secure the password, however it will can result in longer loading times, therefore it is important to balance the need for the security against a smooth user experience. Hashing a password in combination with a salt completes the process of encryption and allows for high levels of security around saved passwords and other potentially sensitive information, that can not be easily reverse engineered. 

- What is the purpose of the Bcrypt module?

The Bcrypt module is a library that covers many methods related to encrpytion and authentication. It provides methods that we can use in the encryption processs such as generate_password_hash (or hashpw) which in both cases take an argument of the password to be hashed + a salt, (salt is made with the bcrypt.gensalt() method)

On the authentication side of things, bcrypt is also very useful as it provides us the method of chech_password_hash() which allows us to compare a user inputted password (inputted for example as part of the login process) agains the hashed user password stored in the DB. 

This is achieved by passing the user inputted password through the hashing (and salting) process and then comparing with the saved password. If they are equal, it may return true, and the higher order function to which it was called from may allow the user to be logged in! 

- What is the difference between authorization and authentication?

Authentication refers to the concept that we can prove the user is who they say they are. In the context of web development this is often achieved through the use of a password, and tested with the check_password_hash() method of bcrypt explained above in the previous question. 

Once authenticated, the user may then be "authorized" to access particular pages on the site. This could be achieved as part of the login route view, for example if User.authenticate == True, we could set the session storage property of guest as the users id. 
session['GUEST_ID'] = user.id
and then in our other view functions we could use the following conditional logic 
if session['GUEST_ID']:
    return_template('user_homepage.html')
else:
    return redirect("/")

The last piece of conditional logic is a simple example of authorization, if the user is logged in and declared (added) to the session storage, authorization is passed and we are allowed view the user homepage. 

If not we will be redirected to the homepage. 