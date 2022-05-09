# Burp Suite: The Basics


## What is Burp Suite?
- Framework written in Java for web application penetration testing
- Burp is an industry standard tool
- Is used commonly when assessing mobile applications
- Burp can capture and manipulate all of the traffic between an attacker and a webserver
	- This traffic can be sent to other parts of the Burp framework
- Burp editions
	- Burp Suite Community
	- Burp Suite Professional
	- Burp Suite Enterprise

## Features of Burp Community
- Proxy - intercept and modify requests/responses in web apps
- Repeater - capture, modify, and resend same request multiple times
- Intruder - spray an endpoint with requests, used for fuzzing and brute forcing
- Decoder - transforms data
- Comparer - compare two pieces of data at word or byte level
- Sequencer - assess randomness of tokens such as cookie values or other supposedly randomly generated data

## The Dashboard
- The Tasks menu allows us to define background tasks that Burp Suite will run whilst we use the application. The Pro version would also allow us to create on-demand scans. The default "Live Passive Crawl" (which automatically logs the pages we visit) will be more than suitable for our uses in this module.
- The Event log tells us what Burp Suite is doing (e.g. starting the Proxy), as well as information about any connections that we are making through Burp.
- The Issue Activity section is exclusive to Burp Pro. It won't give us anything using Burp Community, but in Burp Professional it would list all of the vulnerabilities found by the automated scanner. These would be ranked by severity and filterable by how sure Burp is that the component is vulnerable.
- The Advisory section gives more information about the vulnerabilities found, as well as references and suggested remediations. These could then be exported into a report.

## Navigation
- Navigation can be done by using the top menu bars
- Each selected module can have more than one sub-tab
- Tabs can be detached using the `Window` on the application menu

## Options
- Global settings can be found in the `User options` tab
- Four main sections of the User options tab
```
The options in the Connections sub-tab allow us to control how Burp makes connections to targets. For example, we can set a proxy for Burp Suite to connect through; this is very useful if we want to use Burp Suite through a network pivot.
The TLS sub-tab allows us to enable and disable various TLS (Transport Layer Security) options, as well as giving us a place to upload client certificates should a web app require us to use one for connections.
An essential set of options: Display allows us to change how Burp Suite looks. The options here include things like changing the font and scale, as well as setting the theme for the framework (e.g. dark mode) and configuring various options to do with the rendering engine in Repeater (more on this later!).
The Misc sub-tab contains a wide variety of settings, including the keybinding table (HotKeys), which allowing us to view and alter the keyboard shortcuts used by Burp Suite. Familiarising yourself with these settings would be advisable, as using the keybinds can speed up your workflow massively.
```
- Project specific settings can be found in the `Project options` tab
- Five main sections of the Project options tab
```
Connections holds many of the same options as the equivalent section of the User options tab: these can be used to override the application-wide settings. For example, it is possible to set a proxy for just the project, overriding any proxy settings that you set in the User options tab. There are a few differences between this sub-tab and that of the User options, however. For example, the "Hostname Resolution" option (allowing you to map domains to IPs directly within Burp Suite) can be very handy -- as can the "Out-of-Scope Requests" settings, which enable  us to determine whether Burp will send requests to anything you aren't explicitly targeting (more on this later!).
The HTTP sub-tab defines how Burp handles various aspects of the HTTP protocol: for example, whether it follows redirects or how to handle unusual response codes.
TLS allows us to override application-wide TLS options, as well as showing us a list of public server certificates for sites that we have visited.
The Sessions tab provides us with options for handling sessions. It allows us to define how Burp obtains, saves, and uses session cookies that it receives from target sites. It also allows us to define macros which we can use to automate things such as logging into web applications (giving us an instant authenticated session, assuming we have valid credentials).
There are fewer options in the Misc sub-tab than in the equivalent tab for the "User options" section. Many of the options here are also only available if you have access to Burp Pro (such as those configuring Collaborator). That said, there are a couple of options related to logging and the embedded browser (which we will look at in a couple of tasks) that are well worth perusing.
```

## Introduction to the Burp Proxy
- Captures requests and responses that can be manipulated or sent to tother tools
- When a request is caught, the browser will hang until you decide to forward/drop the request
- Burp will log the requests made when the intercept is off and store them in `HTTP history`
- Proxy has its own options in `Options` tab
	- Notable options are `Intercept Server Responses` and `Match and Replace` (this lets you do things like change your user agent or remove all cookies)

## Connecting throught the Proxy with FoxyProxy
- Two ways to proxy traffic through Burp
	1. Use the embedded browser
	2. Configure our local web browser to proxy traffic through Burp
- Burp Proxy works by opening a port on `127.0.0.1:8080`, and we need to redirect all our traffic through this port
	- Can do so by altering browser settings or using a browser extension [FoxyProxy](https://getfoxyproxy.org/)
- To configure FoxyProxy just install the extension, create a new proxy profile, and set the IP to `127.0.0.1` and the port to `8080`
- Now when intercept is on and you're using the Burp profile on FoxyProxy all traffic will be tunnelled through Burp
- Remember: Whilst you are connected to the proxy and have the Proxy Intercept switched on, your browser will hang whenever you make a request. A very common mistake when you are learning to use Burp Suite (and indeed, later on!) is to accidentally leave the intercept switched on and ergo be unable to make any web requests through your browser. If your browser is hanging and you don't know why: check your proxy!
- Intercept the response to a request with `Do Intercept > Response to this request`

## Proxying HTTPS
- To allow Burp to intercept HTTPS:
	1. With the proxy active navigate to `http://burp/cert`, this will download a file
	2. Navigate to `about:preferences` in firefox, search for `certificates`
	3. Click `View Certificates` and `Import` the downloaded file

## The Burp Suite Browser
- Burp has a build in chromium browser that is pre configured to use the proxy
- People tend to stick to their own browser for customizability
- If you're running Burp as root, then Burp Suite will be unable to create a sandbox environment for the browser and throw an error
- Two solutions
```
The smart option: We could create a new user and run Burp Suite under a low privilege account.
The easy option: We could go to Project options -> Misc -> Embedded Browser and check the Allow the embedded browser to run without a sandbox option. Checking this option will allow the browser to start, but be aware that it is disabled by default for security reasons: if we get compromised using the browser, then an attacker will have access to our entire machine. On the training environment of the AttackBox this is unlikely (and isn't a huge issue even if it does happen), but keep it in mind if you try this on a local installation of Burp Suite.
```

## Scoping and Targeting
- Burp logs everything and can mess up logs that we might want to send to clients
- Scoping - sets a score for the project that allows us to define what gets proxied and logged
- We can restrict Burp to only target the web applications that we want to test
- Navigate to `Target`, right click on the target from the list, and choose `Add to scope`. Then check the `Score` sub-tab

## Site Map and Issue Definitions
- Three sub-tabs under `Target`
```
Site map allows us to map out the apps we are targeting in a tree structure. Every page that we visit will show up here, allowing us to automatically generate a site map for the target simply by browsing around the web app. Burp Pro would also allow us to spider the targets automatically (i.e. look through every page for links and use them to map out as much of the site as-is publicly accessible using the links between pages); however, with Burp Community, we can still use this to accumulate data whilst we perform our initial enumeration steps.
The Site map can be especially useful if we want to map out an API, as whenever we visit a page, any API endpoints that the page retrieves data from whilst loading will show up here.
Scope: We have already seen the Scope sub-tab -- it allows us to control Burp's target scope for the project.
Issue Definitions: Whilst we don't have access to the Burp Suite vulnerability scanner in Burp Community, we do still have access to a list of all the vulnerabilities it looks for. The Issue Definitions section gives us a huge list of web vulnerabilities (complete with descriptions and references) which we can draw from should we need citations for a report or help describing a vulnerability.
```
- Site map - generates a site map of links
