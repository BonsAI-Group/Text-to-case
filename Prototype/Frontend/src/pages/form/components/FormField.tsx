import { Stack, Text } from "@mantine/core";
import { FieldAnswer, FieldType, FormItem } from "../../../generated";
import TextField from "./TextField";
import RadioButtonsField from "./RadioButtonsField";
import MultiSelectField from "./MultiSelectField";

type FormFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};


/**
 * Component for displaying a single form field.
 * @param formItem The form item to display
 * @param answer The answer to the form item. If not provided, the field will be empty.
 * @param showConfidence If true, the confidence of the answer will be displayed.
 * @returns 
 */
const FormField = ({formItem, answer, showConfidence} : FormFieldProps) : JSX.Element => {
  
  let field;
  switch (formItem.fieldType) {
    case FieldType.TEXT:
      field = <TextField formItem={formItem} answer={answer} showConfidence={showConfidence} />;
      break;
    case FieldType.RADIO_BUTTON:
      field = <RadioButtonsField formItem={formItem} answer={answer} showConfidence={showConfidence} />;
      break;
    case FieldType.MULTI_SELECT:
      field = <MultiSelectField formItem={formItem} answer={answer} showConfidence={showConfidence} />;
      break;

    default:
      field = <Text>Unknown field type</Text>;
      break;
  }
  return (
    <Stack p={0} spacing={0}>
      {field}
    </Stack>
  );
};

export default FormField;