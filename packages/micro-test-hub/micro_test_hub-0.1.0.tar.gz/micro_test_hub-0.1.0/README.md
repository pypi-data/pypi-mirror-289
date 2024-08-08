# team-moc-micro-test-hub
A system to support the creation of integration tests for MOC microservices

## GCP Artifacts Registry authentication

To authenticate with Google Cloud Platform's Artifact Registry, follow these steps:

1. **Install the Google Cloud SDK**: If you haven't already, download and install the Google Cloud SDK from [https://cloud.google.com/sdk/docs/install](https://cloud.google.com/sdk/docs/install).

2. **Authenticate your Google Cloud account**:
    Run the following command and follow the on-screen instructions to log in with your Google account:
    
    ```bash
    gcloud auth login

3. **Configure artifacts registry for region**: 
   
    ```bash
    gcloud auth configure-docker europe-west1-docker.pkg.dev

4. **Install micro-test-hub**:
	
	```bash
	python3 setup.py install

5. **Run micro-test-hub - no params**:

	```bash
	micro-test-hub

6. **Run micro-test-hub - with file param**:

	```bash
	micro-test-hub -f config.js	