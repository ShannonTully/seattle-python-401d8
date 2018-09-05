# Authentication and Authorization

## Controlling Access
One thing you may have noticed while testing your app in a browser is that you did not have to log in. Convenient, but not really all that safe. Knowing the kind of place the internet is, you probably don’t want to allow just anyone to post journal entries in your journal.

The process of verifying the identity of a user visiting your website is called authentication (AuthN for short). The closely related, but different process of determining what rights an authenticated user has in your website is called authorization (AuthZ).

## Principals
Both AuthN and AuthZ depend on identity. In a website, Identity is tied to the concept of principals. Principals can be called users, groups, roles, or any of a number of other names. But behind them all stands the basic idea of an identifier that can be used for both authentication and authorization.

## Policies
To authenticate a user, the most basic pattern is to confirm a username and password. In general the steps are to:

1. Harvest a username and password as provided by a visitor
1. Reject them if either is missing
1. Reject them if they cannot be confirmed to be correct
1. Otherwise, persist the fact that the user is authenticated

HTTP is a stateless protocol. That means that no individual request can know anything about any other request. So how do you accomplish that fourth goal? The usual method is to send an encrypted cookie back to the user in an HTTP response. This cookie is saved and re-transmitted to the server with each successive request. This gets around the stateless nature of HTTP by sending the required information back and forth.

By default, Pyramid does not enable authentication. There are a lot of use-cases for building an application that does not require any login. Our applications really do need it, though, so we’ll need to enable AuthN and AuthZ

In Pyramid, both AuthN and AuthZ are implemented using policies. These policies are classes with a specific set of methods and attributes that fulfill a required contract.

Policies for AuthN are made available in the pyramid.authentication package. For our authentication policy we’ll be using the AuthTktAuthenticationPolicy. This policy issues an encrypted, specially formatted cookie to the user’s browser. Whenever a new request comes in, Pyramid unencrypts the cookie and establishes the identity of the user from the data it contains.

## Permissions
Once policies have been configured for authentication and authorization, we are ready to make assertions about what permissions we want to require for our views.

Once again, Pyramid does not, by default, require any permissions for any views. There are many applications where none are required. But our app should.

## Permissions, Context and ACLs
In Pyramid, views are responsible for requiring a permission. But how do we determine what permissions are assigned to a specific principal? That is a task that falls to context.

Context is best defined as where you are in an application. In a basic Pyramid app, context is provided by a root object. The root object is created when an incoming request is handled. A root factory is a class that can be instantiated with a request. A specific instance of the root factory serves as the root for a given request.

When a visitor to a site requests a particular view, the Pyramid framework inspects the configuration of that view to determine which permission is required. Then the framework finds the root object and asks it for information about what permissions are granted to the current principal. The root object must provide an `__acl__` special attribute.

An ACL is an access control list. It is expressed as a list of tuples, each of which specifies a relationship between a principal and a permission. Each tuple contains exactly three values:

- An action (one of pyramid.security.Allow or pyramid.security.Deny)
- A principal (a string or special value that is matched against the current principal)
- A permission (a string or special value that is matched against the required permission)


# Encryption
### _**NEVER store user passwords in plain text.**_

Passwords should always be stored in a hashed form. This means that we should put the plain text password through a one-way algorithm that changes it in a way we cannot undo.

When the user provides their password, we put it through the same algorithm. If the result matches the hashed value we stored, then the starting point must have been the same. The passwords are matched, and the user has proven their identity.
