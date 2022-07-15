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
