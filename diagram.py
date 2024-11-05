from diagrams import Diagram
from diagrams.aws.network import ELB
from diagrams.aws.compute import EC2AutoScaling, EC2
from diagrams.aws.integration import SQS
from diagrams.onprem.client import Users

with Diagram("Scalable Backend Architecture", show=False):
    users = Users("Users")
    
    load_balancer = ELB("Load Balancer")
    auto_scaling_group = EC2AutoScaling("Auto Scaling Group")
    
    ec2_instances = [EC2("FastAPI Instance 1"), EC2("FastAPI Instance 2"), EC2("FastAPI Instance 3")]
    
    sqs = SQS("Message Queue (SQS)")
    
    # Diagram Flow
    users >> load_balancer >> auto_scaling_group
    auto_scaling_group >> ec2_instances[0] >> sqs
    auto_scaling_group >> ec2_instances[1] >> sqs
    auto_scaling_group >> ec2_instances[2] >> sqs
    ec2_instances
