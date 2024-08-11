## 1.27.3 - 2024-08-10
### Extractors
#### Additions
- [bunkr] support `bunkr.ci` and `bunkrrr.org` ([#5970](https://github.com/mikf/gallery-dl/issues/5970))
- [furaffinity] add `submissions` extractor ([#5954](https://github.com/mikf/gallery-dl/issues/5954))
- [hentaicosplays] support `hentai-cosplay-xxx.com` ([#5959](https://github.com/mikf/gallery-dl/issues/5959))
#### Fixes
- [behance] fix `KeyError: 'fields'` ([#5965](https://github.com/mikf/gallery-dl/issues/5965))
- [behance] fix video extraction ([#5965](https://github.com/mikf/gallery-dl/issues/5965))
- [cien] extract all files when authenticated ([#5934](https://github.com/mikf/gallery-dl/issues/5934))
- [deviantart] fix `KeyError - 'category'` ([#5960](https://github.com/mikf/gallery-dl/issues/5960), [#5961](https://github.com/mikf/gallery-dl/issues/5961), [#5969](https://github.com/mikf/gallery-dl/issues/5969), [#5971](https://github.com/mikf/gallery-dl/issues/5971), [#5976](https://github.com/mikf/gallery-dl/issues/5976), [#5978](https://github.com/mikf/gallery-dl/issues/5978))
- [fanbox] update pagination logic ([#5949](https://github.com/mikf/gallery-dl/issues/5949), [#5951](https://github.com/mikf/gallery-dl/issues/5951), [#5956](https://github.com/mikf/gallery-dl/issues/5956))
- [hotleak] fix AttributeError ([#5950](https://github.com/mikf/gallery-dl/issues/5950))
- [instagram] restore GraphQL API functionality ([#5920](https://github.com/mikf/gallery-dl/issues/5920))
- [twitter] update `x-csrf-token` header during login ([#5945](https://github.com/mikf/gallery-dl/issues/5945))
#### Improvements
- [bunkr] fail downloads for `maintenance` files ([#5952](https://github.com/mikf/gallery-dl/issues/5952))
- [zerochan] improve tag redirect handling, add `redirects` option ([#5891](https://github.com/mikf/gallery-dl/issues/5891))
### Post Processors
- [metadata] add `base-directory` option ([#5262](https://github.com/mikf/gallery-dl/issues/5262), [#5728](https://github.com/mikf/gallery-dl/issues/5728))
