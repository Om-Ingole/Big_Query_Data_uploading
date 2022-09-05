# Big_Query_Data_uploading
A python script to fetch data from public Api and Uploading it to BigQuery



**A Little About Big query**



**BigQuery is the public implementation of Dremel that was launched by Google to general availability.**

Dremel is Google’s query engine and it is able to turn SQL queries into an execution tree which reads data from Google’s distributed filesystem. Dremel has high scalability and is able to return queries results within seconds (or tens of seconds) despite the size of the dataset.

BigQuery provides the core features of Dremel to third parties, via a REST API, a command line interface and a Web UI.

But BigQuery is a bit more than Dremel…

In fact, BigQuery leverages multiple technologies developed at Google.

First, it uses Borg (Google’s cluster management system) to allocate the compute capacity for the Dremel jobs. Dremel jobs read data from Google’s file systems using Jupiter, Google’s high-speed network, which exchange data at 10 Gbps.

Thanks to its architecture, BigQuery does not require indexes, the data is stored in a proprietary columnar format called (more on this later) on Colossus (Google’s file system) and each query performs a full scan of the targeted table.

The increase in load is managed mainly by adding servers. This is handled transparently for the user, who does not “add servers” or “use bigger machines” in the way they would using e.g. Redshift or Postgres.


 **Two major factors:**

    **Columnar storage:** the Data is stored by columns and this makes it possible to achieve very high compression ratio and scan throughput.
    **Tree architecture:** a tree execution architecture is used to dispatch queries and aggregate results across thousands of machines.
    
  
  Google has Client Libraries for many of their services and we will be using the official bigquery client library for python. Install the following packages in python if you don’t have them already, you can even install them directly from a Jupyter notebook as below.
  
  #Install and load packages
%pip install google-cloud
%pip install google-cloud-bigqueryfrom google.cloud import bigquery
from google.oauth2 import service_account #Needed for authentication

We will be using the same JSON file which is the service token containing the credentials that we obtained as above to authenticate.
    
    #Authentication
key_path = "/path/to/your/service-account.json"credentials = service_account.Credentials.from_service_account_file(
    key_path,
    scopes=["https://www.googleapis.com/auth/cloud-platform"],
)
  
  
  

![image](https://user-images.githubusercontent.com/92270337/188359141-4d7d79f3-1018-485f-aee1-eaaf76fa2b6e.png)

Here is Small Anallysis Based on  The Data
which gives information about the percentage Change of each stock

![image](https://user-images.githubusercontent.com/92270337/188360588-1dd9b25a-f4d2-4336-b550-8e34e7f76006.png)



