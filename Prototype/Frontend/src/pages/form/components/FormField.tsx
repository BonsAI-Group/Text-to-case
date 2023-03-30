import { Stack, Text, TextInput } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";

type FormFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

/** 
 * Returns a border color based on the confidence of the answer.
 * @param confidence The confidence of the answer. Should be between 0 and 1.
 * @returns  A CSS hsl color string fading from red to orange to yellow to green.
 */
const borderColor = (confidence: number) : string => {
  const hue = confidence * 0.4 * 360;
  const saturation = 90;
  const lightness = 50;
  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
};

/**
 * Component for displaying a single form field.
 * @param formItem The form item to display
 * @param answer The answer to the form item. If not provided, the field will be empty.
 * @param showConfidence If true, the confidence of the answer will be displayed.
 * @returns 
 */
const FormField = ({formItem, answer, showConfidence} : FormFieldProps) : JSX.Element => {
  return (
    <Stack p={0} spacing={0}>
      <TextInput
        label={formItem.fieldName}
        value={answer ? answer.answer : ""}
        disabled={!answer}
        styles={{
          input: answer && showConfidence
           ? {
            borderColor: borderColor(answer.confidence),
            borderWidth: "2px",
            borderStyle: "solid"
          } : {},
          rightSection: {
            paddingRight: "12px"
          }
        }}
        rightSection={answer && showConfidence ? (
          <Text fz={"sm"}>{(answer.confidence*100).toFixed(1)}%</Text>
        ) : undefined}
        />
        
    </Stack>
  );
};

export default FormField;