import boto3
import logging
import os

__version__ = '0.5a3'

LOGGER = logging.getLogger(__name__)


class S3Library:
    u"""
    A test library providing AWS S3 support.

        ``S3Library`` is a Robot Framework third party library that enables test to access and upload files to S3.

        == Table of contents ==

        - `Usage`
        - `Examples`
        - `Author`
        - `Developer Manual`
        - `Importing`
        - `Shortcuts`
        - `Keywords`


    = Usage =

    | =Settings= | =Value=         | =Parameter= | =Parameter= | =Parameter= |
    | Library    | S3Library       | ACCESS_KEY  |  SECRET_KEY | BUCKET_NAME |


    = Examples =

    | =Settings= | =Value=         | =Parameter= | =Parameter= | =Parameter= |
    | Library    | S3Library       | ACCESS_KEY  |  SECRET_KEY | BUCKET_NAME |

    = Author =

    Created: 03/25/2024

    Author: Shiela Buitizon | email:shiela.buitizon@mnltechnology.com

    = Developer Manual =

        Compiling this pip package:
            - python setup.py bdist_wheel

        Uploading build to pip
            - python -m twine upload dist/*
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, access_key_id=None, secret_access_key=None, bucket_name=None):
        """
        Initialize with  credentials
        """
        self.aws_access_key_id = access_key_id
        self.aws_secret_access_key = secret_access_key
        self.bucket_name = bucket_name

    def upload_dir_to_s3(self, local_directory, destination, override_file='false'):
        """Enumerates and uploads files in local path directory to specified AWS S3 destination path. By passing ``override_file=true``, replaces existing files.

        Example:
        | Upload Directory To S3  | ../target/ | destination/ |
        | Upload Directory To S3  | ../target/ | destination/ | true |
        """
        # Initialize client to None
        client = None
        index = 0

        try:
            client = boto3.client('s3',
                                  aws_access_key_id=self.aws_access_key_id,
                                  aws_secret_access_key=self.aws_secret_access_key)
            for root, dirs, files in os.walk(local_directory):
                for filename in files:

                    # construct the full local path
                    local_path = os.path.join(root, filename)

                    # construct the full dropbox path
                    relative_path = os.path.relpath(local_path, local_directory)
                    s3_path = os.path.join(destination, relative_path).replace("\\", "/")

                    # relative_path = os.path.relpath(os.path.join(root, filename))

                    print('Searching "%s" in "%s"' % (s3_path, self.bucket_name))
                    try:
                        # Check if the object exists on S3, uploads incremented file if exists
                        if override_file == 'false':
                            client.head_object(Bucket=self.bucket_name, Key=s3_path)
                            file_name, file_extension = os.path.splitext(s3_path)
                            index += 1
                            incremented_file_path = f'{file_name} ({index}){file_extension}'

                            status = self.file_exists_on_s3(client, incremented_file_path)
                            if status:
                                check = True

                                # While path exists, will continuously increment file
                                while check:
                                    index += 1
                                    incremented_file_path = f'{file_name} ({index}){file_extension}'
                                    check = self.file_exists_on_s3(client, incremented_file_path)

                                print("Uploading %s..." % incremented_file_path)
                                client.upload_file(local_path, self.bucket_name, incremented_file_path)
                            else:
                                client.upload_file(local_path, self.bucket_name, incremented_file_path)

                        # Check if the object exists on S3, replaces file if exists
                        elif override_file == 'true':
                            status = self.file_exists_on_s3(client, s3_path)
                            if status:
                                print("Deleting %s..." % s3_path)
                                client.delete_object(Bucket=self.bucket_name, Key=s3_path)
                                print("Uploading %s..." % s3_path)
                                client.upload_file(local_path, self.bucket_name, s3_path)
                            else:
                                print("Uploading %s..." % s3_path)
                                client.upload_file(local_path, self.bucket_name, s3_path)
                        else:
                            print("Invalid override_file value")
                    except Exception as e:
                        if e.response['Error']['Code'] == '404':
                            # Object does not exist, upload it
                            print("Uploading %s..." % s3_path)
                            client.upload_file(local_path, self.bucket_name, s3_path)
                        else:
                            # Handle other errors
                            print("An error occurred while checking %s: %s" % (s3_path, e))

                    # Reset counter for next file
                    index = 0
        finally:
            # Close client
            if client is not None:
                client.close()

    def file_exists_on_s3(self, client, s3_path):
        """Verifies if specified path exists on AWS S3 destination path

        Example:
        | File Exists On S3  | current_client_session | destination_path/ |
        """
        try:
            client.head_object(Bucket=self.bucket_name, Key=s3_path)
            print("Path found on S3! %s" % s3_path)
            return True
        except Exception as e:
            return False
