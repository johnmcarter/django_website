resource "aws_lb_target_group" "app" {
  name        = "${local.project_name}-tg"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = local.vpc_id

  health_check {
    path = "/"
  }
}

data "aws_lb" "ccswsites" {
  name = "ccsw-ecs-ec2-lb"
}

data "aws_lb_listener" "lb443" {
  load_balancer_arn = data.aws_lb.ccswsites.arn
  port              = 443
}

resource "aws_lb_listener_rule" "fw_to_app" {
  listener_arn = data.aws_lb_listener.lb443.arn

  action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.app.arn
  }

  condition {
    host_header {
      values = [local.host_name]
    }
  }
}
