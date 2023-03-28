import { Stack, Text, TextInput } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";

type FormFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

const borderColor = (confidence: number) : string => {
  // Fade from red to orange to yellow to green
  const hue = confidence * 0.4 * 360;
  const saturation = 90;
  const lightness = 50;
  return `hsl(${hue}, ${saturation}%, ${lightness}%)`;
};

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
            paddingRight: "5px"
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