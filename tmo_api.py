
"""
 This retrieves api info and is a class that won't be instantiated
 It returns the names and the prices of the plans by fetching data from
 tmobile plan app API
 """
import requests

class TmoData(object):
  url = "http://tmobile-plans.herokuapp.com/api/v1/plans"
  data = requests.get(url = url).json()

  """
  Here we search the returned json object and iterate through it, showing only
  plans that have x amount of lines (some plans have line caps)
  we also create an array that contains the returned objects, so that we can
  later search through them to fetch price when price is calculated
   """
  @classmethod
  def get_names(cls, num):
    i = 1
    arr = []
    for d in cls.data['data']:
      if  d['prices']["line%s" % (num)] != 'N/A':
        print "%s. %s($%s)" % (i, d['name'], d['prices']["line%s" % (num)] )
        arr.append({'id': i, 'price': d['prices']["line%s" % (num)] })
        i += 1
    cls.arr = arr

  @classmethod
  def show_prices(cls):
    for d in cls.data['data']:
     for l in d['prices']:
        print l

  @classmethod
  def get_price(cls, num):
    for f in cls.arr:
      if f['id'] == num:
        return f['price']

