#Designs for the homepage and the dashboard

The designs is handled by a branch named designBranch. This simulates the design team working on the similar project

We use a bootstrap framework for the CSS and Javascript for all the pages. Going further, we use a CDN version of the bootstrap. According to research from this link 
https://stackoverflow.com/questions/2180391/why-should-i-use-googles-cdn-for-jquery/2180401#2180401 there are a lot of good reason to use a CDN

In brief :

1. It increases the parallelism available.
(Most browsers will only download 3 or 4 files at a time from any given site.)

2. It increases the chance that there will be a cache-hit.
(As more sites follow this practice, more users already have the file ready.)

3. It ensures that the payload will be as small as possible.

All the pages should have the viewport meta tag for responsiveness. If excluded may cause undesirable behaviour with bootstap

Homepage: 

index.html: This is the homepage of the application where user is presented with a sign in form. If he is a new user, an option to register an account is presented that links to the signup page

signup.html: 

A page to register new users. Uses email and password for registration

OOP UML Diagram:

![uml class diagram](https://github.com/mirr254/Andela-Developer-Challenge-Shopping-List/blob/master/app/Designs/ShoppingListUML.png)

The UML diagram is prepared using www.creately.com and can be found on the link 
http://creately.com/diagram/example/j6tsr7291