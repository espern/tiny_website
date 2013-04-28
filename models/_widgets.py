class HierarchicalSelect(object):
    def __init__(self, db, table_name, title_field, order_field):
        self.options=[]
        self.db = db
        self.tablename = table_name
        self.fieldname = None
        self.title = title_field
        self.order = order_field
        self.type = None
        self.parent=None
        self.rows=None

    def _childs_list(self, field, depth):
        path = XML("&nbsp;&nbsp;&nbsp;&nbsp;")*depth
        self.options.append((field['id'], path+field[self.title]))
        [self._childs_list(child, (depth+1)) for child in self.rows.find(lambda row: row.parent == field.id)]   

    def widget(self, field, value):
        self.fieldname = field.name
        self.type = field.type
        self.rows = self.db(self.tablename).select(orderby=self.order)
        self.parent = field

        [self._childs_list(field,0) for field in self.rows.find(lambda row: row.parent == None)] 

        opt=[OPTION(name, _value=key) for key,name in self.options]
        sel = SELECT(opt,_id="%s_%s" % (self.tablename, self.fieldname),
                        _class=self.type, 
                        _name=self.fieldname,
                        value=value)
        return sel