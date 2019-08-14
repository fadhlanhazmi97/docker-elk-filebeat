### ELK Stack with Elastalert
The purpose of this project is to monitor log and send alert using elastalert when the log has match with certain criteria. Logstash isn't used in this project and use filebeat instead for lightweight log shipper.

### How to run
If you want to run the entire stack and elastalert in your local machine. Do the following:

```git clone https://github.com/fadhlanhazmi97/docker-elk-filebeat && cd docker-elk-filebeat```

then run the entire stack with make:

```make run```

which is equivalent to:

```export HOSTNAME=$HOSTNAME && docker-compose up -d```

### Running in Google Cloud Platform
Please refer to [this](https://github.com/fadhlanhazmi97/elk-terraform) repository (https://github.com/fadhlanhazmi97/elk-terraform) to run the stack in google cloud platform. The reffered repository used terraform to create and configure the VM and then run the stack in each VM.