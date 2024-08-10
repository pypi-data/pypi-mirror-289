# Amazon CodeWhisperer for JupyterLab

Amazon CodeWhisperer is an AI coding companion which provides developers with real-time code suggestions in JupyterLab. Individual developers can use CodeWhisperer for free in JupyterLab and AWS SageMaker Studio.

![Codewhisperer demo](https://docs.aws.amazon.com/images/codewhisperer/latest/userguide/images/codewhisperer-timestamp-record.png)

## Requirements

In order to use CodeWhisperer in JupyterLab, you must have a version of JupyterLab >= 3.5 installed. This extension does not yet support JupyterLab > 4.0. You will also need a free [AWS Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html) account to access CodeWhisperer. (You can set that up the first time you log in.)

In order to use CodeWhisperer in SageMaker Studio, you must have set up a SageMaker Studio notebook instance, along with an execution role with the appropriate IAM Permissions. 

## Getting Started

### Jupyter Lab

You can install and enable the CodeWhisperer extension for JupyterLab with the following commands. 

```
pip install amazon-codewhisperer-jupyterlab-ext
jupyter server extension enable amazon_codewhisperer_jupyterlab_ext
```

Once installed, choose ****Start CodeWhisperer**** from the CodeWhisperer panel at the bottom of the window. This will enable to you log in to [AWS Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html) to access CodeWhisperer. Refer to [Setting up CodeWhisperer with JupyterLab](https://docs.aws.amazon.com/codewhisperer/latest/userguide/jupyterlab-setup.html) for detailed setup instructions.

### SageMaker Studio

To setup the CodeWhisperer extension with a SageMaker Studio notebook instance, you must add IAM Permissions for 
`codewhisperer:GenerateRecommendations` for your user profile. Then you must install and enable the extension with the following commands.

```
conda activate studio
pip install amazon-codewhisperer-jupyterlab-ext
jupyter server extension enable amazon_codewhisperer_jupyterlab_ext
conda deactivate
restart-jupyter-server
```

After you complete installation and refresh your browser, a CodeWhisperer panel will appear at the bottom of the window. Refer to [Setting up CodeWhisperer with SageMaker Studio](https://docs.aws.amazon.com/codewhisperer/latest/userguide/sagemaker-setup.html) for detailed setup instructions. 

## Features

### Code Completion

CodeWhisperer for JupyterLab provides AI powered suggestions as ghost text with the following default keybindings. These can be modified in the settings.


|              Action	                  |      Key Binding       |
| ------------------------------ | ----------- |
| Manually trigger CodeWhisperer | Alt C (Window) / ⌥ C (Mac)        |
| Accept a recommendation        | Tab       |
| Next recommendation            | Right arrow |
| Previous recommendation        | Left arrow  |
| Reject a recommendation        | ESC         |



Python is the only supported programming language for now. Users can start or pause suggestions by toggling the menu item in the CodeWhisperer panel that will appear at the bottom of the window.

### Code References

With the reference log, you can view references to code recommendations. You can also update and edit code recommendations suggested by CodeWhisperer.

To view Code References for accepted suggestions, choose **Open Code Reference Log** from the CodeWhisperer panel at the bottom of the window. Users can also turn off code suggestions with code references in Settings.


## More Resources

* [CodeWhisperer User Guide](https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is-cwspr.html)
* [Setting up Amazon CodeWhisperer with JupyterLab](https://docs.aws.amazon.com/codewhisperer/latest/userguide/jupyterlab-setup.html)
* [Setting up CodeWhisperer with Amazon SageMaker Studio](https://docs.aws.amazon.com/codewhisperer/latest/userguide/sagemaker-setup.html)

## Change Log
1.0.12
* Bug fix: Bump dependency tough-cookie to 4.1.4 from 4.1.2 which is associated with a [CVE](https://nvd.nist.gov/vuln/detail/CVE-2023-26136)

1.0.11
* Bug fix: Toggle off auto suggestion when plugin receives multiple AccessDeniedException

1.0.9
* Bug fix: Fix auto trigger issue when switching between .ipynb and .py
* Bug fix: Improved handling when Jupyter has no access to internet.
* Improvement: Migrated network call to be made asynchronously.

1.0.8
* Add EMR Studio Workspace support
* Bug fix: Only show update nudge for JL3 compatible releases.
* Bug fix: Fix client registration not being updated when it's expired

1.0.6
* Bug fix:  Fix the insert position of native auto completion 
* Bug fix:  Make telemetry send API fail silently without raising exception

1.0.5
* Bug fix: Fail to enable extension in SageMaker Studio in VPC mode
* Bug fix: Documentation link in Glue Studio

1.0.4
* Add Glue Studio Notebook support

1.0.3
* Bug fix: No recommendation when user turn off code suggestions with references in settings.
* Bug fix: Issue with browser login flow for some Builder ID users.
* Bug fix: Fix an issue where SageMaker Studio users will incorrectly see the `Share content with Amazon CodeWhisperer` settings option.

1.0.0
* Initial release
