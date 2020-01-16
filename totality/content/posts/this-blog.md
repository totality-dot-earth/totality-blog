---
title: "How This Blog Was Made"
slug: how-this-blog-was-made
date: 2020-01-14T16:11:17-08:00
draft: false
summary: You know you want to read this, nerd.
categories: 
- build
tags:
- dweb
- ipfs
- nerdery
---

Half of all blog posts are about the tools and platform used to create the blog. Who am I to fight this?

[Hugo](https://gohugo.io/) is the static site generator - I'm writing this in markdown in a text editor, and then I run a simple hugo command to create the HTML and CSS for the site. [Pretty standard, really.](https://genius.com/Austin-powers-movie-the-early-years-annotated)

After the site is built (for example, after I finish this post), I run a [little script](https://github.com/str8d8a/totality-blog/blob/master/totality/deploy.sh) that calls [ipfs-deploy](https://github.com/ipfs-shipyard/ipfs-deploy). This does two important things:

1. It adds the new site to [IPFS](https://ipfs.io/) and tells my chosen pinning service, [Piñata](https://pinata.cloud/), to make sure that the files are always available. This means that, while my blog's files might end up in any number of places and get served from there (the magic of [content addressing](https://flyingzumwalt.gitbooks.io/decentralized-web-primer/avenues-for-access/lessons/power-of-content-addressing.html)), Piñata will make sure that they're always available *somewhere*.
2. It updates a [dnslink](https://dnslink.io/) pointer at Cloudflare, which allows Cloudflare's DNS to direct `teetotality.blog` HTTP traffic to the correct IPFS hash address via [their IPFS Gateway](https://blog.cloudflare.com/distributed-web-gateway/). So even though you've (probably) reached this page through a regular old HTTP link that uses the `teetotality.blog` host name, there is in fact no server with that name - the content is stored on various IPFS nodes, including but not limited to Cloudflare's edge caches.

This means that, in addition to the old and busted way of reaching this content, you can also find it on the IPFS network more directly:

* You can find a particular hash version through an HTTP gateway. For example, the version that is published *now* - i.e., before I update with this post - is at `/ipfs/QmPrQtC7YB9evZwLVcuApMU46X81zhr56WFG1W67ihQdJG`, and you can find it through the [IPFS project's gateway](https://ipfs.io/ipfs/QmPrQtC7YB9evZwLVcuApMU46X81zhr56WFG1W67ihQdJG/), or [Cloudflare's](https://cloudflare-ipfs.com/ipfs/QmPrQtC7YB9evZwLVcuApMU46X81zhr56WFG1W67ihQdJG/), or any other [public gateway](https://ipfs.github.io/public-gateway-checker/).
  
* But that hash address will change as soon as I publish this new version - remember, each hash is associated with a particular arrangement of bytes, and those change every time the site is updated in any way. This is the blessing and curse of content addressing. IPFS has a solution for this - its own naming service, [IPNS](https://docs.ipfs.io/guides/concepts/ipns/), which provides stable names that point to successive versions of a given "site" as its hash changes. You can access this service through an HTTP gateway as well: [https://ipfs.io/ipns/teetotality.blog/](https://ipfs.io/ipns/teetotality.blog/). In this case, this address should always resolve to the most recent version (and this post should be at [https://ipfs.io/ipns/teetotality.blog/posts/this-blog](https://ipfs.io/ipns/teetotality.blog/posts/how-this-blog-was-made), as soon as I hit publish).
  
* Still, you might notice that these methods [all rely on gateways](https://medium.com/pinata/the-ipfs-gateway-problem-64bbe7eb8170) to bridge between the content-addressing world of IPFS and the host-addressing of HTTP. If you *really* want to take off the training wheels, you can install IPFS [on your system](https://docs.ipfs.io/guides/guides/install/), in your browser (e.g., [Chrome](https://chrome.google.com/webstore/detail/ipfs-companion/nibjojkomfdiaoajekhjakgkdhaomnch?hl=en)), or both. Then you'll be able to resolve IPFS hashes and IPNS addresses directly, at which point you'll really be living in the future.


