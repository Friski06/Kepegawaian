import http.client
import xml.dom.minidom

HOST = "www.domain.nl"
API_URL = "/api/url"


def do_request(xml_location):
    """HTTP XML Post request"""
    request = open(xml_location, "r").read()

    webservice = http.client.HTTPConnection(HOST)
    webservice.putrequest("POST", API_URL)
    webservice.putheader("Host", HOST)
    webservice.putheader("User-Agent", "Python post")
    webservice.putheader("Content-type", "text/xml; charset=\"UTF-8\"")
    webservice.putheader("Content-length", "%d" % len(request))
    webservice.endheaders()

    webservice.send(request.encode("utf-8"))

    response = webservice.getresponse()
    statuscode = response.status
    statusmessage = response.reason
    header = response.getheaders()

    result = response.read()
    resultxml = xml.dom.minidom.parseString(result)

    print(statuscode, statusmessage, header)
    print(resultxml.toprettyxml())

    with open("output-%s" % xml_location, "w") as xmlfile:
        xmlfile.write(resultxml.toprettyxml())

do_request("xml-request-file.xml")
