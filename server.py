#!/usr/bin/python

import BaseHTTPServer
import json
import classifier
from PIL import Image
import PIL
import io
from cgi import parse_header, parse_multipart
from tempfile import SpooledTemporaryFile

 
PORT_NUMBER = 8080
BASE_URL = "127.0.0.1"
urls = {
   
}
 
#This class will handles any incoming request from
#the browser
class myHandler( BaseHTTPServer.BaseHTTPRequestHandler ):
   

    #Handler for the GET requests
    def do_POST( self ):

        content_len = int( self.headers['Content-Length'] )
        post_body = self.rfile.read( int( self.headers.getheader( 'Content-Length' ) ) )
        # print post_body
        # objeto = json.loads(post_body.decode("utf-8"))
 
        self.send_response( 200 )
        self.send_header( 'Content-type','text/html' )
        self.end_headers()
 
        # Send the html message
        obj = Image.open( io.BytesIO( post_body ) )
        print( classifier.predicting_label( obj ) )
        self.wfile.write( bytes( "batata", "utf-8" ) )
        return
 
try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = BaseHTTPServer.HTTPServer( ( BASE_URL, PORT_NUMBER ), myHandler )
    print( 'Started httpserver on port ' +  str( PORT_NUMBER ) )
   
    #Wait forever for incoming htto requests
    server.serve_forever()
 
except KeyboardInterrupt:
    print ('^C received, shutting down the web server')
    server.socket.close()