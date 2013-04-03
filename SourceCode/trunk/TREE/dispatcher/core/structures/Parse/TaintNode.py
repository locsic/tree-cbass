class TaintNode(object):
    def __init__(self, initial = None):
        self.uuid=str(initial)
        self.nodeattr = None
        self.ea = None

    def __str__(self):
        return self.uuid

    def label(self):
        return "[%s]%s_%s\n[%s][%s]" % (self.uuid, self.typ, self.name, self.startind, self.endind)
    
    def SetNodeAttr(self, s):
        self.nodeattr = s

    def ExtractData(self, s):
        #Temporary solution is to parse a text file until we get the C struct passed in
        import re
        pattern = re.compile(r"""
                              \[(?P<uuid>\d+)\]
                              (?P<type>(reg|mem|bc))
                              _(?P<name>[\d\w_]+)
                              \[(?P<startind>[\d\w:-]+)\]
                              (\[(?P<endind>[\d\w:-]+)\])?
                              (\<-(?P<edgeann>[\d\w\s\$%(),-]+))?
                              ({D}(?P<child_d>[\d\s]+))?
                              ({C}(?P<child_c>[\d\s]+))?
                              """, re.VERBOSE)
        m = pattern.search(s)
        self.uuid = m.group('uuid')
        self.typ = m.group('type') #Check to see if 'type' is a reserved word
        self.name = m.group('name')
        self.startind = m.group('startind')
        self.endind = m.group('endind')
        self.edgeann = m.group('edgeann')
        self.child_c = m.group('child_c')
        self.child_d = m.group('child_d')