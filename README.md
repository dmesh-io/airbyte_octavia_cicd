prerequisite: installed airbyte

git clone https://github.com/airbytehq/airbyte.git

# switch into Airbyte directory
cd airbyte

# start Airbyte
./run-ab-platform.sh

source:
https://medium.com/@jeremysrgt/airbyte-configuration-as-code-with-octavia-cli-dccd2046b764


1. install octavia
$ curl -s -o- https://raw.githubusercontent.com/airbytehq/airbyte/master/octavia-cli/install.sh | bash

2. octavia init



workflow for creating templates:

1. `octavia list connectors destinations | grep Azure`
2. copy hash id
3. `octavia generate destination <hash-id>` <destination name>
(4. copy to connections folder for template version control)


what does the script have to do?
source .env file
install and start airbyte
install and init octavia
move all templates to folders
octavia apply


problems and questions: 
- there is no orchestration of apply -> first sources and destinations then connections
- how to trigger a sync once? anscheinend mit airflow möglich https://airflow.apache.org/docs/apache-airflow-providers-airbyte/stable/operators/airbyte.html
auch als airbyte api call möglich https://reference.airbyte.com/reference/createjob

https://reference.airbyte.com/reference/createdestination