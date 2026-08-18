import logging

def gcs_trigger(event, context):
    file_name = event['name']
    logging.info(f"New file uploaded: {file_name}")
