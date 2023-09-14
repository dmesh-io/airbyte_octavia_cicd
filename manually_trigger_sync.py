import requests as r

# api base url
base_url="http://localhost:8000/api"

# base64 encoding. this applies for standard credentials user airbyte pw password
# https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html#overview
headers = {"Authorization": "Basic YWlyYnl0ZTpwYXNzd29yZA=="}

def get_workspace_id():
    get_workspace_id_url = f"{base_url}/v1/workspaces/list"    

    workspaces = r.post(get_workspace_id_url, headers=headers).json()['workspaces']

    if len(workspaces) > 1:
        print("currently only the first workspace is considered")

    workspace_id = workspaces[0]['workspaceId']
    return workspace_id

def get_connections_id(workspace_id):
    get_connections_api_url = f"{base_url}/v1/connections/list"

    connections = r.post(get_connections_api_url, headers=headers, json={"workspaceId": workspace_id}).json()["connections"]

    if len(connections) > 1:
        print("currently only the first connection is returned")

    connection_id = connections[0]['connectionId']
    return connection_id

def trigger_connection(connection_id):
    trigger_connection_api_url = f"{base_url}/v1/connections/sync"

    response = r.post(trigger_connection_api_url, headers=headers, json={"connectionId": connection_id}).json()
    
    print(response)


def main():
    workspace_id = get_workspace_id()
    connection_id = get_connections_id( workspace_id=workspace_id)
    trigger_connection(connection_id=connection_id)


if __name__ == "__main__":
    main()
