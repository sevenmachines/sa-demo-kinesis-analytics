#!/usr/bin/env python3

from aws_cdk import core

from stacks.lambda_with_kinesis_trigger import LambdaWithKinesisTrigger


app = core.App()
LambdaWithKinesisTrigger(app, "kinesis-analytics")

app.synth()
