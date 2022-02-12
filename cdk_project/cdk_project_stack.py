from inspect import BlockFinder
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
            versioned= False,
            encryption=_s3.BucketEncryption.S3_MANAGED,
            block_public_access=_s3.BlockPublicAccess.BLOCK_ALL  
        )

        mybucket = _s3.Bucket(
            self,
            "mybucketid1"
        )

        snstopicname = "abcdef"

        if len(snstopicname) > 10 :
            raise ValueError("Maximum value can be only 10 chars")

        print(mybucket.bucket_name)
        

        output_1 = core.CfnOutput(
            self,
            "mybucketoutput1",
            value=mybucket.bucket_name,
            description="my first cdk bucket",
            export_name="mybucketoutput1"
        )
        