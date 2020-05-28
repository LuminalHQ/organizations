
REGIONS ?= '["us-east-1"]'
ADMIN_AWS_PROFILE ?= billing
VENV_NAME = .orgvenv
VENV = source $(VENV_NAME)/bin/activate
AWS = $(VENV) && aws

$(VENV_NAME):
	python -m venv $(VENV_NAME)
	source $(VENV_NAME)/bin/activate && pip install -q awscli

organization.json: $(VENV_NAME)
	$(VENV) && AWS_PROFILE=$(ADMIN_AWS_PROFILE) python describe_organization.py

swagger.yaml:
	wget -q https://api-staging.fugue.co/v0/swagger -O swagger.yaml

fugue_api_client: swagger.yaml
	swagger-codegen generate -i ./swagger.yaml -l python -o fugue_api_client

.PHONY: environments
environments: $(VENV_NAME) fugue_api_client
	$(VENV) && pip install ./fugue_api_client
	$(VENV) && AWS_PROFILE=$(ADMIN_AWS_PROFILE) python create_environments.py

.PHONY: stackset_admin
stackset_admin:
	$(AWS) cloudformation deploy \
		--profile $(ADMIN_AWS_PROFILE) \
		--template-file stackset-admin.yaml \
		--stack-name $(ADMIN_STACK_NAME) \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset

.PHONY: list_stacksets
list_stacksets:
	$(AWS) cloudformation list-stack-sets \
		--profile $(ADMIN_AWS_PROFILE)