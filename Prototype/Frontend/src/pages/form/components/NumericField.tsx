import { NumberInput } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";
import ConfidenceBubble from "./ConfidenceBubble";


type NumericFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
}

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

const NumericField = ({formItem, answer, showConfidence} : NumericFieldProps) : JSX.Element => {
    console.log(answer)
  return (
    <NumberInput
        label={formItem.fieldName}
        value={Number(answer ? answer.answer[0] : 0)}
        disabled={!answer || !answer.isTrusted[0]}
        styles={{
          input: answer && showConfidence
           ? {
            borderColor: borderColor(answer.confidence[0]),
            borderWidth: "2px",
            borderStyle: "solid"
          } : {},
          rightSection: {
            paddingRight: "12px"
          }
        }}
        rightSection={answer && showConfidence ? (
          <>
            <ConfidenceBubble confidence={answer.confidence[0]} />
          </>
        ) : undefined}
        />
  );
};

export default NumericField;