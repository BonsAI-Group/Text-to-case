from models.Form import Form
from models.FormItem import FormItem
from enums.FieldType import FieldType

class ZenyaFormParser:
    """
    A class that parses a form from Zenya's API into a Form object.
    """
    
    @staticmethod
    def parseForm(form: dict) -> Form:
        """
        Parses a dictionary representing a form and returns a Form object.

        Args:
        form (dict): A dictionary representing a form.

        Returns:
        Form: A Form object representing the parsed form.
        """
        name = str(form["title"])
        fields = []
        for element in form["design"]["elements"]:
            if element["element_type"] != "field":
                continue
            
            if element["field"]["type"] == "text":
                fields.append(ZenyaFormParser.parseTextField(element))
            elif element["field"]["type"] == "list":
                if element["field"]["list_display_type"] == "checkbox":
                    fields.append(ZenyaFormParser.parseMultiSelectField(element))
                elif element["field"]["list_display_type"] == "radio":
                    fields.append(ZenyaFormParser.parseRadioField(element))
            else:
                continue

        return Form(name=name, fields=fields)

    @staticmethod
    def parseTextField(field: dict) -> FormItem:
        """
        Parses a dictionary representing a text field and returns a FormItem object.

        Args:
        field (dict): A dictionary representing a text field.

        Returns:
        FormItem: A FormItem object representing the parsed text field.
        """
        type = FieldType.TEXT
        name = field["field"]["name"]
        return FormItem(fieldName=name, fieldType=type, params=None)
    
    @staticmethod
    def parseMultiSelectField(field: dict) -> FormItem:
        """
        Parses a dictionary representing a multi-select field and returns a FormItem object.

        Args:
        field (dict): A dictionary representing a multi-select field.

        Returns:
        FormItem: A FormItem object representing the parsed multi-select field.
        """
        type = FieldType.MULTI_SELECT
        name = field["field"]["name"]
        fields = []
        for option in field["field"]["list_items"]:
            fields.append(option["name"])
        return FormItem(fieldName=name, fieldType=type, params=fields)

    @staticmethod
    def parseRadioField(field: dict) -> FormItem:
        """
        Parses a dictionary representing a radio button field and returns a FormItem object.

        Args:
        field (dict): A dictionary representing a radio button field.

        Returns:
        FormItem: A FormItem object representing the parsed radio button field.
        """
        type = FieldType.RADIO_BUTTON
        name = field["field"]["name"]
        fields = []
        for option in field["field"]["list_items"]:
            fields.append(option["name"])
        return FormItem(fieldName=name, fieldType=type, params=fields)