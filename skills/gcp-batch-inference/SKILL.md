---
name: gcp-batch-inference
description: Run Gemini batch inference on Google Cloud Vertex AI. Use when the user wants to process a large number of prompts asynchronously and cheaply (50% discount) on GCP — bulk classification, annotation, extraction, or generation — from Cloud Storage JSONL files or BigQuery tables.
license: MIT
---

# Overview

Get asynchronous, high-throughput, and cost-effective inference for your large-scale data processing needs with Gemini's batch inference (formerly known as batch prediction). This guide will walk you through the value of batch inference, how it works, its limitations, and best practices for optimal results.

## Why use batch inference?

In many real-world scenarios, you don't need an immediate response from a language model. Instead, you might have a large dataset of prompts that you need to process efficiently and affordably. This is where batch inference shines.

## Key benefits include

- **Cost-Effectiveness** Batch processing is offered at a 50% discounted rate compared to real-time inference, making it ideal for large-scale, non-urgent tasks. Implicit caching is enabled by default for Gemini models (e.g. Gemini 3.5 Flash and Gemini 3.1 Flash-Lite). Implicit caching provides a 90% discount on cached tokens compared to standard input tokens. However, the discounts for cache and batch don't stack. The 90% cache hit discount takes precedence over the batch discount.
- **High rate limits** Process hundreds of thousands of requests in a single batch with a higher rate limit compared to the real time Gemini API.
- **Simplified Workflow** Instead of managing a complex pipeline of individual real-time requests, you can submit a single batch job and retrieve the results once the processing is complete. The service will handle format validation, parallelize requests for concurrent processing, and automatically retry to strive for a high completion rate with 24 hours turnaround time.

## Optimal for tasks

Batch inference is optimized for large-scale processing tasks like:
- **Content Generation** Generate product descriptions, social media posts, or other creative text in bulk.
- **Data Annotation and Classification** Classify user reviews, categorize documents, or perform sentiment analysis on a large corpus of text.
- **Offline Analysis** Summarize articles, extract key information from reports, or translate documents at scale.

# Choosing the input/output source

- **Data already in BigQuery, or naturally tabular** (rows of prompts, results joined back to tables) → use **batch inference from BigQuery**.
- **Everything else** (files, exports, ad-hoc datasets) → use **batch inference from Cloud Storage** with JSONL files. This is the default choice.
- Very large inputs: split into multiple JSONL files / multiple batch jobs to parallelize and to limit the blast radius of a failed job.
- Repeated long shared prefix across requests (e.g. a large system prompt or document)? Put it first in every request so implicit caching kicks in, then verify cache hits in the job metrics — don't assume.

# Worked example (GCS + Python SDK)

Verify details against the linked docs before running — API surfaces change.

1. Prepare `input.jsonl`, one request per line:

```json
{"request": {"contents": [{"role": "user", "parts": [{"text": "Classify this review: ..."}]}]}}
```

2. Upload and submit the job with the `google-genai` SDK:

```python
from google import genai
from google.genai.types import CreateBatchJobConfig

client = genai.Client(vertexai=True, project="YOUR_PROJECT", location="us-central1")
job = client.batches.create(
    model="gemini-3.5-flash",  # or gemini-3.1-flash-lite for cheaper, simpler tasks
    src="gs://your-bucket/input.jsonl",
    config=CreateBatchJobConfig(dest="gs://your-bucket/output/"),
)
print(job.name, job.state)
```

3. Poll until done (typically well under the 24h turnaround), then read the per-line results from the `dest` prefix:

```python
job = client.batches.get(name=job.name)  # repeat until job.state is JOB_STATE_SUCCEEDED / _FAILED / _CANCELLED
```

4. Check the output JSONL: each line echoes the request plus a `response` (or per-line `status` on failure). Failed lines can be collected into a new input file and resubmitted.

# Google Cloud Documentation Links

Review these documentation pages when you need it for the task at hand:
- [Overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-gemini) - See the up-to-date list of supported AI models here.
- [Batch inference from Cloud Storage](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-from-cloud-storage) - Batch inference from JSONL blobs in a GCS bucket
  - [Creating a batch from GCS using the Python SDK](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-from-cloud-storage#create-batch-job-python_genai_sdk) 
- [Batch inference for BigQuery](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-from-bigquery) - Batch inference from table rows in BigQuery
  - [Creating a batch from BigQuery using the Python SDK](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-from-bigquery#create-batch-job-python_genai_sdk) 
- [Resume an incomplete batch inference job](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/batch-prediction-resume)
- [Context caching](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview) - Implicit caching is simpler, but always store and double-check the inference metrics to ensure that prefix caching is actually effective.
- [Labels for billing](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/add-labels-to-api-calls) - Labels are useful for filtering the GCP Billing dashboard for specific models, batches or job executions.
- [Pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing)

# Abbreviations

- GCP: [Google Cloud Platform](https://cloud.google.com/)
- GCS: [Google Cloud Storage](https://cloud.google.com/storage)
