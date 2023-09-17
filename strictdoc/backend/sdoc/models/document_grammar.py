from collections import OrderedDict, defaultdict
from typing import Dict, List, Set, Union

from strictdoc.backend.sdoc.models.type_system import (
    RESERVED_NON_META_FIELDS,
    GrammarElementField,
    GrammarElementFieldReference,
    GrammarElementFieldString,
    GrammarElementRelationParent,
    GrammarReferenceType,
    RequirementFieldName,
)
from strictdoc.helpers.auto_described import auto_described


def create_default_relations(parent) -> List[GrammarElementRelationParent]:
    return [
        GrammarElementRelationParent(
            parent=parent,
            relation_type="Parent",
            relation_role=None,
        )
    ]


@auto_described()
class GrammarElement:
    def __init__(
        self,
        parent,
        tag: str,
        fields: List[GrammarElementField],
        relations: List,
    ):
        self.parent = parent
        self.tag: str = tag
        self.fields: List[GrammarElementField] = fields
        self.relations: List[Union[GrammarElementRelationParent]] = (
            relations
            if relations is not None and len(relations) > 0
            else create_default_relations(self)
        )
        fields_map: OrderedDict = OrderedDict()
        for field in fields:
            fields_map[field.title] = field
        self.fields_map = fields_map

    def get_relation_types(self) -> List[str]:
        return list(
            map(lambda relation_: relation_.relation_type, self.relations)
        )

    def enumerate_meta_field_titles(self):
        for field in self.fields:
            if field.title in (
                RequirementFieldName.TITLE,
                RequirementFieldName.STATEMENT,
            ):
                break
            if field.title in RESERVED_NON_META_FIELDS:
                continue
            yield field.title

    def enumerate_custom_content_field_titles(self):
        after_title_or_statement = False
        for field in self.fields:
            if field.title in (
                RequirementFieldName.TITLE,
                RequirementFieldName.STATEMENT,
            ):
                after_title_or_statement = True
            if field.title in RESERVED_NON_META_FIELDS:
                continue
            if not after_title_or_statement:
                continue
            yield field.title


class DocumentGrammar:
    def __init__(self, parent, elements: List[GrammarElement]):
        self.parent = parent
        self.elements: List[GrammarElement] = elements

        registered_elements: Set[str] = set()
        elements_by_type: Dict[str, GrammarElement] = {}
        fields_by_type: Dict[str, List[str]] = defaultdict(list)

        for element in elements:
            registered_elements.add(element.tag)
            elements_by_type[element.tag] = element
            for element_field in element.fields:
                fields_by_type[element.tag].append(element_field.title)

        self.registered_elements: Set[str] = registered_elements
        self.elements_by_type: Dict[str, GrammarElement] = elements_by_type
        self.fields_order_by_type: Dict[str, List[str]] = fields_by_type

        self.is_default = False

    @staticmethod
    def create_default(parent):
        fields = [
            GrammarElementFieldString(
                parent=None, title=RequirementFieldName.UID, required="False"
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.LEVEL,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.STATUS,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None, title=RequirementFieldName.TAGS, required="False"
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.TITLE,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.STATEMENT,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.RATIONALE,
                required="False",
            ),
            GrammarElementFieldString(
                parent=None,
                title=RequirementFieldName.COMMENT,
                required="False",
            ),
            GrammarElementFieldReference(
                parent=None,
                title=RequirementFieldName.REFS,
                types=[
                    GrammarReferenceType.PARENT_REQ_REFERENCE,
                    GrammarReferenceType.CHILD_REQ_REFERENCE,
                    GrammarReferenceType.FILE_REFERENCE,
                ],
                required="False",
            ),
        ]
        requirement_element = GrammarElement(
            parent=None, tag="REQUIREMENT", fields=fields, relations=[]
        )
        requirement_element.relations = create_default_relations(
            requirement_element
        )

        elements: List[GrammarElement] = [requirement_element]
        grammar = DocumentGrammar(parent=parent, elements=elements)
        grammar.is_default = True

        return grammar

    def dump_fields(self, requirement_type) -> str:
        return ", ".join(
            list(
                map(
                    lambda g: g.title,
                    self.elements_by_type[requirement_type].fields,
                )
            )
        )
