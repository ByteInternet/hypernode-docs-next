# hypernode-docs-next

## Generating new docs

```
DOC_URL=https://support.hypernode.com/en/ecommerce/magento-1/how-to-enable-mysql-query-logging-for-magento-1-x
bin/download_doc --output-dir=docs/ecommerce-applications $DOC_URL
```

## Installing dependencies

```
pip install -r requirements/base.txt
# or for development:
pip install -r requirements/development.txt
```

## Building

```
cd docs
make html
```

## Serving the HTML

```
cd docs
python3 -m http.server --directory _build/html/
```
