---
title: "Comparing AWS stream-like tools"
date: 2020-03-04T12:24:40-08:00
draft: false
categories:
- build
tags:
- aws
- cloud
publish:
- twitter
summary: A comparison of the various stream and streamlike services on AWS (Kinesis, SQS, SNS, etc.)
comments: true
---

I love AWS, unironically. I have been using it since it came into existence, and my admiration for the platform has only grown with time. Even though I spend a lot of time wiring up different services in AWS, I still have trouble keeping all of the streaming facilities straight. Today I got stuck on a JetBlue flight with broken WiFi, so of course I took the opportunity to scrape through the AWS CLI documentation to create a comparison table and get this sorted once and for all.

Service | Model | Volume | FIFO | Put From | Push To | Fan-In | Fan-Out | Default Limit | Rsvd Cap? | 
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- 
[SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) | pub-sub | Low | No | λ, Cloudwatch | λ, http, email, sms, sqs | ∞ | ∞ | 100,000 | No
[SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) | message queue | Med | No | λ, sns | λ | ∞ | 1 |  | No
[SQS FIFO](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html) | FIFO msg queue | Med | Yes | λ | — | ∞ | 1 |  | No
[Kinesis Stream](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) | data stream | High | Kinda | λ, KAnalytics | λ | ∞ | ∞ | 50/region | Yes
[Kinesis Firehose](https://docs.aws.amazon.com/firehose/latest/dev/what-is-this-service.html) | managed data delivery | High | No | λ, KAnalytics | S3, ES, Splunk, Redshift | ∞ | 1 | 50/region | No
[Kinesis Analytics](https://docs.aws.amazon.com/kinesisanalytics/latest/dev/what-is.html) | stream analytics | Med | Yes? | KStream, KFirehose | KStream, KFirehose, λ | 1 | 3 | 50/region | No*
[Dynamo Stream](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) | change log | Med | Yes? | Dynamo | λ | 1 | ∞ | — | No
[S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html) | k/v store | High | — | KFirehose | λ | ∞ | ∞ | — | No
[Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) | Immutable log stream | High | No | λ | KStream, KFirehose, λ | ∞ | ∞ | — | No

What's clear from this table, and will be familiar to AWS veterans, is that Lambda really is the glue that holds all of these services together. In some cases, you'll find yourself resorting to a Lambda when you need to connect two elements in your pipeline that don't know how to talk to each other on their own.

A few notes:
* Astute readers will see some category errors and unfair comparisons.
  * S3 is not a stream in any normal sense; I've included it because with event notifications it can often be an alternative to some of the other tools here, especially if retention is desirable. 
  * Kinesis Analytics is kind of an odd duck as well, much more specialized and compute-centric than the others here. But because it can read from and write to the other Kinesis services, and also write directly to Lambda, it felt worth including here.
  * Dynamo Streams are very specific, and do only one thing. I'm pretty sure they are Kinesis Streams under the hood, though.
* Fan-in and fan-out are approximate. Nothing is truly infinity, of course, and I may update this post with some of the practical limits.
* Kinesis streams have per-shard FIFO if you're careful
* Volume entries are super vague, of course, and are relative to the highest-volume services. SNS can handle lots of notifications by most measures; it's just slow compared to monsters like Kinesis and S3.
---

And here is a prettier version if you'd like:

![AWS Stream Comparison](/img/aws-stream-comparison.png)
