# arxiv-wordcloud

This builds a wordcloud of a person's research using their abstracts on arXiv.

I optimized the images with pngquant:
```
pngquant --ext .pn -s1 16 *.png
ls *.pn | while read -r file; do mv $file ${file}g; done
```

