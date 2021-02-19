import boto3,uuid,datetime
aws_mg_con=boto3.session.Session(profile_name='root')
s3_client=aws_mg_con.client(service_name='s3',region_name='us-west-2')
session_region=aws_mg_con.region_name

def create_bucket_name(buketprefix):
    bucket_join="".join([buketprefix,datetime.datetime.now().strftime("%Y-%m-%d-")])
    bucket_name="".join([bucket_join,str(uuid.uuid4())])
    return bucket_name

get_bucket=create_bucket_name(input("please enter the bucket name"))


def bucket():
    s3_bucket=s3_client.create_bucket(Bucket=get_bucket,
                                          CreateBucketConfiguration={
                                              'LocationConstraint':session_region
                                          })
    print(session_region)
    print(get_bucket)
    return bucket

bucket()
