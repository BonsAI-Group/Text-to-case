import { Stack, TextInput, Title } from "@mantine/core";
import { Form, FormAnswer } from "../../../generated";

type FormComponentProps = {
  form: Form;
  answers?: FormAnswer;
};

/**
 * Component for displaying any form. 
 * @param form The form to display
 * @param answers The answers to the form. If not provided, the field will be empty.
 * @returns 
 */
const FormComponent = ({ form, answers } : FormComponentProps) => {
  return (
    <Stack>
      <Title order={2}>{form.name}</Title>
      {
        form.fields.map((field) => {
          return (
            <TextInput
              key={field.fieldName}
              label={field.fieldName}
              value={answers? answers.answers[field.fieldName].answer : ""}
              disabled={!answers}
              />
          );
        })
      }
    </Stack>
  );
};

export default FormComponent;