import { Stack, Switch, Title } from "@mantine/core";
import { Form, FormAnswer } from "../../../generated";
import FormField from "./FormField";
import { useState } from "react";

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
  const [showConfidence, setShowConfidence] = useState<boolean>(false);
  return (
    <Stack>
      <Title order={2}>{form.name}</Title>
      <Switch label="Show confidence" checked={showConfidence} onChange={(event) => setShowConfidence(event.currentTarget.checked)} size="xs" />
      {
        form.fields.map((field) => {
          return (
            <FormField key={field.fieldName} formItem={field} answer={answers ? answers.answers[field.fieldName] : undefined} showConfidence={showConfidence} />
          );
        })
      }
    </Stack>
  );
};

export default FormComponent;