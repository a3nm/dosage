# -*- coding: iso-8859-1 -*-
# Copyright (C) 2004-2005 Tristan Seligmann and Jonathan Jacobs
# Copyright (C) 2012-2014 Bastian Kleineidam

from re import compile, escape
from ..scraper import _BasicScraper
from ..helpers import bounceStarter, indirectStarter
from ..util import tagre


class Lackadaisy(_BasicScraper):
    description = u'Alcohol-running cats in prohibition St. Louis'
    baseUrl = 'http://lackadaisy.foxprints.com/'
    url = baseUrl + 'comic.php'
    stripUrl = baseUrl + 'comic.php?comicid=%s'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://www\.lackadaisycats\.com/comic/[^"]*)'))
    prevSearch = compile(tagre("a", "href", r"(/comic\.php\?comicid=[0-9]+)") + "&lt; Previous")
    help = 'Index format: n'
    starter = bounceStarter(url,
        compile(tagre("a", "href", r"(/comic.php\?comicid=[0-9]+)") + "Next"))

    @classmethod
    def namer(cls, imageUrl, pageUrl):
        """Use comic id for filename."""
        num = pageUrl.rsplit('=', 1)[-1]
        ext = imageUrl.rsplit('.', 1)[-1]
        return 'lackadaisy_%s.%s' % (num, ext)


class LasLindas(_BasicScraper):
    url = 'http://laslindas.katbox.net/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s/'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/[^"]+)' % rurl, after="attachment-full"))
    multipleImagesPerStrip = True
    prevSearch = compile(tagre("a", "href", r'(%scomic/[^"]+)' % rurl, after="previous"))
    help = 'Index format: stripname'


class LeastICouldDo(_BasicScraper):
    description = u'A daily webcomic series about the life of Rayne Summers. Created by Ryan Sohmer and Lar deSouza.'
    url = 'http://www.leasticoulddo.com/'
    rurl = escape(url)
    stripUrl = url + 'comic/%s'
    firstStripUrl = stripUrl % '20130109'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/\d{8,9}\.\w{1,4})' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%scomic/\d+/)' % rurl, after="Previous"))
    starter = indirectStarter(url,
      compile(tagre("a", "href", r'(%scomic/\d+/)' % rurl, after="feature-comic")))
    help = 'Index format: yyyymmdd'


class Lint(_BasicScraper):
    url = 'http://www.purnicellin.com/lint/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2004/01/10/01102004'
    imageSearch = compile(r'<img src="(%scomics/.+?)"' % rurl)
    prevSearch = compile(r'\| <a href="([^"]+)" rel="prev">')
    help = 'Index format: yyyy/mm/dd/num-name'


class LinuxComFridayFunnies(_BasicScraper):
    description = u"Linux.com: Friday Funnies"
    url = 'https://www.linux.com/news/friday-funnies/'
    stripUrl = url + '%s'
    firstStripUrl = stripUrl % 'the-road-to-japan'
    imageSearch = compile(tagre("img", "src", r'(/news/friday-funnies/episode/[^"]+\?format=image[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(/news/friday-funnies/[^"]+)') + "Previous")
    help = 'Index format: stripname'


class LittleGamers(_BasicScraper):
    description = u'The comic everyone knows, but no one reads'
    url = 'http://www.little-gamers.com/'
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2000/12/01/99'
    imageSearch = compile(tagre("img", "src", r'(http://little-gamers\.com/comics/[^"]+)'))
    prevSearch = compile(tagre("a", "href", r'(http://www\.little-gamers\.com/[^"]+)', before="comic-nav-prev-link"))
    help = 'Index format: yyyy/mm/dd/name'


class LoadingArtist(_BasicScraper):
    description = u'A webcomic by Gregor Czaykowski'
    url = 'http://www.loadingartist.com/'
    rurl = escape(url)
    stripUrl = url + '%s/'
    firstStripUrl = stripUrl % '2011/01/04/born'
    imageSearch = compile(tagre("img", "src", r'(%swp-content/uploads/\d+/\d+/[^"]+)' % rurl))
    prevSearch = compile(tagre("a", "href", r'(%s\d+/\d+/\d+/[^"]+/)' % rurl, after="prev"))
    help = 'Index format: yyyy/mm/dd/stripname'


class LookingForGroup(_BasicScraper):
    url = 'http://www.lfgcomic.com/'
    rurl = escape(url)
    stripUrl = url + 'page/%s/'
    firstStripUrl = stripUrl % '1'
    imageSearch = compile(tagre("img", "src", r'(http://(?:www|cdn)\.lfgcomic\.com/wp-content/uploads/\d+/\d+/lfg[^"]+)'))
    #http://www.lfgcomic.com/wp-content/uploads/2014/06/lfg2827-787-jun30-14.gif
    prevSearch = compile(tagre("a", "href", r'(%spage/[-0-9]+/)' % rurl, after="comic-nav-prev"))
    starter = indirectStarter(url,
        compile(tagre("a", "href", r'(%spage/[-0-9]+/)' % rurl, after="feature-item-link")))
    nameSearch = compile(r'/page/([-0-9]+)/')
    help = 'Index format: nnn'
