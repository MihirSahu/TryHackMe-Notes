# Burp Suite: Repeater


## What is Repeater?
- Allows us to craft or relay intercepted requests at will
- Helps to manually test an endpoint and write different request payloads
- Repeater interface
![Repeater diagram](images/repeater.png)
```
At the very top left of the tab, we have a list of Repeater requests. We can have many different requests going through Repeater: each time we send a new request to Repeater, it will appear up here.
Directly underneath the request list, we have the controls for the current request. These allow us to send a request, cancel a hanging request, and go forwards/backwards in the request history.
Still on the left-hand side of the tab, but taking up most of the window, we have the request and response view. We edit the request in the Request view then press send. The response will show up in the Response view.
Above the request/response section, on the right-hand side, is a set of options allowing us to change the layout for the request and response views. By default, this is usually side-by-side (horizontal layout, as in the screenshot); however, we can also choose to put them above/below each other (vertical layout) or in separate tabs (combined view).
At the right-hand side of the window, we have the Inspector, which allows us to break requests apart to analyse and edit them in a slightly more intuitive way than with the raw editor. We will cover this in a later task.
Finally, above the Inspector we have our target. Quite simply, this is the IP address or domain to which we are sending requests. When we send requests to Repeater from other parts of Burp Suite, this will be filled in automatically.
```

## Basic Usage
- Once request is intercepted in the Proxy, right click and Send to Repeater or `Ctrl+R`
- In the Repeater tab you can resend intercepted requests and view the response
- The requests can be modified and sent again, and the response is intercepted

## Views
- Different views are provided
	- Pretty: This is the default option. It takes the raw response and attempts to beautify it slightly, making it easier to read.
	- Raw: The pure, un-beautified response from the server.
	- Hex: This view takes the raw response and gives us a byte view of it -- especially useful if the response is a binary file.
	- Render: The render view renders the page as it would appear in your browser. Whilst not hugely useful given that we would usually be interested in the source code when using Repeater, this is still a neat trick.

## Inspector
- Supplementary to the request and respond fields, if you know how to read and edit HTTP requests then you won't use the Inspector much
- Displays a prettified breakdown of the requests and responses
- Can be used in both the Proxy and Repeater
- Allows you to modify requests
	- Query Parameters, which refer to data being sent to the server in the URL. For example, in a GET request to https://admin.tryhackme.com/?redirect=false, there is a query parameter called "redirect" with a value of "false".
	- Body Parameters, which do the same thing as Query Parameters, but for POST requests. Anything that we send as data in a POST request will show up in this section, once again allowing us to modify the parameters before re-sending.
	- Request Cookies contain, as you may expect, a modifiable list of the cookies which are being sent with each request.
	- Request Headers allow us to view, access, and modify (including outright adding or removing) any of the headers being sent with our requests. Editing these can be very useful when attempting to see how a webserver will respond to unexpected headers.
	- Response Headers show us the headers that the server sent back in response to our request. These cannot be edited (as we can't control what headers the server returns to us!). Note that this section will only show up after we have sent the request and received a response.
