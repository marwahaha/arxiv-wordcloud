# arxiv-wordcloud

This builds a wordcloud of a person's research using their abstracts on arXiv.

I optimized the images with pngquant:
```
pngquant --ext .pn -s1 16 *.png
ls *.pn | while read -r file; do mv $file ${file}g; done
```


Author searches fetch the live arXiv Atom feed through `https://proxy.cors.dev/`, because arXiv does not send browser CORS headers. The target query uses HTTPS and URLSearchParams. No author-specific snapshots or API keys are used. The anonymous proxy can impose rate, size, or upstream timeout limits; failed requests produce a visible retry message.
