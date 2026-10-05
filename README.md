# arxiv-wordcloud

This builds a wordcloud of a person's research using their abstracts on arXiv.

I optimized the images with pngquant:
```
pngquant --ext .pn -s1 16 *.png
ls *.pn | while read -r file; do mv $file ${file}g; done
```


Kunal Marwaha's search uses the saved arXiv feed in `feeds/kunal-marwaha.xml`, served directly by GitHub Pages. Refresh it manually with `python3 scripts/refresh-abstracts.py`, then commit the updated feed. The script validates the response before replacing the previous snapshot. The page displays the snapshot date. Other author searches still depend on the public AllOrigins proxy.
