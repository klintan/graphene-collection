from graphql.backend.core import GraphQLCoreBackend



class DepthAnalysisBackend(GraphQLCoreBackend):
    """
    From @jkimbo https://github.com/graphql-python/graphene/issues/772#issuecomment-400094405. 
    Analyze and stop queries deeper than a certain depth. 

    backend = DepthAnalysisBackend(max_depth=3)
    result = schema.execute(query_string, backend=backend)

    """
    def __init__(self, max_depth: int = 3):
        self.max_depth = max_depth

    def document_from_string(self, schema, document_string):
        document = super().document_from_string(schema, document_string)
        ast = document.document_ast
        for definition in ast.definitions:
            # We are only interested in queries
            if definition.operation != 'query':
                continue

            depth = self.measure_depth(definition.selection_set)
            if depth > self.max_depth:
                raise Exception('Query is too complex')

        return document

    @staticmethod
    def measure_depth(selection_set, level=1):
        max_depth = level
        for field in selection_set.selections:
            if field.selection_set:
                new_depth = measure_depth(field.selection_set, level=level + 1)
                if new_depth > max_depth:
                    max_depth = new_depth
        return max_depth