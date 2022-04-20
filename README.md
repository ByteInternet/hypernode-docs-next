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
