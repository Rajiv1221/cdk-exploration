from aws_cdk import (
    # Duration,
    core ,
    aws_s3  as  _s3,
   
    # aws_sqs as sqs,
)
from constructs import Construct

class CdkProjectStack(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "CdkProjectQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        _s3.Bucket(
            self,
            "muBucketID",
            bucket_name= "bucket-cdk-2004",
            versioned= True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
            
        )