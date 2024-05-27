# **Secured and monitored web infrastructure**
---
## **Description**
This two-server infrastructure hosts www.foobar.com, securing it by utilizing firewalls to control traffic and SSL certificates to encrypt user
interactions. Each server handles web serving, application functions, and database tasks. Additionally, monitoring clients collect performance
data for proactive maintenance.
## **Specifics about the infrastructure**
- Reason for added elemets:
    - Firewalls: To increase security by controlling network traffic
    - SSL certificate: To secure data in transit
    - Monitoring clients: To collect performance data for proactive maintenance and issue identification
- Purpose for Firewalls:
To regulate network traffic, acting as a barrier between trusted internal networks and untrusted external networks, preventing unauthorized access
to internal resources and potential threats.
- HTTPS for Traffic:
HTTPS encrypts data transmitted between clients and servers, ensuring data security during transmission.
- Monitoring Purpose:
Monitoring tools track server performance, identify potential threats, and aid in proactive maintenance and issue resolution.
- Data Collection by Monitoring Tool:
The monitoring tool collects data through agents or data collectors installed on the servers, gathering metrics, logs, and performance data for
analysis.
- Monitoring Web Server QPS:
To monitor web server QPS (queries per second), ou'd configure the monitoring tool to track the number of incoming requests per second on the webs
servers.
## **Issues with the infrastructure**
- Terminating SSL at Load Balancer Level:
Terminating SSL at the load balancer might expose decrypted data within the internal network, potentially risking data security.
- Single MySQL Server Accepting Writes:
Having only one MySQL server accepting write operations poses a single point of failure. If this server fails, write operations become unavailable
, impacting the website's functionality.
- Identical Servers' Components:
If the serves have identical components (database, web server, and application server), a failure in one component across multiple servers could
lead to a widespread issue affecting the entire infrastructure. Diversifying components across servers mitigates this risk.
