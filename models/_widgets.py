class HierarchicalSelect(object):
    def __init__(self, db, title_field):
        self.options=[]
        self.db = db
        self.tablename = None
        self.fieldname = None
        self.title = title_field
        self.type = None
        self.parent=None
        self.rows=None

    def _childs_list(self, field, depth):
        path = XML("&nbsp;&nbsp;&nbsp;&nbsp;")*depth
        self.options.append((field['id'], path+field[self.title]))
        [self._childs_list(child, (depth+1)) for child in self.rows.find(lambda row: row.parent == field.id)]   

    def widget(self, field, value):
        print str(field)
        self.tablename = field._table
        self.fieldname = field.name
        self.type = field.type
        self.rows = self.db(self.tablename).select()
        self.parent = field

        root_fields = self.db(self.parent==None).select()
        [self._childs_list(field,0) for field in self.rows.find(lambda row: row.parent == None)] 

        opt=[OPTION(name, _value=key) for key,name in self.options]
        sel = SELECT(opt,_id="%s_%s" % (self.tablename, self.fieldname),
                        _class=self.type, 
                        _name=self.fieldname,
                        value=value)
        return sel