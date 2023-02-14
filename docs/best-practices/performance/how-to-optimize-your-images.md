---
myst:
  html_meta:
    description: Optimize your shop's speed with automatic image optimization using
      Hypernode. Learn how to quickly reduce image size-on-disk without losing quality.
    title: How to optimise your images? | Hypernode
redirect_from:
  - /en/best-practices/performance/how-to-optimize-your-images/
  - /knowledgebase/magento-image-optimization-howto/
---

<!-- source: https://support.hypernode.com/en/best-practices/performance/how-to-optimize-your-images/ -->

# How to Optimize Your Images

If you want a faster shop, you have probably looked at [Google Pagespeed Insights](https://developers.google.com/speed/pagespeed/insights/) for useful suggestions. It probably told you to optimize your images. Which means, reducing the size-on-disk without losing quality. This is a very cumbersome process if you do this by hand (opening in Photoshop, saving-as, etcetera). But it is very easy if you use Hypernode. If you follow this article, **it will take you only a couple of minutes to set up automatic image optimization**.

Thanks to Peter Jaap for doing the [initial research](https://www.byte.nl/blog/afbeeldingen-optimaliseren-magento-bespaart-veel-webruimte/) (in Dutch).

> [@Hypernode_com](https://twitter.com/Hypernode_com) hypernode-image-optimizer is pretty effective "Optimization profit over all files: 502812 KB (82%)". Thanks for that!
>
> — Sander Mangel (@sandermangel) [March 16, 2015](https://twitter.com/sandermangel/status/577459189867528192)

## How Much Can You Win?

First, log in on your Hypernode by SSH and type this command:

```console
app@83f01a-example-magweb-cmbl:~$ hypernode-image-optimizer ~/public/media
[46%] /data/web/public/media/custom_options/quote/h/o/46f68f14df54b639546a583a942cd7c2.png (255 KB smaller)
[50%] /data/web/public/media/custom_options/quote/h/o/8a45641021fb82d172b9712f6631c49a.png (405 KB smaller)
[30%] /data/web/public/media/custom_options/quote/p/l/a74e500c8e08c48e54ea65d8422bc68e.png (114 KB smaller)
[77%] /data/web/public/media/custom_options/quote/L/i/8969288f4245120e7c3870287cce0ff3.jpg (426 KB smaller)
[ 0%] /data/web/public/media/custom_options/quote/T/a/6bfddcd09ff981b24fc96e442700f2df.png (0 KB smaller)
[... long list of files ...]
Optimization profit over all files: 226 MB (30%)
```

Great! It has not changed anything yet, but has calculated that you can save 226MB (or 30%) of disk-usage by optimizing your images.

## Saving the optimized images for real

Make sure you have a backup of your media files. Then use this command to replace the old images with the optimized images:

```console
app@83f01a-example-magweb-cmbl:~$ hypernode-image-optimizer --quality 80 --write --newonly ~/path/to/media
```

Visit your site, do a CTRL-F5 (Mac: CMD-R) to refresh your cache and visually inspect the results. You will most likely not see a difference, apart from a much quicker page ;)

## Exclude Directories

To use the `hypernode-image-optimizer` and exclude one or more directories, specify `--exclude` with one or more paths. For example:

```console
app@83f01a-example-magweb-cmbl:~$ hypernode-image-optimizer /data/web/public | wc -l
431
app@83f01a-vdloo-magweb-cmbl:~$ hypernode-image-optimizer /data/web/public --exclude /data/web/public/static/frontend /data/web/public/static/adminhtml/Magento | wc -l
12
# In this example images from the following directories were ignored:
# /data/web/public/static/frontend
# /data/web/public/static/adminhtml/Magento
```

## Recommended: Periodic Optimization Using Cron

To keep the disk usage reduced and your shop fast, we recommend you to add a cronjob to optimize new images every night.

NB: [Magereport.com](http://magereport.com) checks for a cronjob that optimizes your images periodically. If you optimized your images only once, the check will come out red.

```console
app@83f01a-example-magweb-cmbl:~$ crontab -e
```

And add this line:

```bash
30 4 * * * chronic hypernode-image-optimizer --experimental --quality 80 --write --newonly ~/public/media
```

Presto, every night at 4:30 all new images (uploaded the previous day) will be optimized.

## Pro Tips

The image optimizer will do two things.

First, it will set the image compression level to 90% for JPG images, which is a very safe, conservative value. Many image optimization guides even recommend setting it to 80%. You can do so as well, by running `hypernode-image-optimizer --quality 80`. See below for samples at different quality levels.

Second, it will shrink big images: 2000+ pixels in width or height. If you want to change the threshold (for example, 3000 pixels), you can use `hypernode-image-optimizer --size 2000`.

## Experimental mode

Since 21 June 2016, an `--experimental` mode is available. This yields better compression results (notably for PNG) but is slower. Example runs on our test images:

```console
app@83f01a-example-magweb-cmbl:~$ hypernode-image-optimizer ~/public/media
[...]
Safe optimization profit over 1002 files: 11 MB (37%)

app@83f01a-example-magweb-cmbl:~$ hypernode-image-optimizer ~/public/media --experimental
[...]
Safe optimization profit over 1002 files: 17 MB (56%)

```

So this is another huge win in size! It takes 2 to 3 times more time, so especially the first run (where all image files are considered) may take a while (e.g. several days if you have hundred thousands of products). This should not be a problem, as the image optimizer runs in the lowest possible priority, so will not disturb your live performance.

As with the regular optimizer, ensure you have a backup before using the experimental mode.

## Examples of Different Quality Levels

![result100](_res/result100.png)

![result50](_res/result50.png)
