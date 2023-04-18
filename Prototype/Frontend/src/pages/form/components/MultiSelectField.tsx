import { Group, MultiSelect, Text } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";
import { useEffect, useState } from "react";
import ConfidenceBubble from "./ConfidenceBubble";

type MultiSelectFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

const MultiSelectField = ({formItem, answer, showConfidence} : MultiSelectFieldProps) : JSX.Element => {
  const [value, setValue] = useState<string[]>(answer ? answer.answer : []);

  const findIndex = (value: string) => {
    return formItem.params!.findIndex((param) => param === value);
  };

  useEffect(() => {
    setValue(answer ? answer.answer: []);
  }, [answer]);
  return (
    <MultiSelect data={formItem.params!} label={formItem.fieldName} value={value} onChange={setValue} valueComponent={(value) => (
      // Gray box with padding and rounded corners, colored border if showConfidence
      <div style={{backgroundColor: "#f0f0f0", 
                  padding: "2px 4px", 
                  borderRadius: "4px", 
                  marginRight: "4px",
                  marginTop: "4px",
                  marginBottom: "4px",
                  border: showConfidence ? `2px solid ${borderColor(answer ? answer.confidence[findIndex(value.label)] : 0)}` : "none"
                  }}>
        <Group spacing={"xs"}>
          <Text fz={"sm"}>{value.label}</Text>
          {answer && showConfidence ? <ConfidenceBubble confidence={answer ? answer.confidence[findIndex(value.label)] : 0} /> : null}
          {/* <Text fz={"sm"}>{answer && showConfidence ? (answer.confidence[findIndex(value.label)]*100).toFixed(1) + "%" : null}</Text> */}
        </Group>
        
      </div>
    )} />
  );
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

export default MultiSelectField;