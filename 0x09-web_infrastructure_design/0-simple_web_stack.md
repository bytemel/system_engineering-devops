# **Simple web stack**
---
## **Description**
---
This basic web infrastructure hosts www.foobar.com. It operates without firewalls or SSL certificates, leaving the server's network unprotected.
The components—database and application server—rely on shared resources (CPU, RAM, and SSD) provided by the server.
## **Specifics about the infrastructure**
- What is a server
This is a physical or virtual machine that hosts all components of the website. It manages resources, processes requests, and serves content.
- The role of the domain name
The domain name (foobar.com) is a human-readable alias for the server's IP address (8.8.8.8). It allows users to access the website using a
memorable name instead of the numerical IP address.
- Type of DNS record www is in www.foobar.com
It is a CNAME record that maps www.foobar.com to 8.8.8.8.
- Role of the web server
It serves as the entry point for all incoming web traffic. It handles requests and returns responses. Also handles functions like load balancing
and caching.
- Role of the application server
Executes the application logic and generates dynamic content based on user requests. It communicates with the web server to handle these requests
and responses.
- Role of the database
Stores and retrieves the websites content. t's used for reading, writing, and modifying data required by the application.
- What is the server using to communicate with the computer of the user requesting the website
It communicates with the user's computer via HTTP/HTTPS protocols.
## **Issues with the infrastructure**
- Single Point of Failure(SPOF):
Since everything is hosted on one server, any failure in that server can bring down the entire website.
- Downtime during Maintenance:
When performing maintenance or deploying new code, the web server typically needs to be restarted, causing downtime during that period.
This affects user access to the site.
- Scalability Issues:
A single server setup can't efficiently handle sudden spikes in traffic. If there's a surge in visitors, the server might struggle to manage the
load, causing slow website performance or crashes.
