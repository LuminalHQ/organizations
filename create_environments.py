import json
import os
import time
from typing import List
from swagger_client import (
    Configuration,
    ApiClient,
    EnvironmentsApi,
    ScansApi,
    MetadataApi,
    CustomRulesApi,
    Environment,
    CreateEnvironmentInput,
    ProviderOptions,
    ProviderOptionsAws,
    ProviderOptionsAzure,
    Scan,
)


def initialize_client(local: str = "") -> ApiClient:
    c = Configuration()
    if len(local) > 0:
        c.host = "http://localhost:5000"
    else:
        c.host = 'https://%s/%s' % (os.environ["FUGUE_API_HOST"],
                                    os.environ.get("FUGUE_API_VERSION", "v0"))
    c.username = os.environ["FUGUE_API_ID"]
    c.password = os.environ["FUGUE_API_SECRET"]
    client = ApiClient(configuration=c)
    return client


def environments_api(api_client: ApiClient) -> EnvironmentsApi:
    return EnvironmentsApi(api_client)


def metadata_api(api_client: ApiClient) -> MetadataApi:
    return MetadataApi(api_client)


def create_aws_environment(
    environments_api: EnvironmentsApi,
    name: str,
    role_arn: str,
    compliance_families: List[str] = None,
    survey_resource_types: List[str] = None,
) -> Environment:
    aws_provider_opts = ProviderOptionsAws(regions=["*"], role_arn=role_arn)
    environment: Environment = environments_api.create_environment(
        CreateEnvironmentInput(
            name=name,
            provider='aws',
            provider_options=ProviderOptions(aws=aws_provider_opts),
            survey_resource_types=survey_resource_types,
            compliance_families=compliance_families,
            scan_schedule_enabled=True,
            scan_interval=2592000,
        ))
    assert len(environment.id) > 0
    print(f"environment {environment.id} created")
    return environment


def read_json(path):
    with open(path, 'r') as f:
        return json.loads(f.read())


api_client = initialize_client()
metadata_api: MetadataApi = metadata_api(api_client)
resource_types = metadata_api.get_resource_types('aws').resource_types
print(resource_types)

env_api: EnvironmentsApi = environments_api(api_client)

role_fmt = 'arn:aws:iam::%s:role/FugueDeveloper0123456789'
compliance = ['CIS', 'FBP', 'SOC2']

org = read_json('organization.json')
for i, account in enumerate(org['accounts']):
    if account['ou_name'] != 'Testing':
        continue
    print(i+1, account['account_id'], account['account_name'])
    role_arn = role_fmt % account['account_id']
    env = create_aws_environment(env_api, account['account_name'],
                                 role_arn, compliance,
                                 survey_resource_types=resource_types)
    time.sleep(5)
