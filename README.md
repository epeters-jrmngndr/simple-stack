# simple-stack

A simple deployment with Kubernetes, including monitoring by Prometheus

## Testing

### Internal Connectivity

Pick a pod, and confirm that it can fetch the message locally:

`kubectl exec -it <pod_id> -- curl http://localhost:8080/message`

### Service connectivity

When using Minikube, get the service IP with `minikube service --all`.

Then you can make requests like `curl http://<service_ip>:30000/message`. Otherwise, port forwarding could be used.
