# Organizations

This repository contains scripts for using Fugue with AWS organizations.

## Dependenices

Using these scripts requires the following:

 * Python 3.6+
 * AWS credentials for your AWS root account
 * Make

The Makefile automatically installs some Python dependencies when rules run.

## Gathering information about an AWS organization

Run the following to gather account and organizational unit (OU) information
from an AWS organization:

```
make organizations.json
```

You must have AWS credentials for your root account active, with permissions
equivalent to `AWSOrganizationsReadOnlyAccess`.

## Use Cloudformation Stacksets to provision IAM roles

Creating IAM roles in each AWS account for use with Fugue can be accomplished
using the `create_stackset.py` script. This requires credentials for the root
account to be active with `AWSCloudFormationFullAccess` and
`AWSOrganizationsReadOnlyAccess` permissions.

```
python create_stackset.py \
    --name FugueRoleStackset \
    --template cloudformation/account.yaml \
    --description "Provides scan access to Fugue" \
    --ous <space separated OU IDs> \
    --parameters \
        RoleName=FugueRole \
        FugueAccountId=370134896156 \
        FugueExternalId=<external ID provided by Fugue>
```

See [account.yaml](cloudformation/account.yaml) for the CloudFormation template
used to crete the role in each account.

You can specify all OUs with `--ous *`.

See a full list of options by running `python create_stackset.py -h`.

## Creating Fugue Environments for each AWS account

Run the following to create Fugue environments for AWS accounts
where the Fugue IAM role has already been provisioned.

```
make environments
```

You must have Fugue API credentials set in your environment which correspond
to an active API client in Fugue:

* `FUGUE_API_ID` - your Fugue API client ID
* `FUGUE_API_SECRET` - your Fugue API client secret

You also must have previously run `make organizations.json` as described above.

This uses a number of defaults, including:

* All OUs
* Role name: `FugueRole`
* `CIS` and `FBP` for compliance families

To override the defaults, run the Python script directly:

```
pip install ./fugue_api_client
python create_environments.py \
    --ous <space separated OU IDs> \
    --role-name <role name> \
    --compliance-families <space separated compliance families>
```
