<div align="center">
    <img src="https://bookface-images.s3.amazonaws.com/small_logos/053379bcb6d2f8ca33ff9eb81f1d899a06a6872a.png" 
    height="200"
    width="200" alt="Lume Logo">
    <p>Control your data mappings through Lume's API</p>
</div>


## Authentication

Developers will need to create an API Key within your [Developer Portal](https://lume.ai) to make API requests.

# Lume Python SDK (`lume_py`)

## Overview

`lume_py` is a Python SDK designed to facilitate seamless interaction with the Lume API. It provides an intuitive and straightforward interface for developers to integrate Lume's services into their Python applications, enabling efficient access to Lume's powerful features.

## Features

- **Easy API Integration:** Quickly connect to and interact with the Lume API.
- **Asynchronous Support:** Built on top of `httpx`, offering asynchronous capabilities for better performance.
- **Pydantic Integration:** Utilizes `Pydantic` for data validation and settings management.
- **Extensible:** Modular design allows for easy customization and extension.

## Installation

To install the `lume_py` SDK, use the following pip command:

```bash
pip install lume-py

import lume_py

lume_py.set_api_key('...')

# For more information, check the cookbooks folder.

