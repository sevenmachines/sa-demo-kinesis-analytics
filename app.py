#!/usr/bin/env python3

from aws_cdk import core

from sa_demo_kinesis_analytics.sa_demo_kinesis_analytics_stack import SaDemoKinesisAnalyticsStack


app = core.App()
SaDemoKinesisAnalyticsStack(app, "sa-demo-kinesis-analytics")

app.synth()
