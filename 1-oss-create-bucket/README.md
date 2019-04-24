# 1 - Object Storage Service (OSS) - Create bucket

In this challenge, we will be creating an OSS bucket and storing a file in it. OSS is the object storage product of Alibaba Cloud. You can use it to store objects (files) under a certain key. There are no limits on the number of files you can store. You are billed by the number of gigabytes of storage you use per month (everything below 5 GB is free).

A bucket is a container for your files that resides in a certain region. You can create buckets in any region you like. The files will be stored on physical devices managed by Alibaba Cloud. Although the buckets are regional, bucket names have to globally unique. This is important to consider when you are trying to create a bucket like `test-bucket`. Someone else probably already claimed that name.

Although OSS is actually a sharded key-value store, you can mimick a directory structure by storing files under a key with a `/` in it. In the Alibaba Cloud OSS dashboard, the files in your bucket will be shown as if they are in directories. But it is important to remember that those directories are virtual, while the real objects are just stored under their full keys.

## 1.1 - Creating a bucket

Use the Alibaba Cloud CLI (`aliyun`) to create an OSS bucket. The Alibaba Cloud CLI comes with a lot of modules, one for every service. To see the supported modules, use `aliyun --help`. To learn about the commands supported by a module, type `aliyun <module> --help`. The module would be `oss` in this case. To learn more about a subcommand, type `aliyun <module> <subcommand> --help`. These hints should be enough to figure out what's what.

Create a bucket with a name you like. Remember the name.

## 1.2 - Upload file

Now that you have created a bucket, it is time to put something in it! Upload the file `file.txt` in the current directory to your bucket using the Alibaba Cloud CLI. Remember that you can use the `--help` postfix for modules and subcommands when you are unsure how to use them.

## 1.3 - Verify

Run `python verify.py <bucketname>` to verify your solution. Remember to replace `<bucketname>` with the name of the bucket you created in step 1.1.
