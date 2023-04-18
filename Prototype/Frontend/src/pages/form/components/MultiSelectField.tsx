import { MultiSelect } from "@mantine/core";
import { FieldAnswer, FormItem } from "../../../generated";
import { useEffect, useState } from "react";

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
    <MultiSelect data={formItem.params!} label={formItem.fieldName} value={value} onChange={setValue} />
  );
};

export default MultiSelectField;