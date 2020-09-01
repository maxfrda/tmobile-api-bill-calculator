class View:


  def welcome(self):
    print 'Welcome to the T-Mobile Bill Calculator!'
    print ' '
    print '          -----------            '
    print 'How many phone lines do you need?'
    return input()

  def show_count(self, lines, repo):
      print ' '
      print '%s/%s selected' % (len(repo),lines)
      print 'Which Phone would you like to add?'


  def show_phones(self, phones):
    i = 1
    for f in phones:
      print "%s. %s($%s)" % (i, f.name, f.price)
      i += 1
    return input()

   # gets data from our API, which is inside of global TmoData object
  def choose_plan(self):
    print 'Select your plan'
    return input()

  #adds plan price to price of each phone and prints result
  def show_bill(self, total):
    print  "Your bill is $%s per month" % (total)
