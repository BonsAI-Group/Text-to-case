import { Group, Radio } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";
import { useEffect, useState } from "react";
import ConfidenceBubble from "./ConfidenceBubble";

type RadioButtonsFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

const RadioButtonsField = ({formItem, answer, showConfidence} : RadioButtonsFieldProps) : JSX.Element => {
  const [value, setValue] = useState<string>(answer ? answer.answer[0] : "");

  useEffect(() => {
    setValue(answer ? answer.answer[0] : "");
  }, [answer]);
  return (
    <Radio.Group label={formItem.fieldName} value={value} onChange={setValue}>
      <Group>
        {formItem.params!.map((option) => (
          <Radio key={option} value={option} label={option} />
        ))}
        {answer && showConfidence ? <ConfidenceBubble confidence={answer ? answer.confidence[0] : 0} /> : null}
      </Group>
    </Radio.Group>    
  );
};




export default RadioButtonsField;