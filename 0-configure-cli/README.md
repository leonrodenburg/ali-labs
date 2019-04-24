# 0 - Configure CLI

In this lab, we will install and configure the Alibaba Cloud CLI so we can use it in the upcoming labs. Follow the steps to get started.

## 0.1 - Download the CLI

For Linux / MacOS without Homebrew:
- Go to the [Aliyun CLI repository](https://github.com/aliyun/aliyun-cli) and find the download link for Linux
- Download the zipfile containing the executable
- Move the `aliyun` executable file to `/usr/local/bin` or another directory on your `$PATH`

For MacOS with Homebrew:
- Open a terminal and run `brew install aliyun-cli`

For Windows:
- Go to the [Aliyun CLI repository](https://github.com/aliyun/aliyun-cli) and find the download link for Windows
- Move `aliyun.exe` to a directory that you can remember
- Right-click on 'Computer' > select 'Properties'
- In 'System Properties', click the 'Advanced' tab
- Click the 'Environment Variables...' button
- Scroll down to 'Path' and edit it
- Add a semicolon (;) to the value and type the full directory path where you put `aliyun.exe`
- Click 'OK' to save changes

## 0.2 - Configure your account

Before you can start using the CLI to access your cloud resources, you need to tell the CLI which account it should connect to. This assumes that you have already registered an account. If you have not, please do so [here](https://account.alibabacloud.com/register/intl_register.htm?spm=a2c44.11131515.0.0.45e4525cKBru7M). Then follow the steps below:

- Open a terminal / command-line prompt and type `aliyun configure`
- Log in to the Alibaba Cloud console
- Click your avatar in the top-right corner and go to 'AccessKey'
- If a popup shows up warning you about using access keys with a root account, click 'Continue to manage AccessKey'
- If you have no access keys yet, click 'Create AccessKey'
- Copy the access key ID and paste it in the terminal, press Enter
- Copy the access key secret and paste it in the terminal, press Enter
- Specify default region (we recommend `eu-central-1` if you are in Europe, `us-west-1` if you are in the US)
- Specify default language (`en` is probably what you want)

You should see some output stating that the configuration was done successfully.

## 0.3 - Verify

Run `python verify.py` to verify your solution.
