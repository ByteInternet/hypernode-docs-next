---
myst:
  html_meta:
    description: Hypernode clusters allow you to scale your setup to your needs, both
      horizontally and vertically.
    title: Cluster | Hypernode platform
---

# Hypernode Cluster

Hypernode comes as a single server setup by default. This is to make sure that latency between services is as low as possible,
and that the server is as fast as possible. However, if you have a lot of traffic, or a lot of data, you might want to consider a
cluster setup. This is a setup where you have multiple servers, each with their own task. This way, you can scale your setup to
your needs.

Hypernode Cluster is available for both cloud and dedicated nodes. Dedicated nodes benefit extra from a cluster setup, as they
are more prone to going down because of  hardware failures. With a cluster setup, you can make sure that your setup stays up
even if one of your servers fails.

## Cluster vs single server

Choosing between a single server setup and a cluster setup is a trade-off between performance and flexibility. A single server
setup is the fastest, but a cluster setup is more flexible as it allows for more ways of scaling up the available resources.
You can add more servers to your cluster, allowing you to scale your setup to your needs. However, a cluster setup does come
with a performance penalty. The latency between services is higher, which causes a slight overhead in performance.

## Up/downgrading between plans

You're able to up or downgrade your plan with Hypernode whenever you want. This applies to both single server setups and
cluster setups.

In a Hypernode cluster this goes per Hypernode. So if you have a cluster with 3 Hypernodes, you can upgrade 1 Hypernode to a
higher plan, and the other 2 Hypernodes can stay on the old plan. This allows you to scale your setup to your needs while
the rest of the cluster stays up.

## Connecting between cluster Hypernodes

All Hypernodes within the same cluster are connected to each other. You can see how the Hypernodes relate to each other in the
cluster information table by running `hypernode-cluster-info`:

```console
app@abcdef-hnclusterweb1-magweb-tbbm:~$ hypernode-cluster-info
+---------------+--------------------------+-------------+----------------+------------+
| Hypernode     | Roles                    | Private_IP  | Private_subnet | Cluster_IP |
+---------------+--------------------------+-------------+----------------+------------+
| hnclusterdb1  | mysql                    | 192.168.1.5 | 192.168.1.0/24 | 10.0.0.2   |
| hnclusterlb1  | redis, nfs, loadbalancer | 192.168.1.2 | 192.168.1.0/24 | 10.0.0.3   |
| hnclusterweb1 | web                      | 192.168.1.3 | 192.168.1.0/24 | 10.0.0.1   |
| hnclusterweb2 | web                      | 192.168.1.4 | 192.168.1.0/24 | 10.0.0.5   |
+---------------+--------------------------+-------------+----------------+------------+
```

### Wireguard

All nodes within the cluster can communicate with each other over their cluster IP addresses. These are private IP addresses
that are only accessible within the cluster, as they are [Wireguard](https://www.wireguard.com/) tunnels between each Hypernode
in the cluster.

```console
app@abcdef-hnclusterweb1-magweb-tbbm:~$ ssh hnclusterdb1.hypernode.io hostname
abcdef-hnclusterdb1-magweb-tbbm.nodes.hypernode.io

For convenience, you can also use the short hostname
app@abcdef-hnclusterweb1-magweb-tbbm:~$ ssh hnclusterdb1.h hostname
abcdef-hnclusterdb1-magweb-tbbm.nodes.hypernode.io
```

### Private network switch

We can provide you with a private network so that your Hypernodes can communicate with each other with a larger bandwidth than
over a regular internet connection. This is especially useful if you have a lot of traffic between your Hypernodes, or if you
have a lot of data that needs to be transferred between your Hypernodes.

For this we provide a subnet where every Hypernode has its own private network IP address, which is only accessible to Hypernodes
in the same cluster and in the same datacenter/regions. Just like with Wireguard connections you can connect between Hypernodes
over the same private network. When available, we automatically configure the use of the private network over Wireguard
connections because of the larger bandwidth.

## Loadbalancer setup

In essence, loadbalancer servers accept HTTP(S) traffic (also known as web traffic) and forward the requests to application servers.
It balances the load by taking the amount of open connections for an application servers into account, selecting the server with the
least connections.

Web traffic is terminated by NGINX, which (optionally) forwards the request to varnish, which can return a cached page or send the
request to [HAProxy](https://www.haproxy.org/), which sends the request to the application servers.

### Managing NGINX

To add custom NGINX rules for handling specific things on the loadbalancer (like serving assets), the `loadbalancer.` prefix can be
used in `/data/web/nginx` and `/data/web/nginx/<vhost>`. This can be very crucial for your performance, accelerating asset delivery
and lowering pressure on varnish.

When running [hypernode-manage-vhosts](nginx/hypernode-managed-vhosts.md) on a loadbalancer server for a specific vhost, a
preconfigured loadbalancer configuration file will be created for you (for example `/data/web/nginx/example.com/loadbalancer.magento2.conf`).
These preconfigured files act as a good starting point for your loadbalancer setup, but can be customized to your needs.

On application servers, `/data/web/nginx` is an NFS mount to the `/data/web/nginx` directory of the loadbalancer server. Because of
this, changes to this directory from the application server will not trigger the nginx-config-reloader across the cluster. We advise
to do most nginx changes (either configuration files or hypernode-manage-vhosts) on the loadbalancer server.

For consistency, nginx reload events are propagated throughout the cluster, so that an nginx reload on one server also means a reload
on the other servers.

### Filesystem persistence

Application servers behind a loadbalancer will be configured with an NFS mount to the loadbalancer. The NFS share is mounted at
`/data/shared` on the application servers, which points to `/data` on the loadbalancer. For consistency, the loadbalancer itself
has a symlink `/data/shared`, which points to `/data`.

### Background jobs

While the loadbalancer server does not run PHP-FPM, it does have the PHP CLI installed, meaning that you could utilize the loadbalancer
server to run background jobs like crons and queue workers. Typically, background jobs are only ran on a single server, often done on
either the loadbalancer server or one of the application servers.
