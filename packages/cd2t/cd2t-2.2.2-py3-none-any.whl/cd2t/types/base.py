"""
Base Data Type Class as root for all specific DT classes
"""

# pylint: disable=unused-argument,invalid-name
from cd2t.errors import SchemaError
from cd2t.references import ReferenceFinding, OPT, ReferenceElement
from cd2t.results import FindingsList, DataTypeMismatch
from cd2t.run_time_env import RunTimeEnv
import cd2t.schema
from cd2t.types.datatype import DataType


class BaseDataType(DataType):
    customizable = False
    data_type_name = "any"
    matching_classes = []
    options = [
        # option_name, required?, class, init_value
        ("default_value", False, None, None),
        ("description", False, [str, list], ""),
    ]
    support_reference = False

    def __init__(self) -> None:
        self.default_value = None
        self.description = ""
        self.ref_OPT = OPT.NONE
        self.ref_credits = None
        self.ref_key = ""
        self.data_type_mismatch_message = f"Value is not '{self.data_type_name}'"

    def data_matches_type(self, data: any) -> bool:
        if self.data_type_name == "any":
            return True
        for cls in self.matching_classes:
            if isinstance(data, cls):
                return True
        return False

    def build_schema(
        self,
        schema_definition: dict,
        path: str,
        RTE: RunTimeEnv,
        schema: cd2t.schema.Schema,
    ) -> DataType:
        # pylint: disable=too-many-branches,too-many-statements,too-many-locals
        schema_definition = schema_definition.copy()

        # Parse BaseDataType reference options
        reference_options = {}
        if self.support_reference and "reference" in schema_definition.keys():
            reference_options = schema_definition.pop("reference", {})
            _ref_path = path + ".reference"
            if not isinstance(reference_options, dict):
                raise SchemaError("Must be a dictionary.", _ref_path)

            _ref_dic_path = _ref_path + "."
            _key = "key"
            if _key not in reference_options.keys():
                raise SchemaError("Key missing", _ref_dic_path + _key)
            self.ref_key = reference_options.pop(_key)
            if not isinstance(self.ref_key, str):
                raise SchemaError("Must be a string", _ref_dic_path + _key)

            mode = reference_options.pop("mode", "unique")
            u_scope = reference_options.pop("unique_scope", "global")
            p_scope = reference_options.pop("producer_scope", "global")
            c_scope = reference_options.pop("consumer_scope", "global")
            orphan = reference_options.pop("allow_orphan_producer", True)
            ref_credits = reference_options.pop("credits", None)
            if mode == "unique":
                self.ref_OPT = OPT.UNIQUE | OPT.PRODUCER
            elif mode == "producer":
                self.ref_OPT = OPT.PRODUCER
            elif mode == "consumer":
                self.ref_OPT = OPT.CONSUMER
            else:
                raise SchemaError("Unsupported mode", _ref_dic_path + "mode")
            if OPT.UNIQUE in self.ref_OPT:
                if u_scope == "global":
                    self.ref_OPT = self.ref_OPT | OPT.UNIQUE_GLOBAL
                elif u_scope != "namespace":
                    raise SchemaError(
                        "Must be either 'global' or 'namespace'",
                        _ref_dic_path + "unique_scope",
                    )
                if ref_credits is None or ref_credits >= 0:
                    self.ref_credits = ref_credits
                else:
                    raise SchemaError(
                        "Must be >=0",
                        _ref_dic_path + "credits",
                    )
            if OPT.PRODUCER in self.ref_OPT:
                if p_scope == "global":
                    self.ref_OPT = self.ref_OPT | OPT.PRODUCER_GLOBAL
                elif p_scope != "namespace":
                    raise SchemaError(
                        "Must be either 'global' or 'namespace'",
                        _ref_dic_path + "producer_scope",
                    )
                if orphan:
                    self.ref_OPT = self.ref_OPT | OPT.ALLOW_ORPHAN_PRODUCER
                if ref_credits is None or ref_credits >= 0:
                    self.ref_credits = ref_credits
                else:
                    raise SchemaError(
                        "Must be >=0",
                        _ref_dic_path + "credits",
                    )
            if OPT.CONSUMER in self.ref_OPT:
                if c_scope == "global":
                    self.ref_OPT = self.ref_OPT | OPT.CONSUMER_GLOBAL
                elif c_scope != "namespace":
                    raise SchemaError(
                        "Must be either 'global' or 'namespace'",
                        _ref_dic_path + "consumer_scope",
                    )
                if ref_credits is None:
                    self.ref_credits = 1
                elif ref_credits > 0:
                    self.ref_credits = ref_credits
                else:
                    raise SchemaError(
                        "Must be >0",
                        _ref_dic_path + "credits",
                    )

            if not isinstance(orphan, bool):
                raise SchemaError(
                    "Must be bool", _ref_dic_path + "allow_orphan_producer"
                )
            if len(reference_options):
                raise SchemaError(
                    f"Unknown option keys '{','.join(reference_options.keys())}'",
                    _ref_path + "reference",
                )

        # Parse BaseDataType options
        _path = path + "."
        for option, required, cls in [_tuple[0:3] for _tuple in self.options]:
            if option in schema_definition.keys():
                value = schema_definition[option]
                if cls is None:
                    pass
                elif isinstance(cls, list):
                    found = False
                    for _cls in cls:
                        if isinstance(value, _cls):
                            found = True
                            break
                    if not found:
                        raise SchemaError("Wrong value type", _path + option)
                elif not isinstance(value, cls):
                    raise SchemaError("Wrong value type", _path + option)
                # pylint: disable-next=exec-used
                exec("self." + option + " = value")
                schema_definition.pop(option, None)
            elif required:
                raise SchemaError("Option missing", _path + option)
        if len(schema_definition):
            raise SchemaError(
                "Unknown option", _path + list(schema_definition.keys())[0]
            )

        self.verify_options(path=_path)

        return self

    def verify_options(self, path: str) -> None:
        if isinstance(self.description, list):
            for description_string in self.description:
                if not isinstance(description_string, str):
                    raise SchemaError(
                        message="Description must be list of strings.", path=path
                    )
        if self.default_value is not None:
            if not self.data_matches_type(self.default_value):
                raise SchemaError(
                    message="Default value doesn't match data type.", path=path
                )
            findings = self.verify_data(
                data=self.default_value, path=path, RTE=RunTimeEnv()
            )
            if findings:
                raise SchemaError(
                    message="Default value does not match data type definition: "
                    + ", ".join([f.message for f in findings]),
                    path=path,
                )

    def validate_data(self, data: any, path: str, RTE: RunTimeEnv) -> FindingsList:
        findings = FindingsList()
        if not self.data_matches_type(data):
            findings.append(
                DataTypeMismatch(path=path, message=self.data_type_mismatch_message)
            )
            return findings
        findings += self.verify_reference(data, path, RTE)
        findings += self.verify_data(data, path, RTE)
        return findings

    def verify_data(self, data: any, path: str, RTE: RunTimeEnv) -> FindingsList:
        return FindingsList()

    def build_sub_references(self, data: any, path: str, RTE: RunTimeEnv) -> None:
        return

    def build_references(self, data: any, path: str, RTE: RunTimeEnv) -> None:
        if self.data_matches_type(data):
            self.verify_reference(data=data, path=path, RTE=RTE)
            self.build_sub_references(data=data, path=path, RTE=RTE)

    def autogenerate_data(self, data: any, path: str, RTE: RunTimeEnv):
        return data, FindingsList()

    def get_reference_data(self, data: any, path: str) -> any:
        return data, FindingsList()

    def get_reference_element(self, path: str, ref_data: any) -> any:
        return ReferenceElement(
            reference_key=self.ref_key,
            path=path,
            value=ref_data,
            options=self.ref_OPT,
            credits=self.ref_credits,
        )

    def verify_reference(self, data: any, path: str, RTE: RunTimeEnv) -> FindingsList:
        findings = FindingsList()
        if not self.support_reference or OPT.NONE in self.ref_OPT:
            return findings
        ref_data, _findings = self.get_reference_data(data, path)
        findings += _findings
        ref_element = self.get_reference_element(path, ref_data)
        if OPT.UNIQUE in self.ref_OPT:
            other = RTE.references.same_unique(ref_element)
            if other is not None:
                if other.namespace != RTE.references.namespace:
                    _path = f"{other.namespace} > {other.path}"
                else:
                    _path = other.path
                findings.append(
                    ReferenceFinding(
                        path=path,
                        message=f"Unique value already used at '{_path}'",
                        reference=ref_element,
                    )
                )
                return findings
        # If unique or just for producer/consumer mapping, add element to references
        RTE.references.add_element(ref_element)
        return findings
