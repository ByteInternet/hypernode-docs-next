---
myst:
  html_meta:
    description: You want to use a single Shopware installation for several domains
      or shops. This can be realised by adding as much language and/or sub shops as
      you need.
    title: How to set up a multistore in Shopware 5? | Hypernode
redirect_from:
  - /en/ecommerce/shopware/how-to-setup-a-multistore-in-shopware/
---

<!-- source: https://support.hypernode.com/en/ecommerce/shopware/how-to-setup-a-multistore-in-shopware/ -->

# How to Setup a Multistore in Shopware

Just like a Magento webshop you might like to use a single Shopware installation for several domains or shops. This way you can address customers from different countries by serving their native language and currency settings on the shop. This can all be realised by adding as much language and/or sub shops as you need.

## Differences Between Main Shop, Subshop and Language shop

To be able to serve different content you should, depending on what you need, create at least one subshop or language shop. If you want to serve a whole other domain you should create a subshop. But if you want to want to serve a different language you can add a language shop. This language shop will for example be served like `/en` or `/nl`

### Main Shop

The main shop is the default shop that's installed on Shopware and mandatory for each installation.

### Subshop

A subshop is just be what you need if you like to use the Shopware installation for several domains. Subshops are independent from the Main-shop and make use of their own template(s) and data which can be configured on a separate domain. For example you could have the following setup:

- Main shop: `hypernode.com`
- Subshop: `byte.nl`
- Subshop: `hyperformance.nl`

### Language Shop

A language shop allows you to serve different languages for the Main and/of a subshop but with the same template. You can setup a virtual url for your language shops which allows you to reach every language shop via their own url. For example you can setup the mainshop, a subshop and language shops like this:

- Main shop: `hypernode.com`
- Language shop: `hypernode.com/de`
- Language shop: `hypernode.com/nl`
- Subshop: `byte.nl`
- Language shop: `byte.nl/en`

## How to Setup a Subshop or Language Shop

The backend provides a page from which you're able to setup and manage your multishop. You can find these settings by logging into the backend: "exampleshop.nl/backend" and navigate to `Configuration` -> `Basic settings` -> `Shop settings` -> `Shops`.

This page will provide you with an overview of all the available shops. From here you can manage your multishop by adding extra sub/language shops and manage the settings.

To add a subshop or language click on `Add entry`, make sure you edit the following details for your desired shop and click the `Save` button:

- **Shop type:** Subshop / Language shop
- **Name:** Give the shop a name for internal purposes.
- **Title:** Enter a title for the frontend.
- **Position:** This setting determines the order in which the shops are displayed in the dropdown menu in de frontend and in the list on the backend.
- **Host (subshops only):** Enter the domain-name, for example: `example.com`
- **Virtual URL:** You can enter a virtual URL If the URL differs from the store.
- **Path (subshops only):** Enter the path to the Shopware directory
- **SSL support (subshops only):** Check this box if you want to use SSL and already have a valid certificate installed.
- **Host aliases:** You can enter your aliases here when multiple domains are routing to your shop.
- **Currency:** Select the available currency from your shop
- **Localisation:** Select the localisation of the shop.
- **Category:** Choose the main category of the shop. Shopware sets this as the root category and will display all subcategories fo your chosen shop
- **Template (subshops only):** Assign a theme to your shop. You can configure theme in the "Theme Manager".
- **Document template (subshop only):** Choose the document template.
- **Customer Group:** Choose the default customer group for this shop
- **Customer Scope (subshops only):** By default, your customers can log in to every subshop. With the customer scope you can register customers to the shops to which they should have access. Note, when this option is enabled, you should activate this for all shops!
- **Adopt translation (Language shops only):** When you setup multiple language shops with the same language, you can adopt translations from the choosen language shop.
- **Active:** Activate or deactivate the shop.
- **Standard shop (subshops only):** This settings is just to indicate the main shop.
- **Select currencies (subshops only):** Choose your alternative currencies.
- **Select pages:** Set the shop pages. When there are none set, the default set will be used.
