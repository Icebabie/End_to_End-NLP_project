import os
from Hate_speech_classifier.logger import logging
class GcloudSync:

    def sync_folder_to_gcloud(self, gcp_bucket_url, filepath, filename):

        command = f'gsutil cp "{filepath}/{filename}" "gs://{gcp_bucket_url}/"'
        logging.info(command)
        os.system(command)

    def sync_folder_from_gcloud(self, gcp_bucket_url, filename, destination):

        command = f'gsutil cp "gs://{gcp_bucket_url}/{filename}" "{destination}/{filename}"'
        logging.info(command)
        os.system(command)