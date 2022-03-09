![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)

# 0x09. Web infrastructure design
<div style="text-align: justify">
	
In this project, you should be research and learn about of Web Infrastructure Design. So, this project consists a collection of web infrastructure designs that could be implemented in any web development project. The files contain links to each respective whiteboard diagram.
	
<p align="center">
  <img width="250"  
        src="https://github.com/Alexoat76/holberton-system_engineering-devops/blob/main/0x09-web_infrastructure_design/assets/Server-storage.png"
  >
</p>

<div style="text-align: justify">
Don't forget to fully meet the following development requirements. </div>


# Getting Started :running:

## Table of Contents :clipboard:

* [Requirements](#requirements-page_with_curl)
* [Tasks](#tasks-page_with_curl)
* [Credits](#credits)

## Requirements :page_with_curl:

### Resources

**Read or watch** :

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=What+is+Web+infrastructure+design&sxsrf=APq-WBsKK_PLxc_urjgSy0EdwtOe9vTEkQ%3A1646833409261&ei=Aa8oYofMD5SYwbkPqM6DyA0&ved=0ahUKEwjH0PPClLn2AhUUTDABHSjnANkQ4dUDCA4&uact=5&oq=What+is+Web+infrastructure+design&gs_lcp=Cgdnd3Mtd2l6EAMyCAghEBYQHRAeMggIIRAWEB0QHjIICCEQFhAdEB4yCAghEBYQHRAeOgkIIxCwAxAnEBM6CQgAELADEAgQHjoHCCMQsAIQJzoKCAAQCBANEB4QE0oECEEYAUoECEYYAFDWDFjIGGCVTmgCcAB4AIABlwKIAfkKkgEFMC44LjGYAQCgAQHIAQTAAQE&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=What+is+Web+infrastructure+design)

### Concepts:
	
- `DNS`
- `Monitoring`
- `Web Server`
- `Network basics`
- `Load balancer`
- `Server`
- [What is a database](https://www.techtarget.com/searchdatamanagement/definition/database)
- [What’s the difference between a web server and an app server?](https://www.youtube.com/watch?v=S97eKyv2b9M)
- [DNS record types](https://pressable.com/?s=DNS&post_type=knowledgebase)
- [Single point of failure](https://en.wikipedia.org/wiki/Single_point_of_failure)
- [How to avoid downtime when deploying new code](https://softwareengineering.stackexchange.com/questions/35063/how-do-you-update-your-production-codebase-database-schema-without-causing-downt#answers-header)
- [High availability cluster (active-active/active-passive)](https://docs.oracle.com/cd/E17904_01/core.1111/e10106/intro.htm#ASHIA712)
- [What is HTTPS](https://www.instantssl.com/http-vs-https)
- [What is a firewall](https://www.webopedia.com/definitions/firewall/)
	
## General :page_with_curl:
	
- A `README.md` file, at the root of the folder of the project, is mandatory.
- For each task, once you are done whiteboarding (on a whiteboard, piece of paper or software or your choice), take a picture/screenshot of your diagram.
- This project will be manually reviewed:
- As each task is completed, the name of that task will turn green.
- Upload a screenshot, showing that you completed the required levels, to any image hosting service.
- For the following tasks, insert the link from of your screenshot into the answer file.
- After pushing your answer file to GitHub, insert the GitHub file link into the URL box.
- You will also have to whiteboard each task in front of a mentor, staff or student - no computer or notes will be allowed during the whiteboarding session.
- Focus on what you are being asked:
- Cover what the requirements mention, we will explore details in a later project.
- Keep in mind that you will have 30 minutes to perform the exercise, you will get points for what is asked in requirements.
- Similarly in a job interview, you should answer what the interviewer asked for, be careful about being too verbose - always ask the interviewer if going into details is necessary - speaking too much can play against you
- In this project, again, avoid going in details if not asked

## Tasks :page_with_curl:

### 0. `Simple web stack.`
A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a `LAMP` stack.<br/>
 + [x] **[0-simple_web_stack](0-simple_web_stack)** Contains the `URL` of an image containing the design of a one server web infrastructure that hosts the website that is reachable via `www.foobar.com` Start having a user wanting to access your website.

**Contains:**
- 1 server.
- 1 web server `(Nginx).`
- 1 application server.
- 1 application files `(your code base).`
- 1 database `(MySQL).`
- 1 domain name foobar.com configured with a www record that points to your server `IP 8.8.8.8`.

**DESCRIPTION**

This is a simple web infrastructure that hosts a website that is reachable via `www.foobar.com`. There are no firewalls or `SSL certificates` for protecting the server's network. Each component (database, application server) has to share the resources (`CPU`, `RAM`, and `SSD`) provided by the server.

*Specifics About This Infrastructure.*

+ **What a server is.**<br/>A server is a computer hardware or software that provides services to other computers, which are usually referred to as *clients*.

+ **The role of the domain name.**<br/>To provide a human-friendly alias for an `IP Address`. For example, the domain name `www.wikipedia.org` is easier to recognize and remember than `208.80.154.232`. The IP address and domain name alias is mapped in the Domain Name System `(DNS)`

+ **The type of DNS record `www` is in `www.foobar.com`.**<br/>`www.foobar.com` uses an **A record**. This can be checked by running `dig www.foobar.com`.<br/>**Note:** the results might be different but for the infrastructure in this design, an **A** record is used.<br/>
<i>Address Mapping record (A Record)—also known as a DNS host record, stores a hostname and its corresponding IPv4 address.</i>

+ **The role of the web server.**<br/>The web server is a software/hardware that accepts requests via `HTTP` or secure HTTP `(HTTPS)` and responds with the content of the requested resource or an error messsage.

+ **The role of the application server.**<br/>To install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

+ **The role of the database.**<br/>To maintain a collection of organized information that can easily be accessed, managed and updated

+ **What the server uses to communicate with the client (computer of the user requesting the website).**<br/>Communication between the client and the server occurs over the internet network through the TCP/IP protocol suite.
	
*Issues With This Infrastructure.*

+ **There are multiple SPOF (Single Point Of Failure) in this infrastructure.**<br/>For example, if the MySQL database server is down, the entire site would be down.

+ **Downtime when maintenance needed.**<br/>When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime.

+ **Cannot scale if there's too much incoming traffic.**<br/>It would be hard to scale this infrastructure becauses one server contains the required components. The server can quickly run out of resources or slow down when it starts receiving a lot of requests.
	
---
	
### 1. `Distributed web infrastructure.`
+ [x] **[1-distributed_web_infrastructure](1-distributed_web_infrastructure)** Contains the `URL` of an image containing the design of a three server web infrastructure that hosts the website `www.foobar.com.`

**Contains:**
- 2 servers.
- 1 web server `(Nginx).`
- 1 application server.
- 1 load-balancer `(HAproxy).`
- 1 set of application files `(your code base).`
- 1 database `(MySQL).`
	
**DESCRIPTION**

This is a distributed web infrastructure that atttempts to reduce the traffic to the primary server by distributing some of the load to a replica server with the aid of a server responsible for balancing the load between the two servers (primary and replica).

*Specifics About This Infrastructure.*

+ **The distribution algorithm the load balancer is configured with and how it works.**<br/>The `HAProxy` load balancer is configured with the *`Round Robin`* distribution algorithm. This algorithm works by using each server behind the load balancer in turns, according to their weights. It’s also probably the smoothest and most fair algorithm as the servers’ processing time stays equally distributed. As a dynamic algorithm, *`Round Robin`* allows server weights to be adjusted on the go.
	
+ **The setup enabled by the load-balancer.**<br/>The `HAProxy` load-balancer is enabling an *Active-Passive* setup rather than an *`Active-Active`* setup. In an *`Active-Active`* setup, the load balancer distributes workloads across all nodes in order to prevent any single node from getting overloaded. Because there are more nodes available to serve, there will also be a marked improvement in throughput and response times. On the other hand, in an *`Active-Passive`* setup, not all nodes are going to be active (capable of receiving workloads at all times). In the case of two nodes, for example, if the first node is already active, the second node must be passive or on standby. The second or the next passive node can become an active node if the preceding node is inactive.
	
+ **How a database *`Primary-Replica`* (*Master-Slave*) cluster works.**<br/>A *`Primary-Replica`* setup configures one server to act as the *Primary* server and the other server to act as a *`Replica`* of the *`Primary`* server. However, the *`Primary`* server is capable of performing read/write requests whilst the *`Replica`* server is only capable of performing read requests. Data is synchronized between the *`Primary`* and *Replica* servers whenever the *`Primary`* server executes a write operation.
	
+ **The difference between the *Primary* node and the *`Replica`* node in regard to the application.**<br/>The *`Primary`* node is responsible for all the write operations the site needs whilst the *`Replica`* node is capable of processing read operations, which decreases the read traffic to the *`Primary`* node.

*Issues With This Infrastructure.*

+ **There are multiple `SPOF` (Single Point Of Failure).**<br/>For example, if the Primary `MySQL` database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also `SPOFs`.
	
+ **Security issues.**<br/>The data transmitted over the network isn't encrypted using an `SSL certificate` so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
	
+ **No monitoring.**<br/>We have no way of knowing the status of each server since they're not being monitored.
	
---
	
### 2. `Secured and monitored web infrastructure.`
+ [x] **[2-secured_and_monitored_web_infrastructure](2-secured_and_monitored_web_infrastructure)** Contains the `URL` of an image containing the design of a three server web infrastructure that hosts the website `www.foobar.com` it must be secured, serve encrypted traffic, and be monitored.

**Contains:**
- 3 firewalls.
- 1 SSL certificate to serve `www.foobar.com` over `HTTPS`.
- 3 monitoring clients (data collector for `Sumologic` or other monitoring services).

**DESCRIPTION**

This is a 3-server web infrastructure that is secured, monitored, and serves encrypted traffic.

*Specifics About This Infrastructure.*

+ **The purpose of the firewalls.**<br/>The firewalls are for protecting the network (web servers, anyway) from unwanted and unauthorized users by acting as an intermediary between the internal network and the external network and blocking the incoming traffic matching the aforementioned criteria. 
	
+ **The purpose of the SSL certificate.**<br/>The SSL certificate is for encrypting the traffic between the web servers and the external network to prevent man-in-the-middle attacks (MITM) and network sniffers from sniffing the traffic which could expose valuable information. The SSL certs ensure privacy, integrity, and identification.
	
+ **The purpose of the monitoring clients.**<br/>The monitoring clients are for monitoring the servers and the external network. They analyse the performance and operations of the servers, measure the overall health, and alert the administrators if the servers are not performing as expected. The monitoring tool observes the servers and provides key metrics about the servers' operations to the administrators. It automatically tests the accessibility of the servers, measures response time, and alerts for errors such as corrupt/missing files, security vulnerabilities/violations, and many other issues. 

*Issues With This Infrastructure.*

+ Terminating `SSL` at the load balancer level would leave the traffic between the load balancer and the web servers unencrypted.
+ Having one `MySQL server` is an issue because it is not scalable and can act as a single point of failure for the web infrastructure.
+ Having servers with all the same components would make the components contend for resources on the server like `CPU`, `Memory`, `I/O`, etc., which can lead to poor performance and also make it difficult to locate the source of the problem. A setup such as this is not easily scalable. 
	
---
	
## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Angelica Rodríguez`**, **`Elizabeth González`** and **`Alex Arévalo`**.

<3333@holbertonschool.com>

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Angelicarm3)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)]()
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)]()
	
<3907@holbertonschool.com>	

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Artemisse99)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)]()
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)]()

<3915@holbertonschool.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)
	
## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).