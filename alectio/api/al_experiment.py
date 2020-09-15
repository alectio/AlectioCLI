

class ALExperiment():
    def __init__(self, id):
        self.id = id


    def upload_record_db(self, path_to_file):
        "upload index to record mapping"
        return

    def upload_inference_stats(self, path_to_file):
        "upload final layer nn layer, need unlabled pool"
        return

    def upload_and_compute_metrics(self):
        """
        compute metrics and upload metrics to backend
        """
        return

    def unlabeled_pool(self):
        """
        retreive unlabeled pool to perform inference on
        """
        return


