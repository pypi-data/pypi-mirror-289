import tempfile
import textwrap
from micro_test_hub.services.Service import Service
import os
import random
import copy


class PubSubHandler(): 

    default_conf = {
                        "platform": "linux/amd64",
                        "image": "google/cloud-sdk",
                        "healthcheck": 
                        {
                            "test": [
                                "CMD-SHELL", "sh", "-c", "nc -z 127.0.0.1 8085 || exit 1"
                            ],"interval": "5s",
                            "timeout": "2s",
                            "retries": 3,
                            "start_period": "1s"
                        },
                        "environment": {
                                "PUBSUB_PROJECT_ID": "your-project-id"
                            },
                        "ports": "{host_port}:8085",
                        "command": "gcloud beta emulators pubsub start --host-port=0.0.0.0:8085"
                        }
    
    pub_sub_init_config = { 
                            "platform": "linux/amd64",
                            "depends_on": "{pub_sub_emulator_host}",
                            "build": {
                                            "context": "{code_folder}",
                                            "dockerfile": "dockerfile.docker"
                                            },
                            "environment": {
                                "PUBSUB_EMULATOR_HOST": "pub_sub_emulator"
                            }
                    
                            }
    
    docker_file_content = """
# Use the google/cloud-sdk base image
FROM google/cloud-sdk

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Install google-cloud-pubsub
RUN pip3 install google-cloud-pubsub

# Copy local code to the container image.
COPY ./* .

# Set the entrypoint to run the initialization script
ENTRYPOINT ["python3", "/init.py"]
"""

    init_script_content = """from google.cloud import pubsub_v1
import os
import time

# Set the Pub/Sub emulator host
os.environ["PUBSUB_EMULATOR_HOST"] = "pub_sub_emulator:8085"
PROJECT_ID = "your-project-id"

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

topics_subscriptions = {
    # "topic1": [("subscription1", "http://example.com/push1"), ("subscription2", "http://example.com/push2")],
    # "topic2": [("subscription3", "http://example.com/push3"), ("subscription4", "http://example.com/push4")]
    {TOPICS_SUBSCRIPTIONS}
}

for topic, subscriptions in topics_subscriptions.items():
    topic_path = publisher.topic_path(PROJECT_ID, topic)
    publisher.create_topic(request={"name": topic_path})
    print(f"Topic created: {topic}")

    for subscription_name, push_endpoint in subscriptions:
        subscription_path = subscriber.subscription_path(PROJECT_ID, subscription_name)
        push_config = pubsub_v1.types.PushConfig(push_endpoint=push_endpoint)
        subscriber.create_subscription(
            request={
                "name": subscription_path,
                "topic": topic_path,
                "push_config": push_config
            }
        )
        print(f"Subscription created: {subscription_name} with push endpoint: {push_endpoint}")
#time.sleep(60)        
"""
                           
    
                                   
    @classmethod
    def _load_default_config(cls, host_port_index):
        host_port = str(8185 + host_port_index)
        # get filename from file path
        config = copy.deepcopy(cls.default_conf)
        config['ports'] = [config['ports'].replace("{host_port}", host_port)]
        config['command'] = config['command'].replace("{host_port}", host_port)
            
        return config
    
    @classmethod
    def _load_initiator_config(cls, service_name, service_folder):
        
        # get filename from file path
        config = copy.deepcopy(cls.pub_sub_init_config)
        config['depends_on'] = [config['depends_on'].replace("{pub_sub_emulator_host}", service_name)]
        config['build']['context'] = service_folder
        
            
        return config
    
    @classmethod
    def _create_init_file(cls, service_folder, init_file_content):
       os.makedirs(service_folder, exist_ok=True)
       #init_file_content = init_file_content.replace("{code_folder}", service_folder) 
       #docker_file_content = textwrap.dedent(docker_file_content)  # Remove leading spaces
       with open(f"{service_folder}/init.py", "w") as file:
            file.write(init_file_content)    
            file_path = file.name
       os.chmod(file_path, 0o755)  # Set executable permissions
       return file_path    
   
    @classmethod
    def _create_docker_file(cls, code_folder, docker_file_content):
       os.makedirs(code_folder, exist_ok=True)
       docker_file_content = docker_file_content.replace("{code_folder}", code_folder) 
       docker_file_content = textwrap.dedent(docker_file_content)  # Remove leading spaces
       with open(f"{code_folder}/dockerfile.docker", "w") as file:
            file.write(docker_file_content)    
            file_path = file.name
       os.chmod(file_path, 0o755)  # Set executable permissions
       return file_path 

    
    # @classmethod
    # def create_topic_and_subscriptions(cls, project_id, topic):
        
    #     os.environ["PUBSUB_EMULATOR_HOST"] = "pub_sub_emulator:8085"
    #     print(f"after env set {topic.name}")
    #     # Create a Pub/Sub client
    #     publisher = pubsub_v1.PublisherClient()
    #     subscriber = pubsub_v1.SubscriberClient()

    #     # Create a topic
    #     topic_path = publisher.topic_path(project_id, topic.name)
    #     try:
    #         topic = publisher.create_topic(request={"name": topic_path})
    #         print(f"Topic created: {topic.name}")
    #     except AlreadyExists:
    #         print(f"Topic already exists: {topic_path}")
        
    #     for subscription in topic.subscriptions:
    #         push_config = pubsub_v1.types.PushConfig(push_endpoint=subscription.push_config.push_endpoint)
    #         # Create a subscription to the topic
    #         subscription_path = subscriber.subscription_path(project_id, subscription.name)
    #         subscription = subscriber.create_subscription(
    #             request={"name": subscription_path, "topic": topic.name, "push_config": push_config}
    #         )
    #         print(f"Subscription created: {subscription.name}", flush=True)
    @classmethod
    def create_topics_and_subscriptions(cls, service):
        topics_subscriptions_str = ""
        topics = service.topics
        for topic in topics:
            topics_subscriptions_str += f"    '{topic.name}': ["
            for subscription in topic.subscriptions:
                topics_subscriptions_str += f"('{subscription.name}', '{subscription.push_endpoint}'), "
            # remove trailing comma
            #topics_subscriptions_str = topics_subscriptions_str[:-2]    
            topics_subscriptions_str += "],\n"
        #print(f"topics_subscriptions_str: {topics_subscriptions_str}")
        return topics_subscriptions_str
        
       
    @classmethod        
    def build(cls, project_name, service:Service, index: int):                              
            
        return cls._load_default_config(index)             

    @classmethod        
    def build_initiator(cls, project_name, service:Service, index: int):     
        topics_subscriptions = cls.create_topics_and_subscriptions(service)
        init_script_content = cls.init_script_content.replace("{TOPICS_SUBSCRIPTIONS}", topics_subscriptions)
        random_number = random.randint(1000, 9999)
        temp_dir = tempfile.gettempdir()
        service_folder = f"/{temp_dir}/{service.name}_{random_number}"                         
        cls._create_init_file(service_folder, init_script_content)            
        cls._create_docker_file(service_folder, cls.docker_file_content)
        return cls._load_initiator_config(service.name, service_folder)             

