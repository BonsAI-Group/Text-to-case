import { FieldAnswer, FormItem } from "../../../generated";

type MultiSelectFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

const MultiSelectField = ({formItem, answer, showConfidence} : MultiSelectFieldProps) : JSX.Element => {
  return (
    <>
      To be implemented
    </>
  );
};

export default MultiSelectField;