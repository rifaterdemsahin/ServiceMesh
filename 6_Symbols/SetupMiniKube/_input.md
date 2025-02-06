--- input
1. **Start Minikube:**
-   minikube start

2. **Build the Docker image using Minikube's Docker daemon:**
-   eval $(minikube -p minikube docker-env)


-   docker build -t your-service-mesh .


2.5 **Tag the Docker image:**
-   docker tag your-service-mesh orange-guacamole-6w5jqx7vgw3rggw-5000.app.github.dev/your-service-mesh

2.6 **Push the Docker image to the remote repository:**
-   docker push orange-guacamole-6w5jqx7vgw3rggw-5000.app.github.dev/your-service-mesh


3. **Create a Kubernetes deployment:**
-   kubectl create deployment your-service-mesh --image=your-service-mesh 

4. **Expose the deployment:**
-   kubectl expose deployment your-service-mesh --type=LoadBalancer --port=5000

5. **Access the service:**
-   minikube service your-service-mesh