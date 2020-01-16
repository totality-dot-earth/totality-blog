---
title: "Why IPFS"
date: 2020-01-15T11:08:32-08:00
draft: true
summary: Why is IPFS worth the trouble for a blog?
categories:
- think
tags:
- dweb
- ipfs
---

I wrote [here]({{< ref "this-blog" >}}) how this blog is built. The better question - thanks Aman! :pray: - is why? Why not post on medium, or put a static site on github pages or an S3 bucket, or use a virtual private server, or even go super old-school and run a web server at home (I do have this sweet, sweet [Sonic fiber](https://www.sonic.com/gigabit-fiber-internet) after all).

And, just to get this out of the way, part of the reason I did it this way is because I am a huge nerd, and this technology is new, and interesting, and I wanted to. But that's just part of the story - there's lots of new and interesting technology out there, and I don't have time to kick all of the tires.

What are the more specific motivations?

As many have noted, the internet and the web as we know them (including fundamental technologies such as DNS, TCP/IP, HTTP, SMTP, and even Javascript) are flawed in fundamental ways. As a result, it is hard to stop bad actors from doing bad things, from sending too many emails to stealing sensitive data to flooding websites with traffic. More subtly, the core internet technologies have designs that lead, over time and in combination with many other social, economic, and political forces, to centralization and balkanization. It would be silly to say that the design of DNS, for example, is what allows for the dominance of internet giants like Google and Facebook. At the same time, many of the choices that went into DNS and HTTP - including the elements that got left out as those standards moved from idea to adoption - have absolutely been weaponized to consolidate economic and political power.

IPFS is, at best, a small part of the solution to these problems. It does not, on its own, cure the internet's ails - that's what bitcoin is for. :stuck_out_tongue_winking_eye:

The main change that IPFS makes relative to the "old" internet is in how web pages are named: addresses are tied to content, not a particular server. To understand the importance of this shift, let's go back to the old days of the internet. 
