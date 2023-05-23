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
            elif element["field"]["type"] == "date":
                fields.append(ZenyaFormParser.parseDateField(element))
            elif element["field"]["type"] == "time":
                fields.append(ZenyaFormParser.parseTimeField(element))
            else:
                fields.append(ZenyaFormParser.parseOther(element))

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
    def parseNumericField(field: dict) -> FormItem:
        """
        Parses a dictionary representing a numeric field and returns a FormItem object.

        Args:
        field (dict): A dictionary representing a numeric field.

        Returns:
        FormItem: A FormItem object representing the parsed numeric field.
        """
        type = FieldType.NUMERIC
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
    
    @staticmethod
    def parseDateField(field: dict) -> FormItem:
        """
        Parses a dictionary representing a date field and returns a FormItem object.

        Args:
        field (dict): A dictionary representing a date field.

        Returns:
        FormItem: A FormItem object representing the parsed date field.
        """
        type = FieldType.DATE
        name = field["field"]["name"]
        return FormItem(fieldName=name, fieldType=type, params=None)
    
    @staticmethod
    def parseTimeField(field: dict) -> FormItem:
        """
        Parses a dictionary representing a time field and returns a FormItem object.

        Args:
        field (dict): A dictionary representing a time field.

        Returns:
        FormItem: A FormItem object representing the parsed time field.
        """
        type = FieldType.TIME
        name = field["field"]["name"]
        return FormItem(fieldName=name, fieldType=type, params=None)
    
    @staticmethod
    def parseFormList(forms: list[dict]) -> list[Form]:
        """
        Parses a dictionary representing a list of forms (with designs) and returns a list of Form objects.

        Args:
        forms (dict): A dictionary representing a list of forms.

        Returns:
        list: A list of Form objects representing the parsed forms.
        """
        formList = []
        for form in forms:
            formList.append(ZenyaFormParser.parseForm(form))
        return formList
    
    @staticmethod
    def parseOther(field: dict) -> FormItem:
        """
        Parses a dictionary representing a field that is not supported and returns a text FormItem object.

        Args:
        field (dict): A dictionary representing a field that is not supported.

        Returns:
        FormItem: A FormItem object representing the parsed field.
        """
        type = FieldType.TEXT
        name = field["field"]["name"]
        return FormItem(fieldName=name, fieldType=type, params=None)