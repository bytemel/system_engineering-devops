# **Distributed web infrastructure**
---
## **Description**
This is a distributed web infrastructure that utilizes two servers to balance the work load. The load balancer manages traffic distribution
between the primary server and the replica server sharing the load. This infrastructure aims to reduce strain on the primary server, ensuring
smoother operation by distributing incoming requests across both servers.
## **Specifics about the infrastructure**
- Reason for added elements:
    - Additional server: For reducing redundancy
    - Load Balancer: For traffic distribution
- Distribution algorithm for load balanacing and how it works:
The HAproxy load balancer uses a round-robin algorithm to distribute incoming requests across the two servers in a circular order. This ensures a
fair distribution of traffic among the servers.
- Active-Active vs. Active-Passive Setup:
The setup enables Active-Active functionality. In  Active-Active, both servers actively handle incoming requests simultaneously. In Active-Passive
, one server remains inactive (passive) until the active server fails, then it takes over. Active-Active ensures both servers share the workload
constantly.
- Database Primary-Replica Cluster:
This setup involves a Primary (Master) database that handles write operations and replicates data to Replica (Slave) databases. Replicas handle
read operations and maintain a copy of the data from the Primary.
- Primary vs. Replica Node for the Application:
The application typically interacts with the Primary node for write operations, ensuring data consistency. The Replica nodes are utilized for read
operations to distribute the read load and improve performance.
## **Issues with the infrastructure**
- Single Points of Failure (SPOF):
Irregards of there being two servers, components such as the load balancer and database could still lead to single point of failure if they fail,
impacting overall system availability
- Security issues:
Lack of firewall configurations and HTTPS implementation poses security risks, potentially exposing sensitive data to vulnerabilities or
unauthorized access.
- No monitoring:
Without a monitoring system in place, it's challenging to identify performance issues, potential failures, or security breaches in real-time,
hindering proactive problem-solving and system optimization.
