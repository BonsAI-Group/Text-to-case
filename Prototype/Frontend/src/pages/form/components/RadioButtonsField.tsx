import { FieldAnswer, FormItem } from "../../../generated";

type RadioButtonsFieldProps = {
  formItem: FormItem;
  answer?: FieldAnswer;
  showConfidence?: boolean;
};

const RadioButtonsField = ({formItem, answer, showConfidence} : RadioButtonsFieldProps) : JSX.Element => {
  return (
    <>
      To be implemented
    </>
  );
};

export default RadioButtonsField;