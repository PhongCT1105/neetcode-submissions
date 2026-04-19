# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        def get_host_name(url):
            return url.split("/")[2]

        visited = set()
        stack = [startUrl]
        start_host_name = get_host_name(startUrl)

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            if get_host_name(node) != start_host_name:
                continue
            visited.add(node)
            neighbour = htmlParser.getUrls(node)
            for i in neighbour:
                stack.append(i)

        return visited
