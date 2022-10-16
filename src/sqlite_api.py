import sqlite3

def table_exists(conn: sqlite3.Connection, table_name) -> bool:
    cur = conn.cursor()
    query = '''
    SELECT name
    FROM sqlite_schema
    WHERE type = 'table'
    AND name = :name
    '''
    cur.execute(query, {'name': table_name})
    return bool(cur.fetchall())
    

def init_nodes(conn: sqlite3.Connection):
    if not table_exists(conn, 'nodes'):
        cur = conn.cursor()
        query = '''
        CREATE TABLE nodes(
            graph_id INTEGER,
            node_id INTEGER,
            value TEXT,
            exists INTEGER
        )
        '''
        cur.execute(query)

        query = '''
        CREATE INDEX idx_graph_nodes
        ON nodes(graph_id)
        '''
        cur.execute(query)

        conn.commit()

def init_edges(conn: sqlite3.Connection):
    if not table_exists(conn, 'nodes'):
        cur = conn.cursor()
        query = '''
        CREATE TABLE edges(
            graph_id INTEGER,
            edge_id INTEGER,
            from_node INTEGER,
            to_node INTEGER,
            directed INTEGER,
            value TEXT,
            exists INTEGER
        )
        '''
        cur.execute(query)

        query = '''
        CREATE INDEX idx_graph_edges
        ON edges(graph_id)
        '''
        cur.execute(query)

        conn.commit()


class Graph:

    def __init__(self, conn: sqlite3.Connection, graph_id: int):
        self.conn = conn
        self.graph_id = graph_id

    def add_node(self, node_id: int, value: str):
        query = '''
        INSERT INTO nodes VALUES(
            :graph_id,
            :node_id,
            :value,
            1
        )
        '''
        params = {
            'graph_id': self.graph_id,
            'node_id': node_id,
            'value': value
        }
        self._set(query, params)

    def add_edge(self, edge_id, from_node, to_node, directed, value):
        query = '''
        INSERT INTO edges VALUES(
            :graph_id,
            :edge_id,
            :from_node,
            :to_node,
            :directed,
            :value,
            1
        )
        '''
        params = {
            'graph_id': self.graph_id,
            'edge_id': edge_id,
            'from_node': from_node,
            'to_node': to_node,
            'directed': directed,
            'value': value
        }
        self._set(query, params)

    def get(self):
        cur = self.conn.cursor()
        query = '''
        SELECT * FROM edges
        WHERE graph_id = :graph_id
        '''
        cur.execute(query, {'graph_id' : self.graph_id,})

    def _set(self, query: str, params: dict):
        cur = self.conn.cursor()
        cur.execute(query, params)
        self.conn.commit()

    def set_edge(self, node_id):
        query = '''
        '''
        params = {}
        self._set(query, params)

    def set_node(self, node_id):
        query = '''
        '''
        params = {}
        self._set(query, params)

    def delete_edge(self, edge_id):
        query = '''
        '''
        params = {}
        self._set(query, params)

    def delete_node(self, node_id):
        query = '''
        '''
        params = {}
        self._set(query, params)

    def max_id(self, column_name: str):
        cur = self.conn.cursor()
        query = f'''
        SELECT MAX({column_name})
        FROM nodes
        WHERE graph_id = :graph_id
        '''
        cur.execute(query, {'graph_id': self.graph_id})
        return cur.fetchall()[0]


