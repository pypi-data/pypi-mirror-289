```markdown
# msapi

A Python package for executing scripts with Macsploit's API.

## Overview

This package provides a simple way to execute Roblox scripts (with Macsploit API) via a local server connection. It is designed to work with Roblox's Lua scripting language.

## Installation

You can install the package via pip:

```sh
pip install msapi
```

## Usage

To use the package, import and call the `execute` function:

```python
from msapi import execute

script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/EdgeIY/infiniteyield/master/source"))()'
execute(script)
```
```

### **6. `msapi/__init__.py`**

This file makes `execute` directly accessible from `msapi`:

**`msapi/__init__.py`:**

```python
from .msapi import execute
```
