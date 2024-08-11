import json
import requests
from constants import *
from typing import List

class Anote:
    def __init__(self, api_key):
        # self.API_BASE_URL = 'http://localhost:5000'
        self.API_BASE_URL = 'https://api.anote.ai'
        self.headers = {
            # 'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}'
        }

    def train(self, task_type: NLPTask, model_type: ModelType, dataset_name, multi_column_roots, input_text_col_index, document_files=None):
        """
        Train a model with the given parameters.

        Args:
            task_type (str): The type of task (e.g., classification, regression).
            model_type (str): The type of model to train.
            dataset_name (str): The name of the dataset.
            multi_column_roots (list): A list of column roots.
            input_text_col_index (int): The index of the input text column.
            document_files (list): List of paths to document files, if any.

        Returns:
            str: The model ID if training is successful.
        """
        task_type_int = None
        if task_type is not None:
            task_type_int = task_type.value
        model_type_int = None
        if model_type is not None:
            model_type_int = model_type.value
        data = {
            "taskType": task_type_int,
            "modelType": model_type_int,
            "datasetName": dataset_name,
            "multiColumnRoots": multi_column_roots,
            "inputTextColIndex": input_text_col_index,
        }
        files, opened_files = _open_files(document_files)
        response = self._make_request('/public/train', data, files=files)
        print(response)
        return response

    def predictAll(self, report_name, model_types, model_id, dataset_id, actual_label_col_index, input_text_col_index, document_files=None):
        """
        Predict on an entire dataset using the specified model.

        Args:
            model_id (str): The ID of the model to use for prediction.
            datasetId (str): The ID of the dataset to predict on.
            input_text_col_index (int): The index of the input text column.
            document_files (list): List of paths to document files, if any.

        Returns:
            dict: A dictionary containing the predictions.
        """
        data = {
            "modelId": model_id,
            "modelTypes": model_types,
            "reportName": report_name,
            "datasetId": dataset_id,
            "actualLabelColIndex": actual_label_col_index,
            "inputTextColIndex": input_text_col_index,
        }
        files, opened_files = _open_files(document_files)
        response = self._make_request('/public/predictAll', data, files=files)
        return response

    def predict(self, model_id, text, model_type = None, document_files=None):
        """
        Predict on a single piece of text using the specified model.

        Args:
            model_id (str): The ID of the model to use for prediction.
            text (str): The text to predict on.
            document_files (list): List of paths to document files, if any.

        Returns:
            str: The prediction result.
        """
        model_type_int = None
        if model_type is not None:
            model_type_int = model_type.value
        data = {
            "modelId": model_id,
            "text": text,
            "modelType": model_type_int
        }
        files, opened_files = _open_files(document_files)
        response = self._make_request('/public/predict', data, files=files)
        return response

    def evaluate(self, metrics: List[EvaluationMetric], task_type, report_name, dataset_id=None, multi_column_roots=None, input_text_col_index=None, document_files=None):
        """
        Evaluate the model performance using the given metrics.

        Args:
            metrics (dict): The evaluation metrics.
            dataset_id (str, optional): The ID of the dataset.
            multi_column_roots (list, optional): A list of column roots.
            input_text_col_index (int, optional): The index of the input text column.
            document_files (list, optional): List of paths to document files, if any.

        Returns:
            dict: A dictionary containing evaluation results.
        """
        task_type_int = None
        if task_type is not None:
            task_type_int = task_type.value

        data = {
            "metrics": json.dumps(metrics),
            "datasetId": dataset_id,
            "multiColumnRoots": multi_column_roots,
            "inputTextColIndex": input_text_col_index,
            "taskType": task_type_int,
            "reportName": report_name,
        }
        files, opened_files = _open_files(document_files)
        response = self._make_request('/public/evaluate', data, files=files)
        return response

    def checkStatus(self, predict_report_id=None, model_id=None):
        """
        Check the status of a prediction or training process.

        Args:
            predict_report_id (str, optional): The ID of the prediction report.
            model_id (str, optional): The ID of the model.

        Returns:
            bool: True if the process is complete, False otherwise.
        """
        data = {
            "predictReportId": predict_report_id,
            "modelId": model_id,
        }
        response = self._make_request('/public/checkStatus', data)
        return response

    def viewPredictions(self, predict_report_id, dataset_id, search_query, page_number):
        """
        View predictions for a given dataset and query.

        Args:
            predict_report_id (str): The ID of the prediction report.
            dataset_id (str): The ID of the dataset.
            search_query (str): The search query to filter predictions.
            page_number (int): The page number of the results.

        Returns:
            dict: A dictionary containing the predictions.
        """
        data = {
            "predictReportId": predict_report_id,
            "datasetId": dataset_id,
            "searchQuery": search_query,
            "pageNumber": page_number,
        }
        response = self._make_request('/public/viewPredictions', data)
        return response


    def _make_request(self, endpoint, data, files=None):
        url = f"{self.API_BASE_URL}{endpoint}"

        # Print request details for debugging
        print("Request URL:", url)
        print("Headers:", self.headers)
        print("Data:", data)
        print("Files:", files)

        if files:
            # For multipart/form-data
            response = requests.post(url, data=data, headers=self.headers, files=files)
        else:
            # For application/json
            headers = self.headers.copy()
            headers['Content-Type'] = 'application/json'
            response = requests.post(url, json=data, headers=headers)

        # _close_files(files)  # Uncomment if you need to close files

        if response.status_code == 200:
            try:
                return response.json()
            except requests.exceptions.JSONDecodeError:
                raise ValueError(f"Failed to decode JSON response for {endpoint}")
        else:
            raise requests.exceptions.RequestException(f"Request to {endpoint} failed with status code {response.status_code}")


    # def _make_request(self, endpoint, data, files=None):
    #     url = f"{self.API_BASE_URL}{endpoint}"
    #     print("data")
    #     print(data)
    #     print("files")
    #     print(files)
    #     response = requests.post(url, data=data, headers=self.headers, files=files)
    #     # _close_files(files)
    #     if response.status_code == 200:
    #         try:
    #             return response.json()
    #         except requests.exceptions.JSONDecodeError:
    #             raise ValueError(f"Failed to decode JSON response for {endpoint}")
    #     else:
    #         raise requests.exceptions.RequestException(f"Request to {endpoint} failed with status code {response.status_code}")


def _open_files(document_files):
    if document_files is None:
        return {}, []

    files = []
    opened_files = []
    for path in document_files:
        try:
            file = open(path, 'rb')
            opened_files.append(file)
            files.append(("files[]", (path.split('/')[-1], file, "application/octet-stream")))
        except Exception as e:
            print(f"Error opening file {path}: {e}")
            _close_files(opened_files)
            raise e
    return files, opened_files

def _close_files(opened_files):
    for file in opened_files:
        file.close()