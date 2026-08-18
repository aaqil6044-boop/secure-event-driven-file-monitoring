# Secure Event-Driven File Monitoring

An event-driven file monitoring project built using Google Cloud Platform (GCP), Google Cloud Storage, and Google Cloud Functions.

## Overview

This project demonstrates how a serverless function can automatically respond to file upload events in a Google Cloud Storage bucket.

When a file is uploaded, the Cloud Function is triggered and records information about the uploaded file for monitoring and auditing.

## Architecture

```text
User / Service
      |
      | Upload File
      v
Google Cloud Storage
      |
      | Storage Event
      v
Google Cloud Function
      |
      | Log File Information
      v
Cloud Logging
