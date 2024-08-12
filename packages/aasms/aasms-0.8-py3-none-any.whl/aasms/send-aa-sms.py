#!/usr/bin/python

# File: send-aa-sms
# Author: Michael Stevens <mstevens@mstevens.org>
# Copyright (C) 2010

#    This file is part of aasms.
#
#    aasms is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    aasms is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with aasms.  If not, see <http://www.gnu.org/licenses/>.

import aasms
import sys
from optparse import OptionParser
import configparser

def run():
   usage = "usage: %prog -u username -p password -d destination -m message"

   parser = OptionParser(usage=usage, version="%prog 0.7")

   parser.add_option("-u", "--username", dest="username", help="The aaisp username, usually your VoIP number", action="store", type="string")
   parser.add_option("-p", "--password", dest="password", help="The aaisp password", action="store", type="string")
   parser.add_option("-d", "--destination", dest="destination", help="The destination number", action="store", type="string")
   parser.add_option("-m", "--message", dest="message", help="The message to send", action="store", type="string")
   parser.add_option("-f", "--file", dest="file", help="A config file", action="store", type="string")
   parser.add_option("-i", "--iccid", dest="iccid", help="The SIM iccid to send to", type="string", action="store")
   parser.add_option("-o", "--originator", dest="originator", help="The originator to use with an iccid", type="string", action="store")

   (options, args) = parser.parse_args()

   if options.file != None:
      config = configparser.SafeConfigParser()
      config.read(options.file)
      if options.username == None:
         if config.has_option("sms", "username"):
            options.username = config.get("sms", "username")
         else:
            options.username = None

      if options.password == None:
         if config.has_option("sms", "password"):
            options.password = config.get("sms", "password")
         else:
            options.password = None

      if options.iccid == None:
         if config.has_option("sms", "iccid"):
            options.iccid = config.get("sms", "iccid")
         else:
            options.iccid = None
         
   if options.username == None and options.iccid == None:
      parser.error("username or iccid is required\n")

   if options.iccid != None and options.username != None:
      parser.error("Must have only one of username or iccid\n")
      
   if options.password == None:
      parser.error("password is required\n")

   if options.destination == None and options.iccid == None:
      parser.error("destination is required when iccid not set\n")

   if options.message == None:
      parser.error("message is required\n")

   if options.iccid != None and options.originator == None:
      parser.error("If iccid specified must have originator\n")
      
   sender = aasms.aasms.SmsSender(username = options.username,
                           iccid = options.iccid,
                           password = options.password)
   try:
      sender.send(options.message,
                  destination = options.destination,
                  originator = options.originator)
      sys.exit(0)
   except aasms.SmsError as inst:
      sys.stderr.write("%s\n" % (inst.error()))
      sys.exit(1)

