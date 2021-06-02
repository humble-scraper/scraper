# HumbleBundleScraper

A service that retrieves a list of book titles that are packaged in a book
bundle on Humble Bundle. Everytime a new book bundle comes out, the service
will generate a booklist and search for any free download links on z-books or
other sites. The service exposes a RESTful API for its mailing list, in which
the user can add their email address to receive the latest booklists,
along with links to a free download of the book, in their email inbox.
You can also respond to any email from the service with the message "favorite",
"add to favourites", "add to favorites: book1 book2 ..." to add the given books
or list of books to your favourites list, which can be queried via another API.
The service will expose its API via 2 routes: you can respond or send emails to
the service to invoke the API, or you can use the REST API directly. There are
2 ways of authenticating: emails from your address are assumed to be you,
otherwise you use the RESTful API with OAuth2. The service will be designed
from the backend and API first. Afterwards, I may do a basic web gui in react.

