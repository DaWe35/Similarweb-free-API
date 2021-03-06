# Similarweb free API

The Similarweb Chrome extension (or Firefox add-on) provides free access for some basic data (traffic, global and country rank, bounce rate, geo, traffic sources, screenshot, category) using an undocumented API endpoint. With [extension source viewer](https://addons.mozilla.org/hu/firefox/addon/crxviewer/), you can find the URL, which returns free data about a given domain without using any API keys. Example:

    https://data.similarweb.com/api/v1/data?domain=github.com
    
Note that subdomain requests returns the main domain statistics. We don't know what is the limitation of this API endpoint, so be careful and wait some minutes/hours when the limit reached (prevention to getting banned not implemented yet).

**Is it legal?** Yes, the endpoint is just hidden, not forbidden.  The data also available on their website, for free (so you can write a crawler also, if you don't want to use this API).
