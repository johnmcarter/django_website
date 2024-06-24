data "aws_iam_policy_document" "task_execution_policy" {
  statement {
    actions = [
      "ssm:GetParameter",
      "ssm:GetParameters"
    ]
    resources = [
      "arn:aws:ssm:${local.region}:${local.aws_account_id}:parameter/johnjohnphotos/site/*"
    ]
  }
  statement {
    actions = [
      "logs:*"
    ]
    resources = [
      "*"
    ]
  }
  statement {
    actions = [
      "s3:DeleteObject",
      "s3:GetObject",
      "s3:ListBucket",
      "s3:PutObject",
      "s3:ListObjects"
    ]
    resources = [
      "arn:aws:s3:::johnjohnphotos-media/*"
    ]
  }
}
