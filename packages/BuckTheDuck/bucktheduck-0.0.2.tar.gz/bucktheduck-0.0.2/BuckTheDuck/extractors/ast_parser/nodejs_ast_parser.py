from typing import List

from BuckTheDuck import get_logger
from BuckTheDuck.extractors.ast_parser.nodejs_ast import NodejsMethod, NodejsAst

logger = get_logger()


class NodejsAstParser:
    _LOG_PREFIX = 'NodejsAstParser'

    def parse(self, raw_ast: dict) -> List[NodejsAst]:
        if raw_ast['type'] != 'File':
            raise NotImplemented(
                f'{self._LOG_PREFIX}: AST not supported as root is not from type File {raw_ast["type"]}')

        program = raw_ast['program']
        program_body = program['body']
        asts = []
        for class_body in program_body:
            if class_body['type'] == 'ClassDeclaration':
                class_name = class_body['id']['name']
                ast = NodejsAst(class_name, [], [])
                self._parse_class_body(class_body['body'], ast)
                asts.append(ast)
            else:
                logger.warning(f'{self._LOG_PREFIX} Class body is not supported - {class_body["type"]} continuing')
        return asts

    def _parse_class_body(self, class_body: dict, ast: NodejsAst):
        for body_ast in class_body['body']:
            if body_ast['type'] == 'ClassProperty':
                self._parse_class_property(ast, body_ast)
            elif body_ast['type'] == 'ClassMethod':
                self._parse_method(ast, body_ast)

    def _parse_method(self, ast, body_ast):
        method_name = body_ast['key']['name']
        is_async = body_ast['async']
        start_line = body_ast['body']['loc']['start']['line']
        end_line = body_ast['body']['loc']['end']['line']
        return_type = self._get_return_type(body_ast.get('ReturnType'))
        raw_arguments = []
        for raw_param in body_ast['params']:
            raw_arguments.append({
                'name': raw_param['name'],
                'type': self._get_type_annotation(raw_param)
            })
        ast.add_method(method_name, raw_arguments, return_type, start_line, end_line, is_async)

    def _parse_class_property(self, ast, body_ast):
        property_type = self._get_type_annotation(body_ast)
        ast.add_property(body_ast['key']['name'], property_type)

    def _get_type_annotation(self, ast):
        return ast.get('typeAnnotation', {}).get('typeAnnotation', {}).get('type')

    def _get_return_type(self, return_type_ast):
        if return_type_ast:
            return return_type_ast.get('typeAnnotation', {}).get('type')
        return None
