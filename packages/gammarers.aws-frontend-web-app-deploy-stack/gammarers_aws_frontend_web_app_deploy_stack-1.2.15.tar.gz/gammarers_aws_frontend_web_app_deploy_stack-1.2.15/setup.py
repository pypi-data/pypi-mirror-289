import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "gammarers.aws-frontend-web-app-deploy-stack",
    "version": "1.2.15",
    "description": "This is an AWS CDK Construct to make deploying a Frontend Web App (SPA) deploy to S3 behind CloudFront.",
    "license": "Apache-2.0",
    "url": "https://github.com/gammarers/aws-frontend-web-app-deploy-stack.git",
    "long_description_content_type": "text/markdown",
    "author": "yicr<yicr@users.noreply.github.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/gammarers/aws-frontend-web-app-deploy-stack.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "gammarers.aws_frontend_web_app_deploy_stack",
        "gammarers.aws_frontend_web_app_deploy_stack._jsii"
    ],
    "package_data": {
        "gammarers.aws_frontend_web_app_deploy_stack._jsii": [
            "aws-frontend-web-app-deploy-stack@1.2.15.jsii.tgz"
        ],
        "gammarers.aws_frontend_web_app_deploy_stack": [
            "py.typed"
        ]
    },
    "python_requires": "~=3.8",
    "install_requires": [
        "aws-cdk-lib>=2.80.0, <3.0.0",
        "constructs>=10.0.5, <11.0.0",
        "gammarers.aws-secure-bucket>=1.3.1, <1.4.0",
        "gammarers.aws-secure-cloudfront-origin-bucket>=1.5.0, <1.6.0",
        "gammarers.aws-secure-frontend-web-app-cloudfront-distribution>=1.3.0, <1.4.0",
        "jsii>=1.102.0, <2.0.0",
        "publication>=0.0.3",
        "typeguard~=2.13.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
