from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.db import connection



class SQLInfo(MiddlewareMixin):

    def process_response(self, request, response):
        db_queries = len(connection.queries)
        content_types = ('text/plain', 'text/html')
        if request.META['CONTENT_TYPE'] not in content_types:
            return response
        elif db_queries:
            sqltime = 0  # Variable to store execution time
            for query in connection.queries:
                sqltime += float(query['time'])  # Add the time that the query took to the total

            # len(connection.queries) = total number of queries
            print("Page render: " + str(sqltime) + "sec for " + str(len(connection.queries)) + " queries")
            response.content = response.content.replace(b'</body>', str.encode('<div class = "container">'+
                                                                 '<ul class=ml-auto>'+ 'number of SQL requests: '+
                                                                 str(len(connection.queries)) + '</br>' +
                                                                 'total time: '+ str(sqltime) + '</ul></div></body>'))
            return response
        else:
            return response