import { TimeInput } from "@mantine/dates";
import ConfidenceBubble from "./ConfidenceBubble";
import { FieldAnswer, FormItem } from "../../../generated";

type TimeFieldProps = {
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

const TimeField = ({formItem, answer, showConfidence} : TimeFieldProps) : JSX.Element => {
  return (
    <TimeInput
      label={formItem.fieldName}
      value={answer?.answer[0]}
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
          {/* <Text fz={"sm"}>{(answer.confidence[0]*100).toFixed(1)}%</Text> */}
          <ConfidenceBubble confidence={answer.confidence[0]} />
        </>
      ) : undefined}
    />
  );
};

export default TimeField;