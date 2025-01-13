terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }
  backend "s3" {
    bucket  = "ccsw-core"
    key     = "johnjohnphotos/terraform/state.tfstate"
    region  = "us-east-1"
    encrypt = true
  }
  required_version = ">= 0.14.9"
}

provider "aws" {
  region = "us-east-1"
  profile = "prod"
  default_tags {
    tags = {
      project = local.project_name
    }
  }
}

resource "aws_ecs_cluster" "cluster" {
  name = "${local.project_name}-cluster"
}

resource "aws_ecs_service" "app" {
  name            = "${local.project_name}-service"
  cluster         = aws_ecs_cluster.cluster.id
  task_definition = aws_ecs_task_definition.app.id
  desired_count   = 1
  launch_type     = "FARGATE"

  load_balancer {
    target_group_arn = aws_lb_target_group.app.arn
    container_name   = "app"
    container_port   = 80
  }

  network_configuration {
    subnets          = [local.subnet_id]
    security_groups  = [local.security_group_id]
    assign_public_ip = true
  }
}

resource "aws_ecs_task_definition" "app" {
  family                   = "${local.project_name}-task"
  container_definitions    = file("resources/task-containers.json")
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"
  cpu                      = 256
  memory                   = 512
  execution_role_arn       = aws_iam_role.task_execution_role.arn
  task_role_arn            = aws_iam_role.task_execution_role.arn
}

resource "aws_iam_role" "task_execution_role" {
  name = "${local.project_name}-task-execution-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "ecs-tasks.amazonaws.com"
        }
      },
    ]
  })
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy",
    aws_iam_policy.task_execution_policy.arn
  ]
}

resource "aws_iam_policy" "task_execution_policy" {
  name   = "${local.project_name}-task-execution-policy"
  path   = "/"
  policy = data.aws_iam_policy_document.task_execution_policy.json
}
