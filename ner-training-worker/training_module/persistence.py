import boto3
import logging
class ModelPersistence():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)

        self.s3_resource = boto3.resource('s3')
        self.s3_object = self.s3_resource.Object(config['bucket'], config['objectRef'])
        self.output_file = config['outputFile']
    def save(self, model):
        self.logger.info("saving model to mount")
        with open(self.output_file, 'wb') as pickle_file:
            pickle.dump(model, pickle_file)


        self.logger.info("uploading to s3 bucket")
        self.s3_object.upload_file(self.output_file)