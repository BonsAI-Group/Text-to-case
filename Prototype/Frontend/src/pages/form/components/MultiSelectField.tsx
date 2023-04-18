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

  useEffect(() => {
    setValue(answer ? answer.answer: []);
  }, [answer]);
  return (
    <MultiSelect data={formItem.params!} label={formItem.fieldName} value={value} onChange={setValue} valueComponent={(value) => (
      // Gray box with padding and rounded corners
      <div style={{backgroundColor: "#f0f0f0", padding: "2px 4px", borderRadius: "4px", marginRight: "4px"}}>
        <Group spacing={"xs"}>
          <Text fz={"sm"}>{value.label}</Text>
          {answer && showConfidence ? <ConfidenceBubble confidence={answer ? answer.confidence[0] : 0} /> : null}
        </Group>
        
      </div>
    )} />
  );
};

export default MultiSelectField;