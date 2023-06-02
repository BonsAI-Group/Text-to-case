import { Button, Container, Group, Select, Stack, Textarea, Title } from "@mantine/core"
import { useState } from "react";
import FormComponent from "./components/FormComponent";
import LunchLabels from "./components/LunchLabels";
import SecurityForm from "./components/SecurityForm";
import { DefaultApi, FieldSubmit, Form, FormAnswer } from "../../generated";
import { ApiConfiguration } from "../../api/ApiConfiguration";
import UseZenyaForms from "./components/UseZenyaForms";
import RecorderInput from "./components/UserInput/RecorderInput";
import UserInput from "./components/UserInput/UserInput";

/**
 * Page for displaying a form and submitting it.
 * @returns 
 */
const FormPage = () => {
  const [answers, setAnswers] = useState<FormAnswer>({ answers: {} } as FormAnswer);

  const { forms: zenyaForms, arePending } = UseZenyaForms();

  const forms = {
    "Lunch": LunchLabels,
    "Security": SecurityForm,
    ...zenyaForms
  } as { [key: string]: () => Form };

  const [form, setForm] = useState(forms["Lunch"]());

  return (
    <Container>
      <Title order={1}>Form</Title>
      <Group grow align="start">
        <UserInput answers={answers} setAnswers={setAnswers} form={form} />
        <Stack>
          <Select
            label="Form"
            data={Object.keys(forms)}
            value={arePending ? "Loading..." : form.name}
            disabled={arePending}
            onChange={(event) => {
              setForm(forms[event!]);
            }
            }
          />
          <FormComponent form={form} answers={answers} />
        </Stack>

      </Group>

    </Container>
  );
};

export default FormPage;