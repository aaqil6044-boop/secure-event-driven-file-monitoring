# Secure Event-Driven File Monitoring

An event-driven file monitoring system built using Google Cloud Platform (GCP), Google Cloud Storage, and Google Cloud Functions.

## Overview

This project demonstrates how a serverless function can automatically respond to file upload events in a Google Cloud Storage bucket.

When a file is uploaded, the Cloud Function is triggered and records information about the uploaded object for monitoring and auditing purposes.

## Architecture

```text
User / Service
      |
      | Upload file
      v
Google Cloud Storage
      |
      | Storage event
      v
Google Cloud Function
      |
      | Log file information
      v
Cloud Logging
