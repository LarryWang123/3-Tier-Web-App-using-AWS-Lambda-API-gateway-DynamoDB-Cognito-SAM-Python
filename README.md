# 3-Tier-Web-App-using-AWS-Lambda-API-gateway-DynamoDB-Cognito-SAM-Python
3-Tier-Web-App-using-AWS-Lambda-API-gateway-DynamoDB-Cognito-SAM-Python.
…or create a new repository on the command line
 echo "# 3-Tier-Web-App-using-AWS-Lambda-API-gateway-DynamoDB-Cognito-SAM-Python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/LarryWang123/3-Tier-Web-App-using-AWS-Lambda-API-gateway-DynamoDB-Cognito-SAM-Python.git
git push -u origin main
…or push an existing repository from the command line
 git remote add origin https://github.com/LarryWang123/3-Tier-Web-App-using-AWS-Lambda-API-gateway-DynamoDB-Cognito-SAM-Python.git
git branch -M main
git push -u origin main

Features
➢ A 3-tier application architecture is a modular client-server architecture that consists of a
presentation tier, an application tier and a data tier. The three tiers are logical, not physical,
and may or may not run on the same physical server.
➢ Presentation Tier:The presentation tier is the user interface and communication layer of the
application, where the end user interacts with the application. Its main purpose is to display
information to and collect information from the user. This top-level tier can run on a web browser,
as desktop application, or a graphical user interface (GUI), for example.
➢ Application Tier: The application tier, also known as the logic tier or middle tier, is the heart of
the application. In this tier, information collected in the presentation tier is processed - sometimes
against other information in the data tier - using business logic, a specific set of business rules.
➢ Data Tier: The data tier, sometimes called database tier, data access tier or back-end, is where
the information processed by the application is stored and managed.
➢ Serverless Architecture: A way to build and run applications and services without having to manage infrastructure. Automated and
flexible scaling based on your workload volume.
➢ IaC deployment: Automatically deploy the main infrastructure by using SAM template. SAM is an open-source framework for building
Serverless application, it transforms and expands SAM template files to the desired AWS CloudFormantion resources and
dependencies, you can launch and configure them together as a stack.
➢ User authentication: User sign-in/sign-up interface integrated with Amazon Cognito to control the users access to your web app.
➢ Data protection: Encrypt the data in S3 bucket and DynamoDB by Amazon S3 master key(SSE-S3) or using KMS AWS managed CMK.
➢ DynamoDB: A fully managed non-relational database service that provides fast and predictable performance with seamless scalability.
➢ Website protection:
➢ WAF (Web Application Firewall): Filter, block and monitor the traffic between web application and internet. Protect your web
applications or APIs from web attacks.
➢ HTTP over SSL: Secure communication over internet with Custom SSL certificate
➢ GuardDuty enabled: A continuous security monitoring service, analyzes and processes the data sources to find potential threads.
➢ AWS Shield: DDOS protection at network and transportation layer
➢ AWS CloudFront: Global scaled network for fast content delivery with low latency and high performance integrated with AWS shield.

