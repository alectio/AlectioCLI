### Instructions for running experiments from the CLI

For this end-to-end demo we will be using the mnist / fashion-mnist dataset.

1. Make sure the Alectio SDK is set up. For more information about SDK set up please read the README file in the `AlectioSDK` directory as well as the README file in `AlectioSDK/examples/image-classification/fashion-mnist-and-mnist`
2. `cd examples` and modify the experiment.yml file according to your project and SDK specifications. For example, here you should modify the problemType, date, testLen, trainLen, ip (of your SDK), and port number (of your SDK - default is 5000). If you are following along with this mnist demo using the SDK + the CLI README's then the only value which needs to be changed now is the `ip` and `projectName`. 
3. Ensure that you are a paid user on the Alectio platform (otherwise you will not be able to upload a querying strategy)
4. *The process for starting an experiment on the CLI is described below:* 
5. First ensure that you have a project created by running `client.create_project("project.yml")`. Copy the project ID returned.
6. Upload your class labels file. An example file for the mnist dataset has been supplied in this examples folder. `client.upload_class_labels("mnist_labels.json", "<PROJECT_ID>")`
7. Create an experiment. It is important to modify the experiment.yml file with the project ID from step 5. `client.create_experiment("experiment.yml")`. Make note of the experiment ID. 
8. Upload the querying strategy for the experiment. Broadly speaking, Alectio users have two options for uploading querying strategies (simple and advanced). In contrast to simple strategies, using advanced strategies allows you to run different active learning algorithms on different loops as well as specify the lower and upper bounds for confidence, margin, and entropy computations. For this demo, we will be using the simple querying strategy described in simple_confidence_strat.yml. Upload this strategy directly to the experiment by running the following command: `client.experiment("<EXPERIMENT_ID>").upload_query_strategy("simple_confidence_strat.yaml")`
9. Next, we'll start the experiment. Starting an experiment lets our servers know that it's time to start the AL training process and it also triggers the SDK. You can start the experiment when ready with the command: `client.experiment("<EXPERIMENT_ID>").start()`

