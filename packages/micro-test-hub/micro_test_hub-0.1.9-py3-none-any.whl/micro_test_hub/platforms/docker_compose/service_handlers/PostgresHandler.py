from micro_test_hub.services.Service import Service
import os
import tempfile
import textwrap
import copy

class PostgresHandler(): 

    default_conf = {
                    "platform": "linux/amd64",
                        "healthcheck": 
                        {
                            "test": [
                                "CMD-SHELL", "sh", "-c", "nc -z 127.0.0.1 5432 || exit 1"
                            ],"interval": "5s",
                            "timeout": "2s",
                            "retries": 3,
                            "start_period": "1s"
                        },
                        "environment": {
                            "POSTGRES_USER": "postgres",
                            "POSTGRES_PASSWORD": "123456!",
                            "POSTGRES_DB": "{db_name}"
                        },
                        "image": "postgres:13.5",
                        "ports": "{host_port}:5432",
                        "volumes": ["/var/lib/postgresql/13/main/{db_name}:/var/lib/postgresql",
                                    "{sql_init_file_path}:/docker-entrypoint-initdb.d/{sql_init_file}",
                                    "{temp_sh_file}:/docker-entrypoint-initdb.d/init-schema.sh"]

                    }
    sh_file_content = """
#!/bin/bash
set -e

# The database name and user are obtained from the environment variables.
DB_NAME=$POSTGRES_DB
DB_USER=$POSTGRES_USER

# Execute the SQL schema file.
echo "Initializing the database schema..."
psql -v ON_ERROR_STOP=1 --username "$DB_USER" --dbname "$DB_NAME" <<-EOSQL
    \i '/docker-entrypoint-initdb.d/{sql_init_file}'
EOSQL

echo "Database schema initialized successfully."
"""
    @classmethod
    def create_init_db_sh_file(cls, init_sql_file):
       sh_file_content = cls.sh_file_content.replace("{sql_init_file}", init_sql_file) 
       sh_file_content = textwrap.dedent(sh_file_content)  # Remove leading spaces
       with tempfile.NamedTemporaryFile(delete=False, suffix=".sh") as temp_file:
            temp_file.write(sh_file_content.encode())
            temp_file_path = temp_file.name
       os.chmod(temp_file_path, 0o755)  # Set executable permissions
       return temp_file_path
            
                                
    @classmethod
    def load_default_config(cls, service_name, host_port_index, init_sql_file_path, temp_sh_file):
        host_port = str(5432 + host_port_index)
        # get filename from file path
        init_sql_file = os.path.basename(init_sql_file_path)
        config = copy.deepcopy(cls.default_conf)
        config['ports'] = [config['ports'].replace("{host_port}", host_port)]
        config['environment']['POSTGRES_DB'] = config['environment']['POSTGRES_DB'].replace("{db_name}", service_name)
        for index, volume in enumerate(config['volumes']):
            config['volumes'][index] = config['volumes'][index].replace("{db_name}", service_name)
            config['volumes'][index] = config['volumes'][index].replace("{sql_init_file_path}", init_sql_file_path)
            config['volumes'][index] = config['volumes'][index].replace("{sql_init_file}", init_sql_file)
            config['volumes'][index] = config['volumes'][index].replace("{temp_sh_file}", temp_sh_file)
            
        return config
    
    
    @classmethod        
    def build(cls, service: Service, index: int):     
        service_dict = {}
        init_sql_file_path = service.sql_init_file
        init_sql_file = os.path.basename(init_sql_file_path)
        temp_sh_file = cls.create_init_db_sh_file(init_sql_file)
        service_dict = cls.load_default_config(service.name, index, init_sql_file_path, temp_sh_file)
        
        return service_dict                    
    