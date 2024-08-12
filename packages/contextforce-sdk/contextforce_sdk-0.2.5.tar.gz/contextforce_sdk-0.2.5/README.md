# ContextForce SDK Documentation

## Overview

The `ContextForceClient` class provides a Python interface to interact with the ContextForce API. Below are the available methods, how to use them, and the headers each function may require.

## Installation


```bash
pip install contextforce-sdk
```


### Example
```python
from contextforce import ContextForceClient

# API key is optional. For free users, you don't need to have one.
client = ContextForceClient(api_key='your_api_key')
```

## Methods

### 1. extract_content

Extracts content from a given page URL or list of URLs. The content can be returned in Markdown or JSON format.

#### Parameters
- `urls`: A string (single URL) or a list of URLs.
- `result_format`: The format of the result, either `'markdown'` (default) or `'json'`.
- `include_links`: Boolean to include links in the output (default `False`).
- `include_images`: Boolean to include images in the output (default `False`).

#### Headers
- `Accept`: Set to `'application/json'` if `result_format` is `'json'`.
- `CF-Include-Links`: Set to `'true'` if `include_links` is `True`.
- `CF-Include-Images`: Set to `'true'` if `include_images` is `True`.

#### Example Usage
```python
result = client.extract_content("https://example.com", result_format="markdown", include_links=True)
```

### 2. extract_pdf

Extracts content from a PDF URL or file content. The content can be returned in Markdown or JSON format.

#### Parameters
- `pdf_source`: A string (PDF URL) or bytes (PDF file content).
- `result_format`: The format of the result, either `'markdown'` (default) or `'json'`.
- `model`: Optional model to use, e.g., `'gpt-4o-mini'`, `'claude-3.5'`.
- `openai_api_key`: Optional OpenAI API key if `model` is `'gpt-4o-mini'`.
- `claude_api_key`: Optional Claude API key if `model` is `'claude-3.5'`.

#### Headers
- `Accept`: Set to `'application/json'` if `result_format` is `'json'`.
- `CF-Model`: Set to the model name if `model` is specified.
- `CF-OpenAI-API-Key`: Set to the OpenAI API key if `model` is `'gpt-4o-mini'`.
- `CF-Claude-API-Key`: Set to the Claude API key if `model` is `'claude-3.5'`.
- `Content-Type`: Set to `'multipart/form-data'` for file uploads.
- `CF-Content-Type`: Set to `'application/pdf'` when uploading PDF content.

#### Example Usage
```python
result = client.extract_pdf("https://example.com/file.pdf", result_format="markdown", model="gpt-4o-mini")
```

### 3. extract_product

Extracts product information from a given product page URL or list of URLs. The content is returned in JSON format by default.

#### Parameters
- `urls`: A string (single URL) or a list of URLs.
- `result_format`: The format of the result, either `'json'` (default) or `'markdown'`.
- `include_reviews`: Optional boolean to include product reviews in the output.

#### Headers
- `Accept`: Set to `'application/json'` if `result_format` is `'json'`.
- `CF-Include-Reviews`: Set to `'true'` if `include_reviews` is `True`.

#### Example Usage
```python
result = client.extract_product("https://example.com/product-page", include_reviews=True)
```


### 4. search_google

Performs a Google search based on a query.

#### Parameters
- `query`: The search query.
- `result_format`: The format of the result, either `'json'` (default) or `'markdown'`.
- `follow_links`: Optional boolean to follow links on the search results (default `True`).
- `top_n`: Optional integer to specify the number of top pages to crawl if `follow_links` is `True` (default `5`).

#### Headers
- `Accept`: Set to `'application/json'` if `result_format` is `'json'`.
- `CF-Follow-Links`: Set to `'true'` if `follow_links` is `True`.
- `CF-Top-N`: Set to the value of `top_n`.

#### Example Usage
```python
result = client.search_google("example query", result_format="json", follow_links=True, top_n=5)
```

### 5. search_amazon

Performs an Amazon search based on a query.

#### Parameters
- `query`: The search query.
- `result_format`: The format of the result, either `'json'` (default) or `'markdown'`.
- `follow_links`: Optional boolean to follow links on the search results (default `True`).
- `top_n`: Optional integer to specify the number of top pages to crawl if `follow_links` is `True` (default `5`).

#### Headers
- `Accept`: Set to `'application/json'` if `result_format` is `'json'`.
- `CF-Follow-Links`: Set to `'true'` if `follow_links` is `True`.
- `CF-Top-N`: Set to the value of `top_n`.

#### Example Usage
```python
result = client.search_amazon("example product", result_format="json", follow_links=True, top_n=5)
```

### 6. search_youtube

Performs a YouTube search based on a query.

#### Parameters
- `query`: The search query.
- `result_format`: The format of the result, either `'json'` (default) or `'markdown'`.
- `follow_links`: Optional boolean to follow links on the search results (default `True`).
- `top_n`: Optional integer to specify the number of top pages to crawl if `follow_links` is `True` (default `5`).

#### Headers
- `Accept`: Set to `'application/json'` if `result_format` is `'json'`.
- `CF-Follow-Links`: Set to `'true'` if `follow_links` is `True`.
- `CF-Top-N`: Set to the value of `top_n`.

#### Example Usage
```python
result = client.search_youtube("example video", result_format="json", follow_links=True, top_n=5)
```

---

This documentation provides detailed information on how to use each function within the `ContextForceClient` SDK and the headers required for each function.


