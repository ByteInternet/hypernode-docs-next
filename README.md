# hypernode-docs-next

## Generating new docs

``` bash
DOC_URL=https://support.hypernode.com/en/ecommerce/magento-1/how-to-enable-mysql-query-logging-for-magento-1-x
bin/download_doc --output-dir=docs/ecommerce-applications $DOC_URL
```

## Setting up the project

``` bash
mkvirtualenv hypernode-docs-next
echo "export PYTHONPATH=$(pwd)" >> $VIRTUAL_ENV/bin/postactivate
workon hypernode-docs-next
pip install -r requirements/development.txt
pre-commit install
```

## Building the docs

``` bash
bin/build_docs
```

## Serving the docs

``` bash
bin/serve_docs
```
## Setup Frontend step by step
```
clone the repository
pip install -r requirements/development.txt
bin/build_docs
bin/serve_docs
```
in another terminal run
``` bin/watch ```

open localhost and now you can make changes in style and refresh the page without rebuilding

when you're working on scss to compile it automatically run
```
sass --watch docs/_static/scss:docs/_static/css
```

or after changes compile scss once:
```
sass docs/_static/scss:docs/_static/css
```

## Deploying the docs with Hypernode Deploy

To deploy to a local Hypernode Docker environment:
```
$ docker pull docker.hypernode.com/byteinternet/hypernode-buster-docker:latest
$ docker run docker.hypernode.com/byteinternet/hypernode-buster-docker:latest
$ # Note the IP address, it should be 172.17.0.2 (otherwise refer to deploy.php)
```

Next make sure your `~/.ssh/yourdeploykey` equivalent can log in to the Docker host (172.17.0.2) as the app user. You can add it to the `/data/web/.ssh/authorized_keys` file on in the instance manually.

Then deploy to your local Hypernode Docker:
```
docker run --rm -it --env SSH_PRIVATE_KEY="$(cat ~/.ssh/yourdeploykey | base64)" -v ${PWD}:/build quay.io/hypernode/deploy:latest hypernode-deploy build -vvv  # First build the artifact
docker run --rm -it --env SSH_PRIVATE_KEY="$(cat ~/.ssh/yourdeploykey | base64)" -v ${PWD}:/build quay.io/hypernode/deploy:latest hypernode-deploy deploy docker -vvv  # Then perform the deploy
```
