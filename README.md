# Similarweb free API

The Similarweb Chrome extension (or Firefox add-on) provides free access for some basic data (traffic, global and country rank, bounce rate, geo, traffic sources, screenshot, category) using an undocumented API endpoint. With [extension source viewer](https://addons.mozilla.org/hu/firefox/addon/crxviewer/), you can find the URL, which returns free data about a given domain without using any API keys. Example:

    https://api.similarweb.com/v1/SimilarWebAddon/github.com/all
    
Note that at the time we don't know what is the limitation of this API endpoint, so be careful and wait some minutes/hours when the limit reached (prevention to getting banned not implemented yet).
