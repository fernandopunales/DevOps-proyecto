
#VPC
aws_region          = "us-east-1"
environment         = "dev"
vpc_cidr            = "10.0.0.0/16"
public_subnet_cidrs = ["10.0.1.0/24", "10.0.3.0/24"]      # API Gateway
apigateway_port = 8000
