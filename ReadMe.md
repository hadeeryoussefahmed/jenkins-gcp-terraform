<h1>Overview</h1>
This project showcases the creation of a comprehensive CI/CD (Continuous Integration/Continuous Deployment), </br>
pipeline on Google Cloud Platform (GCP). The project evaluates expertise in various domains, including GCP,</br>
Networking, Development, Terraform, Docker, Kubernetes, and Jenkins as the CI/CD tool. </br>
 In this project, we deploy a simple Python Flask web application (stateless) using two primary Jenkins CI/CD pipelines</br>
The first pipeline is responsible for building the project's infrastructure in GCP, and the second pipeline deploys the(stateful) replicated across 3 zones and consisting </br>
Python application.

<h1>Key Features</h1>
1-Jenkins CI/CD Pipeline for Infrastructure Setup:</br>
      -This pipeline is connected to the project on GitHub.</br>
      -Utilizes Terraform modules to build the required infrastructure on GCP.</br>
      -Infrastructure components:</br>
            1-IAM: Sets up 2 service accounts with N roles.</br>
            2-Network: Creates 1 VPC, 2 subnets, N firewall rules, and 1 NAT gateway.</br>
            3-Compute: Deploys 1 public VM and 1 private GKE standard cluster across 3 zones.</br>
            4-Storage: Establishes an Artifact Registry repository to store container images.</br>


 2-Jenkins CI/CD Pipeline for Application Deployment:</br>
         -This pipeline runs on the public VM created in GCP.</br>
         -It is automatically triggered by the first pipeline upon successful completion.</br>
         -The second pipeline performs the following tasks:</br>
             1-Dockerizes the Python Flask web application and pushes the app image to the Artifact Registry on GCP.</br>
             2-Deploys the Python Flask web application to the private GKE Cluster.</br>
             3-Exposes the web application using an ingress/load balancer.</br>

<h1>Security Considerations</h1>
1. The management VM (public) is accessible only from the Jenkins server, enhancing security. </br>
2. The GKE cluster (private) has no direct access to the internet, improving network security.</br>
3. The VM is used for cluster management and building/pushing container images to the Artifact Registry.</br>
4. All deployed images must be stored in the Artifact Registry, ensuring image versioning and traceability.</br>

Prerequisites</h1>
Before setting up this CI/CD pipeline, ensure you have the following prerequisites in place:</br>
1. A GCP account with appropriate permissions.</br>
2.  Jenkins installed and configured on your server.</br>
3. A GitHub repository for the project.</br>
4.  Terraform, Docker, and Kubernetes tools installed on your Jenkins server.</br>

<h1>Usage</h1>
1-Setting up the Infrastructure:</br>
-Clone this GitHub repository.</br>
-Configure Jenkins to run the first CI/CD pipeline, linked to the GitHub repository.</br>
-Trigger the pipeline to build the GCP infrastructure.</br>
2-Deploying the Application:</br>
-Once the infrastructure setup is complete, the second CI/CD pipeline will automatically trigger.</br>
-This pipeline will dockerize the web application, push the image to the Artifact Registry, and deploy it to the GKE cluster.</br>
