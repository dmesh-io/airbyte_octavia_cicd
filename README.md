# Airbyte CI/CD Deployment for Integration tests

## Local Deployment

start in repository root and clone the airbyte repo with:

```bash
git clone https://git.com/airbytehq/airbyte.git
```

Start airbyte server. Let this run in background. You can access this airbyte instance in browser url `http://localhost:8000`. Default username is airbyte, password is password.

```bash
airbyte/run-ab-platform.sh
```

Next, install octavia with this statement:

```bash
curl -s -o- https://raw.githubusercontent.com/airbytehq/airbyte/master/octavia-cli/install.sh | bash
```

### Octavia workflow
The yaml connectors in `airbyte_connection_templates` can now be deployed to the airbyte instance without accessing the UI. First initialize octavia for the airbyte instance:

```bash
mkdir octavia && cd octavia
octavia init
```

Octavia creates empty folders for sources, destinations and connections with additional metadata files. The yaml files need to be copied there now. Execute this:

```bash
./copy_template_files.sh
```

Now octavia can deploy the connector with:
```bash
cd octavia && octavia apply
```

You can go to your airbyte UI and check if the adapters are visible. Note: you can substitute credentials with environment variables. Depending on the connection, these need to be set.

### Secrets in Airbyte / Octavia

Using secrets is a little bit tricky. As octavia command is just an alias for docker, you need to mount an env-var for all your secrets. I did it the following way:

```bash
set -o allexport; source .ovtavia.env; set +o allexport
```

with `.octavia.env` looking like this:
```bash
OCTAVIA_ENV_FILE=$(pwd)/.octavia.env
SECRET1='foobazbar1123'
SECRET2=...
```

The first line sets the environment file, that is mounted to the octavia docker to the file itself. Every environment variable afterwards can be used for storing environment variables. You can access these secret values now in the yaml templates, e.g.

```yaml
configuration:
  secret: ${SECRET1}
```

## Usage in Github actions

Add all secrets you don't want to have in the repository as github secrets and reference them in the github actions yaml as env variable. For reference, look at line 55.

Each airbyte connection is defined by three connection type. First, configure a source and destination. Second, form a connection by connecting the source with the destination plus additional configuration.

Octavia enables using yaml files for configuring these three connection types. Examples can be found in `airbyte_connection_templates`.

## How to generate yaml templates for connector

Octavia/Airbyte helps you with providing empty yaml files for each connector. You just have to fill in your application specific data like connection strings, environment variables linking to secrets, ...

The process of generating these empty templates can be found [here](https://medium.com/@jeremysrgt/airbyte-configuration-as-code-with-octavia-cli-dccd2046b764). You can try deploying these in your local workspace. When working as desired, they can be checked into version control in the `airbyte_connection_templates` folder and will be considered by the ci/cd pipeline.
