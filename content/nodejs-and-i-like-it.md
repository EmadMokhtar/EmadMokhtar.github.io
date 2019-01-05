Title: I tired Nodejs and I like it
Date: 2018-12-31 12:00
Category: python, nodejs
Tags: Python
Authors: Emad Mokhtar

<!-- PELICAN_BEGIN_SUMMARY -->
![The Sign]({static}/images/austin-chan-275638-unsplash.jpg)
Photo by Austin Chan on Unsplash

I had a chance to try Node.js framework last month; I decided to build REST APIs using [Node.js][1] and [express.js][2]. Regularly I'm using JavaScript in my daily work besides using [Django][3] to build Web Applications, but many times I need to develop a front-end feature, This when I need to use JavaScript. I'm always using JavaScript to write front-end logic, but I never wrote back-end logic using it. I took the challenge to develop a simple REST APIs using [express.js][2].

<!-- PELICAN_END_SUMMARY -->
<iframe src="https://giphy.com/embed/d4zHnLjdy48Cc" width="480" height="350" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

**Development environment**

To start developing, I need to get my machine ready, so I installed [node.js][1] via Homebrew (I'm a macOS user), it is quite easy, and node.js installation comes with [npm][4] "npm is a package manager for node.js it is like [pypi][5] or pip for Python". I used [Visual Studio Code][6] as a text editor. Now I'm ready to go 💪🏻.


**What I've learned?**

While building the REST APIs, I've learned many things, mainly that I'm experiencing the new development stack. Let's see the parts I've learned.

**Node.js**

[Node.js][1] is a back-end engine; it is using Google Chrome V8 JavaScript engine to run JavaScript code on your machine instead of a browser. Node is not a language it is an engine.

**Express.js**

[Express.js][2] is a web framework that uses Node.js; it is a minimalist web framework "micro-framework" that receives requests and replies with responses, micro-framework means it doesn't have ORM, template engine, etc. You can feel it is like [Python Flask Framework][7].

**ORM**

I tried to build my models using [sequelize JS](http://docs.sequelizejs.com/) as I'm more familiar with PostgreSQL DB engine, but it turns to be so tricky to implement my feature using RDBMS system. I switched ORM to [Mongoose JS](https://mongoosejs.com/), and my database engine to [MongoDB][8]. I was wrong from the beginning, but after switching to [MongoDB][8], it is much easier to implement the feature, as it is a preferred database engine in Node.js community.

**Asynchronous Programming 🤔**

Getting used to the nature of [JavaScript asynchronous "Promises"](https://developers.google.com/web/fundamentals/primers/promises) was a big challenge for me, I'm used to synchronous programming; thus it was a big paradigm shift 🤯. On a daily basis, I'm using [Django][3], and it is not asynchronous by default ["there is a roadmap for Django to be Async"](https://www.aeracode.org/2018/06/04/django-async-roadmap/). [Python has asynchronous programming since version 3.5](https://docs.python.org/3.5/library/asyncio.html), but frameworks need to adapt it to become asynchronous as well, like [requests-future](https://github.com/ross/requests-futures).

**Final Thoughts 🧐**

I enjoyed using Node.js; the community is excellent, there is nothing you can't find a package for on NPM, it is such an active community, but what I don't like in the community is the quality of tutorials, most of the tutorials targeting starters or naive nodejs developers, yes we need tutorials for starters and naive nodejs developers, but what about the advanced tutorials.

The async programming challenge was an eye-opener for me; I need to dig deep in this way of programming especially in Python. I'm lucky that there is a video course on [Talk Python training about asynchronous in Python](https://training.talkpython.fm/courses/explore_async_python/async-in-python-with-threading-and-multiprocessing), and I think I will watch it.

[1]: https://nodejs.org/en/
[2]: https://expressjs.com/
[3]: https://www.djangoproject.com/
[4]: https://www.npmjs.com/
[5]: https://pypi.org/
[6]: https://code.visualstudio.com/
[7]: http://flask.pocoo.org/
[8]: https://www.mongodb.com/