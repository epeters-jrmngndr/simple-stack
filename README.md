# simple-stack

A simple deployment with Kubernetes, including monitoring by Prometheus

## Testing

### Internal Connectivity

Pick a pod, and confirm that it can fetch the message locally:

`kubectl exec -it <pod_id> -- curl http://localhost:8080/message`

### Service connectivity

When using Minikube, get the service IP with `minikube service --all`.

Then you can make requests like `curl http://<service_ip>:30000/message`. Otherwise, port forwarding could be used.

Once the service manifest has been applied to the cluster, you can also use the service IP. You find the ip with `minikube ip`, and can then sat an alias in the file below:

```/etc/hosts
<service_ip>  local-aliased-domain.com
```

Subsequently, the command `curl http://local-aliased-domain.com:30000/message` will allow you to fetch the message from the API.

### Ingress

Enable ingress addon: `minikube addons enable ingress`
